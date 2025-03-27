# from django.urls import path
# from .views import register_user, submit_request, track_request, list_requests

# urlpatterns = [
#     path('register_user/', register_user, name='register_user'),
#     path('submit_request/', submit_request, name='submit_request'),
#     path('track_request/<int:request_id>/', track_request, name='track_request'),
#     path('list_requests/', list_requests, name='list_requests'),
# ]

from django.urls import path
from .views import register_user, submit_request, track_request, list_requests,get_user_info

urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('submit/', submit_request, name='submit_request'),
    path('track/<int:request_id>/', track_request, name='track_request'),
    path('list/', list_requests, name='list_requests'),
     path('user-info/<int:customer_id>/', get_user_info, name='user-info'),
]
