import unittest
import os
from ContactsApp.models import *
from django.db import models
import time
	
class ContactTests(unittest.TestCase):
	def getTestRecord(self):
		r = Contact()
		r.first_name = "Michael"
		r.last_name = "Rosario"
		r.email = "michael.p.rosario@gmail.com"
		r.company = "test"
		r.notes = "some notes"
		r.age = 36
		r.contact_date = "2014-05-19"
		return r
		
		

	def testContact__Add__MakeSureItWorks(self):
		# arrange
		t = ContactRepo()
		r = self.getTestRecord()
		
		# act
		id = t.add(r)
		
		# assert
		self.assertTrue(t.recordExists(id))

	def testContact__Add__FailWhenInputNull(self):
		t = ContactRepo()
		r = None
	
		# assert
		self.assertRaises(ArgumentException, t.add, r)
		
	def testContactValidator__Validator__NoErrors(self):
		cv = ContactValidator()
		r = self.getTestRecord()
		
		# assert
		errors = cv.validate(r)
		
		self.assertTrue(len(errors) == 0)
		
	def testContactValidator__Validator__FirstNameIsRequired(self):
		cv = ContactValidator()
		r = self.getTestRecord()
		r.first_name = ""
		errors = cv.validate(r)	
		self.assertTrue(len(errors) == 1)
		
	def testContactValidator__Validator__LastNameIsRequired(self):
		cv = ContactValidator()
		r = self.getTestRecord()
		r.last_name = ""
		errors = cv.validate(r)	
		self.assertTrue(len(errors) == 1)
		
	def testContactValidator__Validator__AgeHasJunk(self):
		cv = ContactValidator()
		r = self.getTestRecord()
		r.age = "junk"
		errors = cv.validate(r)	
		self.assertTrue(len(errors) == 1)
		
	def testContactValidator__Validator__AgeIsZero(self):
		cv = ContactValidator()
		r = self.getTestRecord()
		r.age = 0
		errors = cv.validate(r)	
		self.assertTrue(len(errors) == 1)
		
	def testContactRepo__add__FirstNameIsRequired(self):
		t = ContactRepo()
		r = self.getTestRecord()
		r.first_name = ""
		
		self.assertRaises(ValidationException, t.add, r)

	def testContactRepo__Delete__MakeSureItWorks(self):
		# arrange
		t = ContactRepo()
		r = self.getTestRecord()
		id = t.add(r)
		self.assertTrue(t.recordExists(id))
		
		# act
		t.delete(id)
		
		# assert
		self.assertTrue(not t.recordExists(id))
		
	def testContactRepo__Get__MakeSureItWorks(self):
		# arrange
		t = ContactRepo()
		r = self.getTestRecord()
		id = t.add(r)
		self.assertTrue(t.recordExists(id))
		
		# act
		r2 = t.get(id)
		self.assertTrue(r.id == r2.id)
		self.assertTrue(r.first_name == r2.first_name)
		
	def testContactRepo__Update__MakeSureItWorks(self):
		# arrange
		t = ContactRepo()
		r = self.getTestRecord()
		id = t.add(r)
		self.assertTrue(t.recordExists(id))
		
		# act
		r2 = t.get(id)
		r2.first_name = "Mikey"
		
		t.update(r2)
		
		r3 = t.get(id)
		self.assertTrue(r3.first_name == r2.first_name)
		
		
		
if __name__ == "__main__":
	unittest.main() 
