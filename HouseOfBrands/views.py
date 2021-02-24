from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse

from django.contrib.auth import authenticate, login, logout
from decimal import Decimal
from django.conf import settings

import json
import datetime

from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from taggit.models import Tag

from .models import *
from .forms import *
from .filters import *

from .utils import cookieCart, cartData, guestOrder

# Create your views here.

def home(request):
    return render(request, 'home_base.html', {})




def about(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    context = {'cartItems': cartItems, 'items': items, 'order': order,}
    return render(request, 'HouseOfBrands/about.html', context)




def store(request, category_slug=None):
    data = cartData(request)
    name = 'Store'
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    products = houseOfBrandsProduct.objects.all()
    taglist = Tag.objects.annotate(total_products=Count('houseofbrandsproduct'))
    categorylist = houseOfBrandsCategory.objects.annotate(total_products=Count('houseofbrandsproduct'))
    categorylist2 = houseOfBrandsCategoryLayer2.objects.annotate(total_products=Count('houseofbrandsproduct'))
    categorylist3 = houseOfBrandsCategoryLayer3.objects.annotate(total_products=Count('houseofbrandsproduct'))
    categorylist4 = houseOfBrandsCategoryLayer4.objects.annotate(total_products=Count('houseofbrandsproduct'))
    categorylist5 = houseOfBrandsCategoryLayer5.objects.annotate(total_products=Count('houseofbrandsproduct'))
    categorylist6 = houseOfBrandsCategoryLayer6.objects.annotate(total_products=Count('houseofbrandsproduct'))
    context = {'name': name, 'cartItems': cartItems, 'items': items, 'order': order, 'products':products , 'categorylist' : categorylist ,'taglist' : taglist , 'categorylist2' : categorylist2 , 'categorylist3' : categorylist3 , 'categorylist4' : categorylist4 , 'categorylist5' : categorylist5 , 'categorylist6' : categorylist6 , 'shipping': False}
    return render(request, 'HouseOfBrands/store.html', context)




def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'HouseOfBrands/cart.html', context)




def product_details(request, pk):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    category = None
    categorylist = houseOfBrandsCategory.objects.annotate(total_products=Count('houseofbrandsproduct'))
    product = houseOfBrandsProduct.objects.get(id=pk)
    category = None
    context = {'cartItems': cartItems, 'product':product , 'category_list' : categorylist ,'category' : category , 'shipping': False,}
    print("Categry List: ", categorylist)
    return render(request, 'HouseOfBrands/product.html', context)




def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'HouseOfBrands/checkout.html', context)




def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    customer = request.user.houseofbrandscustomer
    product = houseOfBrandsProduct.objects.get(id=productId)
    order, created = houseOfBrandsOrder.objects.get_or_create(customer=customer, status="Pending")
    orderItem, created = houseOfBrandsOrderItem.objects.get_or_create(order=order, product=product)
    if action == 'add':
        if  product.stock >= 1:
            product.stock = (product.stock - 1)
            orderItem.quantity = (orderItem.quantity + 1)
            print("Stock: ",product.stock)
        else:
            messages.success(request, ("There is currently not enough stock available to fullfill your order"))
    elif action == 'remove':
        product.stock = (product.stock + 1)
        print("Stock: ",product.stock)
        orderItem.quantity = (orderItem.quantity - 1)
    elif action == 'cancel':
                product.stock = (product.stock + orderItem.quantity)
                print("Stock: ",product.stock)
                print("Quantity: ",orderItem.quantity)
                orderItem.quantity = (orderItem.quantity == 0)
    product.save()
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)





