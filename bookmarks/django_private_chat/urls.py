# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.urls import path,re_path

from . import views
app_name = 'django_private_chat'
#urlpatterns = [
#    #original
##    url(
##        regex=r'^dialogs/(?P<username>[\w.@+-]+)$',
##        view=views.DialogListView.as_view(),
##        name='dialogs_detail'
##    ),
##    url(
##        regex=r'^dialogs/$',
##        view=views.DialogListView.as_view(),
##        name='dialogs'
##    ),
#     ## original
#    
#    re_path('r^dialogs/(?P<username>[\w.@+-]+)$',views.DialogListView.as_view(),'dialogs_detail' ),
#    re_path(r'^dialogs/$',views.DialogListView.as_view(),'dialogs'),
#    
#]
#app_name = 'hey' 
#  <li {%if section == "chats" %}class = "selected" {% endif %}>
#          <a href = "{% url "chat:dialogs" %}">chats</a>
#          </li>

urlpatterns = [

    re_path(r'^dialogs/(?P<username>[\w.@+-]+)$',view=views.DialogListView.as_view(),name='dialogs_detail'),
    re_path(r'^dialogs/$',view=views.DialogListView.as_view(),name='dialogs'),
    
]
