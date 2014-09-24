
from html.parser import HTMLParser

import urllib.request
import urllib.parse
import re

#params = urllib.parse.urlencode( {'cid': 1, 'eggs': 2, 'bacon': 0})
#site = urllib.request.urlopen("http://www.musi-cal.com/cgi-bin/query?%s" % params)
#print(site.read().decode('utf-8'))
#site = urllib.request.urlopen('http://souke.xdf.cn/Course/1-3858.html?v=5')

startRecNo = 0 #

inFile1 = 'xdf_souke_class_2014_0503.txt'     // Old Search
inFile2 = 'xdf_souke_class_2014_0504.txt'     // New Search
outFile = 'xdf_souke_class_2014_merged.txt'   // Merged Result

tableDate = [ "一","二","三","四", "五", "六","七","八","九","十","十一","十二"]

# tableDate = tableDate5
tableRange =[ "2014/1/1", "2015/1/1" ]

def str2time(txt):
#string example: "9:00-1:30"
  text = re.split(r'-', txt)
  start = re.split(r':', text[0])
  end = re.split(r':', text[1])
  start = [int(start[0]), int(start[1])]
  end = [int(end[0]), int(end[1])]
  minutes1 = start[0]*60 + start[1]
  minutes2 = end[0]*60 + end[1]
  if minutes2 - minutes1 > 0:
    totaltime = minutes2 - minutes1
  else: 
    totaltime = (720-minutes1) + minutes2
  return str(totaltime)

def getSeason(txt):
#string example: "2014/11/30"
  sid = 'x3300001111222233'
  stbl = [  '春季', '暑假', '秋季','寒假' ]
  sm = re.split(r'/', txt)[1]
  season = stbl[int(sid[int(sm[0])])]
  return season

from datetime import date

def getCourseStatus(t_st, t_ed):
#string example: "2014/03/04"
  date_s = re.split(r'/', t_st)
  date_e = re.split(r'/', t_ed)
  dateStart = date( int(date_s[0]), int(date_s[1]),int(date_s[2])) 
  dateEnd = date( int(date_e[0]), int(date_e[1]),int(date_e[2]))
  dateToday = date.today()

  cStatus = '接受报名'
  if dateToday < dateStart:
    cStatus = '接受报名'
  if dateToday >= dateStart and dateToday < dateEnd:
    cStatus = '已开课'
  if dateToday > dateEnd:
    cStatus = '已结束'
  return cStatus

# Prepare Output    

s = '\t'

cityName1 = ""
cityName2 = "beijing"

# if startRecNo == 0 :


fcs = open( outFile, 'w',encoding="utf-8")
if tableType == 0 :
  fcs.write( s+s+s+s+"新东方搜课平台 -业务统计表-\n" )
else:
  fcs.write( s+s+s+s+"新东方搜课平台 -城市业务统计表-\n" )
fcs.write( s+s+s+s+s+s+str(date.today()) + "\n" )


#  fcs.close()


"""
##############################

##############################
"""


#tableCol = [ 0,0,0,  0,0,0,  0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0]

#tableRow = [ tableCol_0, tableCol_1, tableCol_2 , tableCol_3 , tableCol_4 , tableCol_5 , tableCol_6 , tableCol , tableCol , tableCol , tableCol , tableCol  ]

#classData1 = tableCol + tableCol + tableCol+ tableCol+ tableCol+ tableCol+ tableCol+ tableCol+ tableCol+ tableCol+ tableCol+ tableCol+ tableCol

classData = [0 for i in range(36*12)]

# print( tableRow[0][0:2] )

date_s = re.split(r'/', tableRange[0] )
date_e = re.split(r'/', tableRange[1] )
dateStart = date( int(date_s[0]), int(date_s[1]),int(date_s[2])) 
dateEnd = date( int(date_e[0]), int(date_e[1]),int(date_e[2]))


f = open( inFile1, 'r', encoding="utf-8" )
f2 = open( inFile2, 'r', encoding="utf-8" )
f3 = open( outFile, 'w', encoding="utf-8" )

