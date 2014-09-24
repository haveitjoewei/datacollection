
import urllib.request
import urllib.parse

#params = urllib.parse.urlencode( {'span': 1, 'eggs': 2, 'bacon': 0})
#site = urllib.request.urlopen("http://www.musi-cal.com/cgi-bin/query?%s" % params)
#print(site.read().decode('utf-8'))

site = urllib.request.urlopen('http://souke.xdf.cn/')

txt = site.read().decode('utf-8')

#print( txt )

f = open( 'souke_home.xml', 'w',encoding="utf-8")
f.write( txt )
f.close()

from html.parser import HTMLParser  
          
class CityHTMLParser(HTMLParser):

  f1 = open( 'city_url.txt', 'w',encoding="utf-8")
  
  def __init__(self):
    HTMLParser.__init__(self)
    self.recording = 0
    self.isfound = 0
    self.cityid=[]
    self.href = []
    self.data = []
  def handle_starttag(self, tag, attrs):
    if tag != 'a' : return

    for name, value in attrs:
        if name == 'cid':
          self.cityid = value
        if name == 'href':
          self.href = value
          self.recording = 1 
        if name == 'class' and value == 'cityChange' :
          self.isfound = 1
  #        print ("Encountered the beginning of a %s tag" % tag )

  def handle_endtag(self, tag):
    if tag == 'a':
      self.recording -=1
      if self.isfound == 1:
#          print( self.cityid, self.href, self.data)
          self.f1.write( self.href+"\n" )
          print( self.href)
          self.isfound -=1
 #         print ( "Encountered the end of a %s tag" % tag )

  def handle_data(self, data):
    if self.recording:
      self.data = data

p = CityHTMLParser()
# f = urllib2.urlopen('http://www.someurl.com')
# html = f.read()
p.feed(txt)
#print( p.data )
p.f1.close()
p.close()

 
#parser = MyHTMLParser(strict=False)
#parser.feed(txt)
