def order():
    print("Hi! WELCOME TO OUR SHOP.")
    user_input = str(input("What would you like to order? "))

    # Checking if the user wants pizza
    if user_input.lower() == "pizza":
        toppings = str(input("What topping would you like to add? (mushrooms, onions, cheese) "))

    
        if toppings.lower() == "mushrooms" or toppings.lower() == "onions" or toppings.lower() == "cheese":
            print(f"Your pizza with {toppings} is ready!")
        else:
            print("Sorry, we don't have that topping.")

    if user_input.lower() == "burger" :
        drinks = str(input("What side drink would you like to order? (pepsi, coca cola, fanta) "))
        print("Your order will be ready in 15 minutes.")

    elif user_input == "burger" :
        print("sorry!we don't have that drinks. ")   

    if user_input == "pizza" :
        print("Your bill would be Rs 700/- ")

    elif user_input == "burger":
        print("Your bill would be Rs 300/-")  
    else:
        print("We only sell pizza and burger.")     


order()          
             
    
    


                           
    

   