# Assignment #2
# INF1340 Section 1
# Fall-2017
# Fenghe Liu
inventory=[]
Content=["model number","year","colour","make","model","body type","quantity"]
space=[7,5,10,15,15,14,1]
def menu(inventory_size):
    '''(int) -> str
    Returns a string of user's menu selection.
    Prints the full menu if inventory_size is not zero.
    Prints the menu option 1 and Quit if inventory_size is zero.
    '''
    print ("\nCar Inventory Menu\n"+"="*18)
    if inventory_size==0:
        print("\n1- Add a car\nQ- Quit")
    else:
        print("\n1- Add a car\n2- Remove a Car\n3- Find a Car\n4- Show complete Inventory\nQ- Quit")
    user_choice=input("\nEnter your selection:")
    return user_choice
    
def find_index(inventory, model_number, year, colour):
    '''(list, str, int, str) -> int
    Returns the index of the car of the inventory with a matching model_number, year and colour,
    as an int.
    Returns -1 if	the car is not found.
    '''
    for i in range(len(inventory)):
        if inventory[i][0]==model_number and inventory[i][2]==colour and inventory[i][1]==year:  
            return i
    return -1
def add_car(inventory):
    '''(list) -> None
    Adds	a car to	the inventory	if and only if a car with 
    the same model number, year, and colour is not	 already	part	of
    the inventory.If a car with	the	same	model number,	year, and	 colour is already	
    part of the inventory, the function asks the user the quantity to be added
    and increases the current quantity accordingly.	
    '''
    model_number=input("Enter the model number: ")
    year=input("Enter the year: ")
    colour=input("Enter the colour:")
    search_result=find_index(inventory, model_number, year, colour)
    if search_result!=-1:
        print ("\nCar already exists in inventory.")
        addednumber=input("Enter the quantity to be added: ")
        inventory[search_result][-1]+=int(addednumber)
        print ("Increased quantity by %s. New quantity is: %d"%(addednumber,inventory[search_result][-1]))
    else:
        new_car=[]
        made=input("Enter the make: ")
        model=input("Enter the model: ")
        body_type=input("Enter the body type: ")
        quantity=int(input("Enter the quantity: "))
        new_car.extend([model_number,year,colour,made,model,body_type,quantity])
        inventory.append(new_car)
        print ("\nNew car successfully added\n")
    
def remove_car(inventory):
    '''(list) -> None 
    Removes a	car from	the inventory	if and only if the	 car quantity	is one.
    If the car quantity is	greater than one, it decreases the quantity of the car by one.	
    '''
    model_number=input("Enter the model number: ")
    year=input("Enter the year: ")
    colour=input("Enter the colour: ")
    search_result=find_index(inventory,model_number,year,colour)
    if search_result==-1:
        print ("\nCar not found!Cannot remove car!")
    elif inventory[search_result][-1]==1:
        inventory.pop(search_result)
        print("\nCar removed from inventory.")
    else:
        inventory[search_result][-1]-=1
        print("\nDecreased quantity by 1. New quantity is: %s"%(inventory[search_result][-1]))
    
def find_car(inventory):
    '''（list）-> None
        Find	a car by	Model Number,	by Make,	by Model,	or by Body Type.
    	   If the car is part of the inventory, prints the car data,tab-delimited
        on the same line.If	the car is not part of	the	inventory, the function prints	
        the message:“No cars found!”.
    '''
    
    print ("\nSearch Menu\n"+"="*18)
    print("\n1- Search by Model Number\n2- Search by Make\n3- Search by Model\n4- Search by Body Type")
    user_c=input("\nEnter your selection: ")
    choices=["model number","make","model","body type"]
    result=[]
    while int(user_c) not in range(1,5):
        print ("Wrong selection, try again！")
        user_c=input("\nEnter your selection: ")
            
    if int(user_c) in range(1,5):
        keyword=input("Enter the %s: " % (choices[int(user_c)-1]))
        print ()
        for i in range(len(inventory)):
            if keyword==inventory[i][Content.index(choices[int(user_c)-1])]:
                result.append(inventory[i])
        if len(result)!=0:
            for i in range(len(result)):
                for j in range(len(result[i])-1):
                    print (result[i][j]+(space[j]-len(result[i][j]))*" ",end="")
                print (result[i][-1])
                print ()
        else:
            print ("No cars found!")   

def show_inventory(inventory):
    '''(list) -> None
    	Prints all car data, tab-delimited, one car per line.
    '''
    print("\nComplete Inventory:\n"+"="*18+"")
    for i in range(len(inventory)):
                    for j in range(len(inventory[i])-1):
                        print (inventory[i][j]+(space[j]-len(inventory[i][j]))*" ",end="")
                    print (inventory[i][-1])
                    print ()
    
def main():
    choice=menu(len(inventory))
    while choice!="Q" and choice!="q":
        if len(inventory)==0:
            while choice!="1" and choice!="Q" and choice!="q":
                print ("\nWrong selection, try again!\n\n")
                choice=menu(len(inventory))
            if choice=="1":
                add_car(inventory)
            else:
                break
        else:
            while choice!="Q" and choice!="q" and int(choice) not in range(1,5):
                print ("\nWrong selection, try again!\n\n")
                choice=menu(len(inventory))            
            if choice=="1":
                add_car(inventory)
            elif choice=="2":
                remove_car(inventory)
            elif choice=="3":
                find_car(inventory)
            elif choice=="4":
                show_inventory(inventory)
        choice=menu(len(inventory))
    print ("Goodbye!")
    
        
main()
        
           