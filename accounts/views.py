from django.shortcuts import render, HttpResponse, Http404, redirect
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth import authenticate
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required, permission_required
from .models import product

# Create your views here.

# Home Page 
def index(request):
    return render(request, '../templates/home.html')

def postdata(request):
    serial = request.POST["serial"]
    status = request.POST["stat"]
    battery_status = request.POST["batstat"]
    battery_voltage = request.POST["volt"]
    power_panel = request.POST["powpanel"]
    panel_voltage = request.POST["panelvolt"]
    Energy_curr = request.POST["engcurr"]
    Total_energy = request.POST["totaleng"]
    
    pr = product.objects.get(serial_no=serial)

    if pr is None:
        return Http404
    
    pr.attribute = 'puppi'
    pr.status = status
    pr.battery_status = battery_status
    pr.battery_voltage = battery_voltage
    pr.power_panel = power_panel
    pr.panel_voltage = panel_voltage
    pr.energy_curr = Energy_curr
    pr.total_energy = Total_energy
    pr.save()

@login_required(login_url='/login')
@permission_required('accounts.add_user')
def CreateUser(request):
    if request.method == 'POST' and request.user.is_superuser:
        name = request.POST['name']
        username = request.POST['username']
        password = request.POST['password']
        user_type = request.POST['type']
        
        if not username.endswith('@vtech.co.in'):
            return redirect('createuser')
        
        if user_type != 'agency' and user_type != 'user':
            return redirect('createuser')
        
        user = User.objects.create_user(name=name,username=username,password=password)
        user.save()

        if user_type == 'agency':
            group = Group.objects.get(name='Agencies')
            group.user_set.add(user)
        else:
            group = Group.objects.get(name='User')
            group.user_set.add(user)
        return 
    return Http404

@login_required(login_url='/login')
@permission_required('accounts.add_user')
def CreateProduct(request):
    if request.method == 'POST' and request.user.is_superuser:
        serialno = request.POST['serial']
        location = request.POST['location']
        product = product(serial_no=serialno,location=location,attribute='0')
        product.belongs_to.add(request.user)
        product.save()
    return Http404

@login_required(login_url='/login')
@permission_required('accounts.add_user')
def AssignUsertoProduct(request):
    if request.method == 'POST' and request.user.is_superuser:
        serialno = request.POST['serial']
        username = request.POST['username']
        user = User.objects.get(username=username,is_active=True)
        product = product.objects.get(serial_no=serialno)
        product.belongs_to.add(user)
        product.save()
    return Http404

@login_required(login_url='/login')
@permission_required('accounts.delete_user')
def DeleteUser(request):
    if request.method == 'POST' and request.user.is_superuser:
        username = request.POST['username']
        user = User.objects.get(username=username,is_active=True)
        user.is_active = False
        user.save()
    return Http404

@login_required(login_url='/login')
@permission_required('accounts.add_user')
def ViewAgencies(request):
    if request.user.is_superuser:
        agencies = User.objects.get(groups='Agencies')
        return
    pass

@login_required(login_url='/login')
@permission_required('accounts.add_user')
def View(request):
    if request.method == 'GET' and request.user.is_superuser:
        name = request.POST['name']
        agency = User.objects.get(first_name=name)
        return
    pass

@login_required(login_url='/login')
@permission_required('accounts.add_user')
def ViewProductsforAgency(request):
    if request.method == 'POST' and request.user.is_superuser:
        agency = request.POST['agency']
        agency_products = product.objects.get(belongs_to=agency)
        return
    pass

@login_required(login_url='/login')
@permission_required('accounts.view_group')
def ViewUsers(request):
    if request.method == 'POST' and request.user.is_superuser:
        users = User.objects.get(groups="User")
        return
    pass

@login_required(login_url='/login')
def ViewProduct(request):
    if request.method == 'POST':
        name = request.POST['name']
        # e_date = request.POST['date']
        name = 'mani'
        products = product.objects.filter(belongs_to__username=name)
        if products is None:
            print('None')
            return Http404
        products = list(products)
        users = [i.belongs_to.all() for i in products ]
        print(products[0].belongs_to.all())
        context = {
            'products': products,
            'user': users
        }
        return render(request, '../templates/table.html',context)
    return render(request, '../templates/table.html')

@login_required(login_url='/login')
@permission_required('accounts.add_user')
def ChangePassword(request):
    if request.method == 'POST' and request.user.is_superuser:
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.get(username=username)
        user.set_password(password)
    return

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:
            return redirect('/login')
        else:
            return redirect('/table')
    return render(request,'../templates/login.html')

@login_required(login_url='/login')
def logout(request):
    return

@login_required(login_url='/login')
def ControlSSL(request):
    return

@login_required(login_url='/login')
@permission_required('accounts.add_user')
def dashboard(request):
    if request.method == "POST" and request.user.is_authenticated:
        name = request.POST['agency']
        agency = User.objects.get(first_name=name)
        serialno = request.POST['serial']
        product = product.objects.get(serial_no=serialno)
        product.belongs_to.add(user)
        product.save()
        return redirect('/dashboard')
    return redirect('/dashboard')