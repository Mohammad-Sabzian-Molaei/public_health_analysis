import numpy as np
import pandas as pd
from scipy import stats

np.random.seed(0)

data = pd.DataFrame({
    "age": np.random.randint(20, 80, 100),
    "infection_rate": np.random.rand(100)
})

corr = stats.pearsonr(data["age"], data["infection_rate"])

print("Correlation:", corr)
