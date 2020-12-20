from django.db import models as m
from django.conf import settings as s
from django.shortcuts import reverse

CATEGORY_CHOICES=(
    ('S','Shirt'),
    ('SW','Sport wear'),
    ('OW' , 'Outwear'),
)
LABEL_CHOICES=(
    ('P','primary'),
    ('S','secondary'),
    ('D' , 'danger'),
)

class Item(m.Model):
    title = m.CharField(max_length=100)
    price = m.FloatField()
    category = m.CharField(choices=CATEGORY_CHOICES ,
                            max_length=2)
    label = m.CharField(choices=LABEL_CHOICES ,
                            max_length=2)
    slug = m.SlugField()

    def get_absolute_url(self):
        return reverse("estore:product",
                        kwargs=
                        {"slug": self.slug}
                        )

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
