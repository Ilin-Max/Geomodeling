
def calc_UCS_func_of_Esta_correlations(Esta): # GPa
    return 4.366E-11 + 4242 * Esta # KPa

def calk_TSTR_func_of_UCS_correlation(UCS): # KPa
    return 0.1 * UCS # KPa