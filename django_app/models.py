from django.db import models

# Create your models here.


class ConfirmationKey (models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    key = models.CharField(max_length=122)
    emailid = models.CharField(max_length=122)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(null=True)


    def __str__(self):
        return self.key


