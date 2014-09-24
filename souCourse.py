
import urllib.request
import urllib.parse


#params = urllib.parse.urlencode( {'cid': 1, 'eggs': 2, 'bacon': 0})
#site = urllib.request.urlopen("http://www.musi-cal.com/cgi-bin/query?%s" % params)
#print(site.read().decode('utf-8'))

#site = urllib.request.urlopen('http://souke.xdf.cn/Course/1-3858.html?v=5')


from html.parser import HTMLParser  
          
class CourseHTMLParser(HTMLParser):
#  classNum=[]  # Class Num
#  pNum = []    # Class Size
#  location = []    #
  fcs = open( 'city_cat_class_course.txt', 'w',encoding="utf-8")
  def __init__(self):
    HTMLParser.__init__(self)
    self.recording = 0
    self.isfound = 0
    self.courseStart=0
    self.courseEnd=0
    self.sTag = []
    self.items = 0
    self.classNum=[]  # Class Num
    self.pNum = []    # Class Size
    self.location = []    #
    self.start = []
    self.end = []
    self.times = []
    self.price =[]
    self.data = []
    
  def handle_starttag(self, tag, attrs):
    self.sTag = tag
    if tag == 'div' :
        for name, value in attrs:
            if name == 'id' and value == 'course_class_list':
                self.courseStart += 1
        return
    if self.courseStart != 0:
 #       print( attrs )
        for name, value in attrs:
            if name == 'class' and value == 'classNum' :
              self.items = 1
            if name == 'class' and value == 'pNum' :
              self.items = 2
            if name == 'class' and value == 'tLists' :
              self.items = 3
            if name == 'areaname':
              self.location = value
              self.items = 0
            if name == 'class' and value == 'price' :
              self.items = 4
              self.courseEnd = 1
 #   if tag = 'div':
 #     self.courseEnd -= 1
  #        print ("Encountered the beginning of a %s tag" % tag )
  def handle_endtag(self, tag):
    if self.items == 1 and tag == 'a':
      self.classNum = self.data
      self.itmes = 0
    if self.items == 2 and tag == 'span':
      self.pNum = self.data
      self.itmes = 0
    if self.items == 3 and tag == 'dd':
#      print(self.data)
      self.start = self.data[0:8]
      self.end = self.data[11:19]
      xlen = len(self.data)
      self.times = self.data[xlen-5:xlen-4]
      self.itmes = 0
    if self.items == 4 and tag == 'em':
      self.price = self.data
      self.itmes = 0

    if self.courseEnd != 0:
      print( self.classNum, self.pNum, self.start, self.end, self.location, self.price )
      s = '\t'
      self.fcs.write( self.classNum+s+self.pNum+s+self.start+s+self.end+s+self.location+"\n" )
      self.items = 0
      self.classNum=[]
      self.courseEnd=0
 #     self.courseStart=0
 #         print ( "Encountered the end of a %s tag" % tag )

  def handle_data(self, data):
#    if self.items != 0:
#      print( data )
    self.data = data
 
    

p = CourseHTMLParser()

# f = urllib2.urlopen('http://www.someurl.com')
# html = f.read()

f = open( 'city_cat_class_url_1.txt', 'r', encoding="utf-8" )

for line in f:
  
  site_url = "http://souke.xdf.cn" + line[:-1]
  print( site_url )

  site = urllib.request.urlopen( site_url)
  txt = site.read().decode('utf-8')

#print( txt )

  f2 = open( 'souke_class_course_temp.txt', 'w', encoding="utf-8")
  f2.write( txt )
  f2.close()

  p.feed(txt)

"""
  if int(p.page) > 1 :
    for i1 in range(int(p.page)-1):
      site_url1 = site_url + "&page=" + str(i1+2) + "&pagesize=10"
      print( site_url1 )
      site = urllib.request.urlopen( site_url1)
      txt = site.read().decode('utf-8')
      p.feed(txt)
"""
#print( p.data )
  
p.fcs.close()

p.close()

f.close()
 
#parser = MyHTMLParser(strict=False)
#parser.feed(txt)
