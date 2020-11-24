from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):   #customer
    user_full_name = models.CharField(max_length=100)
    user_number = models.IntegerField(blank=False, null=False)
    cooking_experience = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.user_number)


class Creator(models.Model):    #investment
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creators')
    creator_number = models.IntegerField(blank=False, null=False)
    creator_title = models.CharField(max_length=50)
    creator_description = models.CharField(max_length=200)

    def created(self):
        self.acquired_date = timezone.now()
        self.save()

    def updated(self):
        self.recent_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.user)

    def user_number(self):
        return self.user.user_number


class Recipe(models.Model):      #stock
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE, related_name='recipes')
    recipe_name = models.CharField(max_length=50)
    recipe_description = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=1000)
    directions = models.CharField(max_length=5000)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)


    def created(self):
        self.recent_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.creator)

    def creator_number(self):
        return self.creator.creator_number

