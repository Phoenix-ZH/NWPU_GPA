#!/usr/bin/python3
# -*- coding: latin-1 -*-
import requests
studentAssoc=input()
SESSION=input()
__pstsid__=input()
'''
249208
c24a323e-acf8-4c55-bad2-904877ef5c13
3f632e12718fb0de7213cdcfe78d0c0f
'''
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Cookie': 'SESSION=' + SESSION + ';__pstsid__=' + __pstsid__,
    'Referer': 'https://jwxt.nwpu.edu.cn/student/for-std/student-portrait',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'studentAssoc': studentAssoc,
    'semesterAssoc': '',


}
response = requests.get('https://jwxt.nwpu.edu.cn/student/for-std/student-portrait/getMyGrades', params=params, headers=headers)
print(response.text)

