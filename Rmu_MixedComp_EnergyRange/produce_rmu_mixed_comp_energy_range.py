import pandas as pd
import numpy as np

import sys
sys.path.insert(1, '../src')

import MuonMap

#generate theta following cos(theta) sin(theta) distribution over theta range from uniform r.v
def compute_theta(u, theta_min, theta_max):
    return .5*np.arccos(np.cos(2*theta_min) - u*(np.cos(2*theta_min) - np.cos(2*theta_max)))

#generate energy follwing power law with spectram index gamma
def compute_energy(u, energy_min, energy_max, gamma):
    comp_gamma = 1 - gamma
    energy_min_gamma = np.power(energy_min, comp_gamma)
    energy_max_gamma = np.power(energy_max, comp_gamma)
    return np.power(energy_min_gamma - u*(energy_max_gamma - energy_min_gamma), 1 / comp_gamma)

#generate mass composition of primary where 0 = proton, 1 = helium, 2 = nitrogen, 3 = iron
def get_composition(u, frac_mass_file):

    #composition array
    prob_primary =

    if u < frac_mass_file
#generate distribution of rmu from rmu distribution at fixed energy and for each primary
def get_rmu_dist(n_events, energy, theta, model, rmu_dist_list):
