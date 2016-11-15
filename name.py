#-*- coding: UTF-8 -*-
#!/usr/bin/env python # -*- coding: utf-8 -*- 
import re
import xlsxwriter
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

type=sys.getfilesystemencoding()

workbook = xlsxwriter.Workbook('say.xlsx')
worksheet = workbook.add_worksheet()
worksheet.set_column('A:A', 40)
worksheet.set_column('B:B', 10)
worksheet.set_column('C:C', 200)

with open('chatlog.txt') as f:
    s = f.read()
    pa = re.compile(r'^(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) 15资环 王伟懿\(442647835\)\n(.*?)\n$',re.DOTALL+re.MULTILINE)
    ma = re.findall(pa,s)
    # print(len(ma))
    for i in range(len(ma)):
        # print(ma[i][0])
        date = ma[i][0]
        time = ma[i][1]
        word = ma[i][2]

        worksheet.write(int(i),0,date)
        worksheet.write(int(i),1,time)
        worksheet.write(int(i),2,word)

    workbook.close()
    print  '处理完成'.decode('utf-8').encode(type)

