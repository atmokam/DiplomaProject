import GeneticAlgo


class Application:
    def __init__(self):
        self._input_file = ""
        self._parameter_constraints = {"w": (0.2, 2.4), "l": (0.03, 0.03), "nf": (1, 10)}

    @property
    def parameter_constraints(self):
        return self._parameter_constraints
    
    @parameter_constraints.setter
    def parameter_constraints(self, value):
        self._parameter_constraints = value


    def read_from_file(self, path):
        with open(path, 'r') as file:
            self._input_file = file.readlines()        


    def run_genetic_algo(self, generate_from: dict[str, dict[str, str]], population_size, generations):
        gen_algo = GeneticAlgo()
        generations_list = {}
        for i in range(generations):
            pass