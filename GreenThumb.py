#from Arduino import Arduino
import csv
import os

# Below is for testing only
from random import random
def getRandomNum(min, max):
	return min + (random() * (max - min))

# Main plant class
class Plant:
	def __init__(self, name, temp, humidity, soilMoisture, light): # Load main variables and create csv file for plant
		self.__name = name
		self.__temp = temp
		self.__humidity = humidity
		self.__soilMoisture = soilMoisture
		self.__light = light
		self.__filename = "./csvFiles/" + self.__name + ".csv"
		if not os.path.exists('./csvFiles'):
			os.makedirs('./csvFiles')
		self.__writeCSVHeaders(self.__filename)

	def writeCSV(self): # write plants current values to csv
		with open(self.__filename, 'a', newline='') as csvfile:
			csvwriter = csv.writer(csvfile)
			csvwriter.writerow([self.__temp, self.__humidity, self.__soilMoisture, self.__light]) 

	def __writeCSVHeaders(self, filename): # write csv headers
		with open(self.__filename, 'w', newline='') as csvfile:
			csvwriter = csv.writer(csvfile)
			csvwriter.writerow(["Temperature", "Humidity", "Soil Moisture", "Light"]) 

	# For testing only!
	def randomizeValues(self): # Randomizes plant values
		self.__temp = getRandomNum(50,100)
		self.__humidity = getRandomNum(20,80)
		self.__soilMoisture = getRandomNum(0,100)
		self.__light = getRandomNum(3000,6000)

# board = Arduino(115200) # plugged in via USB, serial com at rate 115200

# For testing only!
plants = [Plant("Dragon Lily", getRandomNum(50,100), getRandomNum(20,80), getRandomNum(0,100), getRandomNum(3000,6000)),
		Plant("Spider Plant", getRandomNum(50,100), getRandomNum(20,80), getRandomNum(0,100), getRandomNum(3000,6000)),
		Plant("Jade Plant", getRandomNum(50,100), getRandomNum(20,80), getRandomNum(0,100), getRandomNum(3000,6000)),
		Plant("Pothos", getRandomNum(50,100), getRandomNum(20,80), getRandomNum(0,100), getRandomNum(3000,6000)),
		Plant("Asparagus Fern", getRandomNum(50,100), getRandomNum(20,80), getRandomNum(0,100), getRandomNum(3000,6000))]

for i in range(20):
	for plant in plants:
 		plant.writeCSV()
 		plant.randomizeValues()



# while True:
# 	for plant in plants:
# 		plant.writeCSV()
# 	time.sleep(300) # Wait for 5 mintues