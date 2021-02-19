import requests
import threading
from threading import Thread
import time

# Visit google.com

# GET REQUEST --> Get information from a page
# POST REQUEST --> For submitting information
# DELETE REQUEST --> Deleting information off a website
# PUT REQUEST --> Updating information on a website

class Bot:
  # constructor
  def __init__(self, website, name, search_terms):
    self.site = website
    self.username = name
    self.terms = search_terms

  def get_website(self):
    print("Bot is going to visit: ", self.site)

  def get_username(self):
    print("Bot name is: ", self.username)

  def check_status_code(self, set_request):
    if set_request.status_code == 200:
      print("Successfully visited: ", self.site)
    elif set_request.status_code == 404:
      print("Could not connect to: ", self.site)
    elif set_request.status_code == 429:
      print("Bot has visited site too many times: ")
    else:
      print("Unknown response {}".format(set_request.status_code))

  # visit the site once
  def visit_site(self):
    my_request = requests.get(self.site)
    self.check_status_code(my_request)

  #http://www.google.com/search?q=soccer 
  def search_site(self, search_term):
    my_request = requests.get(self.site + "search?q={}".format(search_term))
    self.check_status_code(my_request)


  def search_site_terms(self):
    for x in self.terms:
      self.search_site(x)

search_terms = ["cats", "dogs", "pigs"]
myGoogleBot = Bot("https://www.google.com/", "bob", search_terms )
myW3SchoolsBot = Bot("https://www.w3schools.com/", "w3_checker", search_terms )


myGoogleBot.get_website()
myGoogleBot.get_username()
#myGoogleBot.visit_site() 

myW3SchoolsBot.get_website()
myW3SchoolsBot.get_username()


print("#hello")

website_threads = [] 

def google_thread():
  print("Website scanner google started... ")
  for i in range(5):
    myGoogleBot.visit_site()
    time.sleep(5)

def w3_thread():
  print("Website scanner w3schools started... ")
  for i in range(5):
    myW3SchoolsBot.visit_site()
    time.sleep(5)

website_thread_1 = threading.Thread(target=google_thread)
website_thread_2 = threading.Thread(target=w3_thread)
website_thread_1.start()
website_thread_2.start()
website_thread_1.join()
website_thread_2.join()
