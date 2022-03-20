from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.core.validators import RegexValidator
from django.db import models
from django.template.loader import render_to_string
# Create your models here.
class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = 'M',('Male')
        FEMALE = 'F',('Female')

    website_url = models.URLField(blank = True)
    bio = models.TextField(blank = True)
    phone_number = models.CharField(max_length=13,blank=True,
                                    validators=[RegexValidator(r"^010-?[1-9]\d{3}-?\d{4}$")])
    gender = models.CharField(max_length=2,blank=True,choices=GenderChoices.choices)
    avatar = models.ImageField(blank=True,upload_to="accounts/avatar/%Y/%m/%d")
    def send_welcome_email(self):
        subject = render_to_string("accounts/welcome_email_subject.txt",{
            "user":self,
        })
        content = render_to_string("accounts/welcome_email_content.txt",{
            "user":self,
        })
        sender_email = settings.WELCOME_EMAIL_SENDER
        return send_mail(subject, content, sender_email, [self.email], fail_silently = False)
# class Profile(models.Model):
#     pass