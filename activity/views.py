from account.models import Patient, Specialist
from .models import History, Referral, Appointment
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse


# Create your views here.


class AppointmentView(APIView):
    @staticmethod
    def patient_appointments(patient):
        return Appointment.objects.filter(patient=patient).values('title', 'notes', 'date', 'date_created', 'status',
                                                                  'specialist__user__name')

    @staticmethod
    def specialist_appointments(specialist):
        return Appointment.objects.filter(specialist=specialist).values('title', 'notes', 'date', 'date_created',
                                                                        'status',
                                                                        'patient__user__name')

    def get(self, request):
        if request.user.user_type == 'patient':
            patient = Patient.objects.get(user__id=request.user.id)
            appointments = self.patient_appointments(patient)
        else:
            specialist = Specialist.objects.get(user__id=request.user.id)
            appointments = self.specialist_appointments(specialist)

        return Response({'success': True, 'result': list(appointments)})

    def post(self, request):
        title = request.data['title']
        notes = request.data['notes']
        date = request.data['date']
        specialist = Specialist.objects.get(id=request.data['specialist'])
        patient = Patient.objects.get(user__id=request.user.id)

        Appointment.objects.create(title=title, notes=notes, date=date, specialist=specialist, patient=patient)
        return Response({'success': True})

    def put(self, request):
        title = request.data['title']
        notes = request.data['notes']
        date = request.data['date']
        appointment = Appointment.objects.get(id=request.data['id'])

        appointment.title = title
        appointment.notes = notes
        appointment.date = date
        appointment.save()

        return Response({'success': True})

    def delete(self, request):
        Appointment.objects.filter(id=request.data['id']).delete()
        return Response({'success': True})


class HistoryView(APIView):
    def get(self, request):
        history = History.objects.filter(specialist__user__id=request.user.id).values('title', 'notes', 'date_created',
                                                                                      'patient__user__name')

        return Response({'success': True, 'result': list(history)})

    def post(self, request):
        title = request.data['title']
        notes = request.data['notes']
        specialist = Specialist.objects.get(user__id=request.data['specialist'])
        patient = Patient.objects.get(user__id=request.user.id)

        History.objects.create(title=title, notes=notes, specialist=specialist, patient=patient)
        return Response({'success': True})

    def put(self, request):
        title = request.data['title']
        notes = request.data['notes']
        history = History.objects.get(id=request.data['id'])

        history.title = title
        history.notes = notes
        history.save()

        return Response({'success': True})

    def delete(self, request):
        History.objects.filter(id=request.data['id']).delete()
        return Response({'success': True})


def refer_patient(request):
    notes = request.POST.get('notes')

    specialist_from = Specialist.objects.get(user__id=request.user.id)
    specialist_to = Specialist.objects.get(user__id=request.POST.get('specialist'))
    patient = Patient.objects.get(user__id=request.POST.get('patient'))

    Referral.objects.create(notes=notes, patient=patient, specialist_from=specialist_from, specialist_to=specialist_to)
    return JsonResponse({"success": True})


def approve_appointment(request):
    appointment_id = request.GET.get('id')
    Appointment.objects.get(id=appointment_id).update(status='confirmed')
    return JsonResponse({"success": True})
