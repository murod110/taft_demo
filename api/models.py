from django.db import models


class BotUser(models.Model):
    user_id = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    username = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

class Feedback(models.Model):
    user_id = models.CharField(max_length=120,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return str(self.botuser.name)

class Charakter(models.Model):
    name = models.CharField(max_length=150)
    pile = models.CharField(max_length=150,null=True,blank=True)
    pile_height = models.IntegerField(null=True,blank=True)
    yarn_weight = models.CharField(max_length=150,null=True,blank=True)
    primary_basic = models.CharField(max_length=150,null=True,blank=True)
    secondary_basic = models.CharField(max_length=150,null=True,blank=True)
    points = models.CharField(max_length=150,null=True,blank=True)
    total_weight = models.CharField(max_length=140,null=True,blank=True)
    
    def __str__(self):
        return self.name
       
class Palet(models.Model):
    name = models.CharField(max_length=150)
    char = models.ManyToManyField(Charakter,blank=True,null=True)
    photo = models.ImageField(upload_to="images/design/",blank=True,null=True)
    
    
    def __str__(self):
        return self.name