import csv

class CsvWriter:
    def __init__(self, file_path):
        self.file_path = file_path
        
    def write(self, ntl_list, fitnesses, measures_data):
        with open(self.file_path, mode='w', newline='') as file:
            for params in ntl_list:
                param_names = list(list(params.values())[0].keys()) 
                tran_names = list(params.keys())
                measures_keys = list(measures_data[0].keys())  
                headers = tran_names + ['fitness'] + measures_keys 
                
                writer = csv.writer(file)
                writer.writerow(headers)
                
                for ntl, fitness, measures in zip(params.values(), fitnesses, measures_data):
                    row = []  
                    for name in param_names:
                        row.extend(ntl[name].values())  
                    row.append(fitness)
                    row.extend(measures.values())  
                    writer.writerow(row)

    