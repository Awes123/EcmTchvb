from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Orders, OrderUpdate, Newsletter, Productcategory
from Login.models import Account_detail, Account_User_ID
from django.contrib.auth.models import User, auth
from django.conf import settings
from math import ceil
from PayTm import Checksum
from Login.views import sendemail
import json
from django.views.decorators.csrf import csrf_exempt
MERCHANT_KEY = 'ypVhWZYXUiqpHstL';
# Create your views here.
def index(request):
    current_user = request.user
    account={}
    if Account_User_ID.objects.filter(user_id=current_user.id).exists():
        acc_Cre=Account_User_ID.objects.get(user_id=current_user.id)
        account=Account_detail.objects.get(account_id=acc_Cre.account_id)
    allprods=[]
    catprods = Product.objects.values('category_id','id')
    cats = {item['category_id'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category_id=cat)
        n=len(prod)
        nSlides=n//4 + ceil((n/4)-(n//4))
        allprods.append([prod,range(1,nSlides),nSlides])
    # param={'no_of_slides' : nSlides, 'range' : range(1,nSlides), 'Product' : product}
    # allprods=[[product, range(1,nSlides), nSlides],[product, range(1,nSlides),nSlides]]
    params= {'allprods': allprods,'account':account}
    return render(request, 'eshop/index.html',params)

def search(request):
    query = request.GET.get('search')
    allprods=[]
    catprods = Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp=Product.objects.filter(category=cat)
        prod=[item for item in prodtemp if searchMatch(query, item)]
        n=len(prod)
        nSlides=n//4 + ceil((n/4)-(n//4))
        if len(prod)!=0:
            allprods.append([prod,range(1,nSlides),nSlides])
    params= {'allprods': allprods,'msg':''}
    if len(allprods)==0 or len(query) < 4:
        params={'msg':'Please Make Sure To Enter Relevent For Search'}
    return render(request, 'eshop/search.html',params)

def searchMatch(query,item):
    # '''return true if query match item'''
    if query.lower() in item.desc.lower() or query.lower() in item.product_name.lower() or query.lower() in item.category.lower():
        return True
    else:
        return False

def about(request):
    return render(request, 'eshop/about.html')

def contact(request):
    thank = False
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('phone','')
        phone=request.POST.get('email','')
        comments=request.POST.get('comments','')
        contact=Contact(name=name,email=email,phone=phone,comments=comments)
        contact.save()
        thank = True
    return render(request, 'eshop/contact.html',{'thank':thank})

def tracker(request):
    if request.method=="POST":
        order_id=request.POST.get('order_id','')
        email=request.POST.get('inputEmail','')
        try:
            order=Orders.objects.filter(order_id=order_id,email=email)
            if len(order)>0:
                update=OrderUpdate.objects.filter(order_id=order_id)
                updates=[]
                for item in update:
                    updates.append({'text':item.update_desc,'time':item.timestamp})
                    response= json.dumps([updates,order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
    return render(request,'eshop/tracker.html')

def prodView(request,myid):
    #Fetch The Product Using the Id
    product=Product.objects.filter(id=myid)
    return render(request, 'eshop/productview.html',{'product': product[0]})

def checkout(request):
    current_user = request.user
    account={}
    if Account_User_ID.objects.filter(user_id=current_user.id).exists():
        acc_Cre=Account_User_ID.objects.get(user_id=current_user.id)
        account=Account_detail.objects.get(account_id=acc_Cre.account_id)
    if request.method=="POST":
        current_user = request.user
        account={}
        if Account_User_ID.objects.filter(user_id=current_user.id).exists():
            acc_Cre=Account_User_ID.objects.get(user_id=current_user.id)
            account=Account_detail.objects.get(account_id=acc_Cre.account_id)
            items_json=request.POST.get('itemsJson','')
            name=account.contact_person
            amount=request.POST.get('amount','')
            email=account.email
            phone=account.mobile
            address=account.Houseno+'__'+account.Colony
            city=account.city
            state='Maharashtra'
            zip_code='431001'
            order=Orders(items_json=items_json,amount=amount,name=name,email=email,phone=phone,address=address,city=city,state=state,zip_code=zip_code)
            order.save()
            update=OrderUpdate(order_id=order.order_id,update_desc="The order has been placed")
            update.save()
            thank = True
            id=order.order_id
        # return render(request, 'eshop/checkout.html',{'thank':thank,'id':id})
        # Request paytm to transfer the amount to our account after payment by user
        param_dict={
            'MID':'XvZFQu70071793970152',#marchent ID
            'ORDER_ID':str(order.order_id),#Order ID
            'TXN_AMOUNT':str(amount),
            'CUST_ID':'acfff@paytm.com',#customer Email
            'INDUSTRY_TYPE_ID':'Retail',
            'WEBSITE':'WEBSTAGING',
            'CHANNEL_ID':'WEB',
	        'CALLBACK_URL':'http://127.0.0.1:8000/shop/handlerequest/',
        }
        param_dict['CHECKSUMHASH']=Checksum.generate_checksum(param_dict,MERCHANT_KEY)
        return render(request,'eshop/paytm.html',{'param_dict':param_dict})
    return render(request, 'eshop/checkout.html')

@csrf_exempt
def handlerequest(request):
    form = request.POST
    response_dict= {}
    for i in form.keys():
        response_dict[i]=form[i]
        if i =='CHECKSUMHASH':
            checksum=form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE']=='01':
            print('order successful')
        else:
            print('order was not successful becuase'+response_dict['RESPMSG'])
    #paytm will send you post request
    return render(request,'eshop/paymentstatus.html',{'response':response_dict})
    pass

def Newsletters(request):
    if request.method=="POST":
        email=request.POST.get('inputEmail','')
        if Newsletter.objects.filter(Email=email).exists():
            return HttpResponse("Already Exists")
            print(email)    
        else:
            newsletters=Newsletter()
            newsletters.Email=email
            newsletters.save()
            Subject = 'Lucky Store Subscription'
            text_content= 'Hi Subscriber,'
            html_content= '<h4>Hi Subscriber,</h4><br>Thanks For Showing Your interest & Subscribed Lucky Store<br><br>Get E-mail updates about our latest shop and special offers.<br><br><b>Best Regards</b><br><b>Lucky Store Team</b>'
            sendemail(Subject,text_content,email,html_content)
            return HttpResponse("Thanks For Subscribe.")

def returncategory(request):
     if request.method=="POST":
        email=request.POST.get('inputEmail','')
        print(email)
        prodcat= Productcategory.objects.get(category_id=email)
        return HttpResponse(prodcat.category)