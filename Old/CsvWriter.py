import csv

class CsvWriter:
    def __init__(self, csv_file, individual):
        self._csv_file = csv_file # path
        self._write_header(individual)

    def _write_header(self, individual):
        with open(self._csv_file, 'w', newline='') as csvfile:
            lst = list(individual.netlist.keys()) + ["fitness"]
            writer = csv.DictWriter(csvfile, fieldnames=lst)
            writer.writeheader()

    def write_csv(self, individual):
        with open(self._csv_file, 'a', newline='') as csvfile:
            vals = individual.netlist.copy() 
            vals["fitness"] = individual.fitness
            writer = csv.DictWriter(csvfile, fieldnames=vals.keys())
            writer.writerow(vals)
            
    # def read_csv(self): 
    #     with open(self._csv_file, 'r', newline='') as csvfile:
    #         reader = csv.DictReader(csvfile)
    #         rows = [dict(row) for row in reader]
    #     return rows