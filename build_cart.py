# 1) Build a Shopping Cart
# You can use either lists or dictionaries. The program should have the following capabilities:

# 1) Takes in input
# 2) Stores user input into a dictionary or list
# 3) The User can add or delete items
# 4) The User can see current shopping list
# 5) The program Loops until user 'quits'
# 6) Upon quiting the program, print out all items in the user's list




def cart_info(item,num_items,shopping_cart):
    shopping_cart[item] = num_items


def cart_responses():
    shopping_cart = {}
    while True:
        user_process = input('\nDo you want to buy stuff today? Type either of the following:add/remove/quit: ')   
        if user_process == 'add':
            item = input('\nWhat do you want to add to your cart? ')
            num_items = input('\nHow many do you want to add? ')
            cart_info(item,num_items,shopping_cart)
            print(f"\nHere are your current items and their quanity: {shopping_cart}")           
        elif user_process == 'remove':
            if shopping_cart:
                item = input('\nWhat do you want to remove ')
                del shopping_cart[item]
                print(f"\nYou have removed your {item} ")
            else:
                print(f"You have nothing in your cart.:(")
        elif user_process == 'quit':
            break

    print(f"\nHere's what you have in your cart!{shopping_cart}")
    
cart_responses()

