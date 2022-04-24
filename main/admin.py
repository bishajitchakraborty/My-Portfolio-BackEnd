from django.contrib import admin
from main.models import Home, About, Service, Contact, Message, WorkProcess, Portfolio


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    model = About
    list_display = ['id', 'image', 'description']


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    model = Home
    list_display = ['id', 'name', 'title', 'shortDescription']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    model = Service
    list_display = ['id', 'title', 'description']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = ['id', 'address', 'email', 'phone']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    model = Message
    list_display = ['id', 'name', 'email', 'phone', 'message']


@admin.register(WorkProcess)
class WorkProcessAdmin(admin.ModelAdmin):
    model = WorkProcess
    list_display = ['id', 'title', 'description']


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    model = Portfolio
    list_display = ['id', 'image', 'title', 'shortDescription', 'link']