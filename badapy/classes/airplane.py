from ..misc.load_data import *
from os import path


class Airplane:
    def __init__(self, plane_type, model):
        self.type = plane_type
        self.model = model

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

        self.masses, self.flight_env, self.aero, self.config, self.engine, self.fuel = split_opf(
            path.join(data_folder, self.type, "__.OPF"))  # add path

        self.proc_climb, self.proc_cruise, self.proc_desc = split_afp(path.join(data_folder, self.type, "__.AFP"))

    def __str__(self):
        pass

    def __repr__(self):
        pass