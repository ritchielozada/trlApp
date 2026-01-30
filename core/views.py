from django.shortcuts import render

# Create your views here.

def hello(request):
	"""Hello"""
	return render(request, 'core/hello.html', {'message': 'Hello, world!'})
