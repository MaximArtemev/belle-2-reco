import pandas as pd
import numpy as np

import sys
import root_numpy
import root_pandas

df  = root_pandas.read_root("../data/raw/cosmic.0008.03420_03427_v4.root",columns=["Channel", "ADC", "Board", "Nhit", "Asic"])
df.to_csv('../data/raw/cosmic.csv.gz', index=False)
del df

dfm = root_pandas.read_root("../data/raw/mcmc.root",columns=["Channel", "ADC", "Board", "Nhit", "Asic","Track"]) # no cross talk
dfm.to_csv('../data/raw/mcmc_noxtalk.csv.gz', index=False)
del dfm

dfm2 = root_pandas.read_root("../data/raw/mcmc_xtalk.root",columns=["Channel", "ADC", "Board", "Nhit", "Asic","Track"])
dfm2.to_csv('../data/raw/mcmc_xtalk.csv.gz', index=False)
del dfm2

