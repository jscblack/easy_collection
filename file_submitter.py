'''
Author       : Gehrychiang
LastEditTime : 2021-03-05 17:56:51
Website      : www.yilantingfeng.site
E-mail       : gehrychiang@aliyun.com
ProbTitle    : (记得补充题目标题)
'''
# filesubmitter
# TSM1PL6kY8MWeVXwPQzugFJWynVLChuY
import upyun
import tkinter
from tkinter import filedialog
import requests
import os
import sys
bucket_name='*'
operator_name='*'
operator_token='*'
'''获取上传地址'''
print("Syncing data with server....\n")
r = requests.get('http://api.yilantingfeng.site/', params={'type':'fsub'})
title =r.json()['data']['title']
underway=r.json()['data']['underway']
if int(underway) == 0:
    print("Collection has ended!")
    os.system('pause')
    sys.exit(5)
print('Collecting: ',title,'\n')
print('Please select the file you want to upload\n')
'''打开选择文件夹对话框'''
root = tkinter.Tk()
root.withdraw()
Filepath = filedialog.askopenfilename() #获得选择好的文件
if not(len(Filepath)):
    print("Invalid operation, Please retry!")
    os.system('pause')
    sys.exit(1)
print('You choose: ',Filepath,'\n')
'''获取文件后缀'''
file_suffix = Filepath.split(".")[1]
name=input("Please input your name\n")
stu_ID=input("Please input your student ID\n")
'''获得名称'''
if not((len(name)) and (len(stu_ID)==10)and stu_ID.isalnum):
    print("Invalid input, Please retry!")
    os.system('pause')
    sys.exit(2) 
Remotepath = eval(r.json()['data']['remotepath'])
'''上传'''
up = upyun.UpYun(bucket_name, operator_name, operator_token, timeout=60, endpoint=upyun.ED_AUTO)
headers = { 'py_file_submiter': '180' }
with open(Filepath, 'rb') as f:
    try:
        res = up.put(Remotepath, f, checksum=True, headers=headers)
    except:
        print("Upload failed, Please retry!")
        os.system('pause')
        sys.exit(3)
print("Upload Succeed, Thank you!")
os.system('pause')
