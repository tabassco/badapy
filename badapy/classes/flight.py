class flight():
    def __init__(self, tailsign, flightno, flightdata, used_plane):
        self.tailsign = tailsign
        self.flightno = flightno
        self.flightdata = flightdata
        self.used_plane = used_plane

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def calculate_fuel(self, method_used='minimum'):  # TODO: Add iterator for individual waypoints.
        """
        Calculates the specific fuel consumption [kg/min] to then calculate the total fuel used
        :param method_used: Choice of "thrust", "minimum", "cruise"
        :return: fuel_flow:
        """
        if method_used not in ['thrust', 'minimum', 'cruise']:
            raise ValueError('Invalid calculation method. Expected one of: %s' % ['thrust', 'minimum', 'cruise'])

        thrust_spec_fuel_flow = self.used_plane.fuel['cf_1'] * (
                    1 + (self.flightdata.airspeed / self.used_plane.fuel['cf_2']))
        if method_used == 'thrust':  # Thrust specific fuel flow
            nom_fuel_flow = thrust_spec_fuel_flow * self.flightdata.thrust
            return nom_fuel_flow

        elif method_used == 'minimum':  # Minimum fuel flow
            min_fuel_flow = self.used_plane.fuel['cf_3'] * (1 - (self.flightdata.height / self.used_plane.fuel['cf_4']))
            return min_fuel_flow

        else:  # Cruise fuel flow
            cruise_fuel_flow = thrust_spec_fuel_flow * self.flightdata.thrust * self.used_plane.fuel['cf_cr']
            return cruise_fuel_flow

    def calculate_distance(self):
        pass

    def waypoint_iterator(self):
        pass

    def show_waypoints(self):
        pass
