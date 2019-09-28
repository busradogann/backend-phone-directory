from django.db import models


class Phone(models.Model):

    PHONE_TYPES = (
        ('home', 'Home'),
        ('work', 'Work')
    )

    type = models.CharField(max_length=80, choices=PHONE_TYPES)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return "Phone: %s" % (self.phone,)


class Email(models.Model):

    EMAIL_TYPES = (
        ('home', 'Home'),
        ('work', 'Work')
    )

    type = models.CharField(max_length=80, choices=EMAIL_TYPES)
    email = models.EmailField(max_length=80)

    def __str__(self):
        return "Email: %s" % (self.email,)


class Person(models.Model):
    photo = models.ImageField(upload_to='images')
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    company = models.CharField(max_length=50)
    phone = models.ForeignKey(Phone, related_name='person_phone', on_delete=models.CASCADE, blank=True, null=True)
    email = models.ForeignKey(Email, related_name='person_email', on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)