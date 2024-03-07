import numpy as np

with np.load('cv05data.npz') as npz_file:
    print()
    xt = npz_file['xt']
    yt = npz_file['yt']