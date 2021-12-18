from django import forms
from .models import  *

### form for add parking slot ##########

class rent_slot_form(forms.ModelForm):

    class Meta :
        model=rented_parking_slot_details
        fields=['spot_name','customer_name','customer_number','customer_location','total_slots_available']


##### form for user registration ############

class user_registration_form(forms.ModelForm):

    class Meta:

        model=user_registration
        fields=['name','phone','username','password']


###########  employee registration form #############

class employee_registration_form(forms.ModelForm):

    class Meta:

        model=employee_registration
        fields=['name','phone','username','password','work_location']

############## reg customer###############
class book_parking(forms.ModelForm):
    class Meta:

        model=customer_details
        fields=['customer_name','vehicle_number','phone_number']

############NOTIFICATAION
