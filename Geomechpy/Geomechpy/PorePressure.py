from scipy.constants import g

def calc_sigma_eff_eaton(v0, b, sigma_eff_norm, vp, tvd, exp = 3):
    #Vn = a + b * tvd
    Vn = v0 * pow(10, (b * tvd))
    sigma_eff = sigma_eff_norm * (vp / Vn) ** exp
    return sigma_eff

def calc_sigma_max(v_max, v0, a, b):
    return ((v_max - v0) / a) ** (1 / b)

def calc_sigma_eff_bowers(v_max, v0, a, b, vp):
    sigma_max = calc_sigma_max(v_max, v0, a, b)
    sigma_eff = sigma_max * ((1 / sigma_max) * ((vp - v0) / a) ** (1 / b))
    return sigma_eff

def calc_by_EathonMetod():
    pass

def calc_by_BowerMetod():
    pass

def calc_by_ConstantFluidDensity(TVD, fluid_density, g = g):
    return TVD * fluid_density * g