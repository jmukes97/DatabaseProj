class Order:
    def __init__(self, orderNumber = 1, orderName = "", orderPrice = 0,
            pickupTime = None, statusCode = "", bowls = [], appetizers = [], payment = None):
        self.orderNumber = orderNumber
        self.orderName = orderName
        self.orderPrice = orderPrice
        self.pickupTime = pickupTime
        self.statusCode = statusCode
        self.bowls = bowls
        self.appetizers = appetizers
        self.payment = payment

    def getStatusCode(status):
        if status == "waiting":
            return 0
        elif status == "readForPickup":
            return 1
        elif status == "completed":
            return 2
        elif status == "canceled":
            return 3
        else:
            return 3
		
class Bowl:
    def __init__(self, bowlNumber = 0, orderNumber = 0, bowlPrice = 0,
            size = "", riceType = 0, sauceType = 0, ingredients = []):
        self.bowlNumber = bowlNumber
        self.orderNumber = orderNumber
        self.bowlPrice = bowlPrice
        self.size = size
        self.riceType = riceType
        self.sauceType = sauceType
        self.ingredients = ingredients


    def getSizeNumber(self):
        if self.size == "small":
            return 0
        elif self.size == "medium":
            return 1
        elif self.size == "large":
            return 2
        else:
            return 3
		
class RiceType:
	def __init__(self, id = 0, name = "", upcharge = 0, available = True):
		self.id = id
		self.name = name
		self.upcharge = upcharge
		self.available = available

class IngredientType:
	def __init__(self, id = 0, name = "", upcharge = 0, ratio = 1, available = True):
		self.id = id
		self.name = name
		self.upcharge = upcharge
		self.ratio = ratio
		self.available = available
		
class SauceType:
	def __init__(self, id = 0, name = "", upcharge = 0, available = True):
		self.id = id
		self.name = name
		self.upcharge = upcharge
		self.available = available
		
class AppetizerType:
	def __init__(self, id = 0, appetizerName = "", price = 0):
		self.id = id
		self.appetizerName = appetizerName
		self.price = price
		
class Payment:
	def __init__(self, paymentType = "", cardInfo = None):
		self.paymentType = paymentType
		self.cardInfo = cardInfo
		
class CardInfo:
	def __init__(self, firstName = "", lastName = "", address = "", cardNumber = "", 
			ccv = "", zipCode = ""):
		self.firstName = firstName
		self.lastName = lastName
		self.address = address
		self.cardNumber = cardNumber
		self.ccv = ccv
		self.zipCode = zipCode
