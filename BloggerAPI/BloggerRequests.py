#!/usr/bin/env python
# -*- coding: utf-8 -*-

global_blogger_http_object = None


def set_global_http(http):
  global global_blogger_http_object
  global_blogger_http_object = http


global_blogger_service = None


def set_global_service(service):
  global global_blogger_service
  global_blogger_service = service


def request_loop(request, http, handle_result_function, get_next_request_function, parameters={}):
  result = None
  while request != None:
    result_of_request = request.execute(http=http)

    result, should_break = handle_result_function(result_of_request, parameters)
    if should_break:
      break
    request = get_next_request_function(request, result_of_request)
  return result


def get_user(service=global_blogger_service, http=global_blogger_http_object, userId='self'):
  users = service.users()
  thisuser = users.get(userId=userId).execute(http=http)
  return thisuser
