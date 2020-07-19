from django.urls import path
from .views import *

app_name = "blogapp"

urlpatterns = [

    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('nepal/', NepalView.as_view(), name='nepal'),
    path('blog/list/', BlogListView.as_view(), name='bloglist'),
    path('blog/event/', EventListView.as_view(), name='eventlist'),
    path('news/list/', NewsListView.as_view(), name='newslist'),
    path('blog/create/', BlogCreateView.as_view(), name='blogcreate'),
    path('blog/detail/', BlogDetailView.as_view(), name='blogdetail'),
    path('blog/<int:pk>/update/', BlogUpdateView.as_view(), name='updateblog'),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='deleteblog'),
    path('news/create', NewsCreateView.as_view(), name='newscreate'),
    path('news/<int:pk>/update/', NewsUpdateView.as_view(), name='updatenews'),
    path('news/<int:pk>/delete/', NewsDeleteView.as_view(), name='deletenews'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('blog/<int:pk>/comment', BlogCommentCreateView.as_view(),
         name='blogcommentcreate'),
    path('search/', SearchView.as_view(), name='search'),






]
