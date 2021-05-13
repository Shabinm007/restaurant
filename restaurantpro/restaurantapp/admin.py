from django.contrib import admin

# Register your models here.
from restaurantapp.models import Category, Rooms, Reservation, Booking, Advance_Payment, Payment, Status, \
    Room_Facilities, Room_Services


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('Category_Name', 'Category_Description')
    search_fields = ('Category_Name', 'Category_Description')


class RoomsAdmin(admin.ModelAdmin):
    list_display = ('Room_Code', 'Category', 'Price', 'Status')
    search_fields = ('Room_Code', 'Price')


    # def Category_Name(self, obj):
    #     return obj.Category


class StatusAdmin(admin.ModelAdmin):
    list_display = ('code', 'Status_Name')
    search_fields = ('code', 'Status_Name')


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('Date_From', 'Name', 'Phone_No', 'No_of_Person', 'No_of_Child', 'No_of_Rooms')
    search_fields = ('Date_From', 'Name', 'Phone_No', 'No_of_Person', 'No_of_Child', 'No_of_Rooms')


class BookingAdmin(admin.ModelAdmin):
    list_display = ('Code', 'Room', 'Name', 'Phone_No', 'No_of_Person', 'No_of_Child', 'No_of_Rooms')
    search_fields = ('Code', 'Room', 'Name', 'Phone_No', 'No_of_Person', 'No_of_Child', 'No_of_Rooms')


class AdvancePaymentAdmin(admin.ModelAdmin):
    list_display = ('Date', 'Party_Name', 'Room', 'Amount', 'Balance')
    search_fields = ('Date', 'Party_Name', 'Room', 'Amount', 'Balance')


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('Date', 'Party_Name', 'Room', 'Amount')
    search_fields = ('Date', 'Party_Name', 'Room', 'Amount')


class RoomFacilitiesAdmin(admin.ModelAdmin):
    list_display = ('Restaurant', 'Purified_Drinking_Water', 'Natural_Environment', 'High_Speed_Wifi', 'Clean_Interiors', 'Free_Parking')


class RoomServicesAdmin(admin.ModelAdmin):
    list_display = ('Work_Desk', 'Hairdryer', 'Ironing')

# def Category_Info(self, obj):
#     return obj.Category_Name


admin.site.register(Category, CategoryAdmin)
admin.site.register(Rooms, RoomsAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Advance_Payment, AdvancePaymentAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Room_Facilities, RoomFacilitiesAdmin)
admin.site.register(Room_Services, RoomServicesAdmin)
