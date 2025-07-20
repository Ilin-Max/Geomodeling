import lasio
from .Traektory import Traektory
import numpy as np
import pandas as pd

class Well():
    def __init__(self, name):
        self.name = name
        self.longtitude = 0
        self.latitude = 0
        self._X_coord = 0
        self._Y_coord = 0
        self._KB = 0
        self.see_floor = 0
        self.traectory = Traektory()
        self.traectory._locked = True
        self.curves = []

    @property
    def KB(self):
        return self._KB
    
    @property
    def X_coord(self):
        return self._X_coord
        
    @property
    def Y_coord(self):
        return self._Y_coord

    @KB.setter
    def KB(self, value):
        self._KB = value
        self.traectory._Z0 = value
    
    @X_coord.setter
    def X_coord(self, value):
        self._X_coord = value
        self.traectory._X0 = value
    
    @Y_coord.setter
    def Y_coord(self, value):
        self._Y_coord = value
        self.traectory._Y0 = value
    
    def show_traectory(self):
        self.traectory.show(self.name)
    
    def traectory_from_excel(self, file_path, MD_col = 0, INKL_col = 1, AZIM_col = 2, headers = True):
        df = pd.read_excel(file_path, header=headers)
        keys = df.keys()
        MD = df[keys[MD_col]]
        INKL = df[keys[INKL_col]]
        AZIM = df[keys[AZIM_col]]
        
        self.traectory.MD = MD
        self.traectory.INKL = INKL
        self.traectory.AZIM = AZIM

    def add_curves(self, new_curves = []):
        self.curves.extend(new_curves)
        
# w1 = Well("w1")

# w1.traectory.MD = np.arange(0, 100, 10)
# w1.traectory.INKL = np.zeros(len(w1.traectory.MD))
# w1.traectory.AZIM = np.zeros(len(w1.traectory.MD))

# w1.KB = 30
# w1.X_coord = 100
# w1.Y_coord = 500000
# print(w1.traectory.to_df())

# w1.show_traectory()