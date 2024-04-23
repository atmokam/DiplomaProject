import keras as k
from CsvParser import CsvParser
from sklearn.preprocessing import MinMaxScaler

class Model:
    def __init__(self, path_to_data):
        self._data_dict = CsvParser(path_to_data).parse()
        
        self._model = k.models.Sequential()

