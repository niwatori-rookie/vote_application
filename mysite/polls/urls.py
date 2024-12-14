from django.urls import path
from . import views
app_name = "polls"
urlpatterns = [

    path("", views.TopView.as_view(), name="top"),
    path("index/", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]

#path( URL パターンを含む文字列,関数参照,URL参照)