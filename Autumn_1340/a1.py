#INF 1340 Section 0101
#Fall-2017
#FENGHE LIU


#Constant
ZONE1_BEGIN=0
ZONE1_END=30
ZONE2_BEGIN=ZONE1_END+1
ZONE2_END=60
ZONE3_BEGIN=ZONE2_END+1
ZONE3_END=90
LIGHT_VEICHLE_CHARGE=0.4085
HEAVY_VEICHLE_CHARGE=0.8175
ENTRY_FEE=1.25
CAMERA_FEE=4.15
ZONE2_SURCHARGE=1.27
TAXES=1.13

#Main function
def main():

    display_instructions()
    entry=int(input("\nEnter the entry marker: "))
    exitd=int(input("Enter the exit marker: "))
    vehicle=input("Enter your vehicle type (L)ight or (H)eavy: ")
    transponder=(True if input("Do you have a transponder (Y)es or (N)o: ").upper()=="N" else False)
    trip=calculate_toll_charge(entry, exitd, vehicle)
    total_bill=calculate_total_bill(trip,transponder)
    print ("\nTotal due is: ",total_bill)
    


#Functions
def display_instructions():
    ''' () -> None
    Displays the instructions of the whole program to the screen
    '''
    print ('''This program calculates the toll charges for a paid highway.
Light vehicles will be charged at a rate of 0.4085 cent per km. Heavy
vehicles will be charged at a rate of 0.8175 cent per km.
There are three travelling zones as follow:
    
     -Zone 1: from km marker 0 to marker 30.
     -Zone 2: from km marker 31 to marker 60.
     -Zone 3: from km marker 61 to marker 90.

There will be a surcharge of 27% to travel in Zone 2.
Each trip will be charged a highway entrance fee of $1.25.
Vehicles without a rental transponder will be charged an additional
camera recording fee of $4.15.
All applicable Ontario taxes (13%) will be added to the total.''')

def determine_zone(marker):
    '''(int) -> int
    Return the determined zone number according to the marker as an int.
    >>>detmermine_zone(28)
    1
    >>>determine_zone(33)
    2
    >>>determine_zone(57)
    3
    '''

    if marker in range(0,ZONE2_BEGIN):
        return 1
    elif marker in range(ZONE2_BEGIN,ZONE3_BEGIN):
        return 2
    else:
        return 3


def calculate_toll_charge(entry, exit, vehicle):
    '''(int,int,str) -> float
    Return the toll charge as a float according to the given customer's entry marker,exit marker,
and the vehicle type.
    >>>calculate_toll_charge(66,88,'L')
    8.987
    >>>calculate_toll_charge(6,52,'H')
    42.46095
    '''
    toll_c=0
    trip=0
    start=min(entry,exit)
    end=max(entry,exit)
    zone_s=determine_zone(start)
    zone_e=determine_zone(end)
    vehicle=vehicle.upper()
    if zone_e==1 or zone_s==3:
        trip+=end-start
    elif zone_e==2 and zone_s==1:
        trip+=(end-ZONE2_BEGIN+1)*ZONE2_SURCHARGE+(ZONE1_END-start)
    elif zone_s==zone_e==2:
        trip+=(end-start)*ZONE2_SURCHARGE
    elif zone_s==2 and zone_e==3:
        trip+=(end-ZONE3_BEGIN+1)+(ZONE2_END-start)*ZONE2_SURCHARGE
    else:
        trip+=(end-ZONE3_BEGIN+1)+(ZONE1_END-start)+(ZONE1_END-ZONE1_BEGIN)*ZONE2_SURCHARGE
    if vehicle=="L":
        toll_c=trip*LIGHT_VEICHLE_CHARGE
    else:
        toll_c=trip*HEAVY_VEICHLE_CHARGE
        
    return toll_c
        


def calculate_total_bill(trip, transponder):
    '''(float,bool) -> float
    Return total bill as a floar according to the toll charges and whether the customer has a transponder or not
    as a bool.
    >>>calculate_total_bill(8.987,True)
    $11.57
    >>>calculate_total_bill(42.46095,False)
    $49.39
    '''
    trip+=ENTRY_FEE
    
    if transponder==True:
        trip+=CAMERA_FEE
        print ('''NOTE: Since you do not own a transponder, you will be required to pay
an additional camera recording fee of $4.15.''')
    trip*=TAXES
    
    return "$%s"%(round(trip,2))



#Invoke the main function
main()