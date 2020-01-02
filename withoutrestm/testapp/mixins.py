from django.core.serializers import serialize
import json

class serializeMixin(object):
    def serialize(self, qs):
        json_data=serialize('json',qs)
        p_data = json.loads(json_data)
        finale_list = []
        for obj in p_data:
            emp_data = obj['fields']
            finale_list.append(emp_data)
        json_data=json.dumps(finale_list)
        return json_data

from django.http import HttpResponse
class HttpResponseMixin(object):
    def render_to_HttpResponse(self, json_data, status=200):
        return HttpResponse(json_data,content_type="application/json",status=status)
