import random, copy
from MainAlgorithm.Individual import Individual



class GeneticAlgorithm:

    def __init__(self, simulator, scales, netlist, spec, parameter_constraints):
        self._scales = scales
        self._parameter_constraints = parameter_constraints
        self._netlist = netlist
        self._spec = spec
        self._sim = simulator


    def _generate_num(self, sample_num, start, until):
        if isinstance(sample_num, int):
            return random.randint(start, until)
        return random.uniform(start, until)

    def _calculate_fintess(self, meas):
        fitness = 0.0
        for key, meas_val in meas.items():
            low = self._spec.get(key, {}).get('SpecLo')
            high = self._spec.get(key, {}).get('SpecHi')

            if low and high:
                spec_key = self._spec.get(key, {}).get('Scale')
                scale = self._scales.get(spec_key)
                fitness += self._fitness_function(meas_val, low * scale, high * scale)
        return fitness


    def _fitness_function(self, measured_val, lower_bound, upper_bound):
        if lower_bound <= measured_val <= upper_bound:
            return 1
        else:
            mid = (lower_bound + upper_bound) / 2
            return -abs((measured_val - mid) / mid)

    def _generate_population(self, netlist, population_size) -> list[Individual]:
        population = []
        for _ in range(population_size):
            new_net = netlist.copy()
            for key in netlist.keys():
                new_net[key] = {param: self._generate_num(new_net[key][param], 
                                                          self._parameter_constraints[param][0], 
                                                          self._parameter_constraints[param][1]) 
                                                          for param in self._parameter_constraints.keys()}

            population.append(Individual(copy.deepcopy(new_net)))

        return population

    def _select_parents(self, population, size):
        if len(population) > size: #tournament selection
            sample_length = random.randint(size, len(population))
            p1 = random.sample(population, sample_length)
            p2 = random.sample(population, sample_length)
        
            p1.sort(key=(lambda x: x.fitness), reverse=True)
            p2.sort(key=(lambda x: x.fitness), reverse=True)
            result1 = p1[:size]
            result2 = p1[:size]

            random.shuffle(result1)
            random.shuffle(result2)
        else:
            result1 = random.sample(population, size)
            result2 = random.sample(population, size)
        return result1, result2

    def _crossover(self, parent_pop1, parent_pop2):
        result = []
        for par1, par2 in zip(parent_pop1, parent_pop2):
            net1, net2 = copy.deepcopy(par1.netlist), copy.deepcopy(par2.netlist)
            size = random.randint(1, len(net1) - 1)
            rand_pop = random.sample(list(net1.keys()), size)
            for key in rand_pop:
                net1[key] = net2[key]

            par1.netlist = net1
            result.append(par1)
        return result

    def _mutate(self, pop, rate):
        for individual in pop:
            rand = random.random()
            if rand < rate:
                key = random.sample(individual.netlist.keys(), 1)[0]
                param = random.sample(individual.netlist[key].keys(), 1)[0]
                individual.netlist[key][param] = self._generate_num(individual.netlist[key][param],
                                                                    self._parameter_constraints[param][0],
                                                                    self._parameter_constraints[param][1])
        return pop


    def _get_measures(self, netl) -> dict:
        return self._sim.run_model(netl)


    def _initialize_individuals(self, population, best_fitness=float('-inf'), best_individual=None):
        for individual in population:
            individual.measures = self._get_measures(copy.deepcopy(individual.netlist))
            individual.fitness = self._calculate_fintess(individual.measures)

            if individual.fitness > best_fitness:
                best_fitness = individual.fitness
                best_individual = individual
        return best_fitness, best_individual


    def genetic_algorithm(self, population_size, generations, mutation_rate):
        population = self._generate_population(copy.deepcopy(self._netlist), population_size)
    
        best_fitness, best_individual = self._initialize_individuals(population)
        fitness_data = [best_fitness]

        for _ in range(generations):
            parent1, parent2 = self._select_parents(population, population_size)
            child = self._crossover(parent1.copy(), parent2.copy())
            child = self._mutate(child, mutation_rate)

            best_fitness, best_individual = self._initialize_individuals(child, best_fitness, best_individual)
            fitness_data.append(best_fitness)
            population.extend(child)

        print(fitness_data)
        return best_individual.netlist, fitness_data