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
    discount_price = m.FloatField(blank=True , null=True)
    price = m.FloatField()
    category = m.CharField(choices=CATEGORY_CHOICES ,
                            max_length=2)
    label = m.CharField(choices=LABEL_CHOICES ,
                            max_length=2)
    slug = m.SlugField()
    description = m.TextField()


    def get_absolute_url(self):
        return reverse("estore:product",
                        kwargs=
                        {"slug": self.slug}
                        )

    def get_add_to_cart_url(self):
        return reverse("estore:add-to-cart",
                        kwargs=
                        {"slug": self.slug}
                        )

    def get_remove_from_cart_url(self):
        return reverse("estore:remove-from-cart",
                        kwargs=
                        {"slug": self.slug}
                        )

    def __str__(self):
        return self.title


class OrderItem(m.Model):
    user = m.ForeignKey(s.AUTH_USER_MODEL ,
                        on_delete= m.CASCADE)
    item = m.ForeignKey(Item , on_delete=m.CASCADE)

    ordered = m.BooleanField(default=False)
    quantity = m.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"


class Order(m.Model):
    user = m.ForeignKey(s.AUTH_USER_MODEL ,
                        on_delete= m.CASCADE )
    items =m.ManyToManyField(OrderItem)
    start_date = m.DateTimeField(auto_now=True)
    ordered_date = m.DateTimeField()
    ordered = m.BooleanField(default=False)

    def __str__(self):
        return self.user.username
