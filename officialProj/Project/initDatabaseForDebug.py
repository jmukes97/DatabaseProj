from dbDataStructures import *
from databaseInit import *
from inventoryFunctions import *
from orderingFunctions import *
import code

brownRice = RiceType(0, "brown")
brownRice.id = addRiceType(brownRice)

whiteRice = RiceType(1, "white")
whiteRice.id = addRiceType(whiteRice)

sweetNSour = SauceType(0, "sweet n sour")
sweetNSour.id = addSauceType(sweetNSour)

teriyaki = SauceType(1, "teriyaki")
teriyaki.id = addSauceType(teriyaki)

mozziSticks = AppetizerType(0, "mozzi sticks")
mozziSticks.id = addAppetizerType(mozziSticks)

onionRings = AppetizerType(0, "onion rings")
onionRings.id = addAppetizerType(onionRings)

chicken = IngredientType(0, "chicken")
chicken.id = addIngredientType(chicken)

tofu = IngredientType(0, "tofu")
tofu.id = addIngredientType(tofu)