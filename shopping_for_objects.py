class Item(): ###This is just a class to create the options that could be in the cart. A dictionary would be more efficient, but I wanted to practice objects.
    def __init__(self, name, cost, availability = True):
        self.name = name
        self.cost = cost
        self.availability = availability

lion = Item('lion', 50, True) ###I manually made the items in the list this way. If I have more time, I might add functionality---
tiger = Item('tiger', 500, True) ###---to allow the user to request items to be added.
bear = Item('bear', 5000, True)
home = Item('Kansas', 50000, False)
#######This section was how I once tried to define the items, but it wasn't working.#######
# lion = {'name': 'lion', 'cost': 50, 'availability': True}
# tiger = {'name': 'tiger', 'cost': 500, 'availability': True}
# bear = {'name': 'bear', 'cost': 5000, 'availability': True}
# home = {'name': 'home', 'cost': 50000, 'availability': False}

discount_codes = {'dorothy': 100, 'toto': 75, 'scarecrow': 50, 'tinman': 25, 'wicked': -100} ###The user can put in discount codes later.

class Cart():
    def __init__(self, items, cost_sum, total_availability, discount, code_in_use): ###The cart has these attributes.
        self.items = items
        self.cost_sum = cost_sum
        self.total_availability = total_availability
        self.discount = discount
        self.code_in_use = code_in_use

    # def define_Cart(self): ###I wasn't sure how to make items a list, cost_sum an integer, etc., so I defined it here.
    #     self.items = []    ###Upon further thought, I could have set the parameters of __init__ equal to these. I adjusted that.
    #     self.cost_sum = 0
    #     self.total_availability = 0
    #     self.discount = 0
    #     self.code_in_use = ''

    def add_item(self):
        print('=' * 60)
        item = input("\nWould you like to add a lion, a tiger, a bear, or a home?" )
        if item == 'lion': ###This was my final workaround. I think it's SO dumb I have to do it this way.
            item = lion
        elif item == 'tiger':
            item = tiger
        elif item == 'bear':
            item = bear
        elif item == 'home':
            item = home
        self.items.append(item.name)
        self.cost_sum += item.cost
        if item.availability == True:
            self.total_availability += 1
        else:
            input("\nThis item is currently unavailable, but will ship when it comes back in stock.")
    
    def remove_item(self):
        print('=' * 60)
        item = input("\nWhat would you like to remove from your cart? ")
        if item == 'lion': ###This was my final workaround. I think it's SO dumb I have to do it this way.
            item = lion
        elif item == 'tiger':
            item = tiger
        elif item == 'bear':
            item = bear
        elif item == 'home':
            item = home
        if item['name'] in self.items:
            self.items.remove(item.name)
            self.cost_sum -= item.cost
            if item.availability == True:
                self.total_availability -= 1
            input(f"\nOne {item['name']} has been removed from your cart.")
        else:
            input("\nThat item is not in your cart.")
    
    def apply_discount(self): ###This tells the user their discount amount, and applies it to the cost_sum.
        
        print('=' * 60)
        code = input("\nWhat is your discount code? ")
        if code in discount_codes.keys() and code != self.code_in_use: ###This checks to make sure it's a valid code.
            self.discount = discount_codes[code]
            if code == 'dorothy':
                input("\nThose ruby slippers grant you every item for free!")
            elif code == 'toto':
                input("\nYou'll get your items, my pretty. And for little price, too!")
            elif code == 'scarecrow':
                input("\nIt was smart of you to use that code. That's half off!")
            elif code == 'tinman':
                input("\nWe'll give you a quarter off your price. We're not heartless!")
            elif code == 'wicked':
                input("\nHow dare you invoke that name here! I'm doubling your price!")
        elif code == self.code_in_use:
            input("\nI'm sorry, each code may only be used once.")
        else:
            input("\nI'm sorry, that's not a valid code.")
    
    def show_cart(self):
        print('=' * 20 + "\n___YOUR SHOPPING CART___\n" + '=' * 20)
        printed = [] ###I made this list to make sure things were not printed more than once.
        for i in self.items:
            if i not in printed:
                print(f'• {i} [x{self.items.count(i)}]')
                printed.append(i)
        print('=' * 20 + "\nTotal Cost = ", end='')
        if self.discount == 0:
            print('$' + str(self.cost_sum))
        else:
            old_price = ''
            for i in str(self.cost_sum):
                old_price = old_price + i + '\u0336' ###I found this sucker on stack overflow.
            print('$' + old_price + '  $' + str(self.cost_sum - self.cost_sum / 100 * self.discount))
        print('=' * 50 + "\nNumber of packages that can immediately ship: " + str(self.total_availability) + " out of " + str(len(self.items)))
        input('=' * 50)

cart = Cart([], 0, 0, 0, '')
input("Welcome to Ozazon. Throughout the program, hit 'Enter' to continue along the Yellow Brick Road.")
while True: ###I'm using the type of format Jesse made to 'gamify' the process.
    print("=" * 60 + "\nWhat would you like to do?\n" + "=" * 60)
    print("""•Type 'add' to add an item.
    ---------------------------------
    •Type 'remove' to remove an item.
    ---------------------------------
    •Have a discount code? Type 'discount.'
    ---------------------------------
    •Type 'cart' to see your cart.
    ---------------------------------
    •Type 'quit' to checkout. You must pay for whatever is in your cart.""")
    print("=" * 60)
    response = input().lower()
    if response == 'add':
        cart.add_item()
    elif response == 'remove':
        cart.remove_item()
    elif response == 'discount':
        cart.apply_discount()
    elif response == 'cart':
        cart.show_cart()
    elif response == 'quit':
        break
    else:
        input("\nI'm sorry, I didn't understand your request.")

print("\nThank you for shopping! Your animals and bill will be forcefully delivered soon.")