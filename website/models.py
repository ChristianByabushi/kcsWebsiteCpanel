from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.core.files import File
from io import BytesIO  

class Messages(models.Model): 
	name = models.CharField(max_length=30)
	subject = models.CharField(max_length=30)
	content = models.TextField(null=False)
	email = models.EmailField(null=False, unique=False) 
	createAt = models.DateTimeField(auto_now_add=True)  
	updateAt = models.DateField(auto_now=True)  
	class Meta:
		ordering = ('-createAt',)
		verbose_name_plural = 'Messages'

	def __str__(self):
		return f'{self.email} created at {self.createAt}'   
	
class backgrounddescription(models.Model): 
	subdescription = models.TextField(null=False)
	description = models.TextField(null=False) 
	image = models.ImageField(upload_to='images/projects/')
	createAt = models.DateTimeField(auto_now_add=True)  
	class Meta:
		ordering = ('-createAt',)
		verbose_name_plural = 'backgrounddescription'

	def __str__(self):
		return f'Background_{self.id} created at {self.createAt}' 

class Socialmediaslinks(models.Model): 
		facebook = models.URLField(null=True)
		linkedin = models.URLField(null=False)
		createAt = models.DateTimeField(auto_now_add=True)  
		twitter = models.URLField(null=False)  
		messageforsocialmedia = models.TextField(null=False)
		class Meta:
			ordering = ('-createAt',)
			verbose_name_plural = 'SocialMedia'
		def __str__(self):
			return f'SocialMediasLinks{self.id} created at {self.createAt}' 		

class Services(models.Model):
	classIcon = models.CharField(max_length=30)
	titleService = models.CharField(max_length=100)
	paragrapheDescription = models.TextField() 
	class Meta:
		verbose_name_plural = 'Services'

	def __str__(self):
		return f'{self.titleService}'

class Contact(models.Model):
	content = models.TextField(null=False)
	createAt = models.DateTimeField(auto_now_add=True)  
	email = models.EmailField(null=False, unique=False) 
	updateAt = models.DateField(auto_now=True)  
	class Meta:
		ordering = ('-createAt',)
		verbose_name_plural = 'Contacts'
	def __str__(self):
		return f'Contact_{self.email}'  

class images(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)  
	updateAt = models.DateField(auto_now=True)  
	img = models.ImageField(upload_to='images/') 
	     	
	class Meta:
		ordering = ('-created_at',) 
		verbose_name_plural = 'images'
	def __str__(self):
		return f'{self.get_name()} créée le{self.created_at} ' 

	def make_thumbnail(self, image, size=(300, 200)):
		""" make 300x200 px thumbnail from given image"""
		img = Image.open(image, encoding='UTF-16')
		img.convert('RGB')
		img.thumbnail(size)
		thumb_io = BytesIO()
		img.save(thumb_io, 'png', quality=85)
		thumbnail = File(thumb_io, name=image.name)
		return thumbnail 
	    
	def get_thumbnail(self):
		if self.thumbnail:
			return self.thumbnail.url
		else:
			if self.image:
				self.thumbnail = self.make_thumbnail(self.image)
				self.save()
				return self.thumbnail.url
			else:
				return ''
			
	def get_image(self):
		if self.img:
			return self.img.url
		return ''  

class ModelUser(AbstractUser): 
    USER_ROLES= [ 
	('admin', 'admin'), 	
	('member', 'Member'),   
	('client', 'Client'),  
	('worker', 'Worker')   ]	
    avatar = models.ImageField(null=True, default="avatar.svg") 
    user_role = models.CharField(max_length=20, choices=USER_ROLES )  
	 
    REQUIRED_FIELDS = ['email']	
    
class Departement(models.Model):
   service = models.CharField(max_length=50) 
   description = models.TextField(default='')
   created_at = models.DateField(auto_now_add=True)
   updated_at = models.DateField(auto_now=True)  
      
   def __str__(self): 
     return self.service 
   
class usersDepartement(models.Model):
	userConcerned = models.ForeignKey(ModelUser, related_name='userConcerned', on_delete=models.CASCADE) 
	departementConcernded = models.ForeignKey(Departement, related_name='Departement', on_delete=models.CASCADE)
	def __str__(self):
		return f'{self.userConcerned}_{self.departementConcernded}'
	
	class Meta:
		verbose_name_plural = 'utilisateursDepartements'
class News(models.Model): 
	writer = models.ForeignKey(ModelUser, related_name="writer", on_delete=models.CASCADE) 
	title = models.TextField(null=True) 
	message = models.TextField(null=True) 
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True) 
	department = models.ForeignKey(Departement, on_delete=models.SET_NULL, null=True) 
	image = models.ImageField(upload_to='images/news', null=True, blank=True)  

	class Meta:
		ordering = ('-created_at',) 
		verbose_name_plural = 'Nouvelles'  
	
	def get_image(self):
		if self.image:
			return self.image.url
		return ''   
		
	def __str__(self):
	 return f'{self.writer} {self.message}' 
	
class ProjectOnWebsite(models.Model):
	projecttitle = models.TextField(null=False, default='')
	description = models.TextField(null=False) 
	date_start = models.DateField() 
	date_end = models.DateField()
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True) 
	image = models.ImageField(upload_to='images/projects/')  
	def __str__(self):
		return f'{self.projecttitle}'
	
class AboutUs(models.Model):
	descriptionKcs = models.TextField()
	paragraphahDescription = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(upload_to='images/about/', null=True, blank=True)    
	class Meta:
		verbose_name_plural = 'About-us'
		ordering = ('-created_at',)  
	def get_image(self):
		if self.image:
			return self.image.url 
		return ''   
	def __str__(self):
		return f'{self.descriptionKcs}'

class teamMembers(models.Model):
	fullName = models.CharField(max_length=60) 
	designation = models.CharField(max_length=60)  
	facebook = models.URLField(null=True)
	linkedin = models.URLField(null=True)
	twitter = models.URLField(null=True)
	image = models.ImageField(upload_to='images/teamMembers/')  
	
	class Meta:
		verbose_name_plural = 'teamMembers' 
	def __str__(self):
		return f'Member_{self.fullName}'

class Partners(models.Model):
	title = models.CharField(max_length=50)
	foundation = models.BooleanField(null=False, default='')
	description = models.TextField() 
	image_ou_logo = models.ImageField(upload_to = 'images/partners/', null=True)
	created_at = models.DateField(auto_now=True)
	updated_at = models.DateField(auto_now_add=True)  
	class Meta:
		verbose_name_plural = 'Partenaires'

	def __str__(self):
		return f'{self.title} created at {self.id}' 
	  
class projectsImages(models.Model):
	image = models.ImageField(upload_to='images/projects/')  
	project = models.ForeignKey(ProjectOnWebsite, on_delete=models.CASCADE) 
	
	def get_image(self):
		if self.image:
			return self.image.url
		return ''
	class Meta: 
	    verbose_name_plural = "IProjectsEtImages"


	


    
	    