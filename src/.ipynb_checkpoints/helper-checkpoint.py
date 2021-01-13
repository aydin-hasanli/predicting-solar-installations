import pandas as pd
import numpy as np
import glob
import os

class Starter():
    '''
    '''
    def __init__(self):
        self.self = self
        self.path = r'/home/aydin/Desktop/dsi_lax3/capstones/capstone3_data'

    def load_concat(self):
        all_files = glob.glob(os.path.join(path, "*.csv")) 
        df_from_each_file = (pd.read_csv(f, engine = 'python', na_values= [-9999, '-9999'] ) for f in all_files)
        df = pd.concat(df_from_each_file, ignore_index=True)
        return df

    
def time_series_plotter(plot_obj, figsize=(6.4 * 2, 4.8 / 2), suptitle='', *args, **kwargs):
    fig, ax = plt.subplots(figsize=figsize)
    fig.suptitle(suptitle, size='xx-large')
    plot_obj(ax, *args, **kwargs)
    
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()