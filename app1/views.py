from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import View
from .utils import render_to_pdf
from .models import *
from .forms import *
from django.template.loader import get_template

# from django.contrib.sessions.models import Session
# from django.contrib.auth.models import User

# session_key = '8cae76c505f15432b48c8292a7dd0e54'

# session = Session.objects.get(session_key=session_key)
# session_data = session.get_decoded()
# print session_data
# uid = session_data.get('_auth_user_id')
# user = User.objects.get(id=uid)


# Create your views here.

################################# admin module ########################################

##load admin page 

def load_admin_dashboard(request):
    obj=rented_parking_slot_details.objects.all().order_by("-id")

    return render(request,'admin_page.html',{'slot_details':obj})


## add parking slots

def add_parking_slots(request):
    if request.method == 'POST':
        
        name=request.POST.get("slot_name")
        
        if not parking_slot_details.objects.filter(slot_name=name).exists():
            status=request.POST.get("status")
            slot_type=request.POST.get("slot_type")
            price=request.POST.get("price")
            
            

            parking_slot_details(slot_name=name,status=status,slot_type=slot_type,price=price).save()
        else:
            messages.error(request,'already entered parking spot')


    return render(request,'add_parking_slots.html')



### remove parking slots

def remove_parking_slot(request):

    obj=parking_slot_details.objects.all().order_by('-id')

    req_id=request.POST.get("id")

    try:
        obj_delete=parking_slot_details.objects.get(id=req_id)
    except parking_slot_details.DoesNotExist:
        obj_delete=None
    
    if request.method =='POST':
        obj_delete.delete()

    return render(request,'remove_slots.html',{'slot_details':obj})


### book slot details 
def book_slot(request):


    return render(request,'book_slot.html')



def approve_employee_function(request):

    obj=employee_registration.objects.all().order_by("-id")

    req_id=request.POST.get("id")

    try:
        obj_update=employee_registration.objects.get(id=req_id)
    except employee_registration.DoesNotExist:
        obj_update=None
    
    if request.method =='POST':
        status_update=request.POST.get("update")
        obj_update.status=status_update
        obj_update.save()
        

    return render(request,'admin_approve_employee.html',{'employee_details':obj})

##### view attendance 
###################################### Registrations ############################################


######################################## Employee Registration ###################################

def employee_registration_function(request):

    if request.method == 'POST':
        get_name=request.POST.get("name")
        
        if not employee_registration.objects.filter(name=get_name).exists():
            
            form=employee_registration_form(request.POST)
            
            if form.is_valid():
                obj=form.save(commit=True)
                obj.status='Not Approved'
                obj.save()
        else:
            messages.error(request,'You have already registered employee.')
    
    else:

        form=employee_registration_form()

    

    return render(request,'employee_registration_form.html')


########################################## User Registration #######################################

def user_registration_function(request):

    if request.method == 'POST':
        get_name=request.POST.get("name")
        
        if not user_registration.objects.filter(name=get_name).exists():
            
            form=user_registration_form(request.POST)
            
            if form.is_valid():
                form.save()
        else:
            messages.error(request,'You have already registered user.')
    
    else:

        form=user_registration_form()

    return render(request,'user_registration_form.html')

    


    




######################################### Sign In Page ###################################################

def load_sign_page(request):

    if request.method == 'POST':
        username=request.POST.get("username")
        password=request.POST.get("password")

        if username == 'admin' :

            sign_in_table(username=username,password=password,role='admin').save()
            
            return render(request,'admin_page.html')
        
        elif user_registration.objects.filter(username=username,password=password).exists() :

            sign_in_table(username=username,password=password,role='user').save()

            return render(request,'user_select_choice.html')
        
        elif employee_registration.objects.filter(username=username,status='Approved',password=password).exists():

            sign_in_table(username=username,password=password,role='employee').save()

            return render(request,'employe_homepage.html')

        else:
            return render(request,'sign_in_error.html')
    return render(request,'signin.html')


########################################## employee module ###############################################

#### employee homepage

def employee_homepage(request):

    return render(request,'employe_homepage.html')


###### employee select choice

def view_choice(request):

    return render(request,'employee_billing_choice.html')



