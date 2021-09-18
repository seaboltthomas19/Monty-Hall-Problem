# Monty-Hall-Problem
To be run from command line. A simple python script demonstrating the solution to the Monty Hall Problem.

https://en.wikipedia.org/wiki/Monty_Hall_problem

To demonstrate the solution, that switching is always a better mofve, the script asks for a number of doors and a number of iterations to simulate. For the classic 3 door problem, running a thousand iterations will reveal a roughly 2:1 split in which switching is the correct choice 2/3 times. Adding more doors demonstrates the solution further; when there are 10,000 doors, simulating 10,000 times will typically only result in roughly one iteration in which the initial choice was correct. 

The code is designed to clearly show the logic behind the problem, which is why the if statement has not been simplified to _if random.randint(1, doors) == random.randint(1, doors)_.
