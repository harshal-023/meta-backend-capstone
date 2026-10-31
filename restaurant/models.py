from django.db import models

# Create your models here.


class Booking(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(default=1)
    BookingDate = models.DateField()

    def __init__(self, *args, **kwargs):
        if 'name' in kwargs:
            kwargs['Name'] = kwargs.pop('name')
        if 'no_of_guests' in kwargs:
            kwargs['No_of_guests'] = kwargs.pop('no_of_guests')
        if 'booking_date' in kwargs:
            kwargs['BookingDate'] = kwargs.pop('booking_date')
        if 'bookingDate' in kwargs:
            kwargs['BookingDate'] = kwargs.pop('bookingDate')
        super().__init__(*args, **kwargs)

    @property
    def name(self):
        return self.Name

    @name.setter
    def name(self, value):
        self.Name = value

    @property
    def no_of_guests(self):
        return self.No_of_guests

    @no_of_guests.setter
    def no_of_guests(self, value):
        self.No_of_guests = value

    @property
    def booking_date(self):
        return self.BookingDate

    @booking_date.setter
    def booking_date(self, value):
        self.BookingDate = value

    def __str__(self):
        return f'{self.Name} for {self.No_of_guests} guests on {self.BookingDate}'


class Menu(models.Model):
    ID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField(default=0)

    def __init__(self, *args, **kwargs):
        if 'title' in kwargs:
            kwargs['Title'] = kwargs.pop('title')
        if 'price' in kwargs:
            kwargs['Price'] = kwargs.pop('price')
        if 'inventory' in kwargs:
            kwargs['Inventory'] = kwargs.pop('inventory')
        super().__init__(*args, **kwargs)

    @property
    def title(self):
        return self.Title

    @title.setter
    def title(self, value):
        self.Title = value

    @property
    def price(self):
        return self.Price

    @price.setter
    def price(self, value):
        self.Price = value

    @property
    def inventory(self):
        return self.Inventory

    @inventory.setter
    def inventory(self, value):
        self.Inventory = value

    def __str__(self):
        return f'{self.Title} : {str(self.Price)}'

    def get_item(self):
        return f'{self.Title} : {str(self.Price)}'

    def __eq__(self, other):
        if isinstance(other, str):
            return str(self) == other
        return super().__eq__(other)