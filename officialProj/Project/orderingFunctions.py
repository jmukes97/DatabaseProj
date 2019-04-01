import datetime

from inventoryFunctions import *
import time
time.strftime('%Y-%m-%d %H:%M:%S')

def getCurrentRiceTypes():
    sql = '''SELECT * FROM RICE_TYPE WHERE AVAILABLE = 1;'''
    cur = conn.execute(sql)
    return createRiceTypeArr(cur)

def getAllRiceTypes():
    sql = '''SELECT * FROM RICE_TYPE'''
    cur = conn.execute(sql)
    return createRiceTypeArr(cur)


def getCurrentSauceTypes():
    sql = '''SELECT * FROM SAUCE_TYPE WHERE AVAILABLE = 1;'''
    cur = conn.execute(sql)
    return createSauceTypeArr(cur)

def getAllSauceTypes():
    sql = '''SELECT * FROM SAUCE_TYPE'''
    cur = conn.execute(sql)
    return createSauceTypeArr(cur)


def getCurrentIngredientTypes():
    sql = '''SELECT * FROM INGREDIENT_TYPE WHERE AVAILABLE = 1;'''
    cur = conn.execute(sql)
    return createIngredientTypeArr(cur)

def getAllIngredientTypes():
    sql = '''SELECT * FROM INGREDIENT_TYPE'''
    cur = conn.execute(sql)
    return createIngredientTypeArr(cur)

def placeOrder(order):
    orderNumber = getStateCounter('currentOrderNumber')
    sql = 'INSERT INTO ORDERS(ORDER_NUMBER, ORDER_NAME, ORDER_PRICE, PICKUP_TIME, STATUS_CODE) VALUES(?, ?, ?, ?, ?)'

    # get order time
    if order.pickupTime == None:
        orderTime = datetime.datetime.now() + datetime.timedelta(minutes = 30)
        order.pickupTime = orderTime

    # get status code
    statusCode = 0
    if order.statusCode == "waiting":
        statucCode = 0
    elif order.statusCode == "readyForPickup":
        statucCode = 1
    elif order.statusCode == 'completed':
        statusCode = 2
    elif order.statusCode == 'canceled':
        statusCode = 3

    conn.execute(sql, (orderNumber, order.orderName, order.orderPrice, order.pickupTime, statusCode))
    addBowlsToOrder(orderNumber, order.bowls)
    addAppetizersToOrder(orderNumber, order.appetizers)

    conn.commit()

def addBowlsToOrder(orderNumber, bowls):
    sql = 'INSERT INTO BOWLS(ORDER_NUMBER, BOWL_NUMBER, BOWL_PRICE, BOWL_SIZE, RICE_TYPE, SAUCE_TYPE) VALUES(?, ?, ?, ?, ?, ?)'

    for i in range(len(bowls)):
        bowl = bowls[i]
        conn.execute(sql, (orderNumber, i, bowl.bowlPrice, bowl.getSizeNumber(), bowl.riceType, bowl.sauceType))
        addIngrediantsToOrder(orderNumber, i, bowl.ingredients)

def addIngrediantsToOrder(orderNumber, bowlNumber, ingredients):
    sql = 'INSERT INTO BOWL_INGREDIENTS(ORDER_NUMBER, BOWL_NUMBER, INGREDIENT_TYPE) VALUES(?, ?, ?)'

    for i in range(len(ingredients)):
        ing = ingredients[i]
        conn.execute(sql, (orderNumber, bowlNumber, ing))

def addAppetizersToOrder(orderNumber, appetizers):
    sql = 'INSERT INTO APPETIZERS(ORDER_NUMBER, APPETIZER_NUMBER, NUMBER_ORDERED) VALUES(?, ?, 1)'

    for i in range(len(appetizers)):
        app = appetizers[i]
        conn.execute(sql, (orderNumber, app))


def getOrder(orderNumber):
    sql = 'SELECT * FROM ORDERS WHERE ORDER_NUMBER = ?'
    cur = conn.execute(sql, (orderNumber, ))
    orderNumber, orderName, orderPrice, pickupTime, statusCode = cur.fetchone()

    order = Order(orderNumber, orderNumber, orderPrice, pickupTime, statusCode)

    bowlsSql = 'SELECT * FROM BOWLS WHERE ORDER_NUMBER = ?'
    order.bowls = getBowls(orderNumber)
    order.appetizers = getAppetizers(orderNumber)
    order.payment = getPayments(orderNumber)
    return order

