# coding=utf-8
from django.http.response import HttpResponse


def my_middleware(get_response):

   def middleware(request):

       if 'a' in request.GET:
           return HttpResponse('a is not allowed')

       res = get_response(request)
       return res


   return middleware
