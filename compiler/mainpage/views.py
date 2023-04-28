from django.shortcuts import render

# Edycja plikow i podzial na sekcje nie potrzebna. Potrzeba umiec skompilowac plik

def mainpage(request):
	# Mozna odzyskac aktualnego uzytkownika
	folders = Folder.objects.order_by('-name')
	files = File.objects.order_by('-name')
	
	# Filter the folder by user

	return render(request, 'mainpage/app.html')