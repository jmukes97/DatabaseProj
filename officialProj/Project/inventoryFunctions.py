from .databaseInit import *
from .dbDataStructures import *

def addRiceType(riceType):
    num = getStateCounter("currentRiceTypeNum")
    sql = '''INSERT INTO RICE_TYPE(TYPE_ID, TYPE_NAME, UPCHARGE, AVAILABLE) 
    VALUES (?, ?, ?, ?);'''
    conn.execute(sql, (num, riceType.name, riceType.upcharge, riceType.available))
    conn.commit()
    return num

def removeRiceType(id):
    sql = '''DELETE FROM RICE_TYPE WHERE TYPE_ID = ?;'''
    conn.execute(sql, (id,))
    conn.commit()

def getRiceType(id):
    sql = '''SELECT * FROM RICE_TYPE WHERE TYPE_ID =?;'''
    cur = conn.execute(sql, (id,))
    return createRiceType(cur.fetchone())

def createRiceType(list):
    id, name, upcharge, available = list
    available = available == 1
    return RiceType(id, name, upcharge, available)

def createRiceTypeArr(sqlCursor):
    arr = sqlCursor.fetchall()
    arr = list(map(createRiceType, arr))
    return arr




def addIngredientType(ingredient):
    num = getStateCounter("currentIngredientTypeNum")
    sql = '''INSERT INTO INGREDIENT_TYPE(TYPE_ID, INGREDIENT_NAME, UPCHARGE, RATIO, AVAILABLE) 
    VALUES(?, ?, ?, ?, ?);'''
    conn.execute(sql, (num, ingredient.name, ingredient.upcharge, ingredient.ratio, ingredient.available))
    conn.commit()
    return num

def removeIngredientType(id):
    sql = '''DELETE FROM INGREDIENT_TYPE WHERE TYPE_ID = ?;'''
    conn.execute(sql, (id, ))
    conn.commit()

def getIngredientType(id):
    sql = '''SELECT * FROM INGREDIENT_TYPE WHERE TYPE_ID = ?;'''
    cur = conn.execute(sql, (id, ))
    return createIngredientType(cur.fetchone())

def createIngredientType(list):
    id, name, upcharge, ratio, available = list
    available = available == 1
    return IngredientType(id, name, upcharge, ratio, available)

def createIngredientTypeArr(sqlCursor):
    arr = sqlCursor.fetchall()
    arr = list(map(createIngredientType, arr))
    return arr





def addSauceType(sauceType):
    num = getStateCounter("currentSauceTypeNum")
    sql = '''INSERT INTO SAUCE_TYPE(TYPE_ID, SAUCE_NAME, UPCHARGE, AVAILABLE) 
    VALUES(?, ?, ?, ?);'''
    conn.execute(sql, (num, sauceType.name, sauceType.upcharge, sauceType.available))
    conn.commit()
    return num

def removeSauceType(id):
    sql = '''DELETE FROM SAUCE_TYPE WHERE TYPE_ID = ?;'''
    conn.execute(sql, (id,))
    conn.commit()

def getSauceType(id):
    sql = '''SELECT * FROM SAUCE_TYPE WHERE TYPE_ID = ?;'''
    cur = conn.execute(sql, (id,))
    return createSauceType(cur.fetchone())

def createSauceType(list):
    id, name, upcharge, available = list
    available = available == 1
    return SauceType(id, name, upcharge, available)

def createSauceTypeArr(sqlCursor):
    arr = sqlCursor.fetchall()
    arr = list(map(createSauceType, arr))
    return arr




def addAppetizerType(appetizer):
    num = getStateCounter("currentAppetizerTypeNum")
    sql = '''INSERT INTO APPETIZER_TYPE(TYPE_ID, APPETIZER_NAME, APPETIZER_PRICE) 
    VALUES(?, ?, ?);'''
    conn.execute(sql, (num, appetizer.appetizerName, appetizer.price))
    conn.commit()
    return num

def removeAppetizerType(id):
    sql = '''DELETE FROM APPETIZER_TYPE WHERE TYPE_ID = ?;'''
    conn.execute(sql, (id,))
    conn.commit()

def getAppetizerType(id):
    sql = '''SELECT * FROM APPETIZER_TYPE WHERE TYPE_ID = ?;'''
    cur = conn.execute(sql, (id,))
    return createAppetizerType(cur.fetchone())

def createAppetizerType(list):
    id, name, price = list
    return AppetizerType(id, name, price)

def createAppetizerTypeArr(sqlCursor):
    arr = sqlCursor.fetchall()
    arr = list(map(createAppetizerType, arr))
    return arr
