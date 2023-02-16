from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Customer)
admin.site.register(Offer)
admin.site.register(Request)
admin.site.register(EmploymentTemplateRequest)
admin.site.register(B2BRequest)
admin.site.register(B2CRequest)
admin.site.register(EmploymentNegotiationRequest)
admin.site.register(EmploymentDocumentRequest)
admin.site.register(RealEstatePurchaseRequest)
admin.site.register(RealEstateLeasebackRequest)
admin.site.register(RealEstateLeaseRequest)
admin.site.register(RealEstateEasementRequest)
admin.site.register(RealEstateConstructionRequest)
admin.site.register(sourcingBusTemplateRequest)
admin.site.register(sourcingSupTemplateRequest)
admin.site.register(sourcingSupAgreementRequest)
admin.site.register(legalRequest)
admin.site.register(disputeCourtRequest)
admin.site.register(disputeArbitrationRequest)
admin.site.register(disputeSettlementRequest)
admin.site.register(mergerRequest)
admin.site.register(corporateRequest)
admin.site.register(dataRequest)
admin.site.register(trainingRequest)