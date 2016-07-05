#-*- coding:utf8 -*-
# name: 身份证号码生存器0.1.1
# author: Sola
# data:24Jun2016

#!/usr/bin/env python
#-*-coding:utf8-*-
import random
import os
import time


def id_creator(distinct='341003', birth=time.strftime("%Y%m%d", time.localtime())):
    last42 = random.randint(0,99)
    if last42 < 10:
        last3 = '0' + str(last42)
    else:
        last3 = str(last42)
    gender = input("请输入性别(男性=1,女性=0):".decode('utf8').encode('gbk'))
    last2 = filter(lambda i: i % 2 == gender, range(10))[random.randint(0,4)]
    first_seventeen = distinct + birth + last3 + str(last2)
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    d = 0
    for i in range(len(first_seventeen)):
        d += int(first_seventeen[i]) * weight[i]
    rslt = [1, 0, 'x', 9, 8, 7, 6, 5, 4, 3, 2]
    print '-' * 20
    print "身份证号码是: ".decode('utf8').encode('gbk'), first_seventeen + str(rslt[d%11])
    print '\n'

def main():
    print "非本地户籍请输入 ----->> e <<".decode('utf8').encode('gbk')
    print "生成身份证号码请输入 ->> w <<".decode('utf8').encode('gbk')
    print "无出生日期请输入 ----->> r <<".decode('utf8').encode('gbk')
    print "退出请输入 ---------->> q <<".decode('utf8').encode('gbk')
    code = raw_input("请输入命令:".decode('utf8').encode('gbk')).lower()
    if code == 'e':
        distinct = raw_input("请输入新的地区编码:".decode('utf8').encode('gbk'))
        if len(distinct) == 6:
            birth = raw_input("请输入出生日期(格式:yyyymmdd):".decode('utf8').encode("gbk"))
            try:
                if len(birth) == 0:
                    id_creator(distinct=distinct)
                if time.strptime(birth, '%Y%m%d'):
                    id_creator(distinct=distinct, birth=birth)
            except:
                print '请输入正确的日期格式 \n'.decode('utf8').encode('gbk')
        else:
            print '请输入6位数地区编码 \n'.decode('utf8').encode('gbk')
        main()
    if code == 'w':
        birth = raw_input("请输入出生日期(格式:yyyymmdd):".decode('utf8').encode("gbk"))
        try:
            if len(birth) == 0:
                id_creator()
            if time.strptime(birth, '%Y%m%d'):
                id_creator(birth=birth)
        except:
            print "请输入正确的日期格式 \n".decode('utf8').encode('gbk')
        main()
    if code == 'r':
        age = input("请输入年龄:".decode('utf8').encode("gbk"))
        year = str(int(time.strftime("%Y", time.localtime())) - age)
        month = time.strftime("%m%d", time.localtime())
        birth = year + month
        id_creator(birth=birth)
        main()
    if code == 'q':
        os.system("exit")
    else:
        print '请输入正确的命令'.decode('utf8').encode('gbk')


if __name__ == "__main__":
    main()
