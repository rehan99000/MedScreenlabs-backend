from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from django.db.models import Count
from datetime import datetime

from djangoapps.appointments.models import Appointment, TimeSlot, Test
from djangoapps.appointments.api.v1.serializers import AppointmentGetSerializer, AppointmentPostSerializer, TimeSlotSerializer, TestSerializer


class AppointmentsViewSet(ModelViewSet):
    """
    Viewset for "Appointment".
    """
    def get_queryset(self):
        """
        """
        username = self.request.query_params.get('user')
        active = True if self.request.query_params.get('active') == 'true' else False
        queryset = Appointment.objects.all()
        if username:
            queryset = queryset.filter(user__username=username)
        if active:
            queryset = queryset.filter(status='confirmed')
        else:
            queryset = queryset.filter(status='done')

        return queryset


    def get_serializer_class(self):
        """
        """
        if self.request.method == 'GET':
            return AppointmentGetSerializer

        return AppointmentPostSerializer

class TimeSlotViewSet(ModelViewSet):
    """
    Viewset for "TimeSlot".
    """
    serializer_class = TimeSlotSerializer
    allowed_methods = ('get')

    def get_queryset(self):
        """
        """
        date = self.request.query_params.get('date')
        if date:
            date = datetime.strptime(date, '%Y-%m-%d')
            return TimeSlot.objects.annotate(appointment_count=Count('appointment')).filter(start_timestamp__date=date, appointment_count__lte=5)

        return TimeSlot.objects.all()


class TestsViewSet(ModelViewSet):
    """
    Viewset for "Test".
    """
    serializer_class = TestSerializer
    allowed_methods = ('get')
    queryset = Test.objects.all()
