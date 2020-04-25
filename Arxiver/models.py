from django.db import models


# Create your models here.

class CommentModel(models.Model):
    userName = models.CharField(max_length=32, default='userName')  # 用户名
    userID = models.CharField(max_length=32, default='USERID')  # 用户ID
    paperID = models.CharField(max_length=32, default='PaperID')  # 论文ID
    contentView = models.TextField(null=True)  # 评论内容
    pubTime = models.DateTimeField(auto_now=True)  # 发表时间
    likeNum = models.IntegerField()  # 赞
    dislikeNum = models.IntegerField()  # 踩
    hot = models.IntegerField()  # 热度 = 赞 - 踩
    replyCommentID = models.IntegerField()  # -1:不是回复；否则表示被回复评论的ID
    replyCommentUserName = models.CharField(max_length=32, default='repliedName')  # 被当前回复回复的用户名
    # avatar = models.CharField(max_length=32,default = 'avatarID')  # 评论人的头像
    replyNum = models.IntegerField(default=0)  # 被回复的数量
    replyList = []  # 回复评论的列表

    # 默认按照创建时间进行倒序排序
    class Meta:
        ordering = ('-pubTime',)

    def __str__(self):
        return self.contentView


class HeadPicture(models.Model):
    commentID = models.IntegerField()
    avatar = models.ImageField()

    def __str__(self):
        return self.commentID


class UserInfo(models.Model):
    username = models.CharField(max_length=32, unique=True)

    password = models.CharField(max_length=64)


class UserToken(models.Model):
    user = models.OneToOneField(UserInfo, null=True, on_delete=models.CASCADE)

    token = models.CharField(max_length=64)