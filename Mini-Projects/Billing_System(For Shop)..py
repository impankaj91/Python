user_name = input("enter a customer name :")
total_value = 0
while(True):
    try:
        user_input = input(" Press y to enter item or press q to exit :")
        if(user_input.lower() == 'y'):
            item_name = input("Enter the item name : ")
            item_qunt = int(input("Enter the Quntity of item :"))
            item_price = int(input("Enter the item price :"))
            print(f"{item_name} * {item_qunt} : {item_price} ")
            with open(f'{user_name}.txt', 'a') as f:
                f.write(f"{item_name} * {item_qunt} : {item_price} \n")
            total_value = total_value+item_price*item_qunt
            print(f"Total order value so far {total_value}.")
        elif(user_input == 'q'):
            with open(f'{user_name}.txt', 'a') as f:
                f.write(
                    f" Your total bill value is : {total_value}\n *****************************thanks for shopping with us*****************************")
            break
        else:
            print("please enter valid input.")
    except Exception as e:
        print("ohhhh something inappropriate you enter.")
