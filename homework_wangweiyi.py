#!/usr/bin/env python
#-*- coding: UTF-8 -*_

__author__ = 'wangweiyi'

#Chinese
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#.decode('utf-8').encode(type)
type=sys.getfilesystemencoding()

import re
import xlsxwriter as xls

#creat excel file
workbook  = xls.Workbook('homework.xlsx')
worksheet = workbook.add_worksheet('homework')

#load data
file = open('chat.txt')
data = file.read()
file.close

#get people who spoke sth
con_peo  = re.compile(r'\(\d{3,12}\)')
people   = re.findall(con_peo, data)
peo_list = list(set(people))

#extract list
count = []
for i in range(0, len(peo_list)):
	t   = peo_list[i]
	p   = re.compile(t) 
	m   = re.findall(p, data)
	l   = len(m)
	peo = [l, t]
	count.append(peo)

#sort
coun = sorted(count, reverse=True)

#print all
row =0
for j in range(0, len(coun)):
	worksheet.write(row, 0, coun[j][1])
	worksheet.write(row, 1, coun[j][0])
	row += 1
#print top10
r = 0
for k in range(0,10):
	worksheet.write(r, 4, coun[k][1])
	worksheet.write(r, 5, coun[k][0])
	r += 1

#close book
workbook.close()
print('打印结束'.decode('utf-8').encode(type))

