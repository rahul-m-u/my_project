from django.urls import path
from myapp import views

urlpatterns = [
    path('welcome/', views.HelloView.as_view(), name='welcome'),
    path('bank-list/', views.Banks.as_view(), name='bank-list'),
    path('branch-details/', views.BranchDetailsView.as_view(), name='bank-details'),
    path('bank-branches/', views.BankBranchesListView.as_view(), name='bank-branch-list'),
]
