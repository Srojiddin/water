
from django.urls import path

from apps.news.views import NewsListView, NewsDetailView, NewsDeleteView


urlpatterns = [
    path('', NewsListView.as_view(), name="list_post"),
    path('post/<int:pk>', NewsDetailView.as_view(), name="detail_post"),
    path('post/<int:pk>/delete/', NewsDeleteView.as_view(), name="delete_post"),
]