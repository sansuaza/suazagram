
from django.http import HttpResponse
from datetime  import datetime
import json


def hello_World(request):

    now = datetime.now()
    return HttpResponse("hello, world {now}".format(now=str(now)))

def sorted(request):
    #numbers = request.GET['numbers']
    sorted_ints = [1,34,56,12]
    data= {
        'status' :'ok',
        'numbers' : sorted_ints,
        'message' : 'integers sorted succesfully'
    }      

    return HttpResponse (json.dumps(data, indent = 4), content_type= 'application/json')

def hi (request, name, age):
    if age < 12:
        message =  "sorry {}".format(name)

    else:
        message = "welcome {}".format(name)

    return HttpResponse(message)
