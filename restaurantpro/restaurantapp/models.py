import datetime

from django.db import models


# Create your models here.

class Category(models.Model):
    Category_Name = models.CharField(max_length=100)
    Category_Description = models.TextField(blank=True, null=True)
    Active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.Category_Name}"


class Status(models.Model):
    code = models.CharField(max_length=100)
    Status_Name = models.CharField(max_length=100)
    Description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.Status_Name}"


class Rooms(models.Model):
    Room_Code = models.CharField(max_length=100)
    Room_Description = models.TextField(null=True, blank=True)
    Long_Description = models.TextField(null=True, blank=True)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Price = models.DecimalField('Price', decimal_places=2, max_digits=12)
    Offer_Price = models.DecimalField('Offer_Price', decimal_places=2, max_digits=12)
    Vat_Amt = models.DecimalField('Vat_Amt', decimal_places=2, max_digits=12)
    Main_Image = models.ImageField(upload_to='images')
    Image_1 = models.ImageField(upload_to='images')
    Image_2 = models.ImageField(upload_to='images')
    Image_3 = models.ImageField(upload_to='images')
    Image_4 = models.ImageField(upload_to='images')
    Status = models.ForeignKey(Status, on_delete=models.CASCADE)
    Active = models.BooleanField(default=True)
    No_of_Person = models.IntegerField(null=True, blank=True)
    Room_Size = models.CharField(max_length=100, null=True, blank=True)
    Room_View = models.CharField(max_length=100, null=True, blank=True)
    Bed_Type = models.CharField(max_length=100, null=True, blank=True)
    User_ID = models.IntegerField()
    Available = models.BooleanField(default=True)
    Reserved = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.Room_Code}"


class Reservation(models.Model):
    Date_From = models.DateField(default=datetime.date.today)
    Date_To = models.DateField(default=datetime.date.today)
    Name = models.CharField(max_length=200)
    Phone_No = models.CharField(max_length=20)
    Email = models.CharField(max_length=200, blank=True, null=True)
    No_of_Person = models.IntegerField()
    No_of_Child = models.IntegerField(null=True, blank=True)
    No_of_Rooms = models.IntegerField()
    Status = models.ForeignKey(Status, on_delete=models.CASCADE)
    Remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.Name}"


class Booking(models.Model):
    Code = models.CharField(max_length=100)
    Date_From = models.DateField(default=datetime.date.today)
    Date_To = models.DateField(default=datetime.date.today)
    Name = models.CharField(max_length=200)
    Phone_No = models.CharField(max_length=20)
    Email = models.CharField(max_length=150, null=True, blank=True)
    Address = models.TextField(max_length=500, null=True, blank=True)
    City = models.CharField(max_length=100, null=True, blank=True)
    State = models.CharField(max_length=100, null=True, blank=True)
    No_of_Person = models.IntegerField()
    No_of_Child = models.IntegerField(null=True, blank=True)
    No_of_Rooms = models.IntegerField()
    Room = models.ForeignKey(Rooms, on_delete=models.CASCADE, null=True, blank=True)
    Status = models.ForeignKey(Status, on_delete=models.CASCADE)
    Amount = models.DecimalField('Amount', decimal_places=2, max_digits=12, null=True, blank=True)
    Advance_Amount = models.DecimalField('Advance_Amount', decimal_places=2, max_digits=12, null=True, blank=True)
    Balance_Amount = models.DecimalField('Balance_Amount', decimal_places=2, max_digits=12, null=True, blank=True)
    Payment_Status = models.CharField(max_length=100)
    Remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.Name}"


class Advance_Payment(models.Model):
    Date = models.DateField(default=datetime.date.today)
    Party_Name = models.CharField(max_length=200)
    Room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    Amount = models.DecimalField('Unitary Value', decimal_places=2, max_digits=12)
    Balance = models.DecimalField('Unitary Value', decimal_places=2, max_digits=12)
    Remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.Party_Name}"


class Payment(models.Model):
    Date = models.DateField(default=datetime.date.today)
    Party_Name = models.CharField(max_length=200)
    Room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    Amount = models.DecimalField('Unitary Value', decimal_places=2, max_digits=12)
    Remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.Party_Name}"


class Room_Facilities(models.Model):
    Restaurant = models.BooleanField(default=False)
    Purified_Drinking_Water = models.BooleanField(default=False)
    Natural_Environment = models.BooleanField(default=False)
    High_Speed_Wifi = models.BooleanField(default=False)
    Clean_Interiors = models.BooleanField(default=False)
    Free_Parking = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.Restaurant}"


class Room_Services(models.Model):
    Work_Desk = models.BooleanField(default=False)
    Hairdryer = models.BooleanField(default=False)
    Ironing = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.Work_Desk}"



