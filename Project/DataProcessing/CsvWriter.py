import csv

class CsvWriter:
    def __init__(self, file_path):
        self.file_path = file_path
        
    def write(self, ntl_list, fitnesses, measures_data):
        tran_names = list(ntl_list[0].keys())
        param_names = list(ntl_list[0].get(tran_names[0]).keys())
        measures_keys = list(measures_data[0].keys())
        headers = tran_names + ['fitness'] + measures_keys 
        

        with open(self.file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            for ntl, fitness, measures in zip(ntl_list, fitnesses, measures_data):
                row = []  
                for parameters in ntl.values():
                    for name in param_names:
                        row.append(parameters.get(name))

                row.append(fitness)
                row.extend(measures.values())  
                writer.writerow(row)

    