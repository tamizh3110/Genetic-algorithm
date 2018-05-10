import random
import numpy as npy
import math

POPULATION_SIZE=100
GENERATION_SIZE=100
PROBOFMUTATION=0.05
PROBOFCROSSOVER=0.7
PERLOCUSPROBCROSSOVER=0.5
class population:

    def __init__(self,pop,fitpop,tourpop,newpop):
        self.pop=pop          ##this is the population array
        self.fitpop=fitpop    ##this is the fitness array of each chromosome in the population
        self.tourpop=tourpop  ##this is an array created after the tournament selection is done for the population
        self.newpop=newpop    ##this is the next generation based population

    def createchromosome(self,CHROMOSOMAL_LENGTH):
        '''
        this function is used to create a chromosome containing binary strings
        '''
        gene_encoding = ''
        for i in range(CHROMOSOMAL_LENGTH):
            gene_encoding += str(random.randint(0,1))
        return gene_encoding

    def createsymbolicchromosome(self,CHROMOSOMAL_LENGTH):
        '''
        this function is used to create a chromosome containing symbolic characters
        '''
        gene_encoding=''
        for i in range(CHROMOSOMAL_LENGTH):
            gene_encoding+=chr(random.randint(65,122))
        return gene_encoding

    def addpopulation(self,CHROMOSOMAL_LENGTH):
        '''
        this function basically calls the createchromosome function and retrieves the returned value and adds it to
        the self.pop array(population array)
        '''
        self.pop.append(self.createchromosome(CHROMOSOMAL_LENGTH))
        return self.pop

    def measurefitness(self,population):
        '''
        this function will measure the fitness of each chromosome(BINARY) in the population
        and adds the value to the self.fitpop(fitness array)
        '''
        for go in population:
            fitvalue = 0
            for i in range(len(go)):
                if go[i] == '1':
                    fitvalue += 1
                elif go[i] == '0':
                    fitvalue += 0
            self.fitpop.append(fitvalue)


    def binarymutation(self,chromosome):
        '''
        this function will take a chromosome as the input and will perform the binary mutation operation
        '''
        temp = list(chromosome)
        for i in range(len(temp)):
            if random.random() <= PROBOFMUTATION:
                if temp[i] == '0':
                    temp[i] = '1'
                elif temp[i] == '1':
                    temp[i] = '0'
        return ''.join(temp)


    def symbolicmutation(self,chromosome):
        '''
        this function will take a chromosome as the input and will perform the symbolic mutation operation
        '''
        temp = list(chromosome)
        for i in range(len(temp)):
            if random.random() <= PROBOFMUTATION:
                temp[i]=chr(ord(temp[i])+1)
        return ''.join(temp)

    def k_pointcrossover(self, c_point, chromosome_one, chromosome_two, CHROMOSOMAL_LENGTH):
        '''
        this function will take the crossover points,two chromosomes,chromosome length as arguments and performs k-point crossover
        '''
        crossoverarray = []
        if random.random() <= PROBOFCROSSOVER:
            for i in range(c_point):
                random_point = random.randint(0, CHROMOSOMAL_LENGTH - 1)
                if random_point in crossoverarray:
                    random_point = random.randint(0, CHROMOSOMAL_LENGTH - 1)
                    crossoverarray.append(random_point)
                else:
                    crossoverarray.append(random_point)
            sortedarray = sorted(crossoverarray)
            print sortedarray
            lengthsorted = len(sortedarray)
            crossonechromo = ''
            crosstwochromo = ''

            if lengthsorted == 1:
                crossonechromo += chromosome_one[:sortedarray[0]] + chromosome_two[sortedarray[0]:]
                crosstwochromo += chromosome_one[:sortedarray[0]] + chromosome_two[sortedarray[0]:]

            elif lengthsorted % 2 != 0:
                crossonechromo += chromosome_one[:sortedarray[0]]
                crosstwochromo += chromosome_two[:sortedarray[0]]
                for j in range(len(sortedarray)):
                    if j == lengthsorted - 1:
                        crossonechromo += chromosome_two[sortedarray[lengthsorted - 1]:]
                        crosstwochromo += chromosome_one[sortedarray[lengthsorted - 1]:]
                    elif j % 2 == 0:
                        crossonechromo += chromosome_two[sortedarray[j]:sortedarray[j + 1]]
                        crosstwochromo += chromosome_one[sortedarray[j]:sortedarray[j + 1]]
                    elif j % 2 != 0:
                        crossonechromo += chromosome_one[sortedarray[j]:sortedarray[j + 1]]
                        crosstwochromo += chromosome_two[sortedarray[j]:sortedarray[j + 1]]

            elif lengthsorted % 2 == 0:
                crossonechromo += chromosome_one[:sortedarray[0]]
                crosstwochromo += chromosome_two[:sortedarray[0]]
                for j in range(len(sortedarray)):
                    if j == lengthsorted - 1:
                        crossonechromo += chromosome_one[sortedarray[lengthsorted - 1]:]
                        crosstwochromo += chromosome_two[sortedarray[lengthsorted - 1]:]
                    elif j % 2 == 0:
                        crossonechromo += chromosome_two[sortedarray[j]:sortedarray[j + 1]]
                        crosstwochromo += chromosome_one[sortedarray[j]:sortedarray[j + 1]]
                    elif j % 2 != 0:
                        crossonechromo += chromosome_one[sortedarray[j]:sortedarray[j + 1]]
                        crosstwochromo += chromosome_two[sortedarray[j]:sortedarray[j + 1]]
            print "crossover child one is %s" % (crossonechromo)
            print "crossover child two is %s" % (crosstwochromo)
            return crossonechromo,crosstwochromo
        else:
            return chromosome_one,chromosome_two

    def onepointcrossover(self, chromosome_one, chromosome_two, CHROMOSOMAL_LENGTH):
        '''
        this function will take two chromosome and chromosomal length as input and will perform one point crossover
        '''
        if random.random() <= PROBOFCROSSOVER:
            onepoint = random.randint(0, CHROMOSOMAL_LENGTH-1)
            print "crossover point is %d"%(onepoint)
            return chromosome_one[:onepoint]+chromosome_two[onepoint:], chromosome_one[onepoint:]+chromosome_two[:onepoint]
        else:
            return chromosome_one, chromosome_two


    def uniformcrossover(self,chromosome_one,chromosome_two,CHROMOSOMAL_LENGTH):
        '''
        this function will take two chromsome,chromosome length and perform uniformcrossover operation
        '''
        temp1 = list(chromosome_one)
        temp2 = list(chromosome_two)
        if random.random() <= PROBOFMUTATION:
            for i in range(CHROMOSOMAL_LENGTH):
                if random.random() <= PERLOCUSPROBCROSSOVER:
                    t = temp1[i]
                    temp1[i] = temp2[i]
                    temp2[i] = t
            chromosome_one = ''.join(temp1)
            chromosome_two = ''.join(temp2)
            return chromosome_one,chromosome_two
        else:
            return chromosome_one,chromosome_two

    def fitnessproportionalselection(self, fitnessarray):
        '''
        this function will perform fitnessproportionalselection with the fitnessarray as input argument
        '''
        totalfitness = npy.sum(fitnessarray)
        temparray = npy.array(fitnessarray)
        fitnessproportion = npy.true_divide(temparray, totalfitness)
        firstrandomselection = random.randint(0, len(fitnessproportion)-1)
        secondrandomselection = random.randint(0, len(fitnessproportion)-1)
        return self.pop[firstrandomselection],self.pop[secondrandomselection]

    def tournamentselection(self, size):
        '''
        this function will perform tournament selection taking size as the input argument
        '''
        randarray = []
        fittuarray = []
        for i in range(size):
            randvalue = random.randint(0, len(self.fitpop) - 1)
            randarray.append(randvalue)
        for j in randarray:
            fittuarray.append(self.fitpop[j])

        print "fitnessarray is %s" % (fittuarray)
        maxval = max(fittuarray)
        print maxval

        for k in range(len(fittuarray)):
            if maxval == fittuarray[k]:
                self.tourpop.append(self.pop[randarray[k]])
                break

    def elitism(self,element):
        '''
        this function will perform elitism with number of elements as the input argument
        '''
        sortedindices=npy.argsort(self.fitpop)
        subsorted=sortedindices[-element:]
        for i in range(len(subsorted)):
            print "elitism elements are"
            return self.pop[subsorted[i]]

    def rastrigin(self, chromosome):
        '''
        this function will take a chromosome as a input and split it into an array of 4 elements and rastrigin function
        is applied to each of them to obtain a minimum value
        '''
        splittedarray = []
        decimalarray = []
        for i in range(len(chromosome)):
            if i == 4:
                splittedarray.append(chromosome[0:4])
            elif i == 8:
                splittedarray.append(chromosome[4:8])
            elif i == 12:
                splittedarray.append(chromosome[8:12])
            elif i == 15:
                splittedarray.append(chromosome[12:16])
        print splittedarray
        for j in range(len(splittedarray)):
            temp = list(reversed(splittedarray[j]))
            adder = 0
            for k in range(len(temp)):
                adder += pow(2, k) * int(temp[k])
            decimalarray.append(adder)
        print decimalarray
        sigmafuncadder = 0
        for l in range(len(decimalarray)):
            sigmafuncadder += pow(decimalarray[l], 2) - (10 * math.cos(2 * math.pi * decimalarray[l]))
        rastrigin = 10 * len(decimalarray) + sigmafuncadder
        return rastrigin
