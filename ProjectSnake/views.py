from django.http import HttpResponse
import datetime
def welcome(request):
    
    return HttpResponse('Welcome to our first web page!')
def users(request):
    
    return HttpResponse("let's show you our graduates users")
def GiveTime(request):
    fecha_actual=datetime.datetime.now()
    documento="""<html>
    <body>
    <h1>
    fecha y hora actuales %s
    <h1/>
    </body>
    </html> """% fecha_actual
    return HttpResponse(documento)