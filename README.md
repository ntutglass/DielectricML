Machine learning models for predicting dielectric constant and loss of oxide glasses under different temperatures and frequencies.

Here, you will first find four pickle files for Scikit-Learn:
1. "const_chem.pkl", an artificial neural network model trained by the chemical composition descriptors for temperature/frequency-dependent dielectric constant prediction.
2. "loss_chem.pkl", an artificial neural network model trained by the chemical composition descriptors for temperature/frequency-dependent dielectric loss prediction.
3. "const_elem.pkl", an artificial neural network model trained by the element physical and chemical properties descriptors for temperature/frequency-dependent dielectric constant prediction.
4. "loss_elem.pkl", a Gaussian process regression model trained by the element physical and chemical properties descriptors for temperature/frequency-dependent dielectric constant prediction.

Second, two Python scripts are used for data pre-processing and executing the trained model.
1. "dielectric_chem.py" is for the model using the chemical composition descriptors (pickle files 1 and 2).
2. "dielectric_elem.py" is for the model using the element physical and chemical properties descriptors (pickle files 3 and 4).  

If you have any questions, please contact Yueh-Ting (Tim) Shih at ytshih@mail.ntut.edu.tw.
