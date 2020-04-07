#!/usr/bin/env python
# coding: utf-8

# In[1]:


from root_pandas import read_root
from glob import glob
import pandas as pd


# In[2]:


from matplotlib.pyplot import *
get_ipython().run_line_magic('matplotlib', 'inline')
from numpy import *
from matplotlib.colors import LogNorm
from matplotlib.patches import *
import matplotlib.pyplot as plt
from scipy.optimize import leastsq
#import b2plot
#style.use('belle2')


# In[3]:


#df = read_root("cosmic.0008.03427.root")

#df = read_root("b.root")
df  = read_root("cosmic.0008.03420_03427_v4.root",columns=["Channel", "ADC", "Board", "Nhit", "Asic"])
#dfm = read_root("mcmc.root",columns=["Channel", "ADC", "Board", "Nhit", "Asic"]) # no cross talk


# In[4]:


dfm = read_root("mcmc.root",columns=["Channel", "ADC", "Board", "Nhit", "Asic","Track"]) # no cross talk
dfm2 = read_root("mcmc_xtalk.root",columns=["Channel", "ADC", "Board", "Nhit", "Asic","Track"])
#dfm2 = read_root("mctt.root",columns=["Channel", "ADC", "Board", "Nhit", "Asic","Track"])
#mc3.root


# In[5]:


xlim(1,8)
h = hist(df[df.ADC_ADC_Sig>1000].Nhit,8,(0,8),density=True,label='Data')
h = hist(dfm[dfm.ADC_ADC_Sig>1000].Nhit,8,(0,8),density=True,label='MC XTalk Off',histtype='step')
h = hist(dfm2[dfm2.ADC_ADC_Sig>1000].Nhit,8,(0,8),density=True,histtype='step',label='MC XTalk ON')
xlabel('Nhit per ASIC for ADC>1000')
legend()
savefig("xtalk_test.png")

