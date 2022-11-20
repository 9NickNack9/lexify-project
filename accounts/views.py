from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
from .models import *
from .forms import *
#from .filters import OrderFilter
from .decorators import unauthenticated_user, allowed_users, admin_only


@unauthenticated_user
def registerPage(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(
                user=user,
                name=user.username,
                )

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')
        

    context = {'form':form}
    return render(request, 'accounts/register.html', context)


@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

def contracts(request):
    requests = Request.objects.all()
    #contracts = Contract.objects.all()
    context = {'requests': requests}
    return render(request, 'accounts/contracts.html', context)


def offers(request):
    """
    offers = Offer.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_offers = offers.count()
    accepted = offers.filter(status='Accepted').count()
    pending = offers.filter(status='Pending').count()
    """
    context = {}
    return render(request, 'accounts/offers.html', context)


@login_required(login_url='login')
def createOffer(request):

    context = {}

    return render(request, 'accounts/order_form.html', context)


@login_required(login_url='login')
def requestSelection(request):
    context = {}
    return render(request, 'accounts/request_selection.html', context)


@login_required(login_url='login')
def contractRequest(request):
    context = {}
    return render(request, 'accounts/contract_request.html', context)


@login_required(login_url='login')
def b2bRequest(request):
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/b2b_request.html', context)


@login_required(login_url='login')
def b2cRequest(request):
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/b2c_request.html', context)


@login_required(login_url='login')
def employmentRequest(request):
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/employment_request.html', context)

@login_required(login_url='login')
def employmentSelection(request):
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/employment_selection.html', context)

@login_required(login_url='login')
def employmentTemplate(request):
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/employment_template.html', context)

@login_required(login_url='login')
def employmentNegotiation(request):
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/employment_negotiation.html', context)

@login_required(login_url='login')
def employmentDocuments(request):
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/employment_documents.html', context)


@login_required(login_url='login')
def realestateRequest(request):
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/realestate_request.html', context)

@login_required(login_url='login')
def realestateSelection(request):
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/realestate_selection.html', context)

@login_required(login_url='login')
def realestatePurchase(request):
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/realestate_purchase.html', context)

@login_required(login_url='login')
def realestateLeaseback(request):
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/realestate_leaseback.html', context)

@login_required(login_url='login')
def realestateLease(request):
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/realestate_lease.html', context)

@login_required(login_url='login')
def realestateEasement(request):
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/realestate_easement.html', context)

@login_required(login_url='login')
def realestateConstruction(request):
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/realestate_construction.html', context)


@login_required(login_url='login')
def sourcingRequest(request):
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/sourcing_request.html', context)

@login_required(login_url='login')
def sourcingSelection(request):
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/sourcing_selection.html', context)

@login_required(login_url='login')
def sourcingBusTemplate(request):
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/sourcing_bustemplate.html', context)

@login_required(login_url='login')
def sourcingSupTemplate(request):
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/sourcing_suptemplate.html', context)

@login_required(login_url='login')
def sourcingSupAgreement(request):
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/sourcing_supagreement.html', context)


@login_required(login_url='login')
def legalRequest(request):
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/legal_request.html', context)


@login_required(login_url='login')
def disputeRequest(request):
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/dispute_request.html', context)

@login_required(login_url='login')
def disputeSelection(request):
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/dispute_selection.html', context)

@login_required(login_url='login')
def disputeCourt(request):
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/dispute_court.html', context)

@login_required(login_url='login')
def disputeArbitration(request):
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/dispute_arbitration.html', context)

@login_required(login_url='login')
def disputeSettlement(request):
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/dispute_settlement.html', context)


@login_required(login_url='login')
def mergerRequest(request):
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/merger_request.html', context)


@login_required(login_url='login')
def corporateRequest(request):
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/corporate_request.html', context)


@login_required(login_url='login')
def dataRequest(request):
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/data_request.html', context)


@login_required(login_url='login')
def trainingRequest(request):
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        print(form.errors)
        if form.is_valid():
            print('valid')
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/training_request.html', context)


@login_required(login_url='login')
def createRequest(request):

    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/request_form.html', context)


@login_required(login_url='login')
def updateRequest(request, pk):

    req = Request.objects.get(id=pk)
    form = RequestForm(instance=req)

    if request.method == 'POST':
        form = RequestForm(request.POST, instance=req)
        if form.is_valid():
            form.save()
            return redirect('contracts')

    context = {'form':form}
    return render(request, 'accounts/request_form.html', context)


@login_required(login_url='login')
def deleteRequest(request, pk):
    req = Request.objects.get(id=pk)
    if request.method == "POST":
        req.delete()
        return redirect('home')

    context = {'item':req}
    return render(request, 'accounts/delete.html', context)


@login_required(login_url='login')
def home(request):
    
    context = {}
    return render(request, 'accounts/dashboard.html', context)


@login_required(login_url='login')
#@allowed_users(allowed_roles=['customer'])
def userPage(request):
    context = {}
    return render(request, 'accounts/user.html', context)

"""
@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin'])
def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)

    #orders = customer.order_set.all()
    #order_count = orders.count()

    #myFilter = OrderFilter(request.GET, queryset=orders)
    #orders = myFilter.qs 
        context = {'customer':customer, 'orders':orders, 'order_count':order_count,
    'myFilter':myFilter}
        context = {'customer':customer}
    return render(request, 'accounts/customer.html', context)
"""


@login_required(login_url='login')
def customer(request):
    context = {}
    return render(request, 'accounts/customer.html', context)
