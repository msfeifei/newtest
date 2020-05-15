#!/usr/bin/env python
# coding:utf-8
#官网下载git  （在终端输入 brew install git）
#在终端输入 git --version
#然后配置用户
#git config --global username 'MengruHan'
#git config --global email 'ru.han@openapply.com'
#global是修饰的是全局的用户
#若需设置单个用户，可在项目目录下输入
#git config username "MengruHan"
# git config email "ru.han#openapply.com"
#查看当前用户下的信息
#git config — list
#然后在GitHub创建一个库（python-）
#cd 到项目目录下
# git init 创建一个仓
#git add  AA.py项目里面的文件添加到缓存中
#git commit -m '测试'将缓存的文件commit到git库
#本地连接到远程
# git remote add origin https://github.com/MengruHan/python-
#git pull
# 执行git pull origin master
#执行git push origin master
#碰到的问题
#1.在push时会要求输入username 和 password，我在输入正确的username和password之后一直报错如下：
#remote: Invalid username or password.
#fatal: Authentication failed for 'https://github.com/MengruHan/python-test/'
# 我是在这个link上面看到解决方法
# https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-com
#然后按照步骤创建了一个Personal access token
#然后push的时候输入账号跟这个token就可以了
#2.push时一直需要输入账号和密码
#我是输入了一行
#git config --global credential.helper store
#然后再次push的时候在输入一次，往后就不用在输入了
#创建
#git branch newbranch
#查看分支
#git branch
#切换分支
#git checkout new branch
#提交改动到当前分支
#git add .
#git commit -a
#查看状态
#git status
#切回主分支
#git checkout master
#将新分支提交的改动合并到主分支上
#git merge new branch
#删除分支
#git branch -D newbranch