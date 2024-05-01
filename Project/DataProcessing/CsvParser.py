import csv 

# all parse classes should have a common ancestor, although they don't for now (again no time)

class CsvParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.ntl_list = []
        self.fitnesses = []
        self.measures_data = []
    
    def parse(self): # todo: refactor this method into 3 different methods
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
                header_start = fitness_index
                row_start = 3*header_start
                for i in range(header_start+1, len(headers)):
                    atkey = headers[i]
                    row_start = row_start + 1
                    measures[atkey] = float(row[row_start])


                self.measures_data.append(measures.copy())
                
        return self.ntl_list, self.fitnesses, self.measures_data
    