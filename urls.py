from holly.urls import Url
from view import Homepage, EpicMath

urlpatterns = [
        Url('^$', Homepage),
        Url('^/math$', EpicMath)
        
        ]
