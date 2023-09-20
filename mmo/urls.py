from django.urls import path
from .views import PostList, PostDetail, ReplyDetail, ReplyList


urlpatterns = [
   path('', PostList.as_view(), name='posts'),
   path('<int:pk>', PostDetail.as_view(), name='post'),
   path('replys/', ReplyList.as_view(), name='replys'),
   path('reply/<int:pk>/', ReplyDetail.as_view(), name='reply')
]