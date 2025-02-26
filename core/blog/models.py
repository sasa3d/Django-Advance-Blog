from django.db import models  # type: ignore

# {"conversationId":"1929b946-2861-42a8-aeb3-faf5a0dfa05d","source":"instruct"}
# from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
#from accounts.models import Profile   جهت جلوگیری از لوپ غلط در همزمانی ایمپورت کردن دو مدل از دو اپ درون یکدیگر 

# from django.utils import timezone

# getting user model object
User = get_user_model()
class Post(models.Model):
    """
    this is a class for post model to define all the fields for
    Blog app.
    """
    # author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    #جهت جلوگیری از لوپ غلط در همزمانی ایمپورت کردن دو مدل از دو اپ درون یکدیگ
    author = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)

    image = models.ImageField(
        _("Image"),
        upload_to=None,
        height_field=None,
        width_field=None,
        null=True,
        blank=True,
    )

    title = models.CharField(max_length=250)
    content = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, null=True, blank=True
    )

    # Remove auto_now and auto_now_add
    created_date = models.DateTimeField(
        null=True,
        blank=True,
        # default=timezone.now
    )
    updated_date = models.DateTimeField(
        null=True,
        blank=True,
        # default=timezone.now
    )
    published_date = models.DateTimeField(
        null=True,
        blank=True,
        # default=timezone.now
    )

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
