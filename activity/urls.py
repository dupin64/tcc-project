from django.conf.urls import url

from . import views

app_name = 'activity'

urlpatterns = [
    url('history', views.HistoryView.as_view()),
    url('appointment', views.AppointmentView.as_view()),
    url('approve_appointment', views.approve_appointment),
    url('refer', views.refer_patient),
]
