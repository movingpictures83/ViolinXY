import torch
import numpy as np
import sys

#from networks.PIsToN_multiAttn import PIsToN_multiAttn
#from networks.ViT_pytorch import get_ml_config

#from utils.dataset import PISToN_dataset
import os
import numpy as np
import pandas as pd

# In[19]:


import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('ggplot')
#sns.set_style('whitegrid')
plt.subplots(figsize=(6, 3))

import PyIO
import PyPluMA
import pickle

class ViolinXYPlugin:
    def input(self, inputfile):
      self.parameters = PyIO.readParameters(inputfile)
    def run(self):
        pass
    def output(self, outputfile):
      if (self.parameters["scorefile"].endswith("csv")):
         self.scores_df = pd.read_csv(PyPluMA.prefix()+"/"+self.parameters["scorefile"])
      else:
         myfile = open(PyPluMA.prefix()+"/"+self.parameters["scorefile"], "rb")
         self.scores_df = pickle.load(myfile)
      self.scores_df.to_csv("trevor2.csv")
      if ("order" in self.parameters):
          order = PyIO.readSequential(PyPluMA.prefix()+"/"+self.parameters["order"])
          gfg = sns.violinplot(data=self.scores_df, x=self.parameters["x"], y=self.parameters["y"], order=order)
      else:
          gfg = sns.violinplot(data=self.scores_df, x=self.parameters["x"], y=self.parameters["y"], cut=0)
      if ("ylim1" in self.parameters):
          ylim1 = float(self.parameters["ylim1"])
          ylim2 = float(self.parameters["ylim2"])
          plt.ylim(ylim1, ylim2)
      # sns.kdeplot(data=scores_df, x='PIsToN_score', hue='CAPRI_quality', fill=True)
      # #sns.despine()
      # plt.show()
      plt.savefig(outputfile,dpi=600)



