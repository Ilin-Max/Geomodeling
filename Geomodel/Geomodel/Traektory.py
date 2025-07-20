import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Traektory():
    def __init__(self, md=np.array([]), azim=np.array([]), inkl=np.array([]), 
                 Z0=0, X0=0, Y0=0):
        self.MD = md
        self.AZIM = azim
        self.INKL = inkl
        self._X0 = X0
        self._Y0 = Y0
        self._Z0 = Z0
        self._locked = False  # По умолчанию разрешаем изменение

    def _unlock(self):
        """Разблокирует изменение координат (для автономного использования)."""
        self._locked = False

    @property
    def X0(self):
        return self._X0

    @X0.setter
    def X0(self, value):
        if self._locked:
            raise AttributeError("Изменение X0 запрещено! Используйте X_coord в классе Well.")
        self._X0 = value

    @property
    def Y0(self):
        return self._Y0

    @Y0.setter
    def Y0(self, value):
        if self._locked:
            raise AttributeError("Изменение Y0 запрещено! Используйте Y_coord в классе Well.")
        self._Y0 = value

    @property
    def Z0(self):
        return self._Z0

    @Z0.setter
    def Z0(self, value):
        if self._locked:
            raise AttributeError("Изменение Z0 запрещено! Используйте KB в классе Well.")
        self._Z0 = value
        
    @property
    def delta_MD(self):
        return np.diff(self.MD)
    
    @property
    def middle_point_INKL(self):
        return self.INKL[:-1] + np.diff(self.INKL)/2
    
    @property
    def middle_point_AZIM(self):
        return self.AZIM[:-1] + np.diff(self.AZIM)/2
    
    @property
    def dX(self):
        dx = np.zeros(len(self.MD))
        dx[1:] = self.delta_MD * np.sin(np.radians(self.middle_point_INKL)) * np.sin(np.radians(self.middle_point_AZIM))
        return dx

    @property
    def dY(self):
        dy = np.zeros(len(self.MD))
        dy[1:] = self.delta_MD * np.sin(np.radians(self.middle_point_INKL)) * np.cos(np.radians(self.middle_point_AZIM))
        return dy

    @property
    def dZ(self):
        dz = np.zeros(len(self.MD)) 
        dz[1:] = self.delta_MD * np.cos(np.radians(self.middle_point_INKL))
        return dz

    @property
    def X(self):
         return self.X0 + np.cumsum(self.dX)

    @property
    def Y(self):
        return self.Y0 + np.cumsum(self.dY)

    @property
    def Z(self):
        return self.Z0 - np.cumsum(self.dZ)
    
    @property
    def TVD(self):
        return np.cumsum(self.dZ)
        
    def to_df(self):
        data = {
            "MD": self.MD,
            "AZIM": self.AZIM,
            "INKL": self.INKL,
            "TVD": self.TVD,
            "dX": self.dX,
            "dY": self.dY,
            "dZ": self.dZ,
            "X": self.X,
            "Y": self.Y,
            "Z": self.Z,
            }
        return pd.DataFrame(data)

    def show(self, name = "Traektory"):
        fig = plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(self.X, self.Y, self.Z, label=name, linewidth=2, color='blue')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('Traektory')
        ax.set_zlim([np.min(self.Z), self.Z0])
        ax.legend()
        plt.show()
    
    def read_excel(self, file_path, MD_col = 0, INKL_col = 1, AZIM_col = 2, headers = True):
        df = pd.read_excel(file_path, header=headers)
        keys = df.keys()
        MD = df[keys[MD_col]]
        INKL = df[keys[INKL_col]]
        AZIM = df[keys[AZIM_col]]
        
        self.MD = MD
        self.INKL = INKL
        self.AZIM = AZIM