if(__name__=="__main__"):

    pops = population([], [], [], [])
    a = 0
    for i in range(POPULATION_SIZE):
        pops.addpopulation(16)     ##create population
    pops.measurefitness(pops.pop)   ##measure fitness value
    print"Initial population is %s"%(pops.pop)
    print"len of initial population is %d"%len(pops.pop)
    print"Initial fitness array is %s"%(pops.fitpop)
    pops.elitism(2)
    while a < GENERATION_SIZE:      ##perform the loop to continue until the generation size is reached
        print "Generation %d"%(a)
        a += 1
        pops.newpop=[]              ##new population(next generation) array
        for j in range(POPULATION_SIZE):
                pops.tournamentselection(3)    ##tournament selection function is called
        print"Tournament selection based array is %s"%(pops.tourpop)
        print"length of tour array is %s"%len(pops.tourpop)
        for k in range(0, len(pops.tourpop)):
            '''
            inside this loop is where the crossover and mutation operation takes place and the
            next generation chromosomes are added to the new population(next generation array)
            and also the fitness of the new population is also performed.In the end the 
            tournament selection array is made empty  
            '''
            if len(pops.tourpop) == 0:
                break
            else:
                print "the tournament array to be established is %s"%pops.tourpop
                parentone=pops.tourpop[0]
                parenttwo=pops.tourpop[1]
                x,y=pops.k_pointcrossover(3,parentone,parenttwo,16)
                childone=pops.binarymutation(x)
                childtwo=pops.binarymutation(y)
                print "child one %s"%(childone)
                print "child two %s"%(childtwo)
                pops.newpop.append(childone)
                pops.newpop.append(childtwo)
                pops.fitpop=[]
                pops.measurefitness(pops.newpop) ##new population fitness is measured
                pops.tourpop.remove(parentone)
                pops.tourpop.remove(parenttwo)
                print "the next generation ones are %s"%(pops.newpop)
                print "the length of newpopulation is %s"%(len(pops.newpop))
                print "the fitness array is %s"%(pops.fitpop)
        print "maximum fitness of new gen is %d"%(max(pops.fitpop))
        '''
        the optimality for one max condition is checked over here
        '''
        if max(pops.fitpop) == 16:
            print "optimal found"
            break