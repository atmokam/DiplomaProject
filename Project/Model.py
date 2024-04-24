import keras as k
import numpy as np

class Model:
    def __init__(self, model=None):
        self._model = model

    def predict(self, ntl):
        ntl = Model.ntl_to_list(ntl)
        print(ntl)
        ntl = np.asarray(ntl).astype(np.float32)
        return self._model.predict(ntl)
    
    def load(self, path):
        self._model = k.models.load_model(path)
    
    @staticmethod
    def ntl_list_to_list(ntl: list[dict[str, dict]]):
        result = []
        for netlist in ntl:
            sample = []
            for params in netlist.values():
                row = []
                for value in params.values():
                    row.append(value)
                sample.extend(row.copy())
            result.append(sample.copy())
        return result
    
    @staticmethod
    def ntl_to_list(ntl: dict[str, dict]):
        sample = []
        for params in ntl.values():
            row = []
            for value in params.values():
                row.append(value)
            sample.extend(row.copy())
        result = []
        result.append(sample)
        return result



