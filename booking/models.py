from django.db import models


# Create your models here.
class Booking(models.Model):

    name = models.CharField(max_length=255, unique=True)
    capacity = models.PositiveIntegerField()
    projector = models.BooleanField(default = True)

    def __str__(self):
        return f"{self.name} {self.capacity} {self.projector} "

    def get_detail_url(self):
        return f"/booking/{self.id}"

class RoomReservation(models.Model):
    room_id = models.ForeignKey(Booking, on_delete=models.CASCADE)
    date = models.DateField()
    comment = models.TextField(null=True)

    def __str__(self):
        return f"{self.room_id} {self.date} {self.comment} "

    # def get_detail_url(self):
    #     return f"/room_reservation/{self.id}"


    class Meta:
        unique_together = ('room_id', 'date',)




