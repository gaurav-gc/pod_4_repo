from django.urls import path
from myapp.views import hello, goodbye

urlpatterns = [
    # myapp/
    path('', hello, name='hello'),
    # path('hello', hello, name='hello'),
    path('goodbye', goodbye, name='goodbye'),
    path('goodbye/<str:name>', goodbye, name='goodbye_name'),
    # myapp/<str:name>
    path('<str:name>', hello, name='hello_name'),
]