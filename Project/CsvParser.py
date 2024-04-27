import csv 

# all parse classes should have a common ancestor

class CsvParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.ntl_list = []
        self.fitnesses = []
        self.measures_data = []
    
    def parse(self):
        with open(self.file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader)
            fitness_index = headers.index('fitness') #is in the middle of xm and meas

            for row in csv_reader:
                netlist = {}
                for i in range(0, 3*fitness_index, 3):
                    w = row[i]
                    l = row[i+1]
                    nf = row[i+2]
                    transistor = {"w": float(w), "l": float(l), "nf": float(nf)}
                    netlist[headers[int(i/3)]] = transistor.copy()

                self.ntl_list.append(netlist)

                fitness = float(row[3*fitness_index])
                self.fitnesses.append(float(fitness))

                measures = {}
                
                for i in range((3*fitness_index), len(row)):
                    measures[headers[(i//3)+1]] = float(row[i-1])

                measures[headers[-1]] = float(row[-1])

                self.measures_data.append(measures.copy())
                
        return self.ntl_list, self.fitnesses, self.measures_data
    