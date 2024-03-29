from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('offers/', views.offers, name='offers'),
    path('customer/', views.customer, name="customer"),
    path('user/', views.userPage, name="user-page"),
    path('register/', views.registerPage, name="register"),
    path('client_register/', views.clientRegisterPage, name="client_register"),
    path('provider_register/', views.providerRegisterPage, name="provider_register"),
    path('login/', views.loginPage, name="login"),
    path('unauthorized/', views.unauthorizedPage, name="unauthorized"),
    path('logout/', views.logoutUser, name="logout"),
    path('contracts/', views.contracts, name='contracts'),
    path('feedback/', views.feedback, name='feedback'),

    path('request_selection/', views.requestSelection, name="request_selection"),
    path('contract_request/', views.contractRequest, name="contract_request"),
    path('legal_request/', views.legal, name="legal_request"),
    path('dispute_request/', views.disputeRequest, name="dispute_request"),
    path('merger_request/', views.merger, name="merger_request"),
    path('corporate_request/', views.corporate, name="corporate_request"),
    path('data_request/', views.dataPrivacy, name="data_request"),
    path('training_request/', views.training, name="training_request"),
    path('b2b_request/', views.b2bRequest, name="b2b_request"),
    path('b2c_request/', views.b2cRequest, name="b2c_request"),
    path('employment_request/', views.employmentRequest, name="employment_request"),
    path('employment_selection/', views.employmentSelection, name="employment_selection"),
    path('employment_template/', views.employmentTemplate, name="employment_template"),
    path('employment_negotiation/', views.employmentNegotiation, name="employment_negotiation"),
    path('employment_documents/', views.employmentDocuments, name="employment_documents"),

    path('realestate_request/', views.realestateRequest, name="realestate_request"),
    path('realestate_selection/', views.realestateSelection, name="realestate_selection"),
    path('realestate_purchase/', views.realestatePurchase, name="realestate_purchase"),
    path('realestate_leaseback/', views.realestateLeaseback, name="realestate_leaseback"),
    path('realestate_lease/', views.realestateLease, name="realestate_lease"),
    path('realestate_easement/', views.realestateEasement, name="realestate_easement"),
    path('realestate_construction/', views.realestateConstruction, name="realestate_construction"),

    path('sourcing_request', views.sourcingRequest, name="sourcing_request"),
    path('sourcing_selection', views.sourcingSelection, name="sourcing_selection"),
    path('sourcing_bustemplate', views.sourcingBusTemplate, name="sourcing_bustemplate"),
    path('sourcing_suptemplate', views.sourcingSupTemplate, name="sourcing_suptemplate"),
    path('sourcing_supagreement', views.sourcingSupAgreement, name="sourcing_supagreement"),

    path('dispute_selection', views.disputeSelection, name="dispute_selection"),
    path('dispute_court', views.disputeCourt, name="dispute_court"),
    path('dispute_arbitration', views.disputeArbitration, name="dispute_arbitration"),
    path('dispute_settlement', views.disputeSettlement, name="dispute_settlement"),
    
    path('create_request/', views.createRequest, name="create_request"),
    path('update_request/<str:pk>/', views.updateRequest, name="update_request"),
    path('delete_request/<str:pk>/', views.deleteRequest, name="delete_request"),
    path('create_offer/', views.createOffer, name="create_offer"),

    #Provider
    path('provider/', views.providerDashboard, name='provider_dashboard'),
    path('provider_offers/', views.providerOffers, name='provider_offers'),
    path('provider_user/', views.providerUser, name='provider_user'),
    path('provider_requests/', views.providerRequests, name='provider_requests'),
    path('unauthorized_requests/', views.unauthorizedRequests, name='unauthorized_requests'),
    path('unauthorized_offers/', views.unauthorizedOffers, name='unauthorized_offers'),

    path('make_offer/<str:pk>/', views.makeOffer, name='make_offer'),
    path('password-change/', views.ChangePasswordView.as_view(), name='password_change'),
    path('user_rating/', views.userRating, name='user_rating'),
]
