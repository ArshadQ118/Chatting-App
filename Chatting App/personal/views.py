from django.shortcuts import render

def index(request):
    return render(request, 'indexx.html')

def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })
