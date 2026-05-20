#----------------------------------------------------------------------------------------------------
def SI_Calc(principal,interest,time):
    Simple_interest=(principal*interest*time)/100
    Total=principal+Simple_interest
    print(f"The Simple interest is {Simple_interest} and along with principal amount it is {Total}")
#----------------------------------------------------------------------------------------------------
while True:
    print("\n=========== Simple Interest Calculator ===========\n")
    print("1.Simple Interest\n2.Exit\n")
    choice=int(input("Enter (1-2):"))
    if choice==1:
        principal=float(input("Enter Principal Amount in Rupees:"))
        interest=float(input("Enter Interest in %:"))
        time=float(input("Enter Time in Years:"))
        SI_Calc(principal,interest,time)
    elif choice==2:
        print("Exiting Program...")
        print("Exit Successful!")
        break
    else:
        print("Invalid Choice!")   
#-------------------------------------------------------------------------------------------------------        