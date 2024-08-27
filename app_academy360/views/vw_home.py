from django.shortcuts import render

def index(request):
    return render (request, 'index.html')
    
def show_message(request, msg):
    return render (request, "message.html", {'message': msg})
