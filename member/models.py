from django.db import models

from cloudinary_storage.storage import RawMediaCloudinaryStorage

class BecomeAMember(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    highest_qualification = models.CharField(max_length=200)
    years_of_pro_expe = models.CharField(max_length=200)
    present_job_title = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class BecomeAMemberFiles(models.Model):
    member= models.ForeignKey(BecomeAMember,on_delete=models.CASCADE)
    file = models.FileField(upload_to='file/%d/%m', null=True, default=None,storage=RawMediaCloudinaryStorage(),)