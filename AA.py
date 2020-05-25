#!/usr/bin/env python
# coding:utf-8
import requests
import json
r = requests.get('https://faria.openapply.cn/api/v1/students?auth_token=12345678906&per_page=10');
res = r.text
response = json.loads(res)
students = response.get('students')
print(students)
for s in students:
    print (s['name'],',',s['id'],',',s['email'],',',s['status'])
for s in students:
    if s['id'] == 1:
        print (s['name'],',',s['id'],',',s['email'],',',s['status'])
for s in students:
    if s['email'] == "billy.spencer@cogidoo.edu":
        print (s['name'],',',s['id'],',',s['country'],',',s['status'])
for s in students:
    if s['grade'] == "Grade 6":
        print (s['name'],',',s['id'],',',s['campus'],',',s['status'])
for s in students:
    if s['last_name'] == "Spencer":
        print (s['name'],',',s['id'],',',s['grade'],',',s['status'])
#添加了一行注释
#ccccc
#saaaaa
#AAA
#111111
#222222
#333333

#444
#555

#666
