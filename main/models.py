from django.db import models


class About(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)


class Home(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    shortDescription = models.CharField(max_length=400, null=True, blank=True)
    about = models.OneToOneField(About, null=True, blank=True, on_delete=models.CASCADE)


class Service(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    home = models.ForeignKey(Home, null=True, blank=True, on_delete=models.CASCADE)


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)


class WorkProcess(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    home = models.ForeignKey(Home, null=True, blank=True, on_delete=models.CASCADE)


class Portfolio(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    shortDescription = models.CharField(max_length=400, null=True, blank=True)
    link = models.CharField(max_length=200, null=True, blank=True)
