from deap import base
from deap import creator
from deap import tools
from deap import algorithms

import random
import numpy

import matplotlib.pyplot as plt
import seaborn as sns

import model_rhbz
from RHBZ_input import RHBZ_input
from vehicle import VehiclePark

def main(inputData : RHBZ_input):
    knapsack = model_rhbz.Knapsack01Problem(inputData)

    def knapsackValue(individual):
        return knapsack.getValue(individual),  # return a tuple

    def mutate(individual):
        pc = inputData.parkCapacity
        a = -pc / 10
        b = pc / 10
        prob = 1.0 / len(individual)
        for i in range(len(individual)):
            if random.random() < prob:
                # individual[i] += random.randint(-10, 10)
                # individual[i] = max(individual[i], 0)
                # individual[i] += random.randint(-inputData.parkCapacity, inputData.parkCapacity)
                individual[i] += int(random.random() * (b-a) + a)
                individual[i] = max(individual[i], 0)
                individual[i] = min(individual[i], pc)
        return individual,

    # POPULATION_SIZE = 800
    POPULATION_SIZE = inputData.populationSize
    # P_CROSSOVER = 0.8
    P_CROSSOVER = inputData.pCrossover
    # P_MUTATION = 0.2
    P_MUTATION = inputData.pMutate
    # MAX_GENERATIONS = 300
    MAX_GENERATIONS = inputData.maxGenerations
    HALL_OF_FAME_SIZE = 1

    RANDOM_SEED = 42
    random.seed(RANDOM_SEED)

    toolbox = base.Toolbox()

    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)

    # rdFuncs = [VehiclePark.randomRepair, VehiclePark.randomBuy]
    rdFuncs = [
        lambda: random.randint(0, inputData.parkCapacity),
        lambda: random.randint(0, inputData.parkCapacity)
    ]
    # rdFuncs = [
    #     lambda: 0,
    #     lambda: 0
    # ]
    years = 10
    inits = len(VehiclePark.types) * years
    toolbox.register("individualCreator", tools.initCycle, creator.Individual, rdFuncs, inits)
    toolbox.register("populationCreator", tools.initRepeat, list, toolbox.individualCreator)
    toolbox.register("evaluate", knapsackValue)
    toolbox.register("select", tools.selTournament, tournsize=8)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", mutate)
    # =============================================================
    # create initial population (generation 0):
    population = toolbox.populationCreator(n=POPULATION_SIZE)

    # prepare the statistics object:
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("max", numpy.max)
    stats.register("avg", numpy.mean)

    # define the hall-of-fame object:
    hof = tools.HallOfFame(HALL_OF_FAME_SIZE)

    # perform the Genetic Algorithm flow with hof feature added:
    population, logbook = algorithms.eaSimple(population, toolbox, cxpb=P_CROSSOVER, mutpb=P_MUTATION,
                                              ngen=MAX_GENERATIONS, stats=stats, halloffame=hof, verbose=True)

    # print best solution found:
    best = hof.items[0]
    print("-- Best Ever Individual = ", best)
    print("-- Best Ever Fitness = ", best.fitness.values[0])
    # print("-- Knapsack Items = ")
    # knapsack.printItems(best)

    # extract statistics:
    maxFitnessValues, meanFitnessValues = logbook.select("max", "avg")

    # plot statistics:
    sns.set_style("whitegrid")
    plt.plot(maxFitnessValues, color='red')
    plt.plot(meanFitnessValues, color='green')
    plt.xlabel('Generation')
    plt.ylabel('Max / Average Fitness')
    plt.title('Max and Average fitness over Generations')
    plt.show()


# if __name__ == "__main__":
#     main()