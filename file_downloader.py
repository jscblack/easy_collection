'''
Author       : Gehrychiang
LastEditTime : 2021-03-05 17:54:13
Website      : www.yilantingfeng.site
E-mail       : gehrychiang@aliyun.com
ProbTitle    : (记得补充题目标题)
'''
# filesubmitter
# TSM1PL6kY8MWeVXwPQzugFJWynVLChuY
# filedownloader
# 4ydSRMSkOUefyBeZenFTRhj6jOXc1Asr
import upyun
import requests
import os
import sys
import json
bucket_name='*'
operator_name='*'
operator_token='*'
up = upyun.UpYun(bucket_name, operator_name, operator_token, timeout=60, endpoint=upyun.ED_AUTO)
headers = { 'py_file_submiter': '180' }
print("Syncing data with server....\n")
r = requests.get('http://api.yilantingfeng.site/', params={'type':'fsub'})
title =r.json()['data']['title']
print('Collecting: ',title,'\n')
print("To continue, please input the authorization code")
psd=input()
q = requests.get('http://api.yilantingfeng.site/', params={'type':'fsub','pwd':psd})
if not(q.json()['msg'] == "pass"):
    print("Invalid authorization code!")
    os.system('pause')
    sys.exit(1)
print("Authorization checked!")
underway=r.json()['data']['underway']
if int(underway) == 1:
    print("Collection has not ended!\n")
    print("Confirm downloading?\n")
    req=input("input yes for futher proceeder   ")
    if not(req == "yes"):
        os.system('pause')
        sys.exit(1)
path = os.getcwd()+'\\'+title
if not(os.path.exists(path)):
    os.mkdir(path)
res = up.getlist('/'+title+'/')
for i in range(len(res)):
    print("downloading: "+res[i]['name']+'\n')
    if(os.path.exists(path+'\\'+res[i]['name'])):
        os.remove(path+'\\'+res[i]['name'])
    with open(path+'\\'+res[i]['name'], 'wb') as f:
        up.get('/'+title+'/'+res[i]['name'], f)
print("download succeed!")
os.system('pause')