rtemp = ""
list1 = []

for line in f:
  lineItems = re.split(r'\t', line)

  if lineItems[3] == rtemp:
    f3.write(line + "\n")
    list1.append(lineItems[5])
  else:
    if list1 == null:
      list1.append(lineItems[5])
      f3.write(line + "\n")
    else: 
      for line2 in f2:
        lineItems2 = re.split(r'\t', line2)
        if lineItems2[3] == rtemp:
          if lineItems2[5] not in list1:
            f3.write(line2 + "\n")
            list1.append(lineItems2[5]) 
        else:
          break
  rtemp = lineItems[3]

"""
for line in f:
  lineItems = re.split( r'\t', line)

  cityName2 = lineItems[2]
  if cityName1 == "" :
    cityName1 = cityName2
    
  if cityName1 != cityName2 :
    if tableType == 1:
      fcs.write( "\n\n\n"+s+cityName1+"\n")
      fcs.write( s+s+s+"中学"+s+s+s+"小学及以下"+s+s+s+s+"出国留学"+s+s+s+s+s+s+"大学考试"+s+s+s+s+s+s+"多语种（英，法...)"+s+s+s+s+s+s+"其他业务（冬夏令营）"+s+s+s+s+s+s+"合计"+ "\n" )
      fcs.write( s+"跟踪月份"+s+"人数"+s+"收入(百万）"+s+"班次"+s+"人数"+s+"收入(百万）"+s+"班次"+s+"人数"+s+"收入(百万）"+s+"班次"+s+"大班人数"+s+"大班收入(百万）"+s+"大班班次"+s+"人数"+s+"收入(百万）"+s+"班次"+s+"大班人数"+s+"大班收入(百万）"+s+"大班班次"+s+"人数"+s+"收入(百万）"+s+"班次"+s+"大班人数"+s+"大班收入(百万）"+s+"大班班次"+s+"人数"+s+"收入(百万）"+s+"班次"+s+"大班人数"+s+"大班收入(百万）"+s+"大班班次"+s+"人数"+s+"收入(百万）"+s+"班次"+s+"大班人数"+s+"大班收入(百万）"+s+"大班班次"+"\n" )  
#
      for i in range(0, 12):
        rowStr = ""
        for j in range(0,36,3):
          rowStr = rowStr + s + str(classData[i*36+j])
          rowStr = rowStr + s + '{:0.2f}'.format(classData[i*36+j+1])
          rowStr = rowStr + s + str(classData[i*36+j+2])
          #print( tableDate[i], rowStr )
        fcs.write( s+tableDate[i] + rowStr + "\n" )
#
      classData = [0 for i in range(36*12)]
      cityName1 = cityName2

#  print( lineItems[2], lineItems[4], lineItems[13], lineItems[14] )

  if lineItems[4] in ["学前辅导", "小学辅导"]:
    iCol = 3
  elif lineItems[4] == "中学辅导":
    iCol = 0
  elif lineItems[4] == "出国留学":
    iCol = 6
  elif lineItems[4] == "大学考试": 
    iCol = 12
  elif lineItems[4] in ["英语学习","小语种" ]: 
    iCol = 18
  else:  #
    iCol = 24
    
  iYear = re.split( r'/', lineItems[13])[0]
  iMon = re.split( r'/', lineItems[13])[1]
  iDat = re.split( r'/', lineItems[13])[2]

  
  if int(iDat) >= 7:
    iRow = int(iMon)
  else:
    iRow = int(iMon)-1

  if iRow >= 12:
    iRow = 0
  

  iRow = int(iMon)-1
  
  if lineItems[11] in ["", "大班"]:
    cNumber = 100
#    m = re.search(r'50人', lineItems[6])
#    if m :
#      cNumber = 50
    if iCol >= 6:
      iCol = iCol + 3
  else:
    cNumber = int( lineItems[11] )

  if int(lineItems[1]) % 10000 == 0 :
    print( lineItems[1])
    
#  iRow =  iMon
  dateClass = date( int(iYear), int(iMon),int(iDat) )
  
#  if iYear == "2014" :
  if (dateClass >= dateStart and dateClass < dateEnd ):
    # print( tableRange[0], iYear, iMon, iDat, tableRange[1], dateStart, dateClass, dateEnd )
    classData[iRow*36+iCol] = classData[iRow*36+iCol] + cNumber
    classData[iRow*36+iCol+1] = classData[iRow*36+iCol+1] + cNumber * float( lineItems[20] )/1000000.0
    classData[iRow*36+iCol+2] = classData[iRow*36+iCol+2] + 1

    classData[iRow*36+30] = classData[iRow*36+30] + cNumber
    classData[iRow*36+30+1] = classData[iRow*36+30+1] + cNumber * float( lineItems[20] )/1000000.0
    classData[iRow*36+30+2] = classData[iRow*36+30+2] + 1
    if iCol in [ 9, 15, 21, 27 ] :
      classData[iRow*36+33] = classData[iRow*36+33] + cNumber
      classData[iRow*36+33+1] = classData[iRow*36+33+1] + cNumber * float( lineItems[20] )/1000000.0
      classData[iRow*36+33+2] = classData[iRow*36+33+2] + 1
#  else :
#    print( tableRange[0], iYear, iMon, iDat, tableRange[1], lineItems[1], lineItems[2], lineItems[4] )
    #tableRow[iRow][iCol] = tableRow[iRow][iCol] + cNumber   # 人数
    #tableRow[iRow][iCol+1] = tableRow[iRow][iCol+1] + cNumber * int( lineItems[20] ) # 收入
    #tableRow[iRow][iCol+2] = tableRow[iRow][iCol+2] + 1  # 班次
    #print( lineItems[2], lineItems[4], lineItems[11], lineItems[13], tableDate[iRow], str(iCol), str(classData[iRow*30+iCol]), str(classData[iRow*30+iCol+1]), str(classData[iRow*30+iCol+2]) )

  
#print( txt )

#  f2 = open( 'souke_course_temp.txt', 'w', encoding="utf-8")
#  f2.write( line )
#  f2.close()

f.close()

# fcs = open( outFile, 'a',encoding="utf-8")

if tableType == 1:
  fcs.write( "\n\n\n"+s+cityName1+"\n")
fcs.write( s+s+s+"中学"+s+s+s+"小学及以下"+s+s+s+s+"出国留学"+s+s+s+s+s+s+"大学考试"+s+s+s+s+s+s+"多语种（英，法...)"+s+s+s+s+s+s+"其他业务（冬夏令营）"+s+s+s+s+s+s+"合计"+ "\n" )
fcs.write( s+"跟踪月份"+s+"人数"+s+"收入(百万）"+s+"班次"+s+"人数"+s+"收入(百万）"+s+"班次"+s+"人数"+s+"收入(百万）"+s+"班次"+s+"大班人数"+s+"大班收入(百万）"+s+"大班班次"+s+"人数"+s+"收入(百万）"+s+"班次"+s+"大班人数"+s+"大班收入(百万）"+s+"大班班次"+s+"人数"+s+"收入(百万）"+s+"班次"+s+"大班人数"+s+"大班收入(百万）"+s+"大班班次"+s+"人数"+s+"收入(百万）"+s+"班次"+s+"大班人数"+s+"大班收入(百万）"+s+"大班班次"+s+"人数"+s+"收入(百万）"+s+"班次"+s+"大班人数"+s+"大班收入(百万）"+s+"大班班次"+"\n" )  
for i in range(0, 12):
  rowStr = ""
  for j in range(0,36,3):
    rowStr = rowStr + s + str(classData[i*36+j])
    rowStr = rowStr + s + '{:0.2f}'.format(classData[i*36+j+1])
    rowStr = rowStr + s + str(classData[i*36+j+2])
#  print( tableDate[i], rowStr )
  fcs.write( s+tableDate[i] + rowStr + "\n" )

fcs.close()

 """
