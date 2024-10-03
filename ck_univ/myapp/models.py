# myapp/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    role = models.CharField(max_length=50, blank=True, null=True, default="Admin")

    class Meta:
        db_table = 'auth_user'

class adcourse(models.Model):
    cname= models.CharField(max_length=60)
    cdetails= models.CharField(max_length=60,null=True)
    cduration= models.CharField(max_length=60)
    cprice=models.CharField(max_length=100)
    cgst= models.IntegerField(null=True)

class ck_table(models.Model):
    Location = models.CharField(max_length=100)
    education = models.CharField(max_length=60)
    comp_year = models.IntegerField(blank=True,null=True)
    parent_name = models.CharField(max_length=60)
    ph_num = models.CharField(max_length=20,unique=True)
    al_ph_num = models.CharField(max_length=20)
    parent_ph_num = models.CharField(max_length=20)
    email = models.EmailField(max_length=100,unique=True)
    address= models.CharField(max_length=100)
    source= models.CharField(max_length=20,null=True)
    payment_type=models.CharField(max_length=50)
    payment_mode=models.CharField(max_length=50)
    amount=models.CharField(max_length=100)
    remark=models.CharField(max_length=50)
    receipt_id=models.CharField(max_length=20,default=0)
    candid_name=models.CharField(max_length=60,null=True)
    price=models.CharField(max_length=100,null=True)
    blc_amnt=models.CharField(max_length=100,null=True)
    acourse= models.ForeignKey(adcourse,on_delete=models.CASCADE,default=1)
    dat=models.DateField(auto_now_add=True,null=True)
    nxt_month=models.DateField(null=True)
    status= models.CharField(max_length=20)
    inactive_dat=models.DateField(null=True)
    dis_price=models.CharField(max_length=100,null=True)
    discount=models.CharField(max_length=100,null=True)
    final_amount=models.CharField(max_length=100,null=True)
    gst_amount=models.CharField(max_length=100,null=True)
    gst_p=models.CharField(max_length=100,null=True)
    cgst=models.CharField(max_length=100,null=True)
    candid_no=models.CharField(max_length=25,null=True)


class Rep_id(models.Model):
    receipt_id=models.IntegerField(default=0)
    dat=models.DateField(auto_now_add=True,null=True)

class paydetails(models.Model):
    candid_name = models.CharField(max_length=60)
    amount=models.CharField(max_length=100,null=True)
    final_amount=models.CharField(max_length=100,null=True)
    gst_p=models.CharField(max_length=100,null=True)
    dat=models.DateField(null=True)
    ckid= models.IntegerField(null=True)
    discount=models.CharField(max_length=100,null=True)

class qualifications(models.Model):
    qualification= models.CharField(max_length=60)
    remark= models.CharField(max_length=60,null=True)
    created_at= models.DateField()

class source(models.Model):
    source_name= models.CharField(max_length=60)
    status= models.CharField(max_length=60,null=True)
    created_at= models.DateField()

class locations_add(models.Model):
    loc_name= models.CharField(max_length=60)
    status= models.CharField(max_length=60,null=True)
    created_at= models.DateField()