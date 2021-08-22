import random
import sys
import time

from dataloader import DataLoader

'''need to program:
# random generation of initial generation

- way of selecting individuals for next generation: _describe_method_

- run for 5 generations and see what we converge to'''

# we use only the first command line argument
filename = sys.argv[1]

# the file is loaded and returned as a list of lists of size 2
# the first item in the list is the value (index 0)
# the second item in the list is the weight (index 1)
data = DataLoader.load_data(filename)

# filename is of form bagsize_capacity
file_metadata = filename.split('_')
bagsize = int(file_metadata[0])
capacity = int(file_metadata[1])

amount_of_instances = 10

print("bag size = {}".format(bagsize))
print("capacity = {}".format(capacity))

def generate_binary_string_of_length_n(n):
	binary_string = ""

	for i in range(n):
		# adds 0 or 1 randomly to the end of the string
		# we do this n times
		binary_string += str(random.randint(0,1))

	return binary_string

def generate_string_of_0s_length_n_with_1_at_index(n, index):
	binary_string = ""

	for i in range(n):
		if i == index:
			binary_string += '1'
			continue
		binary_string += '0'

	return binary_string

# this will caculate the weight of an instance
def calculate_weight_of_instance(instance):
	weight = 0

	# note that activation_function range is {0,1} because instance in a binary string
	# data[index][1] refers to the weight of the item at index in the data list
	for index, item in enumerate(instance):
		activation_function = int(item)
		weight += (activation_function * int(data[index][1]))

	return weight

# this will return an initial instance below the weight capcity of the bag
def generate_initial_instance(max_time_per_instance):
	initial_instance = generate_binary_string_of_length_n(bagsize)
	
	t0 = time.time()
	while calculate_weight_of_instance(initial_instance) > capacity:
		initial_instance = generate_binary_string_of_length_n(bagsize)

		# this ensures that we only take a certain amount of time per
		if time.time() - t0 > max_time_per_instance:
			initial_instance = generate_string_of_0s_length_n_with_1_at_index(bagsize, random.randint(0, bagsize))

	return initial_instance

if __name__ == '__main__':
	initial_instances = [generate_initial_instance(0.1) for i in range(amount_of_instances)]
	print(initial_instances)
	print([calculate_weight_of_instance(instance) for instance in initial_instances])