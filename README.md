# Genetic-algorithm
**Genetic algorithm library written in python** 

> Genetic algorithm is an evolutionary algorithm that can be utilized to find optimal solutions.Here the program is solving the one-max problem where the overall objective is to get all one in a n-bit strings containing only 0 and 1.It can also solve the rastrigin problem but it was fine-tuned only for 16-bit strings not for a n-bit string.

**How it works**
- Create initial population
- Perform fitness evaluation
- Perform selection
- Perform mutation and crossover operations
- Create next population

**Selection**
- It can work with tournament selection
- It can use fitness proportional selection

**Crossover**
- Works with k-point crossover(k number of points).
- Obtain the next population until generation count ends.
- All the parameters such as generation,population size,probability of crossover,probability of mutation can all be tweaked in the code.
