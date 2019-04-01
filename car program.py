class Car():
    def __init__(self,registration, make):
        self.__mileage__ = 0
        self.__registration__ = registration
        self.__make__ = make
        self.__dateOfInspection__ = None

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


car1 = Car('BL68 WFR', 'toyota')
car1.setInspectionData(5000, '03/07/18')
print('Your registration is: ',car1.getRegistration())
print('Your make is: ',car1.getMake())
print('Your mileage is: ',car1.getMileage())
print('Your date of inspection is: ',car1.getDateOfInspection())
