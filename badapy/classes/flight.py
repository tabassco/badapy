import pandas as pd
import scipy.io as sio
import numpy as np
import pickle
from badapy.calculations.calc import *


class Flight:
    def __init__(self, tailsign, flightno, used_plane):
        self.tailsign = tailsign
        self.flightno = flightno
        self.flightdata = None
        self.used_plane = used_plane

    def load_flightdata(self, data_path, data_type='csv'):
        """
        Loads the Flight-Data from a given file path and type
        :param data_path: Path to the Flight-Data file
        :param data_type: Type of the Flight-Data
        :return:
        """
        flight_data = 0
        if data_type == 'csv':
            flight_data = pd.read_csv(data_path)
            flight_data['temp'] = flight_data['temp'].apply(lambda x: x + 273.15)
            flight_data['alt'] = flight_data['alt'].apply(lambda x: x * 0.3048)
            flight_data['rocd'] = flight_data['rocd'].apply(lambda x: x * 0.3048)
            flight_data['airspeed'] = flight_data['airspeed'].apply(lambda x: x * 0.514444)

        elif data_type == 'matlab':
            flight_data = sio.loadmat(data_path)

        elif data_type == 'pickle':
            with open(data_path, 'rb') as data:
                flight_data = pickle.load(data)

        else:
            if data_type not in ['csv', 'matlab', 'pickle']:
                raise ValueError('Invalid file format. Expected one of: %s' % ['csv', 'matlab', 'pickle'])

        self.flightdata = flight_data

    def __repr__(self):
        if self.flightdata is None:
            return 'Flight. No Flight-Data exists.'
        else:
            return 'Flight. Flight-Data exists.'

    def __str__(self):
        if self.flightdata is None:
            return 'No Flight-Data exists. Plane:{}'.format(self.used_plane)
        else:
            return 'Flight with {0} recorded data-points. Plane:{1}'.format(self.flightdata.shape[0], self.used_plane)

    def calculate_specific_fuel(self, method_used, i, thrust = None):
        thrust_spec_fuel_flow = self.used_plane.fuel['cf_1'] * (
                1 + ((self.flightdata.airspeed[i] / 0.514444) / self.used_plane.fuel['cf_2']))

        if method_used == 'thrust':  # Thrust specific fuel flow (climb / descent)
            nom_fuel_flow = thrust_spec_fuel_flow * thrust
            return nom_fuel_flow

        elif method_used == 'minimum':  # Minimum fuel flow (idle descent)
            min_fuel_flow = self.used_plane.fuel['cf_3'] * (
                        1 - (self.flightdata.alt[i] / self.used_plane.fuel['cf_4']))
            return min_fuel_flow

        else:  # Cruise fuel flow (cruise flight)
            cruise_fuel_flow = thrust_spec_fuel_flow * thrust * self.used_plane.fuel['cf_cr']
            return cruise_fuel_flow

    def calculate_fuel(self, sampling_rate=1):  # TODO: Add iterator for individual waypoints.
        """
        Calculates the Total Fuel Consumption [kg} by adding the specific f
        :param sampling_rate: time between recorded signals [Hz]
        :return: fuel_sum: total fuel used [kg]
        """
        fuel_sum = 0
        spec_fuel = []

        for i, row in self.flightdata.iterrows():
            max_cl = max_climb_thrust(row.alt, row.temp, self.used_plane.engine['ctc_1'],
                                      self.used_plane.engine['ctc_2'], self.used_plane.engine['ctc_3'],
                                      self.used_plane.engine['ctc_4'], self.used_plane.engine['ctc_5'])
            max_cr = 0.95 * max_cl
            max_des = self.used_plane.engine['ctd_high'] * max_cl
            c_l = (2 * self.used_plane.masses['reference'] * 9.81) / (density(row.alt * (row.airspeed ** 2) * self.used_plane.aero['surf'] * math.cos(0)))
            c_d = self.used_plane.config['CD0'] + self.used_plane.config['CD2'] * (c_l ** 2)
            drag = 0.5 * c_d * density(row.temp) * (row.airspeed ** 2) * self.used_plane.aero['surf']
            if i == 0:
                #  thrust = drag + self.used_plane.masses['reference'] * 1000 * ((9.81 * self.flightdata.rocd[i]) / self.flightdata.airspeed[i] + 0/sampling_rate)
                curr_fuel = np.nan
                spec_fuel.append(curr_fuel)
                continue
            else:
                thrust = drag + self.used_plane.masses['reference'] * 1000 * ((9.81 * (row.alt-self.flightdata.alt[i-1]) / sampling_rate) / row.airspeed + (row.airspeed-self.flightdata.airspeed[i-1])/sampling_rate)

            if row.rocd == 0 and thrust < max_cr:
                curr_fuel = self.calculate_specific_fuel('cruise', i, thrust/1000)
            elif row.rocd > 0 and thrust < max_cl:
                curr_fuel = self.calculate_specific_fuel('thrust', i, thrust/1000)
            elif row.rocd < 0 and max_des < thrust < max_cr:
                curr_fuel = self.calculate_specific_fuel('minimum', i, thrust/1000)
            else:
                curr_fuel = np.nan
            spec_fuel.append(curr_fuel)
            fuel_sum += curr_fuel / (sampling_rate / 60)
        print(fuel_sum)

        self.flightdata = self.flightdata.assign(current_fuel=np.array(spec_fuel))
        self.flightdata = (self.flightdata.ffill() + self.flightdata.bfill())/2
        self.flightdata = self.flightdata.bfill().ffill()
        return fuel_sum

    def calculate_distance(self):
        pass

    def show_waypoints(self):
        pass
