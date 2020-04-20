from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from blog.views import (index, blog, post, search,
                        post_update, post_delete,
                        post_create, profile
                        )
from marketing.views import email_list_signup

urlpatterns = [
    path('', index),
    path('blog/', blog, name='post-list'),
    path('search/', search, name='search'),
    path('subscribe/', email_list_signup, name='subscribe'),
    path('create/', post_create, name='post-create'),
    path('post/<id>/', post, name='post-detail'),
    path('post/<id>/update/', post_update, name='post-update'),
    path('post/<id>/delete/', post_delete, name='post-delete'),
    path('accounts/profile/', profile, name='profile'),
]
