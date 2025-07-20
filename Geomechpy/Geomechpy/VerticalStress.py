import numpy as np
from scipy.constants import g

def RHOB_interpolated(TVD, density_0, a, b):
    return density_0 + a * TVD**b

def calc(TVD, RHOB, g = g):
    """
    Расчёт вертикального напряжения по TVD и RHOB.

    Параметры:
        tvd (fload, array): истинные вертикальные глубины (м).
        rhob (fload, array): плотность (кг/м³).
        g (fload, array): Ускорение свободного падения (м/с²).
    Возвращает:
        (fload, array масив): вертикальное напряжения (Па).
    """
    delta_z = np.diff(TVD, prepend=0)
    stress = np.cumsum(RHOB * g * delta_z)  # Интегрирование
    return stress