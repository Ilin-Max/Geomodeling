def calc_Sh(Sv, alph, PorPress, Prsta, Esta, ex, ey):
    """
    Расчёт горизонтального минимального напряжения.
    
    Параметры:
        Sv (fload, array): Вертикальные напряжения (Па).
        a (fload, array): Константа био ().
        Prsta (fload, array): Коэффициент Пуассона статический.
        Esta (fload, array): Модуль Юнга статический.
        ex (fload, array): Деформации в направленеии минимального напряжения.
        ey (flfload, arrayoat): Деформации в направленеии максимального напряжения.

    Возвращает:
        array: Массив вертикального напряжения (Па).
    """
        
    return (Sv - alph * PorPress) * (Prsta / (1 - Prsta)) + alph * PorPress + (ex + ey * Prsta) * (Esta / (1 - Prsta ** 2)) 
    
def calc_SH(Sv, alph, PorPress, Prsta, Esta, ex, ey):
    """
    Расчёт горизонтального максимального напряжения.
    Параметры:
        Sv (fload, array): Вертикальные напряжения (Па).
        a (fload, array): Константа био ().
        Prsta (fload, array): Коэффициент Пуассона статический.
        Esta (fload, array): Модуль Юнга статический.
        ex (fload, array): Деформации в направленеии минимального напряжения.
        ey (flfload, arrayoat): Деформации в направленеии максимального напряжения.

    Возвращает:
        array: Массив вертикального напряжения (Па).
    """
    return (Sv - alph * PorPress) * (Prsta / (1 - Prsta)) + alph * PorPress + (ey + ex * Prsta) * (Esta / (1 - Prsta ** 2))
