def calc_Edyn(Vp, Vs, density): 
    """
    Расчёт Модуля Юнга динамического.
    
    Параметры:
        Vp: скорость продольных волн(число, array масив).
        Vs: скорость поперечных волн(число, array масив).
        density: плотность.
    """ 
    Vp_sqrd = Vp**2
    Vs_sqrd = Vs**2
    return (density * Vs_sqrd * (3 * Vp_sqrd - 4 * Vs_sqrd)) / (Vp_sqrd - Vs_sqrd)

def calc_Prdyn(Vp, Vs):
    """
    Расчёт коэфициента Пуассона динамического.
    
    Параметры:
        Vp: скорость продольных волн(число, array масив).
        Vs: скорость поперечных волн(число, array масив).
    """

    Vp_sqrd = Vp**2
    Vs_sqrd = Vs**2
    return (Vp_sqrd - 2 * Vs_sqrd) / (2 * (Vp_sqrd - Vs_sqrd)) 

def calc_Gdyn(Edyn, Prdyn):
    """
    Расчёт модуля сдвига динамического.
    
    Параметры:
        Edyn: Динамический модуль Юнга (число, array масив).
        Prdyn: Динамический коэфициент Пуассона (число, array масив).
    """ 
    return Edyn / (2 * (1 + Prdyn))

def calc_Kdyn(Edyn, Prdyn):
    """
    Расчёт объемного сжатия динамического.
    
    Параметры:
        Edyn: Динамический модуль Юнга (число, array масив).
        Prdyn: Динамический коэфициент Пуассона (число, array масив).
    """ 
    return Edyn / (3 * (1 - 2 * Prdyn))

def calc_Esta_by_Edyn(Edyn): # GPa
    return 0.032 * pow(Edyn, 1.623) # GPa

def calc_Esta_Morales():
    pass

def calc_Prsta(Prdyn):
    pass

def calc_alph():
    pass