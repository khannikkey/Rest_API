from django.shortcuts import render
from django.views.generic import View
from testapp.models import Employee
from django.http import HttpResponse
from testapp.mixins import serializeMixin, HttpResponseMixin
import json
from testapp.utils import is_json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from testapp.forms import EmployeeForm

class EmployeeDetailCBV(HttpResponseMixin,serializeMixin, View):
    def get(self, request,id ,*args, **kwargs):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            json_data= json.dumps({"msg":"The Requested Resource not Available"})
            return self.render_to_HttpResponse(json_data, status=404)
        else:
            json_data= self.serialize([emp,])
            return self.render_to_HttpResponse(json_data)


@method_decorator(csrf_exempt, name='dispatch')
class EmployeeListCBV(HttpResponseMixin,serializeMixin, View):
    def get(self, request,*args, **kwargs):
        qs = Employee.objects.all()
        json_data=self.serialize(qs)
        return HttpResponse(json_data, content_type="application/json")

    def post(self, request,*args, **kwargs):
        data = request.body
        valid_json = is_json(data)

        if not valid_json:
            json_data = json.dumps({"msg":"Please Send Valid Json Data"})
            return self.render_to_HttpResponse(json_data, status=400)
        emp_data = json.loads(data)# Converting Json Data into Python Dict
        form = EmployeeForm(emp_data)# With Python Dict we creating EmployeeForm object

        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({"msg":"Resource Created SuccessFully"})
            return self.render_to_HttpResponse(json_data)

        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_HttpResponse(json_data, status=400)
