import urllib2
from xml.etree import ElementTree
import sys

#User input here since subl doesn't handle that  
#Yes, but terminal can. Don't shy from using raw_input to make your code interactable
currentSystem="Jita"
endSystem="Rens"
item = "Merlin"

#Check whether system names are valid
systems = file('systems.txt')
if currentSystem+"\n" not in systems:
	print currentSystem, "not in system database."
	sys.exit()
#Why do I have to load this again? I don't know but if I don't the following if statement returns a false positive
systems = file('systems.txt')
if endSystem+"\n" not in systems:
	print endSystem, "not in system database."
	sys.exit() #You shouldn't have to use this, make sure all your code is enveloped in functions

#You can combine the two functions into one.

#Local DB with item names and id's
item_data = file('items.txt')
item_id=""
for line in item_data:
	if item in line:
		if line.split(",")[2]==item: #If item name is exact match (many items share subnames for variations on same item)
			item_id=line.split(",")[0]

if item_id=="":
	print "No item with that name found."
	sys.exit()
else:
	#Grab data on buy and sell orders for item in all systems between currentSystem and endSystem
	try: #Nice job on error catching
		root = ElementTree.fromstring(urllib2.urlopen("http://api.eve-central.com/api/quicklook/onpath/from/"+currentSystem+"/to/"+endSystem+"/fortype/"+item_id).read())
	except:
		print "Error querying the database"
		sys.exit()
print "Using", root.tag, root.attrib
print ""
#Data root
quicklook = root[0]

sell_orders = []
for order in quicklook.find("sell_orders"):
    key = order.findtext("price")
    sell_orders.append((float(key), order))
sell_orders.sort()
lowest_sell = sell_orders[0][1]

buy_orders = []
for order in quicklook.find("buy_orders"):
	key = order.findtext("price")
	buy_orders.append((float(key), order))
buy_orders.sort()
highest_buy = buy_orders[-1][1]
#These two loops can be easily be placed inside a function that's called twice so you aren't repeating so much code

if lowest_sell.findtext("price") > highest_buy.findtext("price"):
	print "No Profitable Haul Found." #Buying high and selling low is counter-productive
else:
	jumps = urllib2.urlopen("http://api.eve-central.com/api/route/from/"+str.split(lowest_sell.findtext("station_name"))[0]+"/to/"+str.split(highest_buy.findtext("station_name"))[0]).read().count("systemid")/2
	#How much it will cost per unit to buy the item
	buyPrice = float(lowest_sell.findtext("price"))
	buyVol = int(lowest_sell.findtext("vol_remain"))
	#How much you can sell the unit for
	sellPrice = float(highest_buy.findtext("price"))
	sellVol = int(highest_buy.findtext("vol_remain"))
	profit = (sellPrice-buyPrice)*min([buyVol,sellVol]) #Use the lesser of the two volumes since once a buy order is filled it goes away and same for a sell order
	print "Potential Profit Found:", profit, "ISK with", jumps, "jumps"
	print ""
	print lowest_sell.findtext("station_name")
	print "to"
	print highest_buy.findtext("station_name")
