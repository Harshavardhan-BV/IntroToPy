import os
import glob
import nbconvert
import subprocess
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def preprocess(path):
    ipy_files = glob.glob(path+'*.ipynb') 
    exportor = nbconvert.PythonExporter()
    for file in ipy_files:
        out_file = os.path.splitext(file)[0] + '.py'
        try:
            codes,res = exportor.from_filename(file)
            with open(out_file, 'w', encoding='utf-8') as f:
                f.write(codes)
        except:
            print('Problem with'+file)

def similarity_score(files):
    n = len(files)
    sim_scor = np.eye(n)
    for i in range(n):
        pathi = files[i]
        with open(pathi, 'r') as filei:
            i_lines = filei.readlines()
        for j in range(i+1,n):
            pathj = files[j]
            with open(pathj, 'r') as filej:
                j_lines = filej.readlines()
            file_len = max(len(np.unique(i_lines)),len(np.unique(j_lines)))
            c_lines = len(np.intersect1d(i_lines,j_lines))
            sim_scor[i,j] = c_lines/file_len
    sim_scor = sim_scor+sim_scor.T-np.eye(n)
    return sim_scor

def similarity_score_linux(files):
    comm1="comm -12 --nocheck-order "
    comm2="wc -l"
    n = len(files)
    sim_scor = np.eye(n)
    for i in range(n):
        for j in range(i+1,n):
            command = comm1 + "'" + files[i] +"' '" + files[j] + "' | "+ comm2
            c_lines = int(subprocess.check_output(command,shell=True).decode("utf-8").rstrip('\n'))
            command = comm2 + " '" + files[i] +"'"
            leni=int(subprocess.check_output(command,shell=True).decode("utf-8").split(' ')[0])
            command = comm2 + " '" + files[j] +"'"
            lenj=int(subprocess.check_output(command,shell=True).decode("utf-8").split(' ')[0])
            file_len=max(leni,lenj)
            sim_scor[i,j] = c_lines/file_len
    sim_scor = sim_scor+sim_scor.T-np.eye(n)
    return sim_scor

def sim_df(files,sim_scor):
    files = [x.split('- ')[-1] for x in files]
    df = pd.DataFrame(sim_scor,columns=files,index=files)
    return df

#Input (change here)
Tut = 'Tutorial-03'

indir='./Answers/'
outdir = './Output/'
path = indir+Tut+'-plag_check/'
outdf = outdir+Tut+'-sim_score.csv'
outsvg = outdir+Tut+'-cluster.svg'

preprocess(path)
files = glob.glob(path+'*.py')

ss = similarity_score(files)
df = sim_df(files,ss)
df.to_csv(outdf)

sns.clustermap(df)
plt.savefig(outsvg)
