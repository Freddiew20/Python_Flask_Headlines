from flask import Flask
import feedparser
from flask import render_template

app= Flask(__name__)

BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"
CNN_FEED = "http://rss.cnn.com/rss/edition.rss"
FOX_FEED = "http://feeds.foxnews.com/foxnews/latest"
IOL_FEED = "http://www.iol.co.za/cmlink/1.640"

@app.route("/")
def get_news():
  feed = feedparser.parse(BBC_FEED)
  feedn = feedparser.parse(CNN_FEED)
  feedf = feedparser.parse(FOX_FEED)
  feedi = feedparser.parse(IOL_FEED)
  return render_template("home.html", bbc=feed['entries'], cnn=feedn['entries'], fox=feedf['entries'], iol=feedi['entries'])

if __name__ == '__main__':
  app.run(port=5300,debug=True)

