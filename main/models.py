from django.db import models

# Create your models here.
class reports(models.Model):
    report_id = models.AutoField(primary_key=True)
    report_name=models.CharField(max_length=4000,blank=False,null=False)
    report_type=models.CharField(max_length=100,blank=False,null=False)
    creator=models.CharField(blank=False,null=False,max_length=100)
    created=models.DateTimeField(auto_now_add=True,blank=False,null=False)
    
    class Meta:
        db_table = 'reports'
        managed = True