#Input column 1-39 correspond to p=2, p=3, p=5, p=7, Atomic number, Atomic number_d, Atomic volume, Atomic volume_d, Atomic weight, Atomic weight_d, Boiling point, Boiling point_d, Covalent radius, Covalent radius_d, Density, Density_d, Dipole polarizability, Dipole polarizability_d, Heat of formation, Heat of formation_d, Melting point, Melting point_d, VDW radius, VDW radius_d, Period, Period_d, Group, Group_d, 1st ionization energy, 1st ionization energy_d, 2nd ionization energy, 2nd ionization energy_d, 3rd ionization energy, 3rd ionization energy_d, s/total, p/total, Ionicity, Temp, and logf
import numpy as np
import pickle
from sklearn import preprocessing

#load and standardize data  
cond = open("condition", "r")
X = np.loadtxt(cond, usecols=range(39))
X_std = preprocessing.scale(X)

#load trained model
pkl_filename = "pickle_model.pkl"
with open(pkl_filename, 'rb') as file:
    pickle_model = pickle.load(file)

#test random sample
Y_predictions = pickle_model.predict(X_std)

#output result
np.savetxt('output_predictions', Y_predictions) 