##############status changing##########3
def status_change(request):

    obj3=parking_slot_details.objects.filter(status="unavailable")
    req_id=request.POST.get("id")
    if request.method =='POST':
        obj_update=parking_slot_details.objects.get(id=req_id)
        obj_update.status="available"
        obj_update.save()
    return render(request,'change_employee.html',{'slot_details':obj3})


####### search parking details

#def employee_search(request):

    #obj=parking_slot_details.objects.filter(status="unavailable")

    #req_id=request.POST.get("id")
    #if request.method =='POST':
       # obj_update=parking_slot_details.objects.get(id=req_id)
        #obj_update.status="available"
        #obj_update.save()
    #return render(request,'change.html',{'slot_details':obj})
########## employee update attendance 

#### employee view customer details


   

##########################################  user module ###################################################

#### load  user homepage 

#### load  user homepage 

# def view_page(request):

#     obj=parking_slot_details.objects.all().order_by('-id')

#     req_id=request.POST.get("id")

#     try:
#         obj_save=parking_slot_details.objects.get(id=req_id)
#     except parking_slot_details.DoesNotExist:
#         obj_save=None
    
#     if request.method =='POST':
#         obj_save.save()

#     return render(request,'user_homepage.html',{'slot_details':obj})


def view_user_homepage(request):
    #obj3=parking_slot_details.objects.filter(status="available")
    # obj3=parking_slot_details.objects.filter(slot_type="car",status="available") 
    # global req_id
    # req_id=request.POST.get("id")
        
    return render(request,'car_bike.html')
#def view_user_homepage(request)

def car(request):
    obj=parking_slot_details.objects.filter(slot_type="car",status="available")
   
    return render(request,'change.html',{'slot_details':obj})

def bike(request):
    obj=parking_slot_details.objects.filter(slot_type="bike",status="available")
   
    return render(request,'change.html',{'slot_details':obj})



def save_user_book(request,id=None):
    instance1=parking_slot_details.objects.get(id=id)
    price=instance1.price
    name=instance1.slot_name
       

    if request.method=='POST':
        customer_name=request.POST.get("Customer_name")
        vechile_no=request.POST.get("Vechile_number")
        number=request.POST.get("number")

        p_id=instance1.id
        instance1=parking_slot_details.objects.get(id=id)

        price=instance1.price
        name=instance1.slot_name
       
        


        if parking_slot_details.objects.filter(slot_name=name).exists():
            obj_update=parking_slot_details.objects.get(slot_name=name)
            obj_update.status="unavailable"
            obj_update.save()

        customer_details(customer_name=customer_name,vehicle_number=vechile_no,phone_number=number,price=price,slot_name=name).save()
        temp_customer_details(customer_name=name,vehicle_number=vechile_no,phone_number=number,price=price,slot_name=name).save()
        return redirect('user_homepage')
    return render(request,'user_confirm_slot.html',{'name':name, 'price':price})
    

    #if request.method == 'POST':
       # req_spot=request.POST.get("input_spot")
        
        
        #if parking_slot_details.objects.filter(location=req_spot).exists():
          #  obj=parking_slot_details.objects.filter(location=req_spot)
            #return render(request,'user_parking_slot_details.html',{'slot_details':obj})
        #else:
           # return render(request,'error.html')

    #return render(request,'user_homepage.html')



    #obj=parking_slot_details.objects.all().order_by('-id')

    #req_id=request.POST.get("id")

    #try:
       # obj_delete=parking_slot_details.objects.get(id=req_id)
    #except parking_slot_details.DoesNotExist:
       # obj_delete=None
    
    #if request.method =='POST':
        #obj_delete.delete()

    #return render(request,'user_homepage.html',{'slot_details':obj})


    #obj=parking_slot_details.objects.all()
  
    #return render(request,'user_homepage.html',{'slot_details':obj})


### parking slots availability page

def load_slot_detials(request):

    return render(request,'user_parking_slot_details.html')

### load error page ###

def load_error_page(request):

    return render(request,'error.html')




## load slot selection page ##

