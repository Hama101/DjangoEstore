from django.db import models as m
from django.conf import settings as s

# Create your models here.
class Item(m.Model):
    title = m.CharField(max_length=100)
    price = m.FloatField()

    def __str__(self):
        return self.title


class OderItem(m.Model):
    item = m.ForeignKey(Item , on_delete=m.CASCADE)

    def __str__(self):
        return self.title



class Order(m.Model):
    user = m.ForeignKey(s.AUTH_USER_MODEL ,
                        on_delete= m.CASCADE)
    items =m.ManyToManyField(OderItem)
    start_date = m.DateTimeField(auto_now=True)
    ordered_date = m.DateTimeField()
    ordered = m.BooleanField(default=False)

    def __str__(self):
        return self.user.username
