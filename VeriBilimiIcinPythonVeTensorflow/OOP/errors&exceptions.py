while True:
    try:
        myInt = int(input("Enter your number: "))
    except:
        print("Please enter a number!")
        continue
    else:
        print("Thank you!")
        break
    finally:
        print("finally called")
