from django.db import models
from django.contrib.auth.models import User

class FolderOrFile(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	is_available = models.BooleanField(default=True)
	availability_changed_at = models.DateTimeField(auto_now=True)
	last_content_change_at = models.DateTimeField(auto_now=True)
	# W templacie {% for sub_file in file.subfolders.all %}
	# Oddzielny template od wypisywania folderow, ktory potrafi sie rekurencyjnie wywolywac.

	class Meta:
		abstract = true

class Folder(FolderOrFile):
	parent_folder = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name = 'subfolders')


class File(FolderOrFile):
	content = models.TextField()
	parent_folder = models.ForeignKey(Folder, null=True, blank=True, on_delete=models.SET_NULL, related_name = 'subfiles')

class FileSection(models.Model):
	name = models.CharField(max_length=255, blank=True, null=True)
	description = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	start_line_number = models.PositiveIntegerField()
	end_line_number = models.PositiveIntegerField()
	start_char_number = models.PositiveIntegerField(null=True, blank=True)
	end_char_number = models.PositiveIntegerField(null=True, blank=True)
	SECTION_TYPES = [
		("PR", "Procedure"),
		("CO", "Comment"),
		("CD", "Compiler directive"),
		("VD", "Variable declaration"),
		("IA", "Inline assembly"),
	]
	section_type = models.CharField(max_length=2, choices=SECTION_TYPES)
	SECTIONS_STATUSES = [
		("C", "Correct"),
		("W", "Warning"),
		("E", "Error"),
	]
	status = models.CharField(max_length=1, choices=SECTIONS_STATUSES)
	status_data = models.TextField(blank=True)
	content = models.TextField()
	origin_file = models.ForeignKey(File, on_delete=models.CASCADE)