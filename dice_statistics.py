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
	#populate the list with rolls
	for i in range(times):
		data_list.append(roll(sides))

#this function takes a list of lists, each list containing the same number of elements.
#it takes the highest element out of each list and stores it into a seperate list
def advantage(list_of_lists, list_length):
	#remove previous data from results_list
	results_list = []
	
	#fill the results list with 1's
	for i in range(list_length):
		results_list.append(1)
	#iterate through all of the lists in list_of_lists
	for element in list_of_lists:
		#iterate through this particular list
		#replace the corresponding result with this value
		#if this value is greater than the corresponding result
		for i in range(list_length):
			if element[i] > results_list[i]:
				results_list[i] = element[i]
	return results_list

def create_rolls(num_dice, sides, num_rolls, results_list):
	#iterate through the number of dice we want to roll each time
	for i in range(num_dice):
		#create seperate lists for each roll, add them to results_list
		temp_rolls = []
		form_sample(num_rolls, sides, temp_rolls)
		results_list.append(temp_rolls)
		

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

#declare variables
number_rolls = 0;
dice_sides = 0;
sample_size = 0;
final_sample = []
group_of_rolls = []
mu = 0.0
sigma = 0.0

#talk to the user
print 'This program simulates the rolling of multiple dice, where the highest value is always taken'
print 'Given a number of sides and number of rolls, it can return the average roll and standard deviation in rolls'
print '\n'

number_rolls = int(raw_input('number of rolls: '))
dice_sides = int(raw_input('number of sides: '))
sample_size = int(raw_input('sample size: '))

print '\n'

#fill group of rolls with samples, each with a number of rolls equal to sample size, with a dice_sides sided die
create_rolls(number_rolls, dice_sides, sample_size, group_of_rolls)

#calculate the roll sample when these roll samples are put together with advantage
final_sample = advantage(group_of_rolls, sample_size)

#calculate average and standard deviation
mu = average(final_sample)
sigma = standard_deviation(final_sample, mu)

#and then print them
print 'average roll: ' + str(mu)
print 'standard deviation: ' + str(sigma)
print '\n'
