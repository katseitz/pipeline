import pandas as pd
import numpy as np  
import glob
import csv
import itertools, os, glob

path_conn = ('/projects/b1108/studies/transitions/data/processed/neuroimaging/aib_networks_rest') #or use below for same data
#path_conn = ('/Volumes/ACNL/data_pre_2023/ACarroll/BrainMAPD_T4_rsfMRI/Connectivity')
save_dir1 = ('/projects/b1108/studies/transitions/data/processed/neuroimaging/aib_networks_rest/final_data')
#save_dir2 = ('/Volumes/ACNL/data_pre_2023/ACarroll/BrainMAPD_T4_rsfMRI/Connectivity/Output')
allFiles_conn = glob.glob(os.path.join(path_conn, '*/ses-1/*corrmat.csv'))

#output lists
network_list_output = []
network_output = []

#loop through each file
for file in allFiles_conn:
    parts = file.split("/")[-1].split("_")
    subject = parts[0] #identify particiapnt
    print(subject)
    run = parts[2] #identify network
    network = parts[3]
    print(subject, run, network)
    mattcor = pd.read_csv(file, header=None) #read the network matrix
    mattcor.values[np.tril_indices_from(mattcor)] = np.nan #fill below the diagonal with nans
    mattcor_z = mattcor.transform(lambda x: np.arctanh(x)) #fishers r to z transformation on r values
    #mattcor_z.replace([np.inf, -np.inf], np.nan, inplace=True)
    average = mattcor_z.unstack().mean() #average across all z values that are not nans
    network_list_output.append([subject, network, run, average])
    network_output.append({'participant': subject, 'network': network, 'run': run, 'value': average}) #preferred format
    

Output = pd.DataFrame(network_output)

#convert df to wide format (from long format)
#https://towardsdatascience.com/long-and-wide-formats-in-data-explained-e48d7c9a06cb
#Wide_Output = Output.pivot(index=['participant', 'run'], columns='network', values='value').reset_index()

#save data to both local and ACNL drives

path_output_save1 = save_dir1 + os.path.sep + 'Transitions_rsfMRIConnectivity_071124.csv'
Output.to_csv(path_output_save1, index=False) #do no save the index column
