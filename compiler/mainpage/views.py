from django.shortcuts import redirect, render
from .models import File, Folder
from .forms import UploadFileForm, UploadFolderForm, HandleUpload
import logging
import datetime

def get_rootfolder(current_user):
	if not current_user:
		root_folder = Folder.objects.filter(owner__isnull=True, parent_folder__isnull=True, is_available=True)
	else:
		root_folder = Folder.objects.filter(owner=current_user, parent_folder__isnull=True, is_available=True)
	if len(root_folder) > 0:
		return root_folder[0]
	folder = Folder()
	folder.owner = current_user
	folder.name = 'root'
	folder.parent_folder = None
	folder.save()
	return folder
		

def mainpage(request):
	current_user = request.user
	root_folder = get_rootfolder(current_user)
	
	return render(request, 'mainpage/app.html', {
		'root_folder': root_folder,
	})

def view_file(request, file_id):
	current_user = request.user
	root_folder = get_rootfolder(current_user)
	current_file = File.objects.filter(owner=current_user, id=file_id)
		
	if len(current_file) == 1:
		return render(request, 'mainpage/app.html', {
			'root_folder': root_folder,
			'current_file': current_file[0],
		})
	else:
		return render(request, 'mainpage/app.html', {
			'root_folder': root_folder,
			'no_current_file': True,
		})

def add_file(request, folder_id):
	if not request.user:
		parent_folder = Folder.objects.filter(owner__isnull=True, id=folder_id, is_available=True)
	else:
		parent_folder = Folder.objects.filter(owner=request.user, id=folder_id, is_available=True)
	if len(parent_folder) == 0:
		return render(request, 'mainpage/upload.html', {
			'no_parent_folder': True,
		})
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			uploaded_file = File()
			uploaded_file.name = form.cleaned_data['upload'].name
			HandleUpload(form, uploaded_file, request.user, parent_folder[0])
			file_content = ""
			for chunk in form.cleaned_data['upload'].chunks():
				file_content += chunk.decode("utf-8")
			uploaded_file.content = file_content
			uploaded_file.save()
			return redirect('view_file', uploaded_file.id)
	return render(request, 'mainpage/upload.html', {
		'file_upload': True,
	})

def add_folder(request, folder_id):
	if not request.user:
		parent_folder = Folder.objects.filter(owner__isnull=True, id=folder_id, is_available=True)
	else:
		parent_folder = Folder.objects.filter(owner=request.user, id=folder_id, is_available=True)
	if len(parent_folder) == 0:
		return render(request, 'mainpage/upload.html', {
			'no_parent_folder': True,
		})
	if request.method == 'POST':
		form = UploadFolderForm(request.POST)
		if form.is_valid():
			uploaded_folder = Folder()
			uploaded_folder.name = form.cleaned_data['name']
			HandleUpload(form, uploaded_folder, request.user, parent_folder[0])
			uploaded_folder.save()
			return redirect('mainpage')
	return render(request, 'mainpage/upload.html', {})

def single_removal(file):
	file.availability_changed_at = datetime.datetime.now()
	file.is_available=False
	file.save()

def recursive_removal(file):
	if type(file) == Folder:
		for subfolder in file.subfolders.all():
			recursive_removal(subfolder)
		for subfile in file.subfiles.all():
			recursive_removal(subfile)
	single_removal(file)

def remove_file(request, file_id):
	if not request.user:
		removable = File.objects.filter(owner__isnull=True, id=file_id, is_available=True)
	else:
		removable = File.objects.filter(owner=request.user, id=file_id, is_available=True)
	if len(removable) > 0:
		recursive_removal(removable[0])
	return redirect('mainpage')

def remove_folder(request, folder_id):
	if not request.user:
		removable = Folder.objects.filter(owner__isnull=True, id=folder_id, is_available=True)
	else:
		removable = Folder.objects.filter(owner=request.user, id=folder_id, is_available=True)
	if len(removable) > 0:
		recursive_removal(removable[0])
	return redirect('mainpage')
		