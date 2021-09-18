# Monty-Hall-Problem
To be run from command line. A short and simple python script demonstrating the solution to the Monty Hall Problem.

https://en.wikipedia.org/wiki/Monty_Hall_problem

To demonstrate that switching is a better move, the script asks for a number of doors and a number of iterations to simulate. For the classic 3 door problem, running many iterations will reveal that switching is the correct choice roughly twice as often as not. Adding more doors demonstrates the solution further: when there are 10,000 doors, simulating 10,000 times will result in only about one iteration in which the initial choice was correct. 

The code is designed to show the logic behind the problem, but the if statement could be simplified to _if random.randint(1, doors) == random.randint(1, doors)_.