def load_slot(request,slot_id):

    selected_slot_id=slot_id
    obj=parking_slot_details.objects.get(id=selected_slot_id)
    total_slots=obj.total_slots_available
    two_wheeler_available_slots=obj.two_wheeler_slots
    
    
    
    if request.method == 'POST':
        get_choice=request.POST.get("slots_selected")

        if not slot_status.objects.filter(slot_number_selected=get_choice,status='parked',slot_id=selected_slot_id).exists():
            slot_status(slot_id=selected_slot_id,slot_number_selected=get_choice,location_name=obj.location_name,status='parked').save()
            temp_slot_status(slot_id=selected_slot_id,slot_number_selected=get_choice,location_name=obj.location_name,status='parked').save()

           
            
        else:
            messages.error(request,'this slot has been parked')
        

    return render(request,'user_slot_book.html',{'slots_available':range(total_slots),'two_wheeler_available_slots':two_wheeler_available_slots})


### load confirm booking slot page

def load_booking_slot_page(request):

    if request.method == 'POST':
        
        name=request.POST.get("Customer_name")
        vechile_no=request.POST.get("Vechile_number")
        number=request.POST.get("number")
        customer_details(customer_name=name,vehicle_number=vechile_no,phone_number=number).save()
        temp_customer_details(customer_name=name,vehicle_number=vechile_no,phone_number=number).save()

    return render(request,'user_confirm_slot.html')

#### view invoice of parking

def user_invoice(request):

    obj1=temp_customer_details.objects.all()
    obj2=temp_slot_status.objects.all()

    template=get_template('user_invoice.html')
    html=template.render({'customer_details':obj1,'slot_details':obj2})

    pdf = render_to_pdf('user_invoice.html', {'customer_details':obj1,'slot_details':obj2})
    
    return HttpResponse(pdf, content_type='application/pdf')

   

#### employee view customer details

def view_customer_details(request):


    obj=customer_details.objects.all()


    return render(request,'employee_view_customer_details.html',{'customer_details':obj})


###### logout  user ###########

def user_log_out(request):

    if request.method == 'POST':

       obj1=temp_customer_details.objects.all()
       obj2=temp_slot_status.objects.all()
       obj1.delete()
       obj2.delete()

       return redirect('sign_in_page')

    return render(request,'Log_out.html')



#### page to select the option whether to park or give slot for rent

def load_user_choice(request):

    return render(request,'user_select_choice.html')


### load add slots for rent by user

def load_slot_add(request):

    if request.method == 'POST':
        
        name=request.POST.get("Customer_name")
        vechile_no=request.POST.get("Vechile_number")
        number=request.POST.get("number")
        customer_details(customer_name=name,vehicle_number=vechile_no,phone_number=number).save()
        temp_customer_details(customer_name=name,vehicle_number=vechile_no,phone_number=number).save()

    return render(request,'user_confirm_slot.html')

def user_homepage(request):
    if request.method == 'POST':
        
        name=request.POST.get("customer_name")
        vechile_no=request.POST.get("vechile_number")
        number=request.POST.get("phone_number")
        form=book_parking(request.POST)
        if form.is_valid():
            form.save()

        customer_details(customer_name=name,vehicle_number=vechile_no,phone_number=number).save()
        temp_customer_details(customer_name=name,vehicle_number=vechile_no,phone_number=number).save()

    return render(request,'user_confirm_slot.html')

def book_slot(request):

    obj3=parking_slot_details.objects.filter(status="available")
    req_id=request.POST.get("id")
    if request.method =='POST':
        obj_update=parking_slot_details.objects.get(id=req_id)
        obj_update.status="unavailable"
        obj_update.save()
    return render(request,'change.html',{'slot_details':obj3})
####
def a(request):
    obj=customer_details.objects.all()


    return render(request,'employee_view_customer_details.html',{'customer_details':obj})

##############customer notification

def notification(request):
    if request.method=='POST':
        box=request.POST.get("notification")
        name=request.POST.get("nothing")
        slot=request.POST.get("slot_id")
        notification_user(notification_box=box,user_name=name,slot_id=slot).save()
        
    return render(request,'notification.html')

############employeee_view notifications
def view_notifications(request):
    obj=notification_user.objects.all()
    req_id=request.POST.get("id")
    
    return render(request,'employee_view_notification.html',{'not_details':obj})


