from lxml import html
import requests

carm_page = requests.get('http://menus.tufts.edu/foodpro/shortmenu.asp?sName=Tufts%20Dining&locationNum=09&locationName=Carmichael%20Dining%20Center&naFlag=1')
carm_tree = html.fromstring(carm_page.content)

dewick_page = requests.get('http://menus.tufts.edu/foodpro/shortmenu.asp?sName=Tufts%20Dining&locationNum=11&locationName=Dewick-MacPhie%20Dining%20Center&naFlag=1')
dewick_tree = html.fromstring(dewick_page.content)

carm_food = carm_tree.xpath('//a[@name="Recipe_Desc"]/text()')
dewick_food = dewick_tree.xpath('//a[@name="Recipe_Desc"]/text()')

food = "General Gau's Chicken"
status = 'none';

if food in carm_food:
    status = 'carm'

if food in dewick_food:
    if status == 'carm':
        status = 'both'
    else:
        status = 'dewick'

print(status)


print('Dewick Menu:')
print ('\n '.join(dewick_food))
print ('\n')
print ('Carm Menu:')
print ('\n '.join(carm_food))