def getBowls(orderNumber):
    sql = 'SELECT * FROM BOWLS WHERE ORDER_NUMBER = ?'
    cur = conn.execute(sql, (orderNumber, ))
    arr = cur.fetchall()
    out = []
    for element in arr:
        orderNumber, bowlNumber, bowlPrice, bowlSize, riceType, sauceType = element
        bowl = Bowl(orderNumber, bowlNumber, bowlPrice, bowlSize, riceType, sauceType)
        bowl.ingredients = getIngredients(orderNumber, bowlNumber)
        out = out + [bowl]
    return out

def getIngredients(orderNumber, bowlNumber):
    sql = 'SELECT INGREDIENT_TYPE FROM BOWL_INGREDIENTS WHERE ORDER_NUMBER = ? AND BOWL_NUMBER = ?'
    cur = conn.execute(sql, (orderNumber, bowlNumber))
    arr = cur.fetchall()
    return arr

def getAppetizers(orderNumber):
    sql = 'SELECT APPETIZER_NUMBER FROM APPETIZERS WHERE ORDER_NUMBER = ?'
    cur = conn.execute(sql, (orderNumber, ))
    arr = cur.fetchall()
    return arr

def getPayments(orderNumber):
    sql = 'SELECT PAYMENT_TYPE FROM PAYMENTS WHERE ORDER_NUMBER = ?'
    cur = conn.execute(sql, (orderNumber, ))
    type = cur.fetchone()
    if type is None:
        return None
    else:
        type = type[0]
    if type == 0:
        return Payment('cash')
    else:
        return Payment('card', getCardInfo(orderNumber))

def getCardInfo(orderNumber):
    sql = 'SELECT * FROM CARD_INFO WHERE ORDER_NUMBER = ?'
    cur = conn.execute(sql, (orderNumber, ))
    orderNumber, firstName, lastName, address, cardNumber, ccv, zipCode = cur.fetchone()
    return CardInfo(orderNumber, firstName, lastName, address, cardNumber, ccv, zip)


def getActiveOrders():
    sql = 'SELECT ORDER_NUMBER FROM ORDERS WHERE STATUS_CODE = 0'
    cur = conn.execute(sql)
    arr = cur.fetchall()
    return unwrapOrders(arr)

def unwrapOrders(arr):
    out = []
    for element in arr:
        out = out + [getOrder(element[0])]
    return out





def setOrderStatus(orderNumber, status):
    statusCode = Order.getStatusCode(status)
    sql = 'UPDATE ORDERS SET STATUS_CODE = ? WHERE ORDER_NUMBER = ?;'
    conn.execute(sql, (statusCode, orderNumber))
    conn.commit()





def setOrderPayment(orderNumber, payment):
    if payment.paymentType == "cash":
        setCashPayment(orderNumber)
    else:
        setCardPayment(orderNumber, payment.cardInfo)

def setCashPayment(orderNumber):
    sql = 'INSERT INTO PAYMENTS(ORDER_NUMBER, PAYMENT_TYPE) VALUES(?, 0);'
    conn.execute(sql, (orderNumber, ))
    conn.commit()

def setCardPayment(orderNumber, cardInfo):
    sql = 'INSERT INTO PAYMENTS(ORDER_NUMBER, PAYMENT_TYPE) VALUES(?, 1);'
    conn.execute(sql, (orderNumber, ))

    sql2 = 'INSERT INTO CARD_INFO(ORDER_NUMBER, F_NAME, L_NAME, ADDRESS, CARD_NUMBER, CCV, CARD_ZIP) VALUES(?, ?, ?, ?, ?, ?, ?);'
    conn.execute(sql2, (orderNumber, cardInfo.firstName, cardInfo.lastName, cardInfo.address, cardInfo.cardNumber, cardInfo.ccv, cardInfo.zipCode))
    conn.commit()


def placeDebugOrder():
    order = Order(0, "Reynolds", 10, None, "waiting")
    order.bowls = [
        Bowl(bowlPrice=5, ingredients=[0, 1]),
        Bowl(bowlPrice=5, sauceType = 1, ingredients=[1])
    ]
    order.appetizers = [1]
    placeOrder(order)