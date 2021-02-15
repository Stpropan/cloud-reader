from json.decoder import JSONDecodeError
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.middleware.csrf import get_token
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json

@method_decorator(csrf_exempt, name='dispatch')
class AuthorizeDefaultUser(View):

    def post(self, request:HttpRequest):
        try:
            post_items = json.loads(request.body)
        except JSONDecodeError:
            error_msg = "Error! Be sure to pass data in JSON format!"
            print(error_msg)
            return HttpResponse(error_msg)

        try:
            username = post_items['username']
            email = post_items['email']
            password = post_items['password']
        except KeyError:
            error_msg = "Error! Not all data passed! Check documentation"
            print(error_msg)
            return HttpResponse(error_msg)

        user = User(username = username, email = email)
        user.set_password(raw_password = password)
        user.save()

        return HttpResponse("Success")