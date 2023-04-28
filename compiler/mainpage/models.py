from django.db import models

from django.db import models

class Folder(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey('User', on_delete=models.CASCADE)
	is_available = models.BooleanField(default=True)
	availability_changed_at = models.DateTimeField(auto_now=True)
	last_content_change_at = models.DateTimeField(auto_now=True)
	parent_folder = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

class File(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey('User', on_delete=models.CASCADE)
	is_available = models.BooleanField(default=True)
	availability_changed_at = models.DateTimeField(auto_now=True)
	last_content_change_at = models.DateTimeField(auto_now=True)
	parent_folder = models.ForeignKey('Folder', null=True, on_delete=models.SET_NULL)

class FileSection(models.Model):
	name = models.CharField(max_length=255, blank=True, null=True)
	description = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	start_line_number = models.PositiveIntegerField()
	end_line_number = models.PositiveIntegerField()
	start_char_number = models.PositiveIntegerField(null=True, blank=True)
	end_char_number = models.PositiveIntegerField(null=True, blank=True)
	section_type = models.ForeignKey('SectionType', on_delete=models.CASCADE)
	status = models.ForeignKey('SectionStatus', on_delete=models.CASCADE)
	status_data = models.TextField(blank=True)
	content = models.TextField()
	origin_file = models.ForeignKey('File', on_delete=models.CASCADE)

class SectionType(models.Model):
	name = models.CharField(max_length=255)

class SectionStatus(models.Model):
	name = models.CharField(max_length=255)

class User(models.Model):
	name = models.CharField(max_length=255)
	login = models.CharField(max_length=255, unique=True)
	password = models.CharField(max_length=255)