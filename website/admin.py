from django.contrib import admin
# Register your models here.
from .models import Messages,AboutUs, Socialmediaslinks, backgrounddescription,  teamMembers, Services, News,Contact, Departement, ProjectOnWebsite, Partners, ModelUser
admin.site.register(Messages) 
admin.site.register(teamMembers) 
admin.site.register(AboutUs) 
admin.site.register(Services) 
admin.site.register(News) 
admin.site.register(ProjectOnWebsite) 
admin.site.register(Departement) 
admin.site.register(Partners) 
admin.site.register(Contact)
admin.site.register(ModelUser)
admin.site.register(Socialmediaslinks)
admin.site.register(backgrounddescription)
