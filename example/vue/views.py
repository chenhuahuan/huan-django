from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import json

def hello(request):
    page = request.GET.get('page') #从前端获取listQuery参数中的数据
    limit = request.GET.get('limit') #从前端获取listQuery参数中的数据
    mytype = request.GET.get('type')#从前端获取listQuery参数中的数据
    sort = request.GET.get('sort')#从前端获取listQuery参数中的数据
    dict1 = {}  # 第一行数据
    dict1['id'] = '1'
    dict1['date'] = '606208526029'
    dict1['title'] = 'my title'
    dict1['author'] = 'james'
    dict1['reviewer'] = 'Larry'
    dict1['importance'] = '1'
    dict1['readmings'] = '1'
    dict1['status'] = 'draft'
    dict1['actions'] = '1'
    dict1['edit'] = '1'
    dict1['publish'] = '1'
    dict1['draft'] = '0'
    dict1['content_short'] = 'it is a test'
    dict1['content'] = 'ceshishuju'
    dict1['forecast'] = 99.11
    dict1['type'] = 'JP'
    dict1['status'] = 'draft'
    dict1['display_time'] = '1994-05-26 18:59:04'
    dict1['comment_disabled'] = 'true'
    dict1['pageviews'] = 1823
    dict1['image_uri'] = 'https://wpimg.wallstcn.com'
    dict1['platforms'] = ['a-platform']
    dict2 = {} # 第二行数据
    dict2['id'] = '2'
    dict2['date'] = '602208526029'
    dict2['title'] = 'my title2'
    dict2['author'] = 'james2'
    dict2['reviewer'] = 'Larry2'
    dict2['importance'] = '2'
    dict2['readmings'] = '2'
    dict2['status'] = 'draft'
    dict2['actions'] = '1'
    dict2['edit'] = '1'
    dict2['publish'] = '1'
    dict2['draft'] = '0'
    dict2['content_short'] = 'it is a test2'
    dict2['content'] = 'ceshishuju2'
    dict2['forecast'] = 99.22
    dict2['type'] = 'CN'
    dict2['status'] = 'draft'
    dict2['display_time'] = '1994-05-26 18:59:04'
    dict2['comment_disabled'] = 'true'
    dict2['pageviews'] = 2000
    dict2['image_uri'] = 'https://wpimg.wallstcn.com'
    dict2['platforms'] = ['a-platform']
    mylist = list()
    mylist.append(dict1)
    mylist.append(dict2)
    resultlist = list()
    if mytype == '' or None: #根据请求参数不同，返回的数据不同
        resultlist = mylist
    else:
        for mydict in mylist:
            if mydict['type'] == mytype:
                resultlist.append(mydict)

    return HttpResponse(json.dumps(resultlist),content_type="application/json") #这里返回Json格式数据

