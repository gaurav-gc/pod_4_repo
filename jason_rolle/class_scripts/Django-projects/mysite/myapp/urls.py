from django.urls import path
from myapp.views import hello, goodbye

urlpatterns = [
    # myapp/
    path('', hello, name='hello'),
    # myapp/<str:name>
    path('goodbye', goodbye, name='goodbye'),
    path('goodbye/<str:name>', goodbye, name='hello_name'),
    path('<str:name>', hello, name='hello_name'),
    
]
