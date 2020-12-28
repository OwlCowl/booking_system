from django.shortcuts import render, redirect
from django.views import View
import datetime


# Create your views here.
from .models import Booking, RoomReservation


class RoomListView(View):
    def get(self, request):
        rooms = Booking.objects.all()
        for room in rooms:
            reservation_dates = [reservation.date for reservation in room.roomreservation_set.all()]
            room.reserved = datetime.date.today() in reservation_dates
        return render(request, "rooms.html", context={"rooms": rooms})



class AddRoomView(View):

    def get(self, request):
        return render(request, 'add_room.html')

    def post(self, request):
        name = request.POST.get("name")
        capacity = request.POST.get("capacity", 0)
        capacity = int(capacity) if capacity else 0
        projector = request.POST.get("projector") == 'on'
        if not name:
            return render(request, "add_room.html", context={"error": "Please, give the name of room"})
        if capacity <= 0:
            return render(request, "add_room.html", context={"error": "The number of capacity should be positive"})
        if Booking.objects.filter(name=name).first():
            return render(request, "add_room.html", context={"error": "The rom with such name already exist"})

        Booking.objects.create(name=name, capacity=capacity, projector=projector)
        return redirect("room-list")

class DeleteRoomView(View):
    def get(self, request, room_id):
        room = Booking.objects.get(id=room_id)
        room.delete()
        return redirect("room-list")

class ModifyRoomView(View):
    def get(self, request, room_id):
        room = Booking.objects.get(id=room_id)
        return render(request, "modify_room.html", {"room": room})

    def post(self, request, room_id):
        room = Booking.objects.get(id=room_id)
        name = request.POST.get("name")
        capacity = request.POST.get("capacity", 0)
        capacity = int(capacity) if capacity else 0
        projector = request.POST.get("projector") == "on"

        if not name:
            return render(request, "modify_room.html", context={"error": "Please, give the name of room"})
        if capacity <=0:
            return render(request, "modify_room.html", {"error": "Please, give correct capacity"})

        if name != room.name and Booking.objects.filter(name=name).first():
            return render(request, "modify_room.html", {"room": room, "error": "The rom with such name already exist"})
        room.name = name
        room.capacity = capacity
        room.projector = projector
        room.save()

        return redirect("room-list")


class ReservationView(View):

    def get(self, request, room_id):
        room = Booking.objects.get(id=room_id)
        return render(request, "reservation.html", {"room": room})

    def post(self,request, room_id):
        room = Booking.objects.get(id=room_id)
        date = request.POST.get("reservation-date")
        comment = request.POST.get("comment")

        if RoomReservation.objects.filter(room_id=room, date=date):
            return render(request, "reservation.html", {"room":room, "error":"The room has been already reserved"})

        if date < str(datetime.date.today()):
            return render(request, "reservation.html", {"room": room, "error": "The date is not correct"})

        RoomReservation.objects.create(room_id=room, date=date, comment=comment)
        return redirect("room-list")

class DetailReservationView(View):
    def get(self, request, room_id):
        room = Booking.objects.get(id=room_id)
        reservations=room.roomreservation_set.filter(date__gte=str(datetime.date.today())).order_by('date')
        return render(request, "room_details.html", {"room":room, "reservations": reservations})

    def post(self, request, room_id):
        pass



















