import pandas as pd
import os
from demo4 import data_file

print(os.getcwd())
data=pd.read_csv(data_file)
print(data)