#!/usr/bin/env python
# -*- coding: utf-8 -*-
from BloggerAPI import BloggerRequests
from BloggerRequests import global_blogger_http_object, global_blogger_service


########
# Setup Functions
########

global_blogger_posts=None

def set_global_posts(service=global_blogger_service):
  global global_blogger_posts
  global_blogger_posts = service.posts()
  print global_blogger_posts


#######
# Check if Page exists
#######

def check_if_page_exists(blog_id, page_name, posts=global_blogger_posts, http=global_blogger_http_object):
  request = posts.list(blogId=blog_id)
  result_of_search = BloggerRequests.request_loop(request, http, check_each_post_to_see_if_name_exists, posts.list_next, parameters={'name_to_find':page_name})
  found_page = result_of_search['found']
  print found_page

def check_each_post_to_see_if_name_exists(posts_list, parameters={}):
  name_to_find = parameters['name_to_find']
  if 'items' in posts_list and not (posts_list['items'] is None):
    for post in posts_list['items']:
      post_title = post['title']
      if name_to_find == post_title:
        return {'found': True, 'post': post}, True
  return {'found': False, 'post': None}, False

#######
# Print List of Posts
#######
def print_post_name(posts_doc,parameters):
  if 'items' in posts_doc and not (posts_doc['items'] is None):
    for post in posts_doc['items']:
      print '  %s (%s)' % (post['title'], post['url'])
  return None, False


def list_blog_posts(blog, posts=global_blogger_posts, http=global_blogger_http_object):
  print 'The posts for %s:' % blog['name']
  request = posts.list(blogId=blog['id'])
  BloggerRequests.request_loop(request, http, print_post_name, posts.list_next)
