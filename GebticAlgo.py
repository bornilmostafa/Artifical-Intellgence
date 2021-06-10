import random
from numpy.random import rand

chromo = ["01101", "11000", "01000", "10011"]
population = [list(i) for i in chromo]


def calculatePhenotype(chromo):
    phenotype = []
    for i in range(len(chromo)):
        p = 4
        c = 0
        for b in range(0, 5):

            if population[i][b] == "1":
                c = c + 2 ** p

            p = p - 1

        phenotype.insert(i, c)


    return phenotype


def fitness(phenotype):
    fit = []
    for i in phenotype:
        fx = i * i
        fit.insert(i, fx)
    return fit


def avgWtotal(fit):
    total = sum(fit)
    avg = total / len(fit)
    return avg, total


def fraction(fit, total):
    frac = []
    for i in fit:
        fr = round(i / total, 2)
        frac.insert(i, fr)
    return frac


# tournament selection

def associatedBin(frac):
    bins = []

    next = 0.0
    for i in range(len(frac)):
        next = next + frac[i]
        next = round(next, 2)
        bins.insert(i, next)
    bins.insert(0, 0.0)
    return bins


def selection(bins, chromo):
    num = round(random.random(), 2)
    for i in range(len(bins)):
        if num >= bins[i] and num <= bins[i + 1]:
            st = chromo[i]
    return st


def rand():
    bitlen = len(population[0])
    split = random.randint(1, bitlen - 1)
    return split


def crossover(chromo):
    bitlength = len(population[0])
    for i in range(len(chromo)):
        sp = rand()
        r = 1
        for j in range(bitlength - sp):
            carrier = population[i][bitlength - r]
            population[i][bitlength - r] = population[i + 1][bitlength - r]
            population[i + 1][bitlength - r] = carrier

            r = r + 1
        i = 2
        sp = rand()
        for j in range(bitlength - sp):
            carrier = population[i][bitlength - r]
            population[i][bitlength - r] = population[i + 1][bitlength - r]
            population[i + 1][bitlength - r] = carrier
            r = r + 1
        return population


gen = ["11010", "11111", "01000", "10101"]
hood = []
print(gen)
hood = calculatePhenotype(gen)
print("pheno types:::::::::::::::::::::::::::::::::::::")
print(hood)
print("Fitness::::::::::::::::::::::::::::::::::::::")
sqr = fitness(hood)
print(sqr)
avg, total = avgWtotal(sqr)
print("AVG:::::::::", avg)
print("TOTAL::::::::", total)
avg = round(avg, 2)
print("Rounded average::", avg)
fraction = fraction(sqr, total)
print("fraction of total................")
print(fraction)
bins = []
bins = associatedBin(fraction)
print(bins)
print("----------The random selected from the bin-------------------------")
selected = selection(bins, num)
print(selected)
print("Successful crossover the  new pupulation we get")
newpopulation = crossover(num)
print(newpopulation)
print(":::::::::::::::::The process for the new generation::::::::::::::::::::::::")
p = calculatePhenotype(newpopulation)
print("pheno types::::::::::::::::::::")
print(p)
print("Fitness:::::::::::::::::")
sqr = fitness(p)
print(sqr)
total = avgWtotal(sqr)
print(total)
