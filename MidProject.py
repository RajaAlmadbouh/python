
import random
print(30 * "-", "Welcome to FasterTaxi", 30 * "-")

while True:
    chooseType = input("""You can choose the type of service : 
                       1- Taxi 
                       2- Shared transfer
                       Enter the ID number for the service type : """)
    print()

    if chooseType == "1" or chooseType.lower() == "taxi":
        print("Taxi")
        print()
        captain = [["Toyota Avalon", "Raja Almadbouh", "80081", "0796329390"],
                   ["Chevrolet Menlo", "Montasr Asmer", "17785", "0772182104"]]

        print("Choose the type of car you prefer : ")

        for i in range(0, len(captain)):
            print(f"{i + 1}- {captain[i][0]}")
        
        print()

        while True:
            chooseCaptain = input("Enter the ID number for the Car type : ")

            if chooseCaptain == "1" or chooseCaptain == "2":
                print("{:<15}\t{:<15}\t{:<15}\t{:<15}".format("CarType", "NameCaptain", "PlateNumber", "NumberCaptain"))
                for i in range(0, len(captain[int(chooseCaptain) - 1])):
                    print("{:<15}\t".format(captain[int(chooseCaptain) - 1][i]), end="")
                print()
                print()
                print("""Do you want :
 1- Open flight
 2- trip (repel reply)""")
                print()
                priceKilo = 0.2
                priceTime = 0.05
                while True:
                    chooseUser = input ("Enter the ID number what you want : ")
                    if chooseUser == "1" :
                        print("Open flight \n ")
                        print ("Price per kilo   = ",priceKilo," JD")
                        print ("Price per minute = ",priceTime," JD")
                        print("\n")
                        while True:
                            try:
                                numKilo = float(input("Enter the number of kilometers the user traveled on this trip : "))
                                numTime = float(input("Enter the number of minutes the user traveled on this trip    : "))

                                if numKilo < 0 or numTime < 0:
                                    print("Please enter non-negative values for kilometers and minutes.")
                                    continue  

                                break  

                            except ValueError:
                                print("Invalid input. Please enter valid numerical values.")
                        priceTrip = numKilo*priceKilo + numTime*priceTime
                        print("\n")

                        if priceTrip < 1 :
                            priceTrip = 1
                            print("Minimum trips = 1 JD")

                        print("We wish you a happy trip with captain ",captain[int(chooseCaptain) - 1][1])
                        print("Total price of the trip = ",priceTrip," JD")
                        break
                    elif chooseUser == "2":
                        print("trip (repel reply) \n")

                        print("Note : To activate this service correctly, the trip must exceed a distance of 10 km")
                        print(f"(repel : The price starts at {priceKilo} km and {priceTime} minutes until the end of the first location)")
                        print("The writer takes 40% percent of the value of the first trip")

                        try:
                            print()
                            numKilo1 = float(input("Enter the number of kilometers the user traveled on the first trip:"))
                            numKilo2 = float(input("Enter the number of kilometers the user traveled on the second trip:"))
                            numTime1 = float(input("Enter the number of minutes the user traveled on the first trip    : "))
                            numTime2 = float(input("Enter the number of minutes the user traveled on the second trip   : "))
                            trailingTime = 0
                            trailingSpace = 0


                            if numKilo1 < 0 or numTime1 < 0 or numKilo2 < 0 or numTime2 < 0:
                                    print("Please enter non-negative values for kilometers and minutes.")
                                    continue  
                            
                            if numKilo1 < 10:
                                priceTrip = priceKilo*(numKilo1+numKilo2) + priceTime*(numTime1+numTime2)
                                print(priceTrip)
                                break
                            else:
                                if numKilo1 == numKilo2 or numKilo1 > numKilo2:
                                    priceTripKilo = numKilo1*priceKilo 
                                    priceTripKilo += priceTripKilo*0.4
                                elif numKilo1 < numKilo2 :
                                    trailingSpace = numKilo2 - numKilo1
                                    priceTripKilo = numKilo1*priceKilo + (numKilo1*priceKilo)*0.4 + trailingSpace*priceKilo 
                                    
                                
                                if numTime1 == numTime2 or numTime1 > numTime2:
                                    priceTripTime = numTime1*priceTime
                                    priceTripTime += priceTripTime*0.4
                                elif numTime1 < numTime2 : 
                                    trailingTime = numTime2 - numTime1
                                    priceTripTime = numTime1*priceTime + (numTime1*priceTime)*0.4 + trailingTime*priceTime
                                
                                priceTrip = priceTripKilo + priceTripTime
                                
                                print("Distance traveled (repel)             : ",numKilo1 , "KM => ",round(numKilo1*priceKilo,2),"JD")
                                if trailingSpace > 0:
                                    print("Trailing distance (out of bounds)     : ", trailingSpace,
                                          "KM =>", trailingSpace * priceKilo, "JD")
                                print("Distance traveled (reply)             : ",numKilo2 , "KM => ",round((numKilo1*priceKilo)*0.4,2),"JD")


                                print("time cut off (reply)                  : ",int(numTime1) , "Minutes =>",round(numTime1*priceTime,2),"JD")
                                if trailingTime > 0:
                                    print("Excessive time (out of bounds)        : ",int(trailingTime),"Minutes =>",round(trailingTime*priceTime,2),"JD")
                                print("time cut off (reply)                  : ",int(numTime2) , "Minutes => ",round((numTime1*priceTime)*0.4,2),"JD")

                                print("                                     ----------------------------------Total\n",
                                      "                                       Total = ",priceTrip)
                                 
                        except ValueError:
                                print("Invalid input. Please enter valid numerical values.")


                        break
                    else:
                        print("Choose wrong. You must enter a valid ID")
                      

                break
            else:
                print("Choose wrong. You must enter a valid ID")

        break
    elif chooseType == "2" or chooseType.lower() == "shared transfer":
        print("Shared transfer")

        places = {"Amman" : [ ["Toyota Avalon", "Raja Almadbouh", "80081", "0796329390",random.randint(1, 3)],
                              ["Chevrolet Menlo", "Montasr Asmer", "17785", "0772182104",random.randint(1, 3)] ],

                  "Irbid" : [ ["Fox ID4", "Mahmood AboDhase", "80044", "0755644887",random.randint(1, 3)],
                              ["Toyota Camry", "Osama Owadate", "14465", "0793746845",random.randint(1, 3)] ] }
        count = 0
        print("Choose the place you want to go to : ")
        for i in places.keys():
            count += 1
            print(count," - ",i)

        while True:
            chooseUser = input("Enter the ID number place you want to go to : ")
            
            if chooseUser == "1" or chooseUser == "Irbid" or chooseUser == "2" or chooseUser == "Amman" :
                if chooseUser == "1":
                    chooseUser = "Irbid"
                elif chooseUser == "2":
                    chooseUser = "Amman"
                
                print("")
                for i in range(len(places[chooseUser])):
                    print(i+1,"- ",places[chooseUser][i][0])
                    print("Number of seats reserved = ",places[chooseUser][i][4],"  ","Number of empty seats    = ",4-places[chooseUser][i][4])
                    print()
                
                while True:
                    chooseCar = input("Choose the type of car you prefer : ")

                    if 1 <= int(chooseCar) <= len(places[chooseUser]):
                        chosseCarInfo = places[chooseUser][int(chooseCar) - 1]
                        
                        print("\nChosen Car Information:")
                        print("Car Type             :", chosseCarInfo[0])
                        print("Driver               :", chosseCarInfo[1])
                        print("Plate Number         :", chosseCarInfo[2])
                        print("Driver's Phone Number:", chosseCarInfo[3])
                        #print("Reserved Seats:", chosenCarInfo[4])
                        print("Empty Seats          :", 4 - chosseCarInfo[4])

                        #numSeat = 0

                        while chosseCarInfo[4] < 4:
                            while True:
                                try:
                                    numSeat = int(input("Enter the number of seats you will reserve: "))
                                    
                                    if 0 < numSeat <= (4 - chosseCarInfo[4]):
                                        chosseCarInfo[4] += numSeat
                                        print("Reservation successful.")
                                        print(f"Total reserved seats: {chosseCarInfo[4]}")
                                        
                                        if chosseCarInfo[4] == 4:
                                            print("The number of seats is complete")
                                            print(f"Seat price for {numSeat} seats = {numSeat * 4} JD")
                                        break
                                    else:
                                        print(f"Invalid input. Please enter a number between 1 and {4 - chosseCarInfo[4]}.")
                                except ValueError:
                                    print("Invalid input. Please enter a valid number.")

                            if chosseCarInfo[4] < 4:
                                another_reservation = input("Do you want to make another reservation? (yes/no): ").lower()
                                if another_reservation != 'yes':
                                    break

                        if chosseCarInfo[4] == 4:
                            print("All seats are reserved.")
                            print(f"Total price for all reserved seats: {chosseCarInfo[4] * 4} JD")
                        break
                    else:
                        print("Choose wrong. You must enter a valid ID")
                break
            else :
                print("Invalid input. Please enter crrouct ID number of car.")
        break
    else:
        print("Invalid input. Please enter 1 for Taxi or 2 for Shared transfer.")