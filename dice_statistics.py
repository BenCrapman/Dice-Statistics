#This program was written by Ben Chapman

#include the random library
import random
import math

#this function simulates a dice roll given an n-sided die
def roll(sides):
	return random.randint(1, sides)

#this function fills a given list with a given number of rolls
#of an n-sided die
def form_sample(times, sides, data_list):
	for i in range(times):
		data_list.append(roll(sides))

#this function returns the average value of a list
def average(data_list):
	mu = 0.0
	for i in data_list:
		mu += i
	mu /= len(data_list)
	return mu

#this function returns the standard deviation of a list
#given the average
def standard_deviation(data_list, mean):
	sigma = 0.0
	for i in data_list:
		sigma += math.fabs(i - mean)
	sigma /= len(data_list)
	return sigma

test_list = [1,1,2,2,2,2,2,200,100,50]

print str(standard_deviation(test_list, average(test_list)))
		
	

