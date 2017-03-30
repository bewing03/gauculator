from lxml import html
import requests
import smtplib
import sys

class Person(object):
    """This is the class that makes a person"""
    def __init__(self, email, favorites, msg):
        super(Person, self).__init__()
        self.email = email
        self.favorites = favorites
        self.msg = msg

def sendmail(client):
    if client.msg != "":
        server.sendmail("gauculator@gmail.com", client.email, client.msg)
    return

#Takes a food item and a list of the menu at a dining hall that day
#Must always check carm menu first
def check_menu(food, dining_hall):
    location = ""
    if food in dining_hall:
        if dining_hall == carm_food:
            location = "Carm"
        if dining_hall == dewick_food:
            if location == "Carm":
                location = location + " and Dewick"
            else:
                location = "Dewick"
        return location
    return location

#Passed a Person and changes that person's personal message to contain
#information about their particular food choices
def create_message(client):
    for food_item in client.favorites:
        location = check_menu(food_item, carm_food)
        if location == "Carm" or location == "Dewick" or location == "Carm and Dewick":
            client.msg = client.msg + "\nThere is " + food_item + " at " + location + " today"
        #if location == "none":
            #client.msg = client.msg + "\nThere is no " + food_item + " today"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("gauculator@gmail.com", "generaltufts2017")

carm_page = requests.get('http://menus.tufts.edu/foodpro/shortmenu.asp?sName=Tufts%20Dining&locationNum=09&locationName=Carmichael%20Dining%20Center&naFlag=1')
carm_tree = html.fromstring(carm_page.content)

dewick_page = requests.get('http://menus.tufts.edu/foodpro/shortmenu.asp?sName=Tufts%20Dining&locationNum=11&locationName=Dewick-MacPhie%20Dining%20Center&naFlag=1')
dewick_tree = html.fromstring(dewick_page.content)

carm_food = carm_tree.xpath('//a[@name="Recipe_Desc"]/text()')
dewick_food = dewick_tree.xpath('//a[@name="Recipe_Desc"]/text()')

Ben     = Person("ben.ewing114@gmail.com", ["General Gau's Chicken", "Funfetti Cookie Bar", "Fiery Chicken Fingers", "VM Macaroni & Cheese", "BBQ Chicken and Cheddar Flatbread Sandwich"], "")
Wesley  = Person("twesley1996@aol.com", ["General Gau's Chicken", "Funfetti Cookie Bar", "VM Macaroni & Cheese"], "")
Tommaso = Person("tommaso.lombardi@tufts.edu", ["General Gau's Chicken", "VM Macaroni & Cheese"], "")
Abi     = Person("abinav.gowda@tufts.edu", ["General Gau's Chicken", "VM Macaroni & Cheese"], "")
Suneeth = Person("suneeth.keerthy@tufts.edu", ["General Gau's Chicken", "Ultimate Chocolate Cheese Cake"], "")
Berg    = Person("benjamin.feinberg@tufts.edu", ["General Gau's Chicken", "VM Macaroni & Cheese"], "")
Jonny   = Person("golax510@aol.com", ["General Gau's Chicken", "Funfetti Cookie Bar"], "")
Tucker  = Person("tucker.jaenicke@tufts.edu", ["General Gau's Chicken", "Funfetti Cookie Bar", "VM Macaroni & Cheese"], "")
Langen  = Person("matthewlangen@gmail.com", ["General Gau's Chicken", "Funfetti Cookie Bar", "VM Macaroni & Cheese"], "")
Adler   = Person("nadler117@gmail.com", ["General Gau's Chicken", "Chicken Nuggets", "Fiery Chicken Fingers", "VM Macaroni & Cheese"], "")

list_of_clients = [Ben, Wesley, Tommaso, Abi, Suneeth, Berg, Jonny, Tucker, Langen, Adler]

for client in list_of_clients:
    create_message(client)
    sendmail(client)

server.quit()
