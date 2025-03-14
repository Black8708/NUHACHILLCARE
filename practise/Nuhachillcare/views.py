from django.shortcuts import render , redirect
from .models import bhaiimodel
from datetime import timedelta,datetime
from twilio.rest import Client
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
# NUHACHILLCARE  AC Service project functions



def service(request):
    customer=bhaiimodel.objects.all()
    if request.method=="POST":
        AC_ISSUE_CHARGES = {
        "Cooling Issues": 150,
        "Electrical Problems": 200,
        "Water Leakage": 180,
        "Noisy Operation": 120,
        "Others": 250
          }
        data=request.POST
        name=data.get("name")
        address=data.get("address")
        ph_no=data.get("ph_no")
        ac_brand=data.get("ac_brand")
        ac_issue=data.get("ac_issue")
        service_charges=data.get("service_charges")
        service_date=data.get("service_date")
        nxt_service_date=data.get("nxt_service_date")
        print(ac_issue,"i am issue")
        for i ,j in AC_ISSUE_CHARGES.items():
            if i==ac_issue:
                service_charges=j
        print(service_charges,"i am service charge")

        adddate=datetime.strptime(service_date, "%Y-%m-%d").date()

        if not nxt_service_date:
            nxt_service_date=adddate + timedelta(days=90)
        
        chillcare=bhaiimodel(para_name=name,para_address=address,para_ph_no=ph_no,para_ac_brand=ac_brand,para_ac_issue=ac_issue,para_service_date=service_date,para_nxt_service_date=nxt_service_date, para_service_charges=service_charges)
        chillcare.save()
        
        return redirect('index')
    return render(request,'nuhachill/index.html',{"datavalue":customer})



def update_data(request,id):
    mydata=bhaiimodel.objects.get(id=id) # first get that id of row defaultly its get method so go to last step
    if request.method=="POST": #after its method is post and inside a function
        data=request.POST
        name=data.get("name")
        address=data.get("address")  # get update value and save this variable
        ph_no=data.get("ph_no")
        ac_brand=data.get("ac_brand")
        ac_issue=data.get("ac_issue")
        service_charges=data.get("service_charges")
        service_date=data.get("service_date")
        nxt_service_date=data.get("nxt_service_date")
        service_date=datetime.strptime(service_date, "%Y-%m-%d").date()

        if service_date:
            mydata.para_service_date=service_date           #Adding 90 days from service_date to nxt_service_date


        if service_date:
            if not nxt_service_date:
        
                nxt_service_date=service_date + timedelta(days=90)
                mydata.para_nxt_service_date=nxt_service_date
            else:
                nxt_service_date=datetime.strptime(nxt_service_date, "%Y-%m-%d").date()
                mydata.para_nxt_service_date=nxt_service_date
        


        mydata.para_name=name    #replace the values
        mydata.para_address=address
        mydata.para_ph_no=ph_no
        mydata.para_ac_brand=ac_brand
        mydata.para_ac_issue=ac_issue
        mydata.para_service_charges=service_charges
        
        
        mydata.save()
        return redirect('index')

    return render(request,'nuhachill/update.html',{"mainkey":mydata}) #save the entered data in mydata to mainkey




def delete_data(self,id):
    data=bhaiimodel.objects.get(id=id)
    if data:
        data.delete()
        return redirect("index")





# NXT SERVICE DATE REMINDER USING TWILIO MODULE & FUNCTION 



# def send_sms_reminder(ph_no, name,nxt_service_date):
#     account_sid = 'your_account_sid'
#     auth_token = 'your_auth_token'
#     client = Client(account_sid, auth_token)

#     message = client.messages.create(
#         body=f'Hello {name}, your next AC service is due on {nxt_service_date}.',
#         from_='+1234567890',  # Twilio number
#         to=ph_no
#     )
#     return message.sid



# /i am using this function to sen the service chagrge amount to frontend
@csrf_exempt
def getservicecharge(request):
    # unpaking the data using json.loads
    AC_ISSUE_CHARGES = {
        "Cooling Issues": 800,
        "Electrical Problems": 300,
        "Water Leakage": 700,
        "Noisy Operation": 250,
        "Others": 500
          }
    data=json.loads(request.body)
    servicedata=data.get("requiredservice")
    
    amount=AC_ISSUE_CHARGES[servicedata]
    # /jsonresponse will pake the data
    # for i,j in AC_ISSUE_CHARGES.items():
    #     print(i,servicedata,"i am servie data")
    #     if i==servicedata:
    #         amount=j
    return JsonResponse({"success":"true","message":"amount send succesfully","amount":amount},status=200)
        

    




# ended thsi function