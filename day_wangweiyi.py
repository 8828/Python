#!/usr/bin/env python
#-*- coding: UTF-8 -*-

#Chinese
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#.decode('utf-8').encode(type)
type=sys.getfilesystemencoding()

import re
import xlsxwriter as xls

#load data
file = open('chat.txt')
data = file.read()
file.close

#find 2016-month-day
con = re.compile(r'2016-\d{2}-(\d{2})')
res = con.findall(data)

day_count_list = []

for day in range(1,32):
	if day >= 13 and day <= 18:
		continue
	count = 0
	
	if day >= 1  and day <= 9:
		day = '0' + str(day)

	else:
		day = str(day)
	
	for days in res:
		if days == day:
			count += 1
	day_count_list.append([day, count])

#creat excel file
day_book  = xls.Workbook('day.xlsx')
day_sheet = day_book.add_worksheet('day_10_11')  

#write in created excel file
row = 0
for day_count in day_count_list:
	day_sheet.write(row, 0, day_count[0])
	day_sheet.write(row, 1, day_count[1])
	row = row + 1
day_book.close()

print('打印成功'.decode('utf-8').encode(type))
