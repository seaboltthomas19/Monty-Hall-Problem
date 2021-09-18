import random

switch_was_correct = 0
no_switch_was_correct = 0

print("====================================" +
      "\n" +
      "*** Monty Hall Problem Simulator ***" +
      "\n" +
      "====================================")

print("Doors to choose from: ")
doors = int(input())
print("Iterations to run: ")
iterations = int(input())

for i in range(0, iterations):
    door_array = list(range(1, doors + 1))  # make a list of every door

    # select a correct door at random; this will simulate the door with a prize behind it
    correct_door = random.randint(1, doors)

    # select an initial choice at random; this will simulate the door the contestant has chosen initially
    initial_choice = random.randint(1, doors)

    if initial_choice == correct_door:  
        no_switch_was_correct = no_switch_was_correct + 1
    else: 
        switch_was_correct = switch_was_correct + 1

print("Results: \n")
print("Switching was correct " + str(switch_was_correct) + " times.\n")
print("The initial choice was correct " +
      str(no_switch_was_correct) + " times.")
