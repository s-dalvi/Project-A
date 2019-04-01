class Car():
    def __init__(self,registration, make):
        self.__mileage__ = 0
        self.__registration__ = registration
        self.__make__ = make
        self.__dateOfInspection__ = None
        self.__year__ = (str(self.__registration__[2] + self.__registration__[3]))


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
        if self.__year__[0] == '5' or self.__year__[0] == '6':
            self.__year__= int(self.__year__)-50
        if int(self.__year__)< 17:
            return True

def menu():
    print('A. To print details')
    print('B. To check if you need a new car')
    print('X. To exit')
    choice = input('Enter option: ')
    return choice

def details(car):
    print('Your registration is: ',car.getRegistration())
    print('Your make is: ',car.getMake())
    print('Your mileage is: ',car.getMileage())
    print('Your date of inspection is: ',car.getDateOfInspection())
    
def main():
    car1 = Car('BL67 WFR', 'toyota')
    car1.setInspectionData(5000, '03/07/18')
    option = menu()
    while option != 'X':
        if option == 'A':
            details(car1)
        if option == 'B':
            if car1.needNewCar() == True:
                print('You need a new car')
            else:
                print('Your car is fine :)')
        print()
        option = menu()
    print('goodbye')
            
main ()


