from flask import Flask
import feedparser
from flask import render_template
from flask import request
from flask import make_response
import json
import urllib
import urllib2
import datetime

app= Flask(__name__)

BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"
CNN_FEED = "http://rss.cnn.com/rss/edition.rss"
FOX_FEED = "http://feeds.foxnews.com/foxnews/latest"
IOL_FEED = "http://www.iol.co.za/cmlink/1.640"

@app.route("/")
def get_news():
  feed = feedparser.parse(BBC_FEED)
  return render_template("home.html", articles=feed['entries'])

  
def get_new():
  feed = feedparser.parse(CNN_FEED)
  return render_template("home.html", artic=feed['entries'])



#DEFAULTS = {
 #            'publication' : 'bbc',
 #          }
#RSS_FEEDS = {'bbc':'http://feeds.bbci.co.uk/news/rss.xml',
#             'cnn':'http://rss.cnn.com/rss/edition.rss',
#             'fox':'http://feeds.foxnews.com/foxnews/latest',
#             'iol':'http://www.iol.co.za/cmlink/1.640'}

#
#@app.route("/")
#def home():
#  publication = get_value_with_fallback('publication')
#  articles=get_news(publication)

#  response = make_response(render_template("home.html", articles=articles))
#  expires = datetime.datetime.now() + datetime.timedelta(days=365)
#  response.set_cookie("publication",publication,expires=expires)
#  return response

#def get_news(query):
#  if not query or query.lower() not in RSS_FEEDS:
#    query = DEFAULTS['publication']
#  else:
#  publication =  query.lower()
#  feed = feedparser.parse(RSS_FEEDS[publication])
#  return feed['entries']


#def get_value_with_fallback(key):
#  if request.args.get(key):
#    return request.args.get(key)
#  if request.cookies.get(key):
#    return request.cookies.get(key)
#  return DEFAULTS[key]

if __name__ == '__main__':
  app.run(port=5300,debug=True)

