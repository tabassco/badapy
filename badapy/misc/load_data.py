def split_opf(file_path):
    """
    returns a set of lists with aircraft performance parameters
    :param file_path:
    :return: 
    """
    with open(file_path) as read_in:
        file = read_in.readlines()

    """
    Masses
    """
    mass = file[18].split()
    mass_names = ["reference", "minimum", "maximum", "max_payload", "mass_grad"]
    mass = [float(x) for x in mass[1:6]]
    mass_dict = dict(zip(mass_names, mass))

    """
    Flight Envelope
    """
    flight_env = file[21].split()
    flight_env = [float(x) for x in flight_env[1:6]]
    flight_env_names = ["VMO", "MMO", "max_alt", "h_max", "temp_grad"]
    flight_env_dict = dict(zip(flight_env_names, flight_env))

    """
    Aerodynamics
    """
    aero = file[25].split()
    aero = [float(x) for x in aero[2:6]]
    aero_names = ["surf", "Clbo", "k", "CM16"]
    aero_dict = dict(zip(aero_names, aero))

    # Configuration Characteristics
    config_names = ["Vstall", "CDO", "CD2", "Name"]
    config_CR = file[28].split()
    config_CR = [float(x) for x in config_CR[4:7]].append('clean')
    config_CR_dict = dict(zip(config_names, config_CR))

    config_IC = file[29].split()
    config_IC = [float(x) for x in config_CR[4:7]].append('Flap18')
    config_IC_dict = dict(zip(config_names, config_IC))

    config_TO = file[30].split()
    config_TO = [float(x) for x in config_CR[4:7]].append('Flap24')
    config_TO_dict = dict(zip(config_names, config_TO))

    config_AP = file[31].split()
    config_AP = [float(x) for x in config_CR[4:7]].append('Flap30')
    config_AP_dict = dict(zip(config_names, config_AP))

    config_LD = file[32].split()
    config_LD = [float(x) for x in config_CR[4:7]].append('Flap33')
    config_LD_dict = dict(zip(config_names, config_LD))

    """
    Engine Thrust
    """
    climb_thrust = file[44].split()
    climb_thrust = [float(x) for x in climb_thrust[1:6]]
    climb_names = ["ctc_1", "ctc_2", "ctc_3", "ctc_4", "ctc_5"]
    climb_dict = dict(zip(climb_names, climb_thrust))

    desc_thrust = file[46].split()
    desc_thrust = [float(x) for x in desc_thrust[1:6]]
    desc_names = ["ctcd_low", "ctd_high", "h_des", "ctd_app", "ctd_ld"]
    desc_dict = dict(zip(desc_names, desc_thrust))

    ref_speed = file[48].split()
    ref_speed = [float(x) for x in ref_speed[1:3]]
    ref_names = ["vd_ref", "machd_ref"]
    ref_dict = dict(zip(ref_names, ref_speed))

    engine_dict = {**climb_dict, **desc_dict, **ref_dict}

    """
    Fuel Consumption
    """
    fuel_thrust_val = file[51].split()
    fuel_thrust_val = [float(x) for x in fuel_thrust_val[1:3]]
    fuel_thrust_names = ["cf_1", "cf_2"]
    fuel_thrust_dict = dict(zip(fuel_thrust_names, fuel_thrust_val))

    fuel_desc_val = file[53].split()
    fuel_desc_val = [float(x) for x in fuel_desc_val[1:3]]
    fuel_desc_names = ["cf_3", "cf_4"]
    fuel_desc_dict = dict(zip(fuel_desc_names, fuel_desc_val))

    fuel_cruise = file[55].split()
    fuel_cruise = [float(x) for x in fuel_cruise[1]]
    fuel_dict = dict(zip(["cf_cr"], fuel_cruise))

    fuel_dict = {**fuel_thrust_dict, **fuel_desc_dict, **fuel_dict}

    return mass_dict, flight_env_dict, aero_dict, config_CR_dict, engine_dict, fuel_dict


def split_afp(file_path):
    procedure_climb_dict = None
    procedure_cruise_dict = None
    procedure_desc_dict = None

    return procedure_climb_dict, procedure_cruise_dict, procedure_desc_dict