from rest_framework import serializers
from .models import Person, Phone, Email
import json


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ('id', 'type', 'phone')


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ('id', 'type', 'email')


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    phone = PhoneSerializer()
    email = EmailSerializer()

    class Meta:
        model = Person
        fields = ('id', 'photo', 'first_name', 'last_name', 'company', 'phone', 'email')

    def create(self, validated_data):
        phone_data = validated_data.pop('phone')
        phone_obj = Phone.objects.create(**phone_data)
        email_data = validated_data.pop('email')
        email_obj = Email.objects.create(**email_data)
        person = Person.objects.create(
            email=email_obj, phone=phone_obj, **validated_data)

        return person

    def update(self, instance, validated_data):
        phone_data = validated_data.get('phone')
        instance.phone.type = phone_data.get('type', instance.phone.type)
        instance.phone.phone = phone_data.get('phone', instance.phone.phone)
        instance.phone.save()

        email_data = validated_data.get('email')
        instance.email.type = email_data.get('type', instance.email.type)
        instance.email.email = email_data.get('email', instance.email.email)
        instance.email.save()

        instance.photo = validated_data.get('photo', instance.photo)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.company = validated_data.get('company', instance.company)
        instance.save()
        return instance

