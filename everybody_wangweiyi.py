#!/usr/bin/env python
#-*- coding: UTF-8 -*_

#Chinese
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#.decode('utf-8').encode(type)
type=sys.getfilesystemencoding()

import re
import xlsxwriter as xls

#creat excel file,set coloum width
workbook  = xls.Workbook('mem.xlsx')
worksheet = workbook.add_worksheet('1')
worksheet.set_column('A:EB', 15)

#load data
file = open('chat.txt')
data = file.read()
file.close

#get people who spoke sth
con_peo  = re.compile(r'\(\d{3,12}\)')
people   = re.findall(con_peo, data)
peo_list = list(set(people))

#loop for date-time
count      = 0
row        = 0
elem       = 0
count_list = []

for num in peo_list:
	con  = re.compile(r'^2016-\d{2}-(\d{2}).*'+num, re.M)
	days = re.findall(con, data)
	elem = elem + 4
	count_list = []
	for i in range(1, 32):
		if 13 <= i <=18:
			continue
		
		if i <= 9:
			day = '0'+ str(i)
		else:
			day = str(i)
		
		for ele in days:
			if ele[0] == day:
				count += 1
		cou   = [day, count]
		count_list.append(cou)
		count = 0
		row   = 0
		#print(count_list)				
	for j in count_list:
		worksheet.write(row, elem - 3, j[0])
		worksheet.write(row, elem - 2, j[1])
		worksheet.write(0,   elem - 4, num )
		worksheet.write(row, elem - 1, '##')
		row += 1



workbook.close()
print('打印'.decode('utf-8').encode(type))



