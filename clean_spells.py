import numpy as np
import pandas as pd
data = pd.read_csv('Spells.csv',error_bad_lines=False)

data.columns = data.columns.str.replace(" ", "-")
data.columns = data.columns.str.lower()