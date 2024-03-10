from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.gis.db import models


class User(AbstractBaseUser):
    login = models.CharField(max_length=255, blank=False, unique=True)
    email = models.EmailField(blank=False,unique=True,max_length=150)
    phone_number = models.CharField(max_length=13, blank=False,unique=True)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
    class Meta:
        app_label = "HeartBeat"
        db_table = "User"

class Gender(models.Model):
    gender_name = models.CharField(max_length=20)
    def __str__(self):
        return self.id
    class Meta:
        app_label = "HeartBeat"
        db_table = "Gender"
class Profile(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=False)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE,blank=False)
    name = models.CharField(max_length=60,blank=False)
    discription = models.CharField(max_length=300)
    is_online = models.BooleanField(default=False)
    active_in_search = models.BooleanField(default=True)
    last_coordinates = models.PointField(default='POINT(0 0)',srid=4326)
    contact_data = models.CharField(max_length=100,blank=False)
    birth_day = models.DateField()

    def __str__(self):
        return self.id

    class Meta:
        app_label = "HeartBeat"
        db_table = "Profile"
class Like(models.Model):

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,blank=False)
    liked_profile = models.ForeignKey(Profile, on_delete=models.CASCADE,blank=False)

    def __str__(self):
        return self.id

    class Meta:
        app_label = "HeartBeat"
        db_table = "Likes"

class Disike(models.Model):

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,blank=False)
    disliked_profile = models.ForeignKey(Profile, on_delete=models.CASCADE,blank=False)

    def __str__(self):
        return self.id

    class Meta:
        app_label = "HeartBeat"
        db_table = "Disikes"

class Connection(models.Model):
    first_profile = models.ForeignKey(Profile, on_delete=models.CASCADE,blank=False)
    second_profile = models.ForeignKey(Profile, on_delete=models.CASCADE,blank=False)

    def __str__(self):
        return self.id

    class Meta:
        app_label = "HeartBeat"
        db_table = "Connections"
class PreferenceTag(models.Model):
    name = models.CharField(max_length=40)
    class Meta:
        app_label = "HeartBeat"
        db_table = "PreferencesTags"

class ProfileTag(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,blank=False)
    tag = models.ForeignKey(PreferenceTag,on_delete=models.CASCADE,blank=False)
    class Meta:
        app_label = "HeartBeat"
        db_table = "ProfilesTags"
class Target(models.Model):
    name = models.CharField(max_length=40)
    class Meta:
        app_label = "HeartBeat"
        db_table = "Targets"

class ProfileTarget(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,blank=False)
    target = models.ForeignKey(Target,on_delete=models.CASCADE,blank=False)
    class Meta:
        app_label = "HeartBeat"
        db_table = "ProfilesTargets"
'''
class Images(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,blank=False)
    image_link = models.CharField(max_length=255,blank=False)

    class Meta:
        app_label = "HeartBeat"
        db_table = "Images"
class Device(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=False)
    device_name = models.CharField(max_length=100,blank=False)

    class Meta:
        app_label = "HeartBeat"
        db_table = "Devices"
        '''
