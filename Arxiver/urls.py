from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('searchPaper',views.searchPaper,name = 'searchPaper'),
    path('getPdfFile',views.showPaper,name = 'showPaper'),
    path('getRecommendation',views.recommendPaper,name = 'recommendPaper'),
    
    #path('choose_paper/', views.choosePaper, name='choose_paper'),
    path('getPaperComment', views.getPaperComment, name='display_page'),
    #path('edit_comment/', views.editComment, name='edit_comment'),  # 进入添加评论的页面
    path('postComment', views.postComment, name='post_comment'),  # 添加评论，返回display页面
    #path('edit_reply/', views.editReply, name='edit_reply'),   # 进入添加回复的页面
    path('postReply', views.postReply, name='post_reply'),  # 添加回复，返回display_page
    path('postLike', views.postLike),
    path('cancelLike', views.cancelLike),
    path('register/',  views.register),
    path('login/',  views.login)
]
