from django.urls import path

from app import views


app_name = "app"

urlpatterns = [
    path('persons/', views.PersonListView.as_view()),
    path('persons/<int:pk>/', views.PersonDetailView.as_view()),
    path('phones/', views.PhoneListView.as_view()),
    path('phones/<int:pk>/', views.PhoneDetailView.as_view()),
    path('emails/', views.EmailListView.as_view()),
    path('emails/<int:pk>/', views.EmailDetailView.as_view()),
]
