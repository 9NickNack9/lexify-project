from django.db import models
from django.contrib.auth.models import User
from django.forms import widgets

# Create your models here.


class Customer(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	firstname = models.CharField(max_length=200, null=True)
	lastname = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	company = models.CharField(max_length=200, null=True)
	company_id = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class Offer(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Accepted', 'Accepted')
			)

	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)	
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	note = models.CharField(max_length=1000, null=True)

	
	def __str__(self):
		return self.offer.name


class Request(models.Model):
	TYPES = (
			('Contract(s)', 'Contract(s)'),
			('Day-to-day legal advice', 'Day-to-day legal advice'),
			('Support with dispute resolution', 'Support with dispute resolution'),
			('Support with M&A', 'Support with M&A'),
			('Support with corporate governance', 'Support with corporate governance'),
			)

	CONTRACTS = (
				('Share trade document', 'Share trade document'),
				('APA', 'APA'),
				)

	HOURS = (
			('Corporate law (0-5 hours)', 'Corporate law (0-5 hours)'),
			('Employment law (10 hours)', 'Employment law (10 hours)'),
			('IFR (20 hours)', 'IFR (20 hours)'),
			)

	OFFERERS = (
				('Attorneys-at-law (FI: asianajotoimistot), any size', 'Attorneys-at-law (FI: asianajotoimistot), any size'),
				('Attorneys-at-law, employing at least 5 lawyers', 'Attorneys-at-law, employing at least 5 lawyers'),
				('Attorneys-at-law, employing at least 15 lawyers', 'Attorneys-at-law, employing at least 15 lawyers'),
				('Law firms (FI: lakiasiaintoimistot), any size', 'Law firms (FI: lakiasiaintoimistot), any size'),
				('Law firms, employing at least 5 lawyers', 'Law firms, employing at least 5 lawyers'),
				('Law firms, employing at least 15 lawyers', 'Law firms, employing at least 15 lawyers'),
				)

	LANGS = (		
			('English', 'English'),
			('Finnish', 'Finnish'),
			('Swedish', 'Swedish'),
			('English & Finnish', 'English & Finnish'),
			)

	OFFER_TIMES = (
					('Within 24 hours', 'Within 24 hours'),
					('Within 48 hours', 'Within 48 hours'),
					('Within 7 days', 'Within 7 days'),
					)

	INVOICES = (
				('On a monthly basis, invoice sent at end of each calendar month', 'On a monthly basis, invoice sent at end of each calendar month'),
				('On a quarterly basis, invoice sent at end of each quarter', 'On a quarterly basis, invoice sent at end of each quarter'),
				('One time invoice upon completion of the assignment', 'One time invoice upon completion of the assignment'),
				)

	RUNNING_INVOICES = (
				('On a monthly basis, invoice sent at end of each calendar month', 'On a monthly basis, invoice sent at end of each calendar month'),
				('On a quarterly basis, invoice sent at end of each quarter', 'On a quarterly basis, invoice sent at end of each quarter'),
				)

	ADD_INFO = (
				('Yes', 'Yes'),
				('No', 'No'),
				)

	TRAINING_DURATIONS = (
						('1 hour', '1 hour'),
						('2 hours', '2 hours'),
						('4 hours', '4 hours'),
						('1 full day', '1 full day'),
						('2 full days', '2 full days'),
						)

	TRAINING_PLACES = (
					('Specify place below (under "Other information")', 'Specify place below (under "Other information")'),
					('Remotely (e.g. over Microsoft Teams), with invite to be sent by you to your Lexify service provider', 'Remotely (e.g. over Microsoft Teams), with invite to be sent by you to your Lexify service provider'),
					('Location to be confirmed later (possible travel related costs may be invoiced separately by your legal service provider)', 'Location to be confirmed later (possible travel related costs may be invoiced separately by your legal service provider)'),
					)

	PRIVACY_OPTIONS = (
					('Holistic review of my company’s current level of compliance with data privacy legislation applicable in Finland, including written report of findings', '(a) Holistic review'),
					('Holistic review of my company’s current level of compliance with data privacy legislation applicable in Finland, including written report of findings. Performance of corrective actions needed to remedy any deficiencies identified in the review (e.g. preparation of data privacy statement(s) and/or other necessary documentation, if missing)', '(b) Holistic review + performance of corrective actions'),
					)

	GDPR = (
			('Before May 2016', 'Before May 2016'),
			('After May 2016', 'After May 2016'),
			("I don't know", "I don't know"),
			)

	EMPLOYEE_COUNT = (
					('0-10', '0-10'),
					('10-25', '10-25'),
					('25-100', '25-100'),
					('100-1000', '100-1000'),
					('1000+', '1000+'),
					)

	CORP_COMPANIES = (
					('Private limited company (osakeyhtiö)', 'Private limited company (osakeyhtiö)'),
					('Public  limited company (julkinen  osakeyhtiö)', 'Public  limited company (julkinen  osakeyhtiö)'),
					)


	AREA_CHOICES = (
				('General legal advice', 'General legal advice'),
				('Sales, B2B', 'Sales, B2B'),
				('Sales, B2C', 'Sales, B2C'),
				('Employment', 'Employment'),
				('Real Estate & Construction' ,'Real Estate & Construction'),
				('Sourcing', 'Sourcing'),
				('ICT & IT', 'ICT & IT'),
				('Intellectual Property Rights', 'Intellectual Property Rights'),
				('Data Privacy', 'Data Privacy'),
				('Competition/antitrust', 'Competition/antitrust'),
				)

	LEGAL_MONTHS = (
					('12', '12'),
					('24', '24'),
					('36', '36'),
					)

	LEGAL_HOURS = (
					('5 hours', '5 hours'),
					('10 hours', '10 hours'),
					('15 hours', '15 hours'),
					('20 hours', '20 hours'),
					)

	LEGAL_OFFERS = (
					('Single hourly rate for occasional legal advice in the amount needed from time to time. Billed monthly in arrears.', 'Single hourly rate for occasional legal advice in the amount needed from time to time. Billed monthly in arrears.'),
					('Lump sum monthly price for a fixed number of hours of legal support per month. Billed monthly in arrears.', 'Lump sum monthly price for a fixed number of hours of legal support per month. Billed monthly in arrears.'),
					)

	BUY_OR_SELL = (
					('Buying', 'Buying'),
					('Selling', 'Selling'),
					)

	MERGER_TYPES = (
					('Shares (all shares)', 'Shares (all shares)'),
					('Shares (majority of shares)', 'Shares (majority of shares)'),
					('Shares (minority stake)', 'Shares (minority stake)'),
					('Business', 'Business'),
					('Specific asset(s)', 'Specific asset(s)'),
					)

	MERGER_COMPANIES = (
					('Private Limited Company', 'Private Limited Company'),
					('Public Limited Company', 'Public Limited Company'),
					('Private Person', 'Private Person'),
					)

	MERGER_TARGETS = (
					('Private Limited Company', 'Private Limited Company'),
					('Public Limited Company', 'Public Limited Company'),
					)

	MONEY_RANGES = (
					('0-100 kEUR', '0-100 kEUR'),
					('100 kEUR - 1 mEUR', '100 kEUR - 1 mEUR'),
					('1-10 mEUR', '1-10 mEUR'),
					('10-50 mEUR', '10-50 mEUR'),
					('50+ mEUR', '50+ mEUR'),
					)

	MERGER_AREAS = (
					('Holistic legal representation throughout the transaction process (including but not limited to legal due diligence, drafting of the sale and purchase agreement and related documents, required negotiations with the other party and support with signing and closing related actions)', '(1) Holistic legal representation'),
					('Occasional support with the transaction process (e.g. commenting of transactional documents, legal advice during different stages of the transaction)', '(2) Occasional support'),
					('Legal due diligence regarding the target; reporting of findings with short form ”red flag” LDD report', '(3) Short form LDD report'),
					('Legal due diligence regarding the target; reporting of findings with long form LDD report (comprehensive review of all legal matters related to the target, not only identified ”red flag” issues)', '(4) Long form LDD report'),
					)

	DISPUTE_ROLES = (
					('Claimant', 'Claimant'),
					('Defendant', 'Defendant'),
					)

	DISPUTE_COURT_AREAS = (
							('Holistic legal representation in court proceedings (including e.g. drafting of legal briefs, representation in court hearings, attorney-client communications)', '(a) Holistic legal representation in court proceedings'),
							('Occasional support with court proceedings (e.g. commenting on legal briefs, periodic advice regarding legal strategy, etc.)', '(b) Occasional support with court proceedings'),
							)

	DISPUTE_ARBI_AREAS = (
							('Holistic legal representation in arbitration proceedings (including e.g. drafting of legal briefs, representation in arbitration hearings, attorney-client communications)', '(a) Holistic legal representation in arbitration proceedings'),
							('Occasional support with arbitration proceedings (e.g. commenting on legal briefs, periodic advice regarding legal strategy, etc.)', '(b) Occasional support with arbitration proceedings'),
							)

	DISPUTE_SETTLEMENT_AREAS = (
							('Holistic legal representation in settlement negotiations (including e.g. drafting of a settlement agreement, negotiations with the other party, attorney-client communications)', '(a) Holistic legal representation in settlement negotiations'),
							('Occasional support with settlement negotiations (e.g. commenting on draft settlement agreement, periodic advice regarding legal strategy, etc.)', '(b) Occasional support with settlement negotiations'),
							)

	DISPUTE_AREAS = (
							('Court Proceedings Holistic legal representation', '(a) Court Proceedings Holistic legal representation'),
							('Court Proceedings Occasional support', '(b) Court Proceedings Occasional support'),
							('Arbitration Proceedings Holistic legal representation', '(c) Arbitration Proceedings Holistic legal representation'),
							('Arbitration Proceedings Occasional support', '(d) Arbitration Proceedings Occasional support'),
							('Settlement Negotiations Holistic legal representation', '(e) Settlement Negotiations Court Proceedings Holistic legal representation'),
							('Settlement Negotiations Occasional support', '(f) Settlement Negotiations Court Proceedings Occasional support'),
							)

	DISPUTE_PARTY = (
						('a Party to Court Proceedings', '(a/b) a Party to Court Proceedings'),
						('a Party to Arbitration Proceedings', '(c/d) a Party to Arbitration Proceedings'),
						('a Party to Settlement Negotiations', '(e/f) a Party to Settlement Negotiations'),
						)


	SOURCING_TEMPLATE = (
						('Products','Products'),
						('Services', 'Services'),
						)

	SOURCING_GENERIC = (
						('Generic', 'Generic'),
						('Customized', 'Customized')
						)

	SOURCING_TYPE = (
					('My own contract template', 'My own contract template'),
					("Supplier's contract template", "Supplier's contract template"),
					)

	EMPLOYMENT_CONTRACT = (
							('Employment Contract', 'Employment Contract'),
							('Managing Director Contract','Managing Director Contract'),
							('Mutual Termination Contract','Mutual Termination Contract'),
							)

	REALESTATE_AGREEMENT = (
							('Plot/Parcel of Land', 'Plot/Parcel of Land'),
							('Shares in a Real Estate Company (FI: kiinteistöosakeyhtiö)', 'Shares in a Real Estate Company (FI: kiinteistöosakeyhtiö)'),
							('Shares in a Housing Association (FI: asunto-osakeyhtiö)', 'Shares in a Housing Association (FI: asunto-osakeyhtiö)')
							)

	REALESTATE_PURCHASE = (
						('Holistic legal representation throughout the transaction process (including but not limited to drafting of the sale and purchase agreement and related documents, required negotiations with the other party and completion of signing/closing related legal actions)', '(a) Holistic legal representation'),
						('Occasional support with the transaction process (e.g. commenting of transactional documents, legal advice during different stages of the transaction)', '(b) Occasional support'),
						('First draft of the sale and purchase agreement, ready for delivery to the other party', '(c) First draft of sale and purchase agreement'),
						('First draft of the sale and purchase agreement, ready for delivery to the buyer/seller and thereafter occasional support with the transaction process (e.g. further commenting of transactional documents, legal advice during different stages of the transaction)', '(d) First draft of sale and purchase agreement + occasional support'),
						)

	REALESTATE_LEASEBACK = (
						('Holistic legal representation throughout the transaction process (including but not limited to drafting of the sale and leaseback agreement and related documents, required negotiations with the other party and completion of signing/closing related legal actions)', '(a) Holistic legal representation'),
						('Occasional support with the transaction process (e.g. commenting of transactional documents, legal advice during different stages of the transaction)', '(b) Occasional support'),
						('First draft of the sale and leaseback agreement, ready for delivery to the other party', '(c) First draft of sale and purchase and lease agreement'),
						('First draft of the sale and leaseback agreement, ready for delivery to the other party and thereafter occasional support with the transaction process (e.g. further commenting of transactional documents, legal advice during different stages of the transaction)', '(d) First draft of sale and purchase and lease agreement + occasional support'),
						)

	REALESTATE_LEASE = (
						('Holistic legal representation throughout the transaction process (including but not limited to drafting of the lease and related documents, required negotiations with the other party and completion of signing/closing related legal actions)', '(a) Holistic legal representation'),
						('Occasional support with the transaction process (e.g. commenting of transactional documents, legal advice during different stages of the transaction)', '(b) Occasional support'),
						('First draft of the lease agreement, ready for delivery to the other party', '(c) First draft of lease agreement'),
						('First draft of the lease agreement, ready for delivery to the other party and thereafter occasional support with the transaction process (e.g. further commenting of transactional documents, legal advice during different stages of the transaction)', '(d) First draft of lease agreement + occasional support'),
						)

	REALESTATE_CONSTRUCTION = (
						('Holistic legal representation throughout the transaction process (including but not limited to drafting of the construction agreement and related documents, required negotiations with the other party and completion of signing/closing related legal actions)', '(a) Holistic legal representation'),
						('Occasional support with the transaction process (e.g. commenting of transactional documents, legal advice during different stages of the transaction)', '(b) Occasional support'),
						('First draft of the construction agreement, ready for delivery to the other party', '(c) First draft of construction agreement'),
						('First draft of the construction agreement, ready for delivery to the other party and thereafter occasional support with the transaction process (e.g. further commenting of transactional documents, legal advice during different stages of the transaction)', '(d) First draft of construction agreement + occasional support'),
						)

	CONSTRUCTION_PRICE = (
					('0 - 50kEUR', '0 - 50kEUR'),
					('50 - 100kEUR', '50 - 100kEUR'),
					('100kEUR - 1mEUR', '100kEUR - 1mEUR'),
					('1+mEUR', '1+mEUR'),
					)

	LEASEBACK_ROLE = (
						('Seller and Tenant', 'Seller and Tenant'),
						('Buyer and Landlord', 'Buyer and Landlord'),
						)

	LEASE_AGREEMENT = (
						('Lease of business premises', 'Lease of business premises'),
						('Lease of residential premises', 'Lease of residential premises'),
						('Lease of a plot or a parcel of land', 'Lease of a plot or a parcel of land'),
						)

	LEASE_ROLE = (
					('Tenant', 'Tenant'),
					('Landlord', 'Landlord'),
					)

	LEASE_RANGE = (
					('0-1000 EUR', '0-1000 EUR'),
					('1000 EUR-10 000 EUR', '1000 EUR-10 000 EUR'),
					('10 000 EUR-50 000 EUR', '10 000 EUR-50 000 EUR'),
					('50 000 EUR+', '50 000 EUR+'),
					)

	CONSTRUCTION_AGREEMENT = (
								('Contractor (seller of construction services)', 'Contractor (seller of construction services)'),
								('Client (buyer of construction services)', 'Client (buyer of construction services)')
								)

	EASEMENT_PROPERTY = (
						('Encumbered', 'Encumbered'),
						('Encumbering', 'Encumbering'),
						)

	EASEMENT_SUPPORT = (
						('Holistic legal representation throughout the easement agreement negotiation process (including but not limited to drafting of the easement agreement and related documents (excluding purely technical maps and other similar documents), required communications with the other property owner, participation in necessary easement related meetings with competent authorities, etc.)', '(a) Holistic legal representation'),
						('Occasional support with the easement agreement negotiation process (e.g. commenting of the easement agreement documentation, legal advice during different stages of the process)', '(b) Occasional support'),
						('First draft of the easement agreement (excluding purely technical maps and similar documents), ready for delivery to the other property owner', '(c) First draft of lease agreement'),
						('First draft of the easement agreement (excluding purely technical maps and similar documents), ready for delivery to the other property owner and thereafter occasional support with the easement agreement process (e.g. further commenting of the easement agreement documentation, legal advice during different stages of the process)', '(d) First draft of lease agreement + occasional support'),
						)




	date_created = models.DateTimeField(auto_now_add=True, null=True)
	title = models.CharField(max_length=200, null=True)
	requestType = models.CharField(max_length=200, null=True, choices=TYPES)
	contractType = models.CharField(max_length=200, null=True, choices=CONTRACTS)
	hourCount = models.CharField(max_length=200, null=True, choices=HOURS)
	note = models.TextField(blank=False, null=True)
	offerMaker = models.CharField(max_length=200, null=True, blank=False, choices=OFFERERS)
	language = models.CharField(max_length=200, null=True, blank=False, choices=LANGS)
	offerTime = models.CharField(max_length=200, null=True, choices=OFFER_TIMES)
	invoiceType = models.CharField(max_length=200, null=True, blank=False, choices=INVOICES)
	invoiceTypeRunning = models.CharField(max_length=200, null=True, blank=False, choices=RUNNING_INVOICES)
	additionalInfo = models.CharField(max_length=200, null=True, choices=ADD_INFO)
	otherInfo = models.TextField(blank=True, null=True)

	#Day-to-day legal advice
	legalMonths = models.CharField(max_length=200, null=True, blank=True, choices=LEGAL_MONTHS)
	legalHours = models.CharField(max_length=200, null=True, blank=True, choices=LEGAL_HOURS)
	legalOffers = models.CharField(max_length=200, null=True, blank=True, choices=LEGAL_OFFERS)

	#Dispute resolution support
	dispRole = models.CharField(max_length=200, null=True, blank=True, choices=DISPUTE_ROLES)
	dispParty = models.CharField(max_length=200, null=True, blank=True, choices=DISPUTE_PARTY)
	courtArea = models.CharField(max_length=200, null=True, blank=True, choices=DISPUTE_COURT_AREAS)
	arbiArea = models.CharField(max_length=200, null=True, blank=True, choices=DISPUTE_ARBI_AREAS)
	settlementArea = models.CharField(max_length=200, null=True, blank=True, choices=DISPUTE_SETTLEMENT_AREAS)
	dispArea = models.CharField(max_length=200, null=True, blank=True, choices=DISPUTE_AREAS)
	dispDescription = models.TextField(blank=False, null=True)

	#Mergers & aquisitions
	sellOrBuy = models.CharField(max_length=200, null=True, blank=True, choices=BUY_OR_SELL)
	mergerType = models.CharField(max_length=200, null=True, blank=False, choices=MERGER_TYPES)
	mergerCompany = models.CharField(max_length=200, null=True, blank=True, choices=MERGER_COMPANIES)
	mergerOtherCompany = models.CharField(max_length=200, null=True, blank=True, choices=MERGER_COMPANIES)
	mergerTarget = models.CharField(max_length=200, null=True, blank=True, choices=MERGER_TARGETS)
	mergerBusinessLine = models.TextField(blank=True, null=True)
	mergerRange = models.CharField(max_length=200, null=True, blank=True, choices=MONEY_RANGES)
	mergerArea = models.CharField(max_length=330, null=True, blank=True, choices=MERGER_AREAS)

	#Corporate administration
	corpCompany = models.CharField(max_length=200, null=True, choices=CORP_COMPANIES)
	
	#Data Privacy
	privacyOptions = models.CharField(max_length=400, null=True, choices=PRIVACY_OPTIONS)
	privacyReview = models.CharField(max_length=200, null=True, choices=ADD_INFO)
	privacyGDPR = models.CharField(max_length=200, null=True, choices=GDPR)
	privacyBusinessLine = models.TextField(blank=True, null=True)
	privacyEmployeeCount = models.CharField(max_length=200, null=True, choices=EMPLOYEE_COUNT)


	#Training request
	legalTopic = models.TextField(blank=True, null=True)
	trainingDuration = models.CharField(max_length=200, null=True, choices=TRAINING_DURATIONS)
	dateConfirm = models.CharField(max_length=200, null=True, choices=ADD_INFO, default='No')
	trainingDate = models.DateField(null=True)
	trainingTime = models.TimeField(null=True)
	trainingPlace = models.CharField(max_length=200, null=True, choices=TRAINING_PLACES)
	trainingPlaceInfo = models.TextField(blank=True, null=True)

	#B2B
	b2bDate = models.DateField(null=True)

	#B2C
	b2cDate = models.DateField(null=True)

	#Employment
	employmentTemplate = models.TextField(blank=True, null=True)
	employmentContract = models.CharField(max_length=200, null=True, choices=EMPLOYMENT_CONTRACT)
	employmentPos = models.TextField(blank=True, null=True)

	#Real Estate & Construction
	realestateAgreement = models.CharField(max_length=400, null=True, choices=REALESTATE_AGREEMENT)
	agreementBuyer = models.CharField(max_length=400, null=True, choices=BUY_OR_SELL)
	agreementDescription = models.TextField(blank=True, null=True)
	agreementRange = models.CharField(max_length=400, null=True, choices=MONEY_RANGES)
	agreementInspection = models.CharField(max_length=400, null=True, choices=ADD_INFO)
	realSalePurchase = models.CharField(max_length=400, null=True, choices=REALESTATE_PURCHASE)
	realLeaseBack = models.CharField(max_length=400, null=True, choices=REALESTATE_LEASEBACK)
	realLease = models.CharField(max_length=400, null=True, choices=REALESTATE_LEASE)
	realConstruction = models.CharField(max_length=400, null=True, choices=REALESTATE_CONSTRUCTION)
	
	leasebackSeller = models.CharField(max_length=400, null=True, choices=LEASEBACK_ROLE)
	leasebackDescription = models.TextField(blank=True, null=True)
	leasebackRange = models.CharField(max_length=400, null=True, choices=MONEY_RANGES)
	leasebackInspection = models.CharField(max_length=400, null=True, choices=ADD_INFO)

	leaseAgreement = models.CharField(max_length=400, null=True, choices=LEASE_AGREEMENT)
	leaseRole = models.CharField(max_length=400, null=True, choices=LEASE_ROLE)
	leaseDescription = models.TextField(blank=True, null=True)
	leaseRange = models.CharField(max_length=400, null=True, choices=LEASE_RANGE)

	constructionAgreement = models.CharField(max_length=400, null=True, choices=CONSTRUCTION_AGREEMENT)
	constructionDescription = models.TextField(blank=True, null=True)
	constructionRange = models.CharField(max_length=400, null=True, choices=MONEY_RANGES)
	constructionPrice = models.CharField(max_length=400, null=True, choices=CONSTRUCTION_PRICE)

	#Sourcing
	sourcingTemplate = models.CharField(max_length=400, null=True, choices=SOURCING_TEMPLATE)
	sourcingGeneric = models.CharField(max_length=400, null=True, choices=SOURCING_GENERIC)
	sourcingCustomized = models.TextField(blank=True, null=True)
	sourcingComments = models.TextField(blank=True, null=True)
	sourcingLawyer = models.TextField(blank=True, null=True)
	sourcingType = models.CharField(max_length=400, null=True, choices=SOURCING_TYPE)

	#Easement
	easementProperty = models.CharField(max_length=400, null=True, choices=EASEMENT_PROPERTY)
	easementSupport = models.CharField(max_length=400, null=True, choices=EASEMENT_SUPPORT)

	def __str__(self):
		return self.title