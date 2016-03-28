from django.shortcuts import render

from django.contrib.auth.models import User
# from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from .models import UserProfile, Inventory, SuperVisor


# Create your views here.
@csrf_exempt
def index(request):
    return render(request, 'base/sign_in.html')

def home(request):
    return render(request, 'base/sign_in.html')
@csrf_exempt

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    # import pdb; pdb.set_trace()
    if not user:
        return render_to_response('base/sign_in.html', {'user_invalid':True})
    if user.is_superuser:
        return render_to_response('base/adminHome.html', {'user': user})
    user_profile = UserProfile.objects.get(user=user)
    if user_profile.userRole == 'V':
        # import pdb; pdb.set_trace()
        return render_to_response('base/vendorHome.html', {'user': user})
    if user_profile.userRole == 'S':
        supervisor = user
        vendor = SuperVisor.objects.get(supervisor_id=supervisor.id)
        vendor = vendor.vendor_id
        vendor = User.objects.get(id=vendor)
        inventory = Inventory.objects.get(user_id=vendor.id)
        return render_to_response('base/superVisor.html', {'supervisor': supervisor, 'vendor': vendor, 'inventory': inventory})
    if user_profile.userRole == 'B':
        return render_to_response('base/buyerHome.html', {'user':user})

@csrf_exempt
def addvendor(request):
    vendor_name = request.POST.get('vendor_name')
    vendor_pass = request.POST.get('vendor_password')
    vendor_email = request.POST.get('vendor_email')

    user = User.objects.create_user(vendor_name, vendor_email, vendor_pass)
    user.save()
    user_profile = UserProfile.objects.create(user=user, userRole='V')
    user_profile.save()
    #call function to send email to vendor with username and password
    #option to delete vendor
    return render_to_response('base/thankYou.html', {'user':user})

@csrf_exempt
def addsupervisor(request):
    vendor_id = request.POST.get('vendor')
    supervisor_name = request.POST.get('supervisor_name')
    supervisor_pass = request.POST.get('supervisor_password')
    supervisor_email = request.POST.get('supervisor_email')
    user = User.objects.create_user(supervisor_name, supervisor_email, supervisor_pass)
    user.save()
    user_id = user.id
    user_profile = UserProfile.objects.create(user=user, userRole='S')
    user_profile.save()
    supervisor = SuperVisor.objects.create(supervisor_id=user_id, vendor_id=vendor_id)
    supervisor.save()
    return render_to_response('base/vendorHome.html', {'user':user, 'success1':True})

@csrf_exempt
def additem(request):

    vendor_id = request.POST.get('vendor')
    scooty = request.POST.get('scooty')
    bike = request.POST.get('bike')
    user = User.objects.get(id=vendor_id)
    user_id = user.id
    inventory,created = Inventory.objects.get_or_create(user_id=vendor_id)
    if scooty:
        inventory.scooty += 1
        inventory.save()
    if bike:
        inventory.bike += 1
        inventory.save()
    return render_to_response('base/vendorHome.html', {'user':user, 'inventory':inventory, 'success':True})

@csrf_exempt
def updateitem(request):
    # import pdb; pdb.set_trace()
    supervisor_id = request.POST.get('supervisor')
    scooty = request.POST.get('scooty')
    scooty_d = request.POST.get('scooty_d')
    bike = request.POST.get('bike')
    bike_d = request.POST.get('bike_d')
    vendor_id = SuperVisor.objects.get(supervisor_id=supervisor_id)
    vendor_id = vendor_id.vendor_id
    vendor = User.objects.get(id=vendor_id)
    user_id = vendor.id
    supervisor = User.objects.get(id=supervisor_id)
    inventory = Inventory.objects.get(user_id=vendor_id)
    if scooty:
        inventory.scooty += 1
        inventory.save()
    if scooty_d and inventory.scooty > 0:
        inventory.scooty -= 1
        inventory.save()
    else:
        render_to_response('base/superVisor.html', {'supervisor':supervisor, 'vendor': vendor, 'inventory': inventory, 'failure': True})
    if bike == 'add_bike':
        inventory.bike += 1
        inventory.save()
    if bike_d and inventory.bike > 0:
        inventory.bike -= 1
        inventory.save()
    else:
        render_to_response('base/superVisor.html', {'supervisor':supervisor, 'vendor':vendor, 'inventory': inventory, 'failure': True})
    return render_to_response('base/superVisor.html', {'supervisor':supervisor, 'vendor':vendor, 'inventory': inventory, 'success': True})

@csrf_exempt
def signup(request):
    # import pdb
    # pdb.set_trace()
    request_body = request.body
    request_body = request_body.split('&')
    first_name = request_body[0].split('=')[1]
    last_name = request_body[1].split('=')[1]
    user_name = request_body[2].split('=')[1]
    user_already_reg = User.objects.filter(username=user_name).exists()
    if user_already_reg:
        return render_to_response("base/sign_in.html", {'user_exists':True})
    password = request_body[3].split('=')[1]
    user = User.objects.create_user(user_name, '', password)
    user.first_name = first_name
    user.last_name = last_name
    user.save()
    user = authenticate(username=user_name, password=password)
    if user:
        # import pdb
        # pdb.set_trace()
        user_profile = UserProfile.objects.create(user=user, userRole='B')
        return render_to_response("base/buyerHome.html",{'user':user})
