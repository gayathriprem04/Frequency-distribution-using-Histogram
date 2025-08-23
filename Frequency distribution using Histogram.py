import pandas as pd
import matplotlib.pyplot as plt
df=pd.DataFrame({'class':['A','A','B','A','B','C']})
plt.hist(df['class'],bins=3)
plt.show()