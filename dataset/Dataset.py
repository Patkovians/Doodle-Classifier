
#global
import os
import numpy as np
from urllib.request import urlretrieve

class Dataset:

    def __init__(self,
        name,
        default_url="https://storage.googleapis.com/quickdraw_dataset/full/numpy_bitmap",
        basedir="data/"):

        if not os.path.exists(basedir):
            os.mkdir(basedir)

        filename=f"{basedir}/{name}"
        urlretrieve(f"{default_url}/{name}.npy", filename)
        arr = np.load(filename)
        print(arr)