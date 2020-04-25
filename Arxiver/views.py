from django.shortcuts import render
from django.http import HttpResponse
import json
import requests
from bs4 import BeautifulSoup as bs
import json
import urllib
import os
from . import models
import hashlib
from django.forms.models import model_to_dict

class Paper:
        def __init__(self):
                self.author = []
                self.id = None
                self.updatedTime = None
                self.publishedTime = None
                self.title = None
                self.summary = None
                self.category = []
                self.doiLink = None
                self.paperLink = None
                self.pdfLink = None

def index(request):
    return HttpResponse(json.dumps('Hello World'))

def searchPaper(request):
    method = request.GET.get('method','ti')
    query = request.GET.get('query','electron')
    sortBy = request.GET.get('sortBy','lastUpdatedDate')
    sortOrder = request.GET.get('sortOrder','ascending')
    maxNum = request.GET.get('maxNum','10')
    url = "http://export.arxiv.org/api/query?search_query=" + method + ":" + query + "&sortBy="+sortBy+"&sortOrder="+sortOrder+"&max_results="+maxNum
    '''
    url = 'http://export.arxiv.org/api/query?search_query=ti:%22electron%20thermal%20conductivity%22&sortBy=lastUpdatedDate&sortOrder=ascending'
    '''  
    try:
        res = requests.get(url)
    except:
        res = dict()
        res['resCode'] = 404
        res = json.dump(res)
        return HttpResponse(res)
    data = res.text
    soup = bs(data,'lxml')
    entries = soup.find_all('entry')
    papers = []
    for entry in entries:
        newPaper = Paper()
        newPaper.id = entry.id.string
        newPaper.updatedTime = entry.updated.string
        newPaper.publishedTime = entry.published.string
        newPaper.title = entry.title.string
        newPaper.summary = entry.summary.string
        authors = entry.find_all('author')
        for author in authors:
            newPaper.author.append(author.contents[1].string)
        categories = entry.find_all('category')
        for category in categories:
            newPaper.category.append(category.get('term'))
        links = entry.find_all('link')
        for link in links:
            if link.get('title')=='doi':
                newPaper.doiLink = link.get('href')
            elif link.get('title')=='pdf':
                newPaper.pdfLink = link.get('href')
            else:
                newPaper.paperLink = link.get('href')
        papers.append(newPaper)
    res = dict()
    res['resCode'] = 200
    res['len'] = len(papers)
    res['papers'] = []
    for paper in papers:
        p = dict()
        p['author'] = ''
        for author in paper.author:
            p['author']+=(author+'/')
        p['id'] = paper.id
        p['updatedTime'] = paper.publishedTime
        p['title'] = paper.title
        p['summary'] = paper.summary
        p['category'] = ''
        for category in paper.category:
            p['category'] +=(category+'/')
        p['doiLink'] = paper.doiLink
        p['paperLink'] = paper.paperLink
        p['pdfLink'] = paper.pdfLink
        res['papers'].append(p)
    res = json.dumps(res)
    return HttpResponse(res)

