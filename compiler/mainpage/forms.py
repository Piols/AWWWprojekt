from django import forms
from .models import Folder

class UploadFileForm(forms.Form):
	upload = forms.FileField()
	description = forms.CharField(widget=forms.Textarea, required=False)

class UploadFolderForm(forms.Form):
	name = forms.CharField(widget=forms.Textarea)
	description = forms.CharField(widget=forms.Textarea, required=False)

def HandleUpload(form, upload, user, parent_folder):
	upload.description = form.cleaned_data['description']
	if not user:
		upload.owner = Null
	else:
		upload.owner = user
	upload.parent_folder = parent_folder