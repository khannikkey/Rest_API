from django.shortcuts import render
from django.http import HttpResponse

def emp_data_view(request):
    emp_data = {
    'eno':100,
    'ename':'Nikkey',
    'esal':1000,
    'eaddr':'Hyderabad',
    }
    resp = '<h1>employee Number:{} employee Name:{} employee Salary:{} employee Address:{}</h1>'.format(emp_data['eno'],emp_data['ename'],emp_data['esal'],emp_data['eaddr'])
    return HttpResponse(resp)

import json
def emp_data_jsonview(request):
    emp_data = {
    'eno':100,
    'ename':'Nikkey',
    'esal':1000,
    'eaddr':'Hyderabad',
    }
    json_data = json.dumps(emp_data)
    return HttpResponse(json_data, content_type="application/json")

from django.http import JsonResponse
def emp_data_jsonview2(request):
    emp_data = {
    'eno':100,
    'ename':'Nikkey',
    'esal':1000,
    'eaddr':'Hyderabad',
    }
    # json_data = json.dumps(emp_data)
    # return HttpResponse(json_data, content_type="application/json")
    return JsonResponse(emp_data)


from django.views.generic import View
from testapp.mixin import HttpResponseMixin

class JsonCBV( HttpResponseMixin ,View):
    def get(self ,request,*args,**kwrgs):
        json_data = json.dumps({'msg':'This is From Get Method'})
        return self.render_to_HttpResponse(json_data)

    def post(self ,request,*args,**kwrgs):
        json_data = json.dumps({'msg':'This is From POST Method'})
        return self.render_to_HttpResponse(json_data)

    def put(self ,request,*args,**kwrgs):
        json_data = json.dumps({'msg':'This is From PUT Method'})
        return self.render_to_HttpResponse(json_data)

    def delete(self ,request,*args,**kwrgs):
        json_data = json.dumps({'msg':'This is From DELETE Method'})
        return self.render_to_HttpResponse(json_data)
