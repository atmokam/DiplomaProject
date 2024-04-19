import csv

class CsvWriter:
    def __init__(self, file_path):
        self.file_path = file_path
        
    def write(self, ntl_list, fitnesses, measures_data):
        with open(self.file_path, mode='w', newline='') as file:
            param_names = list(list(ntl_list.values())[0].keys()) 
            tran_names = list(ntl_list.keys())
            measures_keys = list(measures_data[0].keys())  
            headers = tran_names + ['fitness'] + measures_keys 
            
            writer = csv.writer(file)
            writer.writerow(headers)
            
            for ntl, fitness, measures in zip(ntl_list.values(), fitnesses, measures_data):
                row = []  
                for name in param_names:
                    row.extend(ntl[name].values())  
                row.append(fitness)
                row.extend(measures.values())  
                writer.writerow(row)

    # def __init__(self, csv_file, individual):
    #     self._csv_file = csv_file # path
    #     self._write_header(individual)

    # def _write_header(self, individual):
    #     with open(self._csv_file, 'w', newline='') as csvfile:
    #         lst = list(individual.netlist.keys()) + ["fitness"]
    #         writer = csv.DictWriter(csvfile, fieldnames=lst)
    #         writer.writeheader()

    # def write_csv(self, individual):
    #     with open(self._csv_file, 'a', newline='') as csvfile:
    #         vals = individual.netlist.copy() 
    #         vals["fitness"] = individual.fitness
    #         writer = csv.DictWriter(csvfile, fieldnames=vals.keys())
    #         writer.writerow(vals)
            
    # def read_csv(self): 
    #     with open(self._csv_file, 'r', newline='') as csvfile:
    #         reader = csv.DictReader(csvfile)
    #         rows = [dict(row) for row in reader]
    #     return rows