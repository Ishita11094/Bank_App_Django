from django.db import models

class CreateModel(models.Model):
	name = models.CharField(max_length=30)
	email = models.EmailField()
	phone = models.IntegerField()
	balance = models.PositiveIntegerField()

	def __str__(self):
		return self.name

class TransactionModel(models.Model):
	sender = models.CharField(max_length=30)
	receiver = models.CharField(max_length=30)
	amount = models.PositiveIntegerField()
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.receiver