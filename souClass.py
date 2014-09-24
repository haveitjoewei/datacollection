
import urllib.request
import urllib.parse


#params = urllib.parse.urlencode( {'cid': 1, 'eggs': 2, 'bacon': 0})
#site = urllib.request.urlopen("http://www.musi-cal.com/cgi-bin/query?%s" % params)
#print(site.read().decode('utf-8'))

#site = urllib.request.urlopen('http://souke.xdf.cn/Course/1-3858.html?v=5')


from html.parser import HTMLParser  
          
class ClassHTMLParser(HTMLParser):
  fcat = open( 'city_cat_class_url.txt', 'w',encoding="utf-8")
  def __init__(self):
    HTMLParser.__init__(self)
    self.recording = 0
    self.isfound = 0
    self.catStart=0
    self.page = 0
    self.page1 = 0
    self.href = []
    self.data = []    
  def handle_starttag(self, tag, attrs):
    self.sTag = tag
    if tag == 'select' :
        for name, value in attrs:
            if name == 'id' and value == 'page01_pagesize':
                self.page = self.page1
                print( "page:", self.page )
    if tag == 'a' :
        for name, value in attrs:
            if name == 'class' and value == 'u-btn':
                self.catStart += 1
    if self.catStart != 0:
         for name, value in attrs:
            if name == 'href':
              self.href = value
              self.fcat.write( self.href+"\n" )
              print( self.href )
  def handle_endtag(self, tag):
    if tag == 'a':
      self.catStart = 0
    if tag == 'option': self.page1 = self.data

  def handle_data(self, data):
#    if self.items != 0:
#      print( data )
    self.data = data
   
p = ClassHTMLParser()
# f = urllib2.urlopen('http://www.someurl.com')
# html = f.read()

f = open( 'city_cat_url_1.txt', 'r', encoding="utf-8" )

for line in f:
  
  site_url = "http://souke.xdf.cn" + line[:-1]
  print( site_url )

  site = urllib.request.urlopen( site_url)
  txt = site.read().decode('utf-8')

#print( txt )

  f2 = open( 'souke_class_temp.txt', 'w', encoding="utf-8")
  f2.write( txt )
  f2.close()

  p.feed(txt)
  if int(p.page) > 1 :
    for i1 in range(int(p.page)-1):
      site_url1 = site_url + "&page=" + str(i1+2) + "&pagesize=10"
      print( site_url1 )
      site = urllib.request.urlopen( site_url1)
      txt = site.read().decode('utf-8')
      p.feed(txt)

#print( p.data )
  
p.fcat.close()
p.close()

f.close()
 
#parser = MyHTMLParser(strict=False)
#parser.feed(txt)
