from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('''
    <a style="color:green; font-size:20em; font-family:sans-serif">Hello Yo!</a> <br>You're at the polls index!
    <img src="https://www.tynker.com/projects/screenshot/5cdc63bfff13b72e100b1583/shrek-memes-2.png" alt="Shreek">
    ''')