def showPaper(request):
    url = request.GET.get('url',"http://arxiv.org/pdf/cond-mat/0402245v1")
    
    filename = url[-9:]+'.pdf'
    try:
        res = requests.get(url+'.pdf')
    except:
        res = dict()
        res['retCode'] = 404
        return HttpResponse(res)
    f = open(filename,'wb')
    f.write(res.content)
    f.close()
    with open (filename,'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
    os.remove(filename)
    return response
    '''
    fileurl = urllib.request.pathname2url(filename) 
    rp = dict()
    rp['retCode'] = 200
    rp['url'] = fileurl
    return HttpResponse(json.dumps(rp))
    '''


def recommendPaper(request):
    user = request.GET.get('user')
    '''
    获取user阅读记录
    根据阅读记录与其他用户计算相似度
    推荐相似度最高的用户的记录
    '''
    

'''
# demo所需函数
def choosePaper(request):
    return render(request, 'choose_paper.html')


def editComment(request):
    return render(request, 'post_comment.html')


def editReply(request):
    return render(request, 'post_reply.html')
'''


# 根据评论ID获取回复
# 非通信函数!!!
def getCommentReply(commentID=1, sortedBy='time'):
    res = []
    replys = []
    if sortedBy == 'time':
        replys = models.CommentModel.objects.filter(replyCommentID=commentID).order_by('-pubTime', 'hot')
    elif sortedBy == 'hot':
        replys = models.CommentModel.objects.filter(replyCommentID=commentID).order_by('hot', '-pubTime')
    for reply in replys:
        reply = model_to_dict(reply)
        res.append(reply)
    return res


# 根据paperID获取评论
def getPaperComment(request):
    # for debug
    # return render(request, 'display_page.html')
    # paperID = 1
    res = []
    paperID = request.POST.get('paperID', 1)
    # sortedBy = 'time'
    sortedBy = request.POST.get('sortedBy', 'time')
    # if sortedBy == 'time':
    # 根据发布时间进行排序
    comments = models.CommentModel.objects.order_by('-pubTime', 'hot').filter(paperID=paperID)
    # 根据热度进行排序
    if sortedBy == 'hot':
        comments = models.CommentModel.objects.filter(paperID=paperID).order_by('hot', '-pubTime')
    for comment in comments:
        comment.replyList = getCommentReply(commentID=comment.id, sortedBy=sortedBy)
        comment = model_to_dict(comment)
        res.append(comment)
    print('成功获取评论')
    return HttpResponse(json.dumps({'comments': res}))


# 发布评论
def postComment(request):
    # print('开始添加评论')
    res = []
    paperID = request.POST.get('paperID', 'PAPERID')
    userID = request.POST.get('userID', 'USERID')
    userName = request.POST.get('userName', 'USERNAME')
    contentView = request.POST.get('contentView', 'CONTENTVIEW')
    sortedBy = request.POST.get('sortedBy', 'SORTEDBY')
    avatar = request.POST.get('avatar', 'AVATAR')
    new_comment = models.CommentModel.objects.create(paperID=paperID,
                                                     userID=userID,
                                                     userName=userName,
                                                     contentView=contentView,
                                                     likeNum=0,
                                                     dislikeNum=0,
                                                     hot=0,
                                                     replyCommentID=-1,
                                                     replyNum=0,
                                                     # avatar=avatar
                                                     )

    models.HeadPicture.objects.create(commentID=new_comment.id,
                                      avatar=avatar)

    # print('成功添加评论')
    comments = models.CommentModel.objects.filter(paperID=paperID)
    for comment in comments:
        comment.replyList = getCommentReply(commentID=comment.id, sortedBy=sortedBy)
        comment = model_to_dict(comment)
        res.append(comment)

    return HttpResponse(json.dumps({'comments': res}))


# 获取评论的头像
def getCommentAvatar(request):
    commentID = request.POST.get('commentID', )
    headPicture = models.CommentModel.objects.get(commentID=commentID)
    return HttpResponse(headPicture.avatar)


# 进行回复
def postReply(request):
    res = []
    paperID = request.POST.get('paperID', 'PAPERID')
    userID = request.POST.get('userID', 'USERID')
    userName = request.POST.get('userName', 'USERNAME')
    sortedBy = request.POST.get('sortedBy', 'SORTEDBY')
    commentID = request.POST.get('commentID', 1)
    contentView = request.POST.get('contentView', 'CONTENTVIEW')
    repliedName = request.POST.get('repliedName', 'REPLIEDNAME')
    models.CommentModel.objects.create(paperID=-1,
                                       userID=userID,
                                       userName=userName,
                                       contentView=contentView,
                                       likeNum=0,
                                       dislikeNum=0,
                                       hot=0,
                                       replyCommentID=commentID,
                                       replyCommentUserName=repliedName)
    tmp_comment = models.CommentModel.objects.get(id=commentID)
    tmp_comment.replyNum += 1
    tmp_comment.save()
    comments = models.CommentModel.objects.filter(paperID=paperID)
    for comment in comments:
        comment.replyList = getCommentReply(commentID=comment.id, sortedBy=sortedBy)
        comment = model_to_dict(comment)
        res.append(comment)
    return HttpResponse(json.dumps({'comments': res}))


# 点踩功能
def postLike(request):
    res = []
    paperID = request.POST.get('paperID', 'PAPERID')
    commentID = request.POST.get('commentID', 'COMMENTID')
    isLike = request.POST.get('isLike', True)
    sortedBy = request.POST.get('sortedBy', 'time')
    comment = models.CommentModel.objects.filter(id=commentID)
    if isLike:
        comment.likeNum += 1
        comment.hot += 1
    else:
        comment.dislikeNum += 1
        comment.hot -= 1
    comment.save()
    comments = models.CommentModel.objects.filter(paperID=paperID)
    for comment_ in comments:
        comment_.replyList = getCommentReply(commentID=comment_.id, sortedBy=sortedBy)
        comment = model_to_dict(comment)
        res.append(comment)
    return HttpResponse(json.dumps({'comments': res}))


def register(request): # 等同于if request.method == 'POST':
    ret = {'code': 1000, 'msg': None} 
    try:
        user = request._request.POST.get('username') 
        pwd = request._request.POST.get('password')
        obj = models.UserInfo.objects.filter(username=user).first()
        if not obj:
            models.UserInfo.objects.create(username=user, password=pwd)
            ret['code'] = 100
            ret['msg'] = u'创建成功'
        else:
            ret['code'] = 101
            ret['msg'] = u'用户名存在'
    except Exception as e:
        ret['code'] = 102
        ret['msg'] = 'getting username or password error or database error'
                
    return HttpResponse(json.dumps(ret))

def login(request):
    ret = {'code': 1000, 'msg': None}
    try:
        user = request._request.POST.get('username')
        pwd = request._request.POST.get('password')
        obj = models.UserInfo.objects.filter(username=user, password=pwd).first()
        if not obj:
            ret['code']=1001
            ret['msg']='username or password is wrong'
            # 为登录用户创建token
        token = hashlib.md5(user)
            # 存在则更新，反之创建
        models.UserToken.objects.update_or_create(user=obj, defaults={'token': token})
        ret['token'] = token
    except Exception as e:
        ret['code'] = 1002
        ret['msg'] = 'getting username or password error or database error'
    return HttpResponse(json.dumps(ret))