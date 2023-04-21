from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
from .models import *
from .forms import *
#from .filters import OrderFilter
from .decorators import unauthenticated_user, allowed_users, admin_only



class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'accounts/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = 'accounts/user.html'


@unauthenticated_user
def registerPage(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            #group = Group.objects.get(name='customer')
            #user.groups.add(group)
            Customer.objects.create(
                user=user,
                name=user.username,
                firstname=form.cleaned_data.get('first_name'),
                lastname=form.cleaned_data.get('last_name'),
                email=form.cleaned_data.get('email'),
                company=request.POST['company'],
                company_id=request.POST['company_id'],
                phone=request.POST['phone'],
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

@login_required(login_url='login')
def contracts(request):
    requests = Request.objects.all()
    employmentRequests = EmploymentTemplateRequest.objects.all()
    #contracts = Contract.objects.all()
    context = {'requests': requests, 'emp' : employmentRequests}
    return render(request, 'accounts/contracts.html', context)

@login_required(login_url='login')
def makeOffer(request, pk):
    req = EmploymentTemplateRequest.objects.get(id=pk)
    context = {'request': req}
    return render(request, 'accounts/make_offer.html', context)

@login_required(login_url='login')
def offers(request):
    context = {}
    return render(request, 'accounts/offers.html', context)

@login_required(login_url='login')
def providerOffers(request):
    """
    offers = Offer.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_offers = offers.count()
    accepted = offers.filter(status='Accepted').count()
    pending = offers.filter(status='Pending').count()
    """
    requests = Request.objects.all()
    context = {'requests': requests}
    return render(request, 'accounts/provider_offers.html', context)

@login_required(login_url='login')
def providerRequests(request):
    """
    offers = Offer.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_offers = offers.count()
    accepted = offers.filter(status='Accepted').count()
    pending = offers.filter(status='Pending').count()
    """
    
    requests = Request.objects.all()
    b2b = B2BRequest.objects.all()
    b2c = B2CRequest.objects.all()
    employmentRequests = EmploymentTemplateRequest.objects.all()
    empNegRequests = EmploymentNegotiationRequest.objects.all()
    empDocRequests = EmploymentDocumentRequest.objects.all()
    RealEstatePurchaseRequests = RealEstatePurchaseRequest.objects.all()
    RealEstateLeasebackRequests = RealEstateLeasebackRequest.objects.all()
    RealEstateLeaseRequests = RealEstateLeaseRequest.objects.all()
    RealEstateEaseRequests = RealEstateEasementRequest.objects.all()
    RealEstateConstRequests = RealEstateConstructionRequest.objects.all()
    sourcingBusTempRequests = sourcingBusTemplateRequest.objects.all()
    sourcingSupTempRequests = sourcingSupTemplateRequest.objects.all()
    sourcingSupAgRequests = sourcingSupAgreementRequest.objects.all()
    legalRequests = legalRequest.objects.all()
    disputeCourtRequests = disputeCourtRequest.objects.all()
    disputeArbiRequests = disputeArbitrationRequest.objects.all()
    disputeSettRequests = disputeSettlementRequest.objects.all()
    mergerRequests = mergerRequest.objects.all()
    corporateRequests = corporateRequest.objects.all()
    dataRequests = dataRequest.objects.all()
    trainRequests = trainingRequest.objects.all()
    context = {'requests': requests, 'emp' : employmentRequests, 'b2b' : b2b, 'b2c' : b2c, 'empNegRequests' : empNegRequests, 
    'empDocRequests' : empDocRequests, 'RealEstatePurchaseRequests' : RealEstatePurchaseRequests, 'RealEstateLeasebackRequests' : RealEstateLeasebackRequests, 
    'RealEstateLeaseRequests' : RealEstateLeaseRequests, 'RealEstateEaseRequests' : RealEstateEaseRequests, 'RealEstateConstRequests' : RealEstateConstRequests, 
    'sourcingBusTempRequests' : sourcingBusTempRequests, 'sourcingSupTempRequests' : sourcingSupTempRequests, 'sourcingSupAgRequests' : sourcingSupAgRequests, 
    'legalRequests' : legalRequests, 'disputeCourtRequests' : disputeCourtRequests, 'disputeArbiRequests' : disputeArbiRequests, 'disputeSettRequests' : disputeSettRequests, 
    'mergerRequests' : employmentRequests, 'mergerRequests' : employmentRequests, 'corporateRequests' : corporateRequests, 'dataRequests' : dataRequests, 'trainRequests' : trainRequests}
    return render(request, 'accounts/provider_requests.html', context)

@login_required(login_url='login')
def feedback(request):

    user = request.user
    customer = Customer.objects.get(name=user.username)
    context = {'customer': customer}

    return render(request, 'accounts/feedback.html', context)


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
    form = B2BRequestForm()
    if request.method == 'POST':
        q = request.POST
        datadict = {k: q.getlist(k) if len(q.getlist(k))>1 else v for k, v in q.items()}
        template = datadict.get('b2b_help')
        templist = str(', '.join(template))
        lang = datadict.get('language')
        langlist = str(', '.join(lang))
        data = {
        'b2b_help': templist,
        'otherInfo' : datadict.get('otherInfo'),
        'offerMaker' : datadict.get('offerMaker'),
        'invoiceType' : datadict.get('invoiceType'),
        'language' : langlist,
        'b2bDate' : datadict.get('b2bDate'),
        'title' : datadict.get('title'),
        'note': datadict.get('note'),
        }
        form = B2BRequestForm(data)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/b2b_request.html', context)


@login_required(login_url='login')
def b2cRequest(request):
    form = B2CRequestForm()
    if request.method == 'POST':
        q = request.POST
        datadict = {k: q.getlist(k) if len(q.getlist(k))>1 else v for k, v in q.items()}
        template = datadict.get('b2b_help')
        templist = str(', '.join(template))
        lang = datadict.get('language')
        langlist = str(', '.join(lang))
        data = {
        'b2b_help': templist,
        'otherInfo' : datadict.get('otherInfo'),
        'offerMaker' : datadict.get('offerMaker'),
        'invoiceType' : datadict.get('invoiceType'),
        'language' : langlist,
        'b2bDate' : datadict.get('b2bDate'),
        'title' : datadict.get('title'),
        'note': datadict.get('note'),
        }
        form = B2CRequestForm(data)
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
    return render(request, 'accounts/employment_selection.html')

@login_required(login_url='login')
def employmentTemplate(request):
    form = EmploymentTemplateRequestForm()
    if request.method == 'POST':
        q = request.POST
        datadict = {k: q.getlist(k) if len(q.getlist(k))>1 else v for k, v in q.items()}
        template = datadict.get('employment_conTemplate')
        templist = str(', '.join(template))
        lang = datadict.get('language')
        langlist = str(', '.join(lang))
        data = {
        'employment_conTemplate': templist,
        'employmentTemplate' : datadict.get('employmentTemplate'),
        'otherInfo' : datadict.get('otherInfo'),
        'offerMaker' : datadict.get('offerMaker'),
        'invoiceType' : datadict.get('invoiceType'),
        'language' : langlist,
        'b2bDate' : datadict.get('b2bDate'),
        'title' : datadict.get('title'),
        'priceOffer' : "Lump sum fixed price for the entire work.",
        }
        form = EmploymentTemplateRequestForm(data)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/employment_template.html', context)

@login_required(login_url='login')
def employmentNegotiation(request):
    form = EmploymentNegotiationRequestForm()
    if request.method == 'POST':
        q = request.POST
        datadict = {k: q.getlist(k) if len(q.getlist(k))>1 else v for k, v in q.items()}
        lang = datadict.get('language')
        langlist = str(', '.join(lang))
        data = {
        'employmentContract' : datadict.get('employmentContract'),
        'otherInfo' : datadict.get('otherInfo'),
        'offerMaker' : datadict.get('offerMaker'),
        'invoiceType' : datadict.get('invoiceType'),
        'language' : langlist,
        'b2bDate' : datadict.get('b2bDate'),
        'title' : datadict.get('title'),
        'employmentPos': datadict.get('employmentPos'),
        }
        form = EmploymentNegotiationRequestForm(data)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/employment_negotiation.html', context)

@login_required(login_url='login')
def employmentDocuments(request):
    form = EmploymentDocumentRequestForm()
    if request.method == 'POST':
        q = request.POST
        datadict = {k: q.getlist(k) if len(q.getlist(k))>1 else v for k, v in q.items()}
        template = datadict.get('employment_docTemplate')
        templist = str(', '.join(template))
        lang = datadict.get('language')
        langlist = str(', '.join(lang))
        data = {
        'employment_docTemplate': templist,
        'otherInfo' : datadict.get('otherInfo'),
        'offerMaker' : datadict.get('offerMaker'),
        'invoiceType' : datadict.get('invoiceType'),
        'language' : langlist,
        'b2bDate' : datadict.get('b2bDate'),
        'title' : datadict.get('title'),
        }
        form = EmploymentDocumentRequestForm(data)
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
    form = RealEstatePurchaseRequestForm()
    if request.method == 'POST':
        q = request.POST
        datadict = {k: q.getlist(k) if len(q.getlist(k))>1 else v for k, v in q.items()}
        lang = datadict.get('language')
        langlist = str(', '.join(lang))
        data = {
        'realestateAgreement' : datadict.get('realestateAgreement'),
        'agreementBuyer' : datadict.get('agreementBuyer'),
        'agreementDescription' : datadict.get('agreementDescription'),
        'agreementRange' : datadict.get('agreementRange'),
        'agreementInspection' : datadict.get('agreementInspection'),
        'realSalePurchase' : datadict.get('realSalePurchase'),
        'otherInfo' : datadict.get('otherInfo'),
        'offerMaker' : datadict.get('offerMaker'),
        'invoiceType' : datadict.get('invoiceType'),
        'language' : langlist,
        'b2bDate' : datadict.get('b2bDate'),
        'title' : datadict.get('title'),
        }
        form = RealEstatePurchaseRequestForm(data)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/realestate_purchase.html', context)

@login_required(login_url='login')
def realestateLeaseback(request):
    form = RealEstateLeasebackRequestForm()
    if request.method == 'POST':
        q = request.POST
        datadict = {k: q.getlist(k) if len(q.getlist(k))>1 else v for k, v in q.items()}
        lang = datadict.get('language')
        langlist = str(', '.join(lang))
        data = {
        'leasebackSeller' : datadict.get('leasebackSeller'),
        'leasebackDescription' : datadict.get('leasebackDescription'),
        'leasebackRange' : datadict.get('leasebackRange'),
        'leasebackInspection' : datadict.get('leasebackInspection'),
        'realLeaseBack' : datadict.get('realLeaseBack'),
        'otherInfo' : datadict.get('otherInfo'),
        'offerMaker' : datadict.get('offerMaker'),
        'invoiceType' : datadict.get('invoiceType'),
        'language' : langlist,
        'b2bDate' : datadict.get('b2bDate'),
        'title' : datadict.get('title'),
        }
        form = RealEstateLeasebackRequestForm(data)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/realestate_leaseback.html', context)

@login_required(login_url='login')
def realestateLease(request):
    form = RealEstateLeaseRequestForm()
    if request.method == 'POST':
        q = request.POST
        datadict = {k: q.getlist(k) if len(q.getlist(k))>1 else v for k, v in q.items()}
        lang = datadict.get('language')
        langlist = str(', '.join(lang))
        data = {
        'realLease' : datadict.get('realLease'),
        'leaseAgreement' : datadict.get('leaseAgreement'),
        'leaseRole' : datadict.get('leaseRole'),
        'leaseDescription' : datadict.get('leaseDescription'),
        'leaseRange' : datadict.get('leaseRange'),
        'otherInfo' : datadict.get('otherInfo'),
        'offerMaker' : datadict.get('offerMaker'),
        'invoiceType' : datadict.get('invoiceType'),
        'language' : langlist,
        'b2bDate' : datadict.get('b2bDate'),
        'title' : datadict.get('title'),
        }
        form = RealEstateLeaseRequestForm(data)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/realestate_lease.html', context)

@login_required(login_url='login')
def realestateEasement(request):
    form = RealEstateEasementRequestForm()
    if request.method == 'POST':
        q = request.POST
        datadict = {k: q.getlist(k) if len(q.getlist(k))>1 else v for k, v in q.items()}
        lang = datadict.get('language')
        langlist = str(', '.join(lang))
        data = {
        'constructionDescription' : datadict.get('constructionDescription'),
        'easementProperty' : datadict.get('easementProperty'),
        'easementSupport' : datadict.get('easementSupport'),
        'otherInfo' : datadict.get('otherInfo'),
        'offerMaker' : datadict.get('offerMaker'),
        'invoiceType' : datadict.get('invoiceType'),
        'language' : langlist,
        'b2bDate' : datadict.get('b2bDate'),
        'title' : datadict.get('title'),
        }
        form = RealEstateEasementRequestForm(data)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/realestate_easement.html', context)

@login_required(login_url='login')
def realestateConstruction(request):
    form = RealEstateConstructionRequestForm()
    if request.method == 'POST':
        q = request.POST
        datadict = {k: q.getlist(k) if len(q.getlist(k))>1 else v for k, v in q.items()}
        lang = datadict.get('language')
        langlist = str(', '.join(lang))
        data = {
        'realConstruction' : datadict.get('realConstruction'),
        'constructionAgreement' : datadict.get('constructionAgreement'),
        'constructionDescription' : datadict.get('constructionDescription'),
        'constructionPrice' : datadict.get('constructionPrice'),
        'otherInfo' : datadict.get('otherInfo'),
        'offerMaker' : datadict.get('offerMaker'),
        'invoiceType' : datadict.get('invoiceType'),
        'language' : langlist,
        'b2bDate' : datadict.get('b2bDate'),
        'title' : datadict.get('title'),
        }
        form = RealEstateConstructionRequestForm(data)
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
    form = sourcingBusTemplateRequestForm()
    if request.method == 'POST':
        q = request.POST
        datadict = {k: q.getlist(k) if len(q.getlist(k))>1 else v for k, v in q.items()}
        lang = datadict.get('language')
        langlist = str(', '.join(lang))
        data = {
        'sourcingTemplate' : datadict.get('sourcingTemplate'),
        'sourcingGeneric' : datadict.get('sourcingGeneric'),
        'sourcingCustomized' : datadict.get('sourcingCustomized'),
        'otherInfo' : datadict.get('otherInfo'),
        'offerMaker' : datadict.get('offerMaker'),
        'invoiceType' : datadict.get('invoiceType'),
        'language' : langlist,
        'b2bDate' : datadict.get('b2bDate'),
        'title' : datadict.get('title'),
        }
        form = sourcingBusTemplateRequestForm(data)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/sourcing_bustemplate.html', context)

@login_required(login_url='login')
def sourcingSupTemplate(request):
    form = sourcingSupTemplateRequestForm()
    if request.method == 'POST':
        q = request.POST
        datadict = {k: q.getlist(k) if len(q.getlist(k))>1 else v for k, v in q.items()}
        lang = datadict.get('language')
        langlist = str(', '.join(lang))
        data = {
        'sourcingComments' : datadict.get('sourcingComments'),
        'otherInfo' : datadict.get('otherInfo'),
        'offerMaker' : datadict.get('offerMaker'),
        'invoiceType' : datadict.get('invoiceType'),
        'language' : langlist,
        'b2bDate' : datadict.get('b2bDate'),
        'title' : datadict.get('title'),
        }
        form = sourcingSupTemplateRequestForm(data)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/sourcing_suptemplate.html', context)

@login_required(login_url='login')
def sourcingSupAgreement(request):
    form = sourcingSupAgreementRequestForm()
    if request.method == 'POST':
        q = request.POST
        datadict = {k: q.getlist(k) if len(q.getlist(k))>1 else v for k, v in q.items()}
        lang = datadict.get('language')
        langlist = str(', '.join(lang))
        data = {
        'sourcingLawyer' : datadict.get('sourcingLawyer'),
        'sourcingType' : datadict.get('sourcingType'),
        'otherInfo' : datadict.get('otherInfo'),
        'offerMaker' : datadict.get('offerMaker'),
        'invoiceType' : datadict.get('invoiceType'),
        'language' : langlist,
        'b2bDate' : datadict.get('b2bDate'),
        'title' : datadict.get('title'),
        }
        form = sourcingSupAgreementRequestForm(data)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/sourcing_supagreement.html', context)


@login_required(login_url='login')
def legal(request):
    form = legalRequestForm()
    if request.method == 'POST':
        q = request.POST
        datadict = {k: q.getlist(k) if len(q.getlist(k))>1 else v for k, v in q.items()}
        template = datadict.get('legal_area')
        templist = str(', '.join(template))
        lang = datadict.get('language')
        langlist = str(', '.join(lang))
        data = {
        'legal_area' : templist,
        'legalMonths' : datadict.get('legalMonths'),
        'legalHours' : datadict.get('legalHours'),
        'legalOffers' : datadict.get('legalOffers'),
        'otherInfo' : datadict.get('otherInfo'),
        'offerMaker' : datadict.get('offerMaker'),
        'invoiceType' : datadict.get('invoiceType'),
        'language' : langlist,
        'b2bDate' : datadict.get('b2bDate'),
        'title' : datadict.get('title'),
        }
        form = legalRequestForm(data)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/legal_request.html', context)


@login_required(login_url='login')
def disputeRequest(request):
    form = disputeCourtRequestForm()
    if request.method == 'POST':
        q = request.POST
        datadict = {k: q.getlist(k) if len(q.getlist(k))>1 else v for k, v in q.items()}
        lang = datadict.get('language')
        langlist = str(', '.join(lang))
        data = {
        'dispRole' : datadict.get('dispRole'),
        'courtArea' : datadict.get('courtArea'),
        'dispDescription' : datadict.get('dispDescription'),
        'otherInfo' : datadict.get('otherInfo'),
        'offerMaker' : datadict.get('offerMaker'),
        'invoiceType' : datadict.get('invoiceType'),
        'language' : langlist,
        'b2bDate' : datadict.get('b2bDate'),
        'title' : datadict.get('title'),
        }
        form = disputeCourtRequestForm(data)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/dispute_request.html', context)


@login_required(login_url='login')
def disputeSelection(request):
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm()
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/dispute_selection.html', context)

@login_required(login_url='login')
def disputeCourt(request):
    form = disputeCourtRequestForm()
    if request.method == 'POST':
        q = request.POST
        datadict = {k: q.getlist(k) if len(q.getlist(k))>1 else v for k, v in q.items()}
        lang = datadict.get('language')
        langlist = str(', '.join(lang))
        data = {
        'courtArea' : datadict.get('courtArea'),
        'dispDescription' : datadict.get('dispDescription'),
        'otherInfo' : datadict.get('otherInfo'),
        'offerMaker' : datadict.get('offerMaker'),
        'invoiceType' : datadict.get('invoiceType'),
        'language' : langlist,
        'b2bDate' : datadict.get('b2bDate'),
        'title' : datadict.get('title'),
        }
        form = disputeCourtRequestForm(data)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/dispute_court.html', context)

@login_required(login_url='login')
def disputeArbitration(request):
    form = disputeArbitrationRequestForm()
    if request.method == 'POST':
        q = request.POST
        datadict = {k: q.getlist(k) if len(q.getlist(k))>1 else v for k, v in q.items()}
        lang = datadict.get('language')
        langlist = str(', '.join(lang))
        data = {
        'arbiArea' : datadict.get('arbiArea'),
        'dispDescription' : datadict.get('dispDescription'),
        'otherInfo' : datadict.get('otherInfo'),
        'offerMaker' : datadict.get('offerMaker'),
        'invoiceType' : datadict.get('invoiceType'),
        'language' : langlist,
        'b2bDate' : datadict.get('b2bDate'),
        'title' : datadict.get('title'),
        }
        form = disputeArbitrationRequestForm(data)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/dispute_arbitration.html', context)

@login_required(login_url='login')
def disputeSettlement(request):
    form = disputeSettlementRequestForm()
    if request.method == 'POST':
        q = request.POST
        datadict = {k: q.getlist(k) if len(q.getlist(k))>1 else v for k, v in q.items()}
        lang = datadict.get('language')
        langlist = str(', '.join(lang))
        data = {
        'settlementArea' : datadict.get('settlementArea'),
        'dispDescription' : datadict.get('dispDescription'),
        'otherInfo' : datadict.get('otherInfo'),
        'offerMaker' : datadict.get('offerMaker'),
        'invoiceType' : datadict.get('invoiceType'),
        'language' : langlist,
        'b2bDate' : datadict.get('b2bDate'),
        'title' : datadict.get('title'),
        }
        form = disputeSettlementRequestForm(data)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/dispute_settlement.html', context)


@login_required(login_url='login')
def merger(request):
    form = mergerRequestForm()
    if request.method == 'POST':
        q = request.POST
        datadict = {k: q.getlist(k) if len(q.getlist(k))>1 else v for k, v in q.items()}
        lang = datadict.get('language')
        langlist = str(', '.join(lang))
        data = {
        'sellOrBuy' : datadict.get('sellOrBuy'),
        'mergerType' : datadict.get('mergerType'),
        'mergerCompany' : datadict.get('mergerCompany'),
        'mergerOtherCompany' : datadict.get('mergerOtherCompany'),
        'mergerTarget' : datadict.get('mergerTarget'),
        'mergerBusinessLine' : datadict.get('mergerBusinessLine'),
        'mergerRange' : datadict.get('mergerRange'),
        'mergerArea' : datadict.get('mergerArea'),
        'otherInfo' : datadict.get('otherInfo'),
        'offerMaker' : datadict.get('offerMaker'),
        'invoiceType' : datadict.get('invoiceType'),
        'language' : langlist,
        'b2bDate' : datadict.get('b2bDate'),
        'title' : datadict.get('title'),
        }
        form = mergerRequestForm(data)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/merger_request.html', context)


@login_required(login_url='login')
def corporate(request):
    form = corporateRequestForm()
    if request.method == 'POST':
        q = request.POST
        datadict = {k: q.getlist(k) if len(q.getlist(k))>1 else v for k, v in q.items()}
        lang = datadict.get('language')
        langlist = str(', '.join(lang))
        data = {
        'corpCompany' : datadict.get('corpCompany'),
        'otherInfo' : datadict.get('otherInfo'),
        'offerMaker' : datadict.get('offerMaker'),
        'invoiceType' : datadict.get('invoiceTypeRunning'),
        'language' : langlist,
        'b2bDate' : datadict.get('b2bDate'),
        'title' : datadict.get('title'),
        }
        form = corporateRequestForm(data)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/corporate_request.html', context)


@login_required(login_url='login')
def dataPrivacy(request):
    form = dataRequestForm()
    if request.method == 'POST':
        q = request.POST
        datadict = {k: q.getlist(k) if len(q.getlist(k))>1 else v for k, v in q.items()}
        lang = datadict.get('language')
        langlist = str(', '.join(lang))
        data = {
        'privacyOptions' : datadict.get('privacyOptions'),
        'privacyReview' : datadict.get('privacyReview'),
        'privacyGDPR' : datadict.get('privacyGDPR'),
        'privacyBusinessLine' : datadict.get('privacyBusinessLine'),
        'privacyEmployeeCount' : datadict.get('privacyEmployeeCount'),
        'otherInfo' : datadict.get('otherInfo'),
        'offerMaker' : datadict.get('offerMaker'),
        'invoiceType' : datadict.get('invoiceType'),
        'language' : langlist,
        'b2bDate' : datadict.get('b2bDate'),
        'title' : datadict.get('title'),
        }
        form = dataRequestForm(data)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    context = {'form':form}

    return render(request, 'accounts/data_request.html', context)


@login_required(login_url='login')
def training(request):
    form = trainingRequestForm()
    if request.method == 'POST':
        q = request.POST
        datadict = {k: q.getlist(k) if len(q.getlist(k))>1 else v for k, v in q.items()}
        lang = datadict.get('language')
        langlist = str(', '.join(lang))
        data = {
        'legalTopic' : datadict.get('legalTopic'),
        'trainingDuration' : datadict.get('trainingDuration'),
        'dateConfirm' : datadict.get('dateConfirm'),
        'trainingDate' : datadict.get('trainingDate'),
        'trainingTime' : datadict.get('trainingTime'),
        'trainingPlace' : datadict.get('trainingPlace'),
        'trainingPlaceInfo' : datadict.get('trainingPlaceInfo'),
        'otherInfo' : datadict.get('otherInfo'),
        'offerMaker' : datadict.get('offerMaker'),
        'language' : langlist,
        'b2bDate' : datadict.get('b2bDate'),
        'title' : datadict.get('title'),
        }
        form = trainingRequestForm(data)
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
def providerDashboard(request):
    
    context = {}
    return render(request, 'accounts/provider_dashboard.html', context)


@login_required(login_url='login')
#@allowed_users(allowed_roles=['customer'])
def userPage(request):
    user = request.user
    customer = Customer.objects.get(name=user.username)
    allCustomers = Customer.objects.all()
    if request.method == 'POST':
        q = request.POST
        datadict = {k: q.getlist(k) if len(q.getlist(k))>1 else v for k, v in q.items()}
        if datadict.get("companyName") == "":
            comp = customer.company
        else:
            comp = datadict.get("companyName")

        if datadict.get("companyId") == "":
            compId = customer.company_id
        else:
            compId = datadict.get("companyId")

        if datadict.get("firstName") == "":
            fname = customer.firstname
        else:
            fname = datadict.get("firstName")

        if datadict.get("lastName") == "":
            lname = customer.lastname
        else:
            lname = datadict.get("lastName")

        if datadict.get("phoneNumber") == "":
            pnum = customer.phone
        else:
            pnum = datadict.get("phoneNumber")

        if datadict.get("eMail") == "":
            mail = customer.email
        else:
            mail = datadict.get("eMail")

        if datadict.get("companyAddress") == "":
            compAdd = customer.company_address
        else:
            compAdd = datadict.get("companyAddress")

        data = {
        'company': comp,
        'company_id': compId,
        'firstname': fname,
        'lastname': lname,
        'phone': pnum,
        'email': mail,
        'company_address': compAdd,
        }
        form = UpdateCustomerForm(data, instance=customer)
        print(form.errors)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account information was saved for ' + user.username)
            return redirect('user-page')
    else:
        form = UpdateCustomerForm(instance=customer)
    context = {'form':form, 'customer':customer, 'customerList': allCustomers}
    return render(request, 'accounts/user.html', context)


@login_required(login_url='login')
#@allowed_users(allowed_roles=['customer'])
def providerUser(request):
    user = request.user
    customer = Customer.objects.get(name=user.username)
    form = RequestForm(instance=customer)
    if request.method == 'POST':
        form = RequestForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('user-page')
    context = {'form':form, 'customer':customer}
    return render(request, 'accounts/provider_user.html', context)

@login_required(login_url='login')
def userRating(request):
    context = {}
    return render(request, 'accounts/user_rating.html', context)


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
