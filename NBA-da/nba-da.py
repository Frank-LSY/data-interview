import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

if int(os.environ.get('MODERN_PANDAS_EPUB',0)):
    import prep

pd.options.display.max_rows=10
sns.set(style='ticks',context='talk')