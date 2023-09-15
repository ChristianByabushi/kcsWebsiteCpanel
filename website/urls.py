from django.urls import path , include
from . import views 
from django.conf.urls.static import static
from django.conf import settings 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
              path('', views.home, name='index'),
    
               path('news/', views.indexNews, name="news"), 
               path('newsdetails/<int:pk>/',  views.detailsNews, name="newsdetails"), 
               
               path('about-us/',  views.indexAboutus, name="about-us"), 

               path('projects/',  views.projectsindex, name="projectsindex"),  
               path('detailsproject/<int:pk>/',  views.detailsProject, name="detailsproject"), 


               path('contact-us/', views.contactus, name ="contact-us") ,

               path('postmessage/', views.postmessage, name ="postmessage"),

               path('services/', views.servicesindex, name ="services"),
               
               
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns() 

