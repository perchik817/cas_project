import email

from django.db import models

class Elems_1(models.Model):
	img = models.ImageField(upload_to = '')
	title = models.CharField(max_length = 200)
	description = models.CharField(max_length = 300)
	price = models.FloatField()
	
	def __str__(self):
		return self.title

class Elems_2(models.Model):
	img_2 = models.ImageField(upload_to = '')
	title_2 = models.CharField(max_length = 200)
	description_2 = models.CharField(max_length = 300)
	price_2 = models.FloatField()
	
	def __str__(self):
		return self.title_2

class Elems_3(models.Model):
	img_3 = models.ImageField(upload_to = '')
	title_3 = models.CharField(max_length = 200)
	description_3 = models.CharField(max_length = 300)
	price_3 = models.FloatField()
	
	def __str__(self):
		return self.title_3

class Elems_4(models.Model):
	img_4 = models.ImageField(upload_to = '')
	title_4 = models.CharField(max_length = 200)
	description_4 = models.CharField(max_length = 300)
	price_4 = models.FloatField()
	
	def __str__(self):
		return self.title_4

class Order(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	email = models.EmailField()
	phone_number = models.PositiveIntegerField()
	address = models.CharField(max_length =200)
	created = models.DateTimeField(auto_now_add = True)
	quantity = models.PositiveIntegerField(default = 1)
	
	def __str__(self):
		return self.first_name

class About_us(models.Model):
	image_per = models.ImageField(upload_to = '', null = True)
	person = models.CharField(max_length = 200)
	about_person = models.CharField(max_length = 200)