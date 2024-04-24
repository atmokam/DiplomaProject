import keras as k
import numpy as np
from CsvParser import CsvParser
from sklearn.preprocessing import StandardScaler
from Model import Model

class Trainer:
    def __init__(self, path_to_data):
        self._ntl, self._fitnesses, self._measures = CsvParser(path_to_data).parse()

        self._input_data = Model.ntl_list_to_list(self._ntl)
        self._output_data = [list(measure.values()) for measure in self._measures]

        #self._scaler = StandardScaler()
        #self._input_data = self._scaler.fit_transform(self._input_data)
        #scaling gives 0 what do i do
        self._input_data = np.asarray(self._input_data).astype(np.float32)
        self._output_data = np.asarray(self._output_data).astype(np.float32)

        input_count = self._input_data.shape[1]
        output_count = self._output_data.shape[1]

        self._model = k.models.Sequential()

        self._model.add(k.layers.Dense(64, input_dim=input_count, activation='relu'))
        self._model.add(k.layers.Dense(output_count, activation='linear'))
        self._model.compile(optimizer='adam', loss='mae')

    def train(self, epochs, batch_size):
        self._model.fit(self._input_data, self._output_data, epochs=epochs, batch_size=batch_size)
   
    def save(self, path):
        self._model.save(path)

    def get_trained_model(self):
        return Model(self._model)