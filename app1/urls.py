
from django.urls import path
from .import views

urlpatterns = [

    ########### admin module urls ######################################

    path('admin_dashboard',views.load_admin_dashboard,name='admin_dashboard'),
    path('add_parking_slots',views.add_parking_slots,name='add_slots'),
    #path('book',views.book,name='book slots'),
    path('remove_parking_slot',views.remove_parking_slot,name='remove_slot'),
 
    path('approve_employee',views.approve_employee_function,name='approve_employee'),
    
    ################# Sign In page #######################################

    path('',views.load_sign_page,name='sign_in_page'),


    #################  Registrations #####################################

    #################  Employee ############################################
    
    path('employee_registration',views.employee_registration_function,name='employee_registration'),

    ################## user ##############################

    path('user_registration',views.user_registration_function,name='user_registration'),

    ############### User module urls ######################################
    path('user_homepage',views.view_user_homepage,name='user_homepage'),
    path('user_slot_detials',views.load_slot_detials,name='slot_details'),
    path('error_page',views.load_error_page),
    path('load_slots<int:slot_id>',views.load_slot,name='select_slot'),
    path('load_booking_slot_page',views.load_booking_slot_page,name='confirm_booking'),
    path('view_invoice',views.user_invoice,name='invoice'),
    path('log_out_page',views.user_log_out,name='log_out_page'),
    path('load_user_choice',views.load_user_choice,name='load_choice'),
    path('load_spot_rent',views.load_slot_add,name='load_spot_rent'),

    #################### Employee Urls #################################

    path('employee_homepage',views.employee_homepage,name='employee_homepage'),
    path('status_change',views.status_change,name='status_change'),
    path('employee_view-customer_details',views.view_customer_details,name='customer_details'),
    path('employee_select-choice',views.view_choice,name='view_choice'),
    path('change',views.status_change,name='status_change'),
    path('book_slot',views.book_slot,name='book_slot'),
    path('a',views.a,name='a'),
    path('user_homepage',views.user_homepage,name='user_homepage'),
    path('save_user_book/<int:id>/',views.save_user_book,name='save_user_book'),
    path('notification',views.notification,name='notification'),
    path('view_notifications',views.view_notifications,name='view_notifications'),
    # path('delete_notification',views.delete_notification,name='delete_notification'),
    path('car',views.car,name='car'),
    path('bike',views.bike,name='bike')
    ]
