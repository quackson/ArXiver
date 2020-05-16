from django.db import models
from typing import Iterable
import django.utils.timezone as timezone


# Create your models here.


class ListField(models.TextField):
    """
    A custom Django field to represent lists as comma separated strings
    """

    def __init__(self, *args, **kwargs):
        self.token = kwargs.pop('token', ',')
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs['token'] = self.token
        return name, path, args, kwargs

    def to_python(self, value):

        class SubList(list):
            def __init__(self, token, *args):
                self.token = token
                super().__init__(*args)

            def __str__(self):
                return self.token.join(self)

        if isinstance(value, list):
            return value
        if value is None:
            return SubList(self.token)
        return SubList(self.token, value.split(self.token))

    def from_db_value(self, value, expression, connection):
        return self.to_python(value)

    def get_prep_value(self, value):
        if not value:
            return
        assert (isinstance(value, Iterable))
        return self.token.join(value)

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return self.get_prep_value(value)


class CommentModel(models.Model):
    userName = models.CharField(max_length=32, default='userName')  # 用户名
    userID = models.CharField(max_length=32, default='USERID')  # 用户ID
    paperID = models.CharField(max_length=200, default='PaperID')  # 论文ID
    contentView = models.TextField(null=True)  # 评论内容
    pubTime = models.DateTimeField(default=timezone.now)  # 发表时间
    likeNum = models.IntegerField()  # 赞
    dislikeNum = models.IntegerField()  # 踩
    hot = models.IntegerField()  # 热度 = 赞 - 踩
    replyCommentID = models.IntegerField()  # -1:不是回复；否则表示被回复评论的ID
    replyCommentUserName = models.CharField(max_length=32, default='repliedName')  # 被当前回复回复的用户名
    avatar = models.CharField(max_length=200, default='avatarID')  # 评论人的头像
    replyNum = models.IntegerField(default=0)  # 被回复的数量
    likeUserIDList = ListField(default=['-1'])  # 点赞用户ID列表
    dislikeUserIDList = ListField(default=['-1'])  # 点踩用户ID列表
    replyList = []  # 回复评论的列表

    # 默认按照创建时间进行倒序排序
    class Meta:
        ordering = ('-pubTime',)

    def __str__(self):
        return self.contentView


'''
class HeadPicture(models.Model):
    commentID = models.IntegerField()
    avatar = models.ImageField()

    def __str__(self):
        return self.commentID
'''

'''
class UserInfo(models.Model):
    username = models.CharField(max_length=32, unique=True)

    password = models.CharField(max_length=64)


class UserToken(models.Model):
    user = models.OneToOneField(UserInfo, null=True, on_delete=models.CASCADE)

    token = models.CharField(max_length=64)
'''


class UserModel(models.Model):
    userName = models.CharField(max_length=32, default='userName')  # 登录用户名
    password = models.CharField(max_length=32, default='000000')  # 登陆密码

    profession = models.CharField(max_length=32, default='undefined')  # 职业
    email = models.CharField(max_length=32, default='undefined')  # 电子邮件
    phoneNumber = models.CharField(max_length=32, default='undefined')  # 电话号码
    area = models.CharField(max_length=32, default='undefined')  # 地区
    personHomepage = models.CharField(max_length=200, default='undefined')  # 个人主页
    note = models.TextField(default='undefined')  # 备注
    headImg = models.ImageField(upload_to="img/")  # 头像

    isOnline = models.IntegerField(default=0)

    collectDict = models.TextField()  # 收藏夹，存储paper的Info
    focusList = ListField()  # 关注领域，存储二级学科的list

    def __str__(self):
        return self.userName
