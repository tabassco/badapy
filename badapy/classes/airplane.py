from ..misc.load_data import *
from os import path
class airplane:
    def __init__(self, type, model):
        self.type = type
        self.model = model


    def load_information(self, file_path):
        data_folder = path.join(file_path)

        self.masses, self.flight_env, self.wing_area, self.config, self.engine, self.fuel = split_opf(path.join(data_folder, self.type, "__.OPF")) # add path
        self.proc_climb, self.proc_cruise, self.proc_desc = split_afp(path.join(data_folder, self.type, "__.AFP"))


    def __str__(self):
        pass


    def __repr__(self):
        pass
