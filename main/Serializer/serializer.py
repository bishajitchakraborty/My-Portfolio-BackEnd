from rest_framework import serializers

from main.models import Home, About, Service, Contact, Message, WorkProcess, Portfolio


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class WorkProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkProcess
        fields = "__all__"


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = "__all__"


class HomeSerializer(serializers.ModelSerializer):
    about = AboutSerializer(read_only=True)
    contact = ContactSerializer(read_only=True, many=True, source="contact_set")
    service = ServiceSerializer(read_only=True, many=True, source="service_set")
    workProcess = WorkProcessSerializer(read_only=True, many=True, source="workprocess_set")
    class Meta:
        model = Home
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"


