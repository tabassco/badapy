from ..misc.load_data import *
from os import path


class Airplane:
    def __init__(self, plane_type, model):
        self.type = plane_type
        self.model = model
        self.description = None

        # Information from OPF File
        self.masses = None
        self.flight_env = None
        self.aero = None
        self.config = None
        self.engine = None
        self.fuel = None

        # Information from AFP File
        self.proc_climb = None
        self.proc_cruise = None
        self.proc_desc = None

    def load_information(self, file_path):
        data_folder = path.join(file_path)

        self.description, self.masses, self.flight_env, self.aero, self.config, self.engine, self.fuel = split_opf(
            path.join(data_folder, self.type + "__.OPF"))

        self.proc_climb, self.proc_cruise, self.proc_desc = split_afp(path.join(data_folder, (self.type + "__.AFP")))

    def __str__(self):
        return '{}'.format(self.description)

    def __repr__(self):
        return '{}'.format(self.description)
