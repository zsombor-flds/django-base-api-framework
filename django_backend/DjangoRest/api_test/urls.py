from django.urls import path
from .views import ArticleApiView, ArticleDetails
from .views import GenericApiViews

urlpatterns = [
    path('article/', ArticleApiView.as_view()),
    path('detail/<int:id>', ArticleDetails.as_view()),
    
    # path('generic/article', GenericApiViews.as_view()),
    path('generic/article', GenericApiViews.as_view()),
    path('generic/article/<int:id>/', GenericApiViews.as_view()),
]
