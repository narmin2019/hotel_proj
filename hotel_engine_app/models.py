from django.db import models
from django.contrib.auth.models import User as SystemUser
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(SystemUser, on_delete=models.CASCADE, verbose_name="Sistem istifadəçisi")

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name="Müştəri"
        verbose_name_plural="Müştərilər"


class Manager(models.Model):
    user = models.OneToOneField(SystemUser, on_delete=models.CASCADE, verbose_name="Sistem istifadəçisi")

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name="Otel meneceri"
        verbose_name_plural="Otel menecerləri"


class Hotel(models.Model):
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, verbose_name='Otelin meneceri')
    name = models.CharField(max_length=30, blank=False, verbose_name='Adı')
    region = models.CharField(max_length=250, blank=True)
    price = models.IntegerField(verbose_name='Qiymət')
    photo = models.ImageField(upload_to='hotels/cover/', verbose_name='Şəkil')
    room_capacity = models.IntegerField(default=50, verbose_name="Nömrələrin sayı")
    guest_capacity = models.IntegerField(default=80, verbose_name="Nömrələrin sayı")
    contact_info = models.TextField(max_length=500, blank=True)

    class Meta:
        verbose_name='Otel'
        verbose_name_plural='Otellər'

    def rating(self):
        count = self.review_set.count()
        if count == 0:
            return 0
        sum = sum(map(lambda x:x.rate,self.review_set.all()))
        return int(sum/count)

    def __str__(self):
        return self.name


class Receptionist(models.Model):
    user = models.OneToOneField(SystemUser, on_delete=models.CASCADE, verbose_name="Sistem istifadəçisi")
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name="İşlədiyi otel")

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name="Resepşn"
        verbose_name_plural="Resepşnlar"


class Order(models.Model):
    by_whom = models.ForeignKey(SystemUser, on_delete=models.CASCADE, verbose_name='Sifarişçi')
    from_date = models.DateField(blank=True, null=True, verbose_name='Giriş vaxtı')
    to_date = models.DateField(blank=True, null=True, verbose_name='Çıxış vaxtı')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name='Otel')
    number_of_rooms = models.IntegerField(default=1, verbose_name='Nömrələrin sayı')
    number_of_guest = models.IntegerField(default=1, verbose_name='Qonaqların sayı')
    is_approved = models.BooleanField(default=False, verbose_name='Təstiq statusu')

    class Meta:
        verbose_name='Sifariş'
        verbose_name_plural='Sifarişlər'

    def __str__(self):
        return self.by_whom.get_full_name() + ' - ' + self.hotel.name


class Review(models.Model):
    by_whom = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Fikir bildirən")
    to_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name='Otel')
    comment = models.TextField(max_length=1000, verbose_name='Şərh')
    rate = models.IntegerField(verbose_name="Qiymət")

    class Meta:
        verbose_name='Fikir'
        verbose_name_plural='Fikirlər'
