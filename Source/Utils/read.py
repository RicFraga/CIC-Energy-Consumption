import os
import pandas as pd
from datetime import datetime

def read_data(ignore_irregular = False):
    PATH = '../Data/Raw'
    files = os.listdir(PATH)
    df = pd.DataFrame()
    for file in files:
        aux_df = pd.read_excel(os.path.join(
            PATH,
            file
        ), sheet_name = file.split('.')[0], usecols = ['Fecha', 'Medida'])

        df = pd.concat([aux_df.iloc[:-3], df])
    if(ignore_irregular):
        cut_date = datetime.strptime('2018-12-31 23:50:00', '%Y-%m-%d %H:%M:%S')
        df = df[df['Fecha'] > cut_date]

    return df.reset_index(drop = True)