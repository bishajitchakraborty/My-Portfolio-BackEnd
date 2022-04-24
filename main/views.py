from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from main.Serializer.serializer import HomeSerializer, AboutSerializer, ServiceSerializer, MessageSerializer, \
    ContactSerializer, WorkProcessSerializer, PortfolioSerializer
from main.models import Home, About, Service, Message, Contact, WorkProcess, Portfolio


class HomeApi(viewsets.ModelViewSet):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer


class AboutApi(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class ServiceApi(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class MessageApi(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class ContactApi(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class WorkProcessApi(viewsets.ModelViewSet):
    queryset = WorkProcess.objects.all()
    serializer_class = WorkProcessSerializer


class PortfolioApi(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer