from django.shortcuts import render

def mainpage(request):
	folders = Folder.objects.order_by('-name')
	files = File.objects.order_by('-name')
	
	# Filter the folder by user

	return render(request, 'mainpage/app.html')