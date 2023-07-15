from django.db import models
from embed_video.fields import EmbedVideoField
from django.core.validators import FileExtensionValidator
from django.conf import settings

# Create your models here.
class User_info(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    user_password = models.CharField(max_length=100)
    user_img = models.ImageField(upload_to='user-images', null=True)

    def __str__(self):
        return self.user.username



class Program(models.Model):
    title = models.CharField(max_length=150)
    course_img = models.ImageField(upload_to='programs/')
    video_file = models.FileField(upload_to='videos_uploaded/',null=True,
        validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])]
    )
    date_uploaded = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=500)
    date_field = models.DateField(auto_now=True)


    def __str__(self):
        return self.title


#series
class VideoSeries(models.Model):
    program = models.ForeignKey('SpecialProgram', on_delete=models.CASCADE, related_name='video_series')
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    video_file = models.FileField(upload_to='special_videos_uploaded/', null=True,
                                  validators=[FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    

class SpecialProgram(models.Model):
    title = models.CharField(max_length=150)
    course_img = models.ImageField(upload_to='special_programs/')
    video_file = models.FileField(upload_to='special_videos_uploaded/',null=True,
        validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])]
    )
    date_uploaded = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=500)
    date_field = models.DateField(auto_now=True)



    def __str__(self):
        return self.title
    

class User_course(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    courses = models.ManyToManyField(Program, blank=True)
    special_courses = models.ManyToManyField(SpecialProgram, blank=True)
    date_field = models.DateField(auto_now=True)


    def __str__(self):
        return self.user.username