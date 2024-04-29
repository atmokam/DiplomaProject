import keras as k
import numpy as np
from ANN.Model import Model

class Trainer:
    def __init__(self, netlist, measures):

        self._input_data = Model.ntl_list_to_list(netlist)
        self._output_data = [list(measure.values()) for measure in measures]

        self._input_data = np.asarray(self._input_data).astype(np.float32)
        self._output_data = np.asarray(self._output_data).astype(np.float32)

        input_count = self._input_data.shape[1]
        output_count = self._output_data.shape[1]

        self._model = k.models.Sequential()

        self._model.add(k.layers.Dense(50, input_dim=input_count, activation='relu'))
        self._model.add(k.layers.Dense(output_count, activation='linear'))
        self._model.compile(optimizer='adam', loss='mean_squared_logarithmic_error', metrics=['accuracy'])

    def train(self, epochs, batch_size):
        self._model.fit(self._input_data, self._output_data, epochs=epochs, batch_size=batch_size)
   
    def save(self, path):
        self._model.save(path)

    def get_trained_model(self):
        return Model(self._model)
    
   