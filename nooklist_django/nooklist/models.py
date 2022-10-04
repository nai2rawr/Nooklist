from django.db import models

# Create your models here.
class Houseware(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    bid_price = models.CharField(max_length=250)
    photo = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Recipes(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    bid_price = models.CharField(max_length=250)
    photo = models.CharField(max_length=500)

        def __str__(self):
            return self.name


class Clothing(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    bid_price = models.CharField(max_length=250)
    photo = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Villager(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    bid_price = models.CharField(max_length=250)
    photo = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Resources(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    bid_price = models.CharField(max_length=250)
    photo = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class ThreadModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')

    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')

    has_unread = models.BooleanField(default=False)

class MessageModel(models.Model):
    thread = models.ForeignKey('ThreadModel', related_name='+', on_delete=models.CASCADE, blank=True, null=True)

    sender_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')

    receiver_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')

    body = models.CharField(max_length=1000)

    image = models.ImageField(upload_to='', blank=True, null=True)

    date = models.DateTimeField(default=timezone.now)

    is_read = models.BooleanField(default=False)


class Notification(models.Model):
    notification_type = models.IntegerField(null = True, blank=True)

    to_user = models.ForeignKey(User, related_name='notification_to', on_delete=models.CASCADE, null = True)

    from_user = models.ForeignKey(User, related_name='notification_from', on_delete = models.CASCADE, null =True)

    post= models.ForeignKey('Post', on_delete=models.CASCADE, related_name='+', blank=True, null=True)

    comment = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='+', blank=True, null= True)

    thread = models.ForeignKey('ThreadModel', on_delete=models.CASCADE, related_name='+', blank=True, null= True)

    date = models.DateTimeField(default=timezone.mow)

    user_has_seen = models.BooleanField(default=False)