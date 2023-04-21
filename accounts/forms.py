from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *
from .widgets import *


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']

class UpdateCustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = ['firstname','lastname', 'phone', 'email', 'company', 'company_id', 'company_address']


class RequestForm(ModelForm):

	class Meta:
		model = Request
		fields = '__all__'
		widgets = {
			'trainingDate' : DatePickerInput(),
			'trainingTime' : TimePickerInput(),
			'b2bDate' : DatePickerInput(),
			'b2cDate' : DatePickerInput(),
			}


class B2BRequestForm(ModelForm):

	class Meta:
		model = B2BRequest
		fields = '__all__'
		widgets = {
			'b2bDate' : DatePickerInput(),
			}

class B2CRequestForm(ModelForm):

	class Meta:
		model = B2CRequest
		fields = '__all__'
		widgets = {
			'b2bDate' : DatePickerInput(),
			}


class EmploymentTemplateRequestForm(ModelForm):

	class Meta:
		model = EmploymentTemplateRequest
		fields = '__all__'
		widgets = {
			'b2bDate' : DatePickerInput(),
			}


class EmploymentNegotiationRequestForm(ModelForm):

	class Meta:
		model = EmploymentNegotiationRequest
		fields = '__all__'
		widgets = {
			'b2bDate' : DatePickerInput(),
			}


class EmploymentDocumentRequestForm(ModelForm):

	class Meta:
		model = EmploymentDocumentRequest
		fields = '__all__'
		widgets = {
			'b2bDate' : DatePickerInput(),
			}


class RealEstatePurchaseRequestForm(ModelForm):

	class Meta:
		model = RealEstatePurchaseRequest
		fields = '__all__'
		widgets = {
			'b2bDate' : DatePickerInput(),
			}

class RealEstateLeasebackRequestForm(ModelForm):

	class Meta:
		model = RealEstateLeasebackRequest
		fields = '__all__'
		widgets = {
			'b2bDate' : DatePickerInput(),
			}

class RealEstateLeaseRequestForm(ModelForm):

	class Meta:
		model = RealEstateLeaseRequest
		fields = '__all__'
		widgets = {
			'b2bDate' : DatePickerInput(),
			}

class RealEstateEasementRequestForm(ModelForm):

	class Meta:
		model = RealEstateEasementRequest
		fields = '__all__'
		widgets = {
			'b2bDate' : DatePickerInput(),
			}

class RealEstateConstructionRequestForm(ModelForm):

	class Meta:
		model = RealEstateConstructionRequest
		fields = '__all__'
		widgets = {
			'b2bDate' : DatePickerInput(),
			}

class sourcingBusTemplateRequestForm(ModelForm):

	class Meta:
		model = sourcingBusTemplateRequest
		fields = '__all__'
		widgets = {
			'b2bDate' : DatePickerInput(),
			}

class sourcingSupTemplateRequestForm(ModelForm):

	class Meta:
		model = sourcingSupTemplateRequest
		fields = '__all__'
		widgets = {
			'b2bDate' : DatePickerInput(),
			}

class sourcingSupAgreementRequestForm(ModelForm):

	class Meta:
		model = sourcingSupAgreementRequest
		fields = '__all__'
		widgets = {
			'b2bDate' : DatePickerInput(),
			}

class legalRequestForm(ModelForm):

	class Meta:
		model = legalRequest
		fields = '__all__'
		widgets = {
			'b2bDate' : DatePickerInput(),
			}

class disputeCourtRequestForm(ModelForm):

	class Meta:
		model = disputeCourtRequest
		fields = '__all__'
		widgets = {
			'b2bDate' : DatePickerInput(),
			}

class disputeArbitrationRequestForm(ModelForm):

	class Meta:
		model = disputeArbitrationRequest
		fields = '__all__'
		widgets = {
			'b2bDate' : DatePickerInput(),
			}

class disputeSettlementRequestForm(ModelForm):

	class Meta:
		model = disputeSettlementRequest
		fields = '__all__'
		widgets = {
			'b2bDate' : DatePickerInput(),
			}

class mergerRequestForm(ModelForm):

	class Meta:
		model = mergerRequest
		fields = '__all__'
		widgets = {
			'b2bDate' : DatePickerInput(),
			}

class corporateRequestForm(ModelForm):

	class Meta:
		model = corporateRequest
		fields = '__all__'
		widgets = {
			'b2bDate' : DatePickerInput(),
			}

class dataRequestForm(ModelForm):

	class Meta:
		model = dataRequest
		fields = '__all__'
		widgets = {
			'b2bDate' : DatePickerInput(),
			}

class trainingRequestForm(ModelForm):

	class Meta:
		model = trainingRequest
		fields = '__all__'
		widgets = {
			'b2bDate' : DatePickerInput(),
			}