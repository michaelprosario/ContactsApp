from django.db import models

def toInt(value):
	try:
		x = int(value)
	except ValueError:
		x = 0
	
	return x
	
class ArgumentException(Exception):
	def __init__(self, value):
		self.value = value
		
	def __str__(self):
		return repr(self.value)

class ApplicationException(Exception):
	def __init__(self, value):
		self.value = value
		
	def __str__(self):
		return repr(self.value)
		
class ValidationException(Exception):
	def __init__(self, errors):
		self.errors = errors
		
	def __str__(self):
		return repr(self.errors)

class ContactValidator():
	def validate(self, record):
		errors = []
		if(record.first_name == "" or record.first_name is None):
			errors.append("first_name: First name is required.")

		if(record.last_name == "" or record.last_name is None):
			errors.append("last_name: Last name is required.")

		if(record.email == "" or record.email is None):
			errors.append("email: E-mail is required.")

		if(not isinstance(record.age, int)):
			errors.append("age: age must be a valid integer.")
		else:	
			if(record.age < 0):
				errors.append("age: age should be positive.")

		return errors	
		
class ContactRepo():
	def add(self,record):
		if (record is None):
			raise ArgumentException("Record is null.")
			
		cv = ContactValidator()
		errors = cv.validate(record)
		if(len(errors) > 0):
			raise ValidationException(errors)
		
		record.save()	
		return record.id
	
	def get(self, recordID):
		record = Contact.objects.get(id=recordID)
		return record
		
	def recordExists(self,recordID):
		return Contact.objects.filter(id=recordID).count() > 0
		
	def delete(self, recordID):
		record = Contact.objects.get(id=recordID)
		record.delete()
		
	def getAll(self):
		list = Contact.objects.all()
		return list
		
	def update(self, record):
		if (record is None):
			raise ArgumentException("Record is null.")

		cv = ContactValidator()
		errors = cv.validate(record)
		if(len(errors) > 0):
			raise ValidationException(errors)
						
		record.save()
		
		
class Contact(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.CharField(max_length=300)
	company = models.CharField(max_length=100)
	notes = models.CharField(max_length=100)
	age = models.IntegerField(default=0)
	contact_date = models.DateTimeField()


	
