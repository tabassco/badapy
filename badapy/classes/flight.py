import pandas as pd
import scipy.io as sio
import pickle


class Flight():
    def __init__(self, tailsign, flightno, used_plane):
        self.tailsign = tailsign
        self.flightno = flightno
        self.flightdata = None
        self.used_plane = used_plane

    def load_flightdata(self, data_path, data_type = 'csv'):
        """
        Loads the Flight-Data from a given file path and type
        :param data_path: Path to the Flight-Data file
        :param data_type: Type of the Flight-Data
        :return:
        """

        if data_type == 'csv':
            flight_data = pd.read_csv(data_path)

        elif data_type == 'matlab':
            flight_data = sio.loadmat(data_path)

        elif data_path == 'pickle':
            with open(data_path, 'rb') as data:
                flight_data = pickle.load(data)

        else:
            if data_type not in ['csv', 'matlab', 'pickle']:
                raise ValueError('Invalid calculation method. Expected one of: %s' % ['csv', 'matlab', 'pickle'])

        flight_data

        self.flightdata = flight_data

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def calculate_specific_fuel(self, method_used, i):
        thrust_spec_fuel_flow = self.used_plane.fuel['cf_1'] * (
                1 + (self.flightdata.airspeed / self.used_plane.fuel['cf_2']))

        if method_used == 'thrust':  # Thrust specific fuel flow
            nom_fuel_flow = thrust_spec_fuel_flow * self.flightdata.thrust
            return nom_fuel_flow

        elif method_used == 'minimum':  # Minimum fuel flow
            min_fuel_flow = self.used_plane.fuel['cf_3'] * (
                        1 - (self.flightdata.height / self.used_plane.fuel['cf_4']))
            return min_fuel_flow

        else:  # Cruise fuel flow
            cruise_fuel_flow = thrust_spec_fuel_flow * self.flightdata.thrust * self.used_plane.fuel['cf_cr']
            return cruise_fuel_flow

    def calculate_fuel(self, method_used='minimum', sampling_rate=1):  # TODO: Add iterator for individual waypoints.
        """
        Calculates the Total Fuel Consumption [kg} by adding the specific f
        :param method_used: Choice of "thrust", "minimum", "cruise"
        :param sampling_rate: time between waypoints [min]
        :return: fuel_sum: total fuel used [kg]
        """

        if method_used not in ['thrust', 'minimum', 'cruise']:
            raise ValueError('Invalid calculation method. Expected one of: %s' % ['thrust', 'minimum', 'cruise'])
        fuel_sum = 0
        spec_fuel = []

        for i in range(self.flightdata.shape[0]):
            curr_fuel = self.calculate_specific_fuel(method_used, i) * sampling_rate
            spec_fuel.append(curr_fuel)
            fuel_sum += curr_fuel

        return fuel_sum

    def calculate_distance(self):
        pass

    def show_waypoints(self):
        pass
