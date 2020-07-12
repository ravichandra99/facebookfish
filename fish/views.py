from django.shortcuts import render
from fish.models import User
# Create your views here.
def index(request):
	if request.is_ajax():
		#print(request.GET)
		user = User(user = request.GET)
		user.save()
	return render(request,'index.html')


