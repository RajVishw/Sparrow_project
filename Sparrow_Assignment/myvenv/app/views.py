from django.shortcuts import render,HttpResponse,redirect
from.models import *
from .forms import PurchaseForm, PurchaseDetailsFormset
# Create your views here.
def Dashboard(request):
    return render(request, 'Homepage.html')

def InsertPageView(request):
    return render(request, 'Index.html')

def InsertData(request):
    item_name=request.POST.get("item_name")
    item_code=request.POST.get("item_code")
    price=request.POST.get("price")
    datetime=request.POST.get("datetime")
    status=request.POST.get("status")
    
    newItem = Item.objects.create(item_name=item_name,item_code=item_code,price=price,datetime=datetime,status=status)
    return redirect("views")

def ViewItems(request):
    alldata=Item.objects.all()
    return render(request, 'Allitems.html',{'key1':alldata})
    
def EditPage(request,pk):
    #Fetcting the data of perticular ID
    get_data=Item.objects.get(id=pk)
    return render(request, 'edit.html',{'key2':get_data})    
    
def updateData(request,pk):
    update=Item.objects.get(id=pk)
    update.item_name=request.POST["item_name"]
    update.item_code=request.POST["item_code"]
    update.price=request.POST["price"]
    update.datetime=request.POST["datetime"]
    update.status=request.POST["status"]
    update.save()
    return redirect('views')

def DeleteData(request,pk):
    ddta=Item.objects.get(id=pk)
    ddta.delete()
    return redirect("views")


def InsertPageSupp(request):
    return render(request, 'supplier.html')

def create_supplier(request):
    supplier_name=request.POST.get("supplier_name")
    mobile_no=request.POST.get("mobile_no")
    address=request.POST.get("address")
    datetime=request.POST.get("datetime")
    status=request.POST.get("status")
    
    newItem = Supplier.objects.create(supplier_name=supplier_name,mobile_no=mobile_no,address=address,date=datetime,status=status)
    return HttpResponse("Added Succesfully")
#---------------------------------------------------------------------------------
def create_purchase(request):
    if request.method == 'POST':
        purchase_form = PurchaseForm(request.POST)
        detail_formset = PurchaseDetailsFormset(request.POST)

        if purchase_form.is_valid() and detail_formset.is_valid():
            purchase = purchase_form.save()  # Save the purchase
            for form in detail_formset:
                detail = form.save(commit=False)
                detail.purchase_master = purchase
                detail.save()  # Save each purchase detail

            # Redirect or display success message
            return redirect('purchase_success')
    else:
        purchase_form = PurchaseForm()
        detail_formset = PurchaseDetailsFormset()

    return render(request, 'create_purchase.html', {
        'purchase_form': purchase_form,
        'detail_formset': detail_formset,
    })
    

    
    
   
