import sys

from apiclient.discovery import build
from oauth2client import client
from apiclient import sample_tools
from BloggerAPI import BloggerPosts
from BloggerAPI.BloggerPosts import check_if_page_exists, list_blog_posts, global_blogger_posts

import PersonalClientSecrets
import BloggerRequests


def get_this_users_blogs(service):
  thisusersblogs = service.blogs().listByUser(userId='self').execute()
  return thisusersblogs


def list_blog_urls(thisusersblogs):
  for blog in thisusersblogs['items']:
    print 'The blog named \'%s\' is at: %s' % (blog['name'], blog['url'])



def insert_or_update_page(page_name,body_html,service):
  posts = service.posts()
  page_exists = True
  if page_exists == False:
    posts.insert(blogId='1004062766284827324', body=new_page).execute()

def main(argv):
  # Authenticate and construct service.
  service, flags = sample_tools.init(
    argv, 'plus', 'v1', __doc__, __file__,
    scope='https://www.googleapis.com/auth/blogger')
  http = PersonalClientSecrets.init_google_api()
  service = build('blogger', 'v3', http=http)

  try:
    BloggerRequests.set_global_http(http)
    BloggerRequests.set_global_service(service)
    BloggerPosts.set_global_posts(service)

    thisusersblogs = get_this_users_blogs(service)

    # List the posts for each blog this user has
    for blog in thisusersblogs['items']:
      print blog['id']
      list_blog_posts(blog,posts=global_blogger_posts)


    check_if_page_exists('1004062766284827324', "A String")

  except client.AccessTokenRefreshError:
    print ('The credentials have been revoked or expired, please re-run'
           'the application to re-authorize')


new_page = {
  "status": "DRAFT",  # The status of the page for admin resources (either LIVE or DRAFT).
  "blog": {  # Data about the blog containing this Page.
             "id": "1004062766284827324",  # The identifier of the blog containing this page.
  },
  "kind": "blogger#page",  # The kind of this entity. Always blogger#page
  "title": "A String",  # The title of this entity. This is the name displayed in the Admin user interface.
  #"url": "A String", # The URL that this Page is displayed at.
  "author": {  # The author of this Page.
               "url": "http://www.alasdairmorrison.com",  # The URL of the Page creator's Profile page.
               #"image": { # The page author's avatar.
               #  "url": "A String", # The page author's avatar URL.
               #},
               "displayName": "Ali",  # The display name.
               #"id": "A String", # The identifier of the Page creator.
  },
  #"updated": "A String", # RFC 3339 date-time when this Page was last updated.
  "content": "A String",  # The body content of this Page, in HTML.
  #"published": "A String", # RFC 3339 date-time when this Page was published.
  #"id": "A String", # The identifier for this resource.
  #"selfLink": "A String", # The API REST URL to fetch this resource from.
}

if __name__ == '__main__':
  main(sys.argv)
