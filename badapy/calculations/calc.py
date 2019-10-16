import math


def density(T):
    """
    Calculate the density
    :param T:
    :param h:
    :return:
    """
    return 1.225 * ((T / 288.15) ** 4.25583)


def max_cruise_thrust(h, T, C_1, C_2, C_3, C_4, C_5):
    """
    Maximum Thrust for Cruise flight
    :param h:
    :param T:
    :param C_1: ctc_1
    :param C_2: ctc_2
    :param C_3: ctc_3
    :param C_4: ctc_4
    :param C_5: ctc_5
    :return:
    """
    return 0.95 * max_climb_thrust(h, T, T, C_1, C_2, C_3, C_4, C_5)


def max_climb_thrust(h, T, C_1, C_2, C_3, C_4, C_5):
    """
    Maximum Thrust
    :param h: height in Meters
    :param T: Temperature in Celsius
    :param C_1: ctc_1
    :param C_2: ctc_2
    :param C_3: ctc_3
    :param C_4: ctc_4
    :param C_5: ctc_5
    :return: max climb thrust in Newton
    """
    t_isa = isa_temp(h)
    h /= 0.3048
    thrust_isa = C_1 * (1 - (h / C_2) + C_3 * (h ** 2))
    return thrust_isa * (1 - C_5 * (t_isa - T - C_4))


def calc_speed_of_sound(h):
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
    :return: Temperature in Kelvin
    """
    t = 288.15 - (6.5 / 1000) * h
    t_trop = 288.15 - (6.5 / 1000) * 11000
    if t > t_trop:
        return 216.65  # Unit: Kelvin
    else:
        return t


def transition_alt(v_cas, h):
    """
    Calculate the transition altitude for the tropopause
    :param v_cas: calculated air speed
    :param h: height
    :return: transition height
    """
    mach = calc_speed_of_sound(h)
    t_0_isa = 288.15  # Unit: Kelvin
    delta_trans = ((1 + 0.2 * (v_cas / 340.29) ** 2) ** 3.5 - 1) / (
        (1 + 0.2 * (mach ** 2)) ** 3.5 - 1
    )  # Func: 3.2-20
    theta_trans = delta_trans ** (1 / 5.25583)  # Using Approx: 3.2-15  -- Func: 3.2-19
    h_trans = (1000 / (0.3048 * 6.5)) * t_0_isa * (1 - theta_trans)  # Func: 3.2-18

    return h_trans
