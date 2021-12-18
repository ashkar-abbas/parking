from django.db import models

# Create your models here.


########### Sign In Table ################

class sign_in_table(models.Model):

    username=models.CharField(max_length=250)
    password=models.CharField(max_length=250)
    role=models.CharField(max_length=250)



#### registration tables ###

##### user #############

class user_registration(models.Model):

    name=models.CharField(max_length=250)
    phone=models.CharField(max_length=20)
    username=models.CharField(max_length=250)
    password=models.CharField(max_length=250)

###### Employee ##############

class employee_registration(models.Model):

    name=models.CharField(max_length=250)
    phone=models.CharField(max_length=20)
    username=models.CharField(max_length=250)
    password=models.CharField(max_length=250)
    work_location=models.CharField(max_length=250)
    status=models.CharField(max_length=250)
    attendance=models.CharField(max_length=250)

class slot_type(models.Model):

    slot_type=models.CharField(max_length=500)
   

# table to store parking slot details

class parking_slot_details(models.Model):

    slot_name=models.SlugField(max_length=500)
    status=models.CharField(max_length=500)
    slot_type=models.CharField(max_length=500)
    price=models.IntegerField()
## table to store rented parking slot details

class rented_parking_slot_details(models.Model):

    spot_name=models.CharField(max_length=500)
    customer_name=models.CharField(max_length=500)
    customer_number=models.CharField(max_length=500)
    customer_location=models.CharField(max_length=500)
    total_slots_available=models.IntegerField()


   
## table to store status of slots

class slot_status(models.Model):

    slot_id=models.IntegerField()
    location_name=models.CharField(max_length=500)
    status=models.CharField(max_length=500)
    slot_number_selected=models.IntegerField()

### temporary table
class temp_slot_status(models.Model):
    
    slot_id=models.IntegerField()
    location_name=models.CharField(max_length=500)
    status=models.CharField(max_length=500)
    slot_number_selected=models.IntegerField()

### Customer parking details

class customer_details(models.Model):

    customer_name=models.CharField(max_length=500)
    vehicle_number=models.CharField(max_length=500)
    phone_number=models.CharField(max_length=20)
    price=models.CharField(max_length=20)
    slot_name=models.CharField(max_length=30)

#### temporary storage ######
class temp_customer_details(models.Model):
    
    customer_name=models.CharField(max_length=500)
    vehicle_number=models.CharField(max_length=500)
    phone_number=models.CharField(max_length=20)
    price=models.CharField(max_length=20)
    slot_name=models.CharField(max_length=30)

######## notifications

class notification_user(models.Model):
    notification_box=models.CharField(max_length=20000)
    user_name=models.CharField(max_length=20000)
    slot_id=models.CharField(max_length=200)
