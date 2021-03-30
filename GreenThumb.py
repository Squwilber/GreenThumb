#from Arduino import Arduino
import csv
import os
from datetime import datetime
import time

from random import random
def getRandomNum(min, max): # For testing only. Generates random number between [min, max)
	return min + (random() * (max - min))

# Main plant class
class Plant:
	def __init__(self, name, airTemp, airHumidity, soilTemp, soilMoisture, ambientLight): # Load main variables and create csv file for plant
		self.__name = name
		self.__airTemp = airTemp
		self.__airHumidity = airHumidity
		self.__soilTemp = soilTemp
		self.__soilMoisture = soilMoisture
		self.__ambientLight = ambientLight
		self.__filename = "./csvFiles/" + self.__name + ".csv"
		if not os.path.exists('./csvFiles'):
			os.makedirs('./csvFiles')
		self.__writeCSVHeaders()

	def writeCSV(self): # write plants current values to csv
		time = datetime.now()
		with open(self.__filename, 'a', newline='') as csvfile:
			csvwriter = csv.writer(csvfile)
			csvwriter.writerow([self.__airTemp, self.__airHumidity, self.__soilTemp, self.__soilMoisture, self.__ambientLight,
				time.strftime("%d/%m/%Y"), time.hour * 3600 + time.minute + time.second]) 

	def __writeCSVHeaders(self): # write csv headers
		with open(self.__filename, 'w', newline='') as csvfile:
			csvwriter = csv.writer(csvfile)
			csvwriter.writerow(["Air Temperature", "Air Humidity", "Soil Humidity", "Soil Moisture", "Ambient Light", "Date", "Time"]) 

	# For testing only!
	def randomizeValues(self): # Randomizes plant values
		self.__airTemp = getRandomNum(50,100)
		self.__airhumidity = getRandomNum(20,80)
		self.__soilTemp = getRandomNum(50,100)
		self.__soilMoisture = getRandomNum(0,100)
		self.__ambientLight = getRandomNum(3000,6000)

# board = Arduino(115200) # plugged in via USB, serial com at rate 115200

# For testing only!
plants = [Plant("Dragon Lily", getRandomNum(50,100), getRandomNum(20,80), getRandomNum(50,100), getRandomNum(0,100), getRandomNum(3000,6000)),
		Plant("Spider Plant", getRandomNum(50,100), getRandomNum(20,80), getRandomNum(50,100), getRandomNum(0,100), getRandomNum(3000,6000)),
		Plant("Jade Plant", getRandomNum(50,100), getRandomNum(20,80), getRandomNum(50,100), getRandomNum(0,100), getRandomNum(3000,6000)),
		Plant("Pothos", getRandomNum(50,100), getRandomNum(20,80), getRandomNum(50,100), getRandomNum(0,100), getRandomNum(3000,6000)),
		Plant("Asparagus Fern", getRandomNum(50,100), getRandomNum(20,80), getRandomNum(50,100), getRandomNum(0,100), getRandomNum(3000,6000))]

for i in range(20):
	for plant in plants:
 		plant.writeCSV()
 		plant.randomizeValues()



# while True:
# 	for plant in plants:
#		plant.readSensorData()
# 		plant.writeCSV()
# 	time.sleep(300) # Wait for 5 mintues