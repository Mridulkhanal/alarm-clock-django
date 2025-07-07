from django.shortcuts import render

def set_alarm(request):
    return render(request, 'alarmapp/alarm.html')