def contact(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    context = {'cartItems': cartItems, 'items': items, 'order': order,}
    if request.method == 'POST':
        message = request.POST['message']
        if request.user.is_authenticated:
            name = request.user.username
            email = request.user.email
            message = name + "\n" + email + "\n"+ message
            send_mail('Contact Form', message, settings.EMAIL_HOST_USER, ['christopher@3rdaxis.co.za', 'mcn10.foxx@gmail.com'], fail_silently="false" )
            messages.success(request, ("Your message has been sent successfully..."))
        else:
            name = request.POST['name']
            email = request.POST['email']
            message = name + "\n" + email + "\n"+ message
            send_mail('Contact Form', message, settings.EMAIL_HOST_USER, ['christopher@3rdaxis.co.za', 'mcn10.foxx@gmail.com'], fail_silently="false" )
            messages.success(request, ("Your message has been sent successfully..."))
        return redirect('houseOfBrands:store')
    return render(request, 'HouseOfBrands/contact.html', context)




def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = houseOfBrandsOrder.objects.get_or_create(customer=customer, status="Pending")
    else:
        customer, order = guestOrder(request, data)
    total = Decimal(data['form']['total'])
    order.transaction_id = transaction_id
    print("Order total:::::::: ", total)
    if total == order.get_cart_total:
        print("Order total is correct")
        order.status = "Payment Confirmed, Processing Order"
        order.save()
    else:
        print("Order total is incorrect")
    if order.shipping == True:
        shippingAddress, created = houseOfBrandsShippingAddress.objects.create(
        country=data['shipping']['country'],
        address1=data['shipping']['address1'],
        address2=data['shipping']['address2'],
        city=data['shipping']['city'],
        province=data['shipping']['province'],
        postal_code=data['shipping']['postal_code'],
        )
        customer.shippingAddress = shippingAddress
# Add code to send email to Store Owner
    return JsonResponse('Payment submitted..', safe=False)




#-------------------(CRUD ORDERS) -------------------

def dashboard(request):
    return render(request, "HouseOfBrands/dashboard.html")



def upload(request):
    form = CsvModelsForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelsForm()
        obj = Csv.objects.get(activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader= csv.reader(f)

            for i, row in enumerate(reader):

                if i==0:
                    pass
                else:
                    row = "".join(row)
                    print(row)
                    print(type(row))

    context = {'form': form}
    return render(request, 'HouseOfBrands/ShopCRM/upload.html', context)

#def upload(request):
#    data = {}
#    form = CsvModelsForm(request.POST or None, request.FILES or None)
#
#
#    # if not GET, then proceed
#    try:
#        csv_file = request.FILES[""]
#        if not csv_file.name.endswith('.csv'):
#            messages.error(request,'File is not CSV type')
#            return HttpResponseRedirect(reverse("houseOfBrands:upload"))
#        #if file is too large, return
#        if csv_file.multiple_chunks():
#            messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
#            return HttpResponseRedirect(reverse("houseOfBrands:upload"))
#
#        file_data = csv_file.read().decode("utf-8")
#
#        lines = file_data.split("\n")
#        #loop over the lines and save them in db. If error , store as string and then display
#        for line in lines:
#            fields = line.split(",")
#            data_dict = {}
#            data_dict["name"] = fields[0]
#            data_dict["sku"] = fields[1]
#            data_dict["description"] = fields[2]
#            data_dict["specifications"] = fields[3]
#            data_dict["price"] = fields[4]
#            data_dict["image1"] = fields[5]
#            data_dict["image2"] = fields[6]
#            data_dict["image3"] = fields[7]
#            data_dict["image4"] = fields[7]
#            data_dict["category"] = fields[8]
#            data_dict["categorylayer2"] = fields[10]
#            data_dict["categorylayer3"] = fields[11]
#            data_dict["categorylayer4"] = fields[12]
#            data_dict["categorylayer5"] = fields[13]
#            data_dict["categorylayer6"] = fields[14]
#            data_dict["stock"] = fields[15]
#            data_dict["tags"] = fields[16]
#
#            try:
#                form = EventsForm(data_dict)
#                if form.is_valid():
#                    form.save()
#                    form = form = CsvModelsForm()
#                    obj = Csv.objects.get(activated=False)
#                    with open(obj.file_name.path, 'r') as f:
#                        reader = csv.reader(f)
#
#                        for i, row in enumerate(reader):
#                            if i==0:
#                                pass
#                            else:
#                                print(row)
#
#                    obj.activated = True
#                    obj.save()
#                else:
#                    logging.getLogger("error_logger").error(form.errors.as_json())
#            except Exception as e:
#                logging.getLogger("error_logger").error(repr(e))
#                pass
#
#    except Exception as e:
#        logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
#        messages.error(request,"Unable to upload file. "+repr(e))
#
#    return HttpResponseRedirect(reverse("houseOfBrands:upload"))
#

def orders(request):
    orders = houseOfBrandsOrder.objects.all().order_by('-status')[0:5]
    customers = houseOfBrandsCustomer.objects.all()

    total_customers = customers.count()

    total_orders = houseOfBrandsOrder.objects.all().count()
    delivered = houseOfBrandsOrder.objects.filter(status='Delivered').count()
    pending = houseOfBrandsOrder.objects.filter(status='Pending').count()

    context = {'customers':customers, 'orders':orders,
    'total_customers':total_customers,'total_orders':total_orders,
    'delivered':delivered, 'pending':pending}
    return render(request, 'HouseOfBrands/ShopCRM/orders.html', context)


def customer(request, pk):
    customer = houseOfBrandsCustomer.objects.get(id=pk)
    orders = customer.houseofbrandsorder_set.all()
    shippingDetails = houseOfBrandsShippingAddress.objects.all()
    total_orders = orders.count()

    orderFilter = OrderFilter(request.GET, queryset=orders)
    orders = orderFilter.qs

    context = {'shippingDetails':shippingDetails, 'customer':customer, 'orders':orders, 'total_orders':total_orders,
    'filter':orderFilter}
    return render(request, 'HouseOfBrands/ShopCRM/customer.html', context)

#-------------------(CRUD ORDERS) -------------------
def shippingDetails(request):
    action = 'update'
    shippingDetails = houseOfBrandsShippingAddress.objects.all()
    form = ShippingDetailsForm(instance=shippingDetails)

    context =  {'action':action, 'form':form}
    return render(request, 'HouseOfBrands/ShopCRM/order_form.html', context)


def createOrder(request):
    action = 'create'
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context =  {'action':action, 'form':form}
    return render(request, 'HouseOfBrands/ShopCRM/order_form.html', context)

def updateOrder(request, pk):
    action = 'update'
    order = houseOfBrandsOrder.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/order_details/' + str(order.id))

    context =  {'action':action, 'form':form}
    return render(request, 'HouseOfBrands/ShopCRM/order_form.html', context)

def deleteOrder(request, pk):
    order = houseOfBrandsOrder.objects.get(id=pk)
    if request.method == 'POST':
        customer_id = order.customer.id
        customer_url = '/customer/' + str(customer_id)
        order.delete()
        return redirect(customer_url)

    return render(request, 'HouseOfBrands/ShopCRM/delete_item.html', {'item':order})

def viewOrder(request, pk):
    order = houseOfBrandsOrder.objects.get(id=pk)
    # shippingDetails = Order.shippingDetails
    items = order.houseofbrandsorderitem_set.all()
    customer = request.user.customer
    cartItems = order.get_cart_items

    form = OrderItemsForm(instance=order)
    if request.method == 'POST':
        form = OrderItemsForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/customer/' + str(order.customer.id))

    shippingDetails = customer.shippingAddress
    print("Shipping Address: ", customer.shippingAddress)


    context =  { 'order':order,  'form':form, 'shippingDetails': shippingDetails, 'items':items, 'cartItems': cartItems}
    return render(request, 'HouseOfBrands/ShopCRM/order_details.html', context)



#-------------------(CRUD - PRODUCTS) -------------------

def addProduct(request):
    action = 'create'
    name = "Product"
    form = ProductsForm()
    if request.method == 'POST':
        form = ProductsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/houseOfBrands/products/')

    context =  {'action':action, 'form':form, 'name':name }
    return render(request, 'HouseOfBrands/ShopCRM/order_form.html', context)

def products(request):
    products = houseOfBrandsProduct.objects.all()
    productFilter = ProductFilter(request.GET, queryset=products)
    total_products = products.count()
    products = productFilter.qs

    context = {'total_products': total_products, 'products':products, 'filter': productFilter}

    return render(request, 'HouseOfBrands/ShopCRM/products.html', context)

def updateProduct(request, pk):
    action = 'update'
    product = houseOfBrandsProduct.objects.get(id=pk)
    name = product.name
    form = ProductsForm(instance=product)

    if request.method == 'POST':
        form = ProductsForm(request.POST, instance=product)
        if form.is_valid():
            newproduct = form.save(commit=False)
            newproduct.slug = slugify(newproduct.name)
            newproduct.save()
            # Without this next line the tags won't be saved.
            form.save()
            return redirect('/products/')

    context =  {'action':action, 'form':form, 'name':name, 'product': product, }
    return render(request, 'HouseOfBrands/ShopCRM/order_form.html', context)

def deleteProduct(request, pk):
    product = houseOfBrandsProduct.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('/products')

    return render(request, 'HouseOfBrands/ShopCRM/delete_item.html', {'item':product})


#-------------------(CRUD - CATEGORIES) -------------------

def categories(request):
    categories = houseOfBrandsCategory.objects.all()
    categoryFilter = CategoryFilter(request.GET, queryset=categories)
    total_categories = categories.count()
    categories = categoryFilter.qs

    context = {'total_categories': total_categories, 'categories':categories, 'filter': categoryFilter}

    return render(request, 'HouseOfBrands/ShopCRM/category.html', context)

def addCategory(request):
    action = 'create'
    name = "Category"
    form = CategoriesForm()
    if request.method == 'POST':
        form = CategoriesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/houseOfBrands/categories/')

    context =  {'action':action, 'form':form,  }
    return render(request, 'HouseOfBrands/ShopCRM/order_form.html', context)

def updateCategory(request, pk):
    action = 'update'
    category = houseOfBrandsCategory.objects.get(id=pk)
    name = category.category_name
    form = CategoriesForm(instance=category)

    if request.method == 'POST':
        form = CategoriesForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('/categories/')

    context =  {'action':action, 'form':form, 'name':name }
    return render(request, 'HouseOfBrands/ShopCRM/order_form.html', context)

def deleteCategory(request, pk):
    category = houseOfBrandsCategory.objects.get(id=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('/categories/')

    return render(request, 'HouseOfBrands/ShopCRM/delete_item.html', {'item':category})



def get_categorylayer2(request):
    id = request.GET.get('id', '')
    result = list(houseOfBrandsCategoryLayer2.objects.filter(category_id=int(id)).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type="application/json")

def get_categorylayer3(request):
    id = request.GET.get('id', '')
    result = list(houseOfBrandsCategoryLayer3.objects.filter(category_id=int(id)).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type="application/json")

def get_categorylayer4(request):
    id = request.GET.get('id', '')
    result = list(houseOfBrandsCategoryLayer4.objects.filter(category_id=int(id)).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type="application/json")

def get_categorylayer5(request):
    id = request.GET.get('id', '')
    result = list(houseOfBrandsCategoryLayer5.objects.filter(category_id=int(id)).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type="application/json")

def get_categorylayer6(request):
    id = request.GET.get('id', '')
    result = list(houseOfBrandsCategoryLayer6.objects.filter(category_id=int(id)).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type="application/json")





#-------------------(CRUD - CATEGORIES) -------------------

def tags(request):
    taglist = Tag.objects.annotate(total_products=Count('houseofbrandsproduct'))
    context =  {'taglist':taglist, }
    return render(request, 'HouseOfBrands/ShopCRM/tags.html', context)
