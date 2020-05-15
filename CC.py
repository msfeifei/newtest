#!/usr/bin/env python
# coding:utf-8
import requests
import json
r = requests.get('https://faria.openapply.cn/api/v1/students?auth_token=12345678906&per_page=10');
print(r); #<Response [200]>
res = r.text #获取文本
print('输出json数组res：'+ res); #输出str
response = json.loads(res);
print(response); #输出python字典 dict
print('response:',type(response))
students = response.get('students') #得到students --key list
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