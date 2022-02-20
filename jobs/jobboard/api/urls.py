from django.urls import path
from jobboard.api.views import JobofferdetailAPIView,JobofferlistAPIView,EmployeelistAPIView


urlpatterns = [
    path('joboffers/',JobofferlistAPIView.as_view(),name = "job-list"),
    path('joboffers/<int:pk>',JobofferdetailAPIView.as_view(),name = "job-details"),
        path('employees/',EmployeelistAPIView.as_view(),name = "employee-details")
]