from django.shortcuts import render
from Login.models import Account_User_ID
from django.http import HttpResponse
from EShop.models import Productcategory, Product
import datetime
import json
# Create your views here.
def dashboard(request):
    current_user = request.user
    if Account_User_ID.objects.filter(user_id=current_user.id).exists():
        acc_Cre=Account_User_ID.objects.get(user_id=current_user.id)
        if acc_Cre.role=="Admin":
            print('exits')
            response = render(request, 'admins/index.html')
        else:
            response = redirect(request,'/Login/Login')
    return response

def Products(request):
    current_user = request.user
    if Account_User_ID.objects.filter(user_id=current_user.id).exists():
        acc_Cre=Account_User_ID.objects.get(user_id=current_user.id)
        if acc_Cre.role=="Admin":
            print('exits')
            response = render(request, 'admins/product.html')
        else:
            response = redirect(request,'/Login/Login')
    return response

def AddProduct(request):
    current_user = request.user
    if Account_User_ID.objects.filter(user_id=current_user.id).exists():
        acc_Cre=Account_User_ID.objects.get(user_id=current_user.id)
        if acc_Cre.role=="Admin":
            response = render(request, 'admins/addproduct.html')
        else:
            response = redirect(request,'/Login/Login')
    if request.method=="POST":
        try:
            Category = request.POST.get('Category')
            productname = request.POST.get('Product')
            Subcategory = request.POST.get('Subcategory')
            sPrice = request.POST.get('Price')
            sale = request.POST.get('sale')
            Price = request.POST.get('FinalPrice')
            Unit = request.POST.get('Unit')
            Quantity = request.POST.get('Quantity')
            Description = request.POST.get('Description')
            Status = request.POST.get('Status')
            Image1 = request.FILES['Imageone'] if 'Imageone' in request.FILES else False
            Image2 = request.FILES['Imagetwo'] if 'Imagetwo' in request.FILES else False
            Image3 = request.FILES['Imagethree'] if 'Imagethree' in request.FILES else False
            if Productcategory.objects.filter(category=Category).exists():
               cartegory= Productcategory.objects.get(category=Category)
            else:
                cartegory=Productcategory()
                cartegory.category=Category
                cartegory.pub_date=datetime.date
                cartegory.save()
            print(cartegory.category_id)
            product=Product()
            product.product_name=productname
            product.category_id=cartegory.category_id
            product.subcategory=Subcategory
            product.sales=sale
            product.price=Price
            product.sprice=sPrice
            product.desc=Description
            product.Unit=Unit
            product.Qty=Quantity
            if Status =="True":
                product.Status=True
            else:
                product.Status=False
            product.image=Image1
            product.image1=Image2
            product.image2=Image3
            product.pub_date=datetime.date.today()
            product.save()
            response = render(request, 'admins/addproduct.html')
        except Exception as e:
            print(e)
            return HttpResponse(e)
    return response

def searchcategory(request):
     if request.method=="POST":
        try:
            query = request.POST.get('searchinput')
            allcategory=[]
            print(query)
            cattemp=Productcategory.objects.all()
            for item in cattemp:
                if query.lower() in item.category.lower():
                    allcategory.append({'name':item.category,'id':item.category_id})
            res_list = removeduplicate(allcategory)
            response= json.dumps([res_list], default=str)
            return HttpResponse(response)
        except Exception as e:
            print(e)
            return HttpResponse('{}')

def searchproduct(request):
     if request.method=="POST":
        try:
            query = request.POST.get('searchinput')
            allcategory=[]
            cattemp=Product.objects.all()
            for item in cattemp:
                if query.lower() in item.product_name.lower():
                    allcategory.append({'name':item.product_name,'id':item.product_id})
            res_list = removeduplicate(allcategory)
            response= json.dumps([res_list], default=str)
            return HttpResponse(response)
        except Exception as e:
            return HttpResponse('{}')

def searchunit(request):
     if request.method=="POST":
        try:
            query = request.POST.get('searchinput')
            allcategory=[]
            cattemp=Product.objects.all()
            for item in cattemp:
                if query.lower() in item.Unit.lower():
                    allcategory.append({'name':item.Unit,'id':item.product_id})
            res_list = removeduplicate(allcategory)
            response= json.dumps([res_list], default=str)
            return HttpResponse(response)
        except Exception as e:
            return HttpResponse('{}')


def removeduplicate(allskills):
    res_list = [] 
    for i in range(len(allskills)): 
        if allskills[i] not in allskills[i + 1:]: 
            res_list.append(allskills[i]) 
    return res_list
            