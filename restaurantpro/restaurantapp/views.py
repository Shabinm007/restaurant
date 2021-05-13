import datetime

from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from django.templatetags.tz import datetimeobject

from restaurantapp.models import Reservation, Rooms, Booking, Status


def main(request):
    ObjRooms = Rooms.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        phone_no = request.POST.get('phone_no')
        email = request.POST.get('email')
        date_from = request.POST.get('date_from'.format('%Y-%m-%d'))
        date_to = request.POST.get('date_to'.format('%Y-%m-%d'))
        date_from = datetime.datetime.strptime(date_from, '%m/%d/%Y')
        date_to = datetime.datetime.strptime(date_to, '%m/%d/%Y')
        person = request.POST.get('person')
        room = request.POST.get('room')
        status = 1

        if date_from < datetime.datetime.today():
            messages.info(request, "Check In Date is less than today. Please choose the proper Check In Date")
            return render(request, 'index.html')
        elif date_to < date_from:
            messages.info(request, "Check Out Date is less than Check in Date. Please choose the proper Check Out Date")
            return render(request, 'index.html')
        else:
            Reserve = Reservation(Name=name, Phone_No=phone_no, Email=email, Date_From=date_from, Date_To=date_to,
                                  No_of_Person=person, No_of_Rooms=room, Status_id=status)
            Reserve.save()
            return render(request, 'index.html')
    else:
        return render(request, 'index.html', {'Room': ObjRooms})


def index(request):
    ObjRooms = Rooms.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        phone_no = request.POST.get('phone_no')
        email = request.POST.get('email')
        date_from = request.POST.get('date_from'.format('%Y-%m-%d'))
        date_to = request.POST.get('date_to'.format('%Y-%m-%d'))
        date_from = datetime.datetime.strptime(date_from, '%m/%d/%Y')
        date_to = datetime.datetime.strptime(date_to, '%m/%d/%Y')
        person = request.POST.get('person')
        room = request.POST.get('room')
        status = 1

        if date_from < datetime.datetime.today():
            messages.info(request, "Check In Date is less than today. Please choose the proper Check In Date")
            return render(request, 'index.html')
        elif date_to < date_from:
            messages.info(request, "Check Out Date is less than Check in Date. Please choose the proper Check Out Date")
            return render(request, 'index.html')
        else:
            Reserve = Reservation(Name=name, Phone_No=phone_no, Email=email, Date_From=date_from, Date_To=date_to,
                                  No_of_Person=person, No_of_Rooms=room, Status_id=status)
            Reserve.save()
            return render(request, 'index.html')
    else:
        return render(request, 'index.html', {'Room': ObjRooms})


def about(request):
    return render(request, 'about.html')


def gallery_standard(request):
    return render(request, 'gallery-standard.html')


def gallery_details(request):
    return render(request, 'gallery-details.html')


def rooms(request):
    return render(request, 'rooms.html')


def rooms_details(request):
    return render(request, 'rooms-details.html')


def service(request):
    return render(request, 'service.html')


def service_details(request):
    return render(request, 'service-details.html')


def staff(request):
    return render(request, 'staff.html')


def staff_details(request):
    return render(request, 'staff-details.html')


def contact(request):
    return render(request, 'contact.html')


def booking_details(request):
    ObjRooms = Rooms.objects.all()
    ObjStatus = Status.objects.all()
    if request.method == 'POST':
        room = request.POST.get('Room')
        name = request.POST.get('name')
        phone_no = request.POST.get('phone_no')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        date_from = request.POST.get('date_from'.format('%Y-%m-%d'))
        date_to = request.POST.get('date_to'.format('%Y-%m-%d'))
        date_from = datetime.datetime.strptime(date_from, '%m/%d/%Y')
        date_to = datetime.datetime.strptime(date_to, '%m/%d/%Y')
        no_of_person = request.POST.get('no_of_person')
        no_of_child = request.POST.get('no_of_child')
        no_of_room = request.POST.get('no_of_room')
        amount = request.POST.get('amount')
        advance_amount = request.POST.get('advance_amount')
        balance_amount = request.POST.get('balance_amount')
        status_id = request.POST.get('Status')

        if amount != advance_amount:
            status = 'Partially Paid'
        elif advance_amount == 0:
            status = 'Not Paid'
        elif amount == advance_amount:
            status = 'Paid'
        else:
            status = 'Not Paid'

        booking_details = Booking(Name=name, Phone_No=phone_no, Email=email, Address=address,
                                  City=city, State=state, Date_From=date_from, Date_To=date_to,
                                  No_of_Person=no_of_person, No_of_Child=no_of_child, No_of_Rooms=no_of_room,
                                  Amount=amount, Advance_Amount=advance_amount, Balance_Amount=balance_amount,
                                  Payment_Status=status, Room_id=room, Status_id=status_id)
        booking_details.save()
        return render(request, 'booking_details.html')
    else:
        return render(request, 'booking_details.html', {'rooms': ObjRooms, 'RoomStatus': ObjStatus})


def rooms_status(request):
    ObjRooms = Rooms.objects.all()
    return render(request, 'room_status.html', {'rooms': ObjRooms})


