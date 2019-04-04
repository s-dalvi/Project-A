class Car():
    def __init__(self,registration, make):
        self.__mileage__ = 0
        self.__registration__ = registration
        self.__make__ = make
        self.__dateOfInspection__ = None
        self.__year__ = str((self.__registration__[2] + self.__registration__[3]))


    def getYear(self):
        if self.__year__[0] == '5' or self.__year__[0] == '6':
            self.__year__= int(self.__year__)-50
        return self.__year__
        
    def getRegistration(self):
        return self.__registration__
 
    def getMake(self):
        return self.__make__
    
    def getMileage(self):
        return self.__mileage__
    
    def getDateOfInspection(self):
        return self.__dateOfInspection__

    def setInspectionData(self, mileage, dateOfInsp):
        self.__mileage__ = mileage
        self.__dateOfInspection__ = dateOfInsp


    def needNewCar(self):
        self.getYear()
        if int(self.__year__)< 14:
            return True
        else:
            return (19-int(self.__year__))
            

def menu():
    print('1. To input new car details')
    print('2. To print details')
    print('3. To check if you need a new car')
    print('4. To view all cars')
    print('0. To exit')
    print()
    choice = input('Enter option: ')
    while True:
        try:
            choice = int(choice)
            break
        except ValueError:
            print('\nPlease enter a valid option')
            choice = input()
    return choice

def details(cars):
    print()
    allCars(cars)
    print()
    car = input('Which car do you want to check? ')
    try:
        car=cars.get(int(car))
    except ValueError:
        car=cars.get(car)
    while True:
        try:
            print('\nYour registration is: ',car.getRegistration())
            print('Your make is: ',car.getMake())
            print('Your mileage is: ',car.getMileage())
            print('Your date of inspection is: ',car.getDateOfInspection())
            break
        except AttributeError as e:
            #print(e)
            print('\nPlease enter a valid car name from the list below')
            allCars(cars)
            car = input()
            car = cars.get(car)

def allCars(cars):
    for key,value in cars.items():
        print(key ,':' ,value.getMake(),',',value.getRegistration())
    print()
                
    

def addCar():
    reg = input('Enter reg: ')
    name = input('Enter name: ')
    newCar = Car(reg,name)
    inspData = input('Set inspection data?Y or N ')
    if inspData == 'Y':
        miles = input('Enter no. of miles: ' )
        date = input('Enter date of inspection: ')
        newCar.setInspectionData(miles,date)
                  
    return name, newCar
    
def main():
    cars = 0
    car1 = Car('BL17 WFR', 'toyota aygo')
    car1.setInspectionData(5000, '03/07/18')
    carDict = {'default':car1}

    option = menu()
    while option != 0:
        if option ==1:
            name, newCar= addCar()
            cars +=1
            carDict.update({cars: newCar})
        if option == 2:
            details(carDict)
        if option == 3:
            if car1.needNewCar() == True:
                print('You need a new car')
            else:
                remainingYrs = car1.needNewCar()
                print('Your car is fine: You have',remainingYrs,'years remaining')
        if option == 4:
            allCars(carDict)
        print()
        option = menu()
    print('goodbye')
            
main ()


