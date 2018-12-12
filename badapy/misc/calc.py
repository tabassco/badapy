import math


def calc_mach(h):
    """
    Calculate the mach number
    :param h:
    :return:
    """
    temp = isa_temp(h)
    if temp == 216.65:
        return 295.07  # Unit: meters / second
    else:
        return 340.29 * math.sqrt(temp / 288.15)  # Unit: meters / second


def isa_temp(h):
    """
    Calculate the ISA Temperature
    :param h: Height in Meters
    :return: Temp in Kelvin
    """
    t = 288.15 - (6.5 / 1000) * h
    t_trop = 288.15 - (6.5 / 1000) * 11000
    if t > t_trop:
        return 216.65  # Unit: Kelvin
    else:
        return t


def transition_alt(v_cas, h):
    """

    :param v_cas:
    :param h:
    :return:
    """
    mach = calc_mach(h)
    t_0_isa = 288.15  # Unit: Kelvin
    delta_trans = ((1 + 0.2 * (v_cas / 340.29) ** 2) ** 3.5 - 1) / ((1 + 0.2 * (mach ** 2)) ** 3.5 - 1)  # Func: 3.2-20
    theta_trans = delta_trans ** (1/5.25583)  # Using Approx: 3.2-15  -- Func: 3.2-19
    h_trans = (1000 / (0.3048 * 6.5)) * t_0_isa * (1 - theta_trans)  # Func: 3.2-18

    return h_trans
