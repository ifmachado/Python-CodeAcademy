class Menu:
  # class constructor
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

 # when printing the object it will return its name
  def __repr__(self):
    return self.name

  #method to calculate bill pased on a list of consumed products
  def calculate_bill(self, purchased_items):
    total_cost = 0
    for item in purchased_items:
      total_cost += self.items[item]
    return total_cost

#items in brunch menu
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
# brunch object - instance of Menu class
brunch = Menu("Brunch", brunch_items, 1100, 1600)

early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00 }

early_bird = Menu("Early-bird Dinner", early_bird_items, 1500, 1800)

dinner_items = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

dinner = Menu("Dinner", dinner_items, 1700, 2300)

kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids = Menu("Kids", kids_items, 1100, 2100)

class Franchise:
  # class constructor
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
 # when printing the object it will return its address
  def __repr__(self):
    return self.address

  #method will return available menus based on time client arrived.
  def available_menus(self, time):
    available_menu = []
    #iterate through list of menus defines on constructor. this also make "menu" an object.
    for menu in self.menus:
      #the menu object will take start and end time from its instanciation of Menu class.
      if time >= menu.start_time and time <= menu.end_time:
        available_menu.append(menu)
    #return list of available menus.
    return available_menu

#list of menus using the objects created previously.
menus = [brunch, early_bird, dinner, kids]

#2 instances of Francise Class
flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)

# print(flagship_store)
print(flagship_store.available_menus(1700))

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

first_business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

arepa_menu_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
#new instance of menu class
arepa_menu = Menu("Take a’ Arepa", arepa_menu_items, 1000, 2000)

#new instance of franchise class
arepas_place = Franchise("189 Fitzgerald Avenue", [arepa_menu])

# print(arepas_place.available_menus(1700))

second_business = Business("Take a' Arepa", [arepas_place])
