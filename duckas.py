# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 18:14:56 2024

@author: Armin
"""

import torch

# Check if GPU is available
if torch.cuda.is_available():
    print(f"CUDA is available. Using GPU: {torch.cuda.get_device_name(0)}")
else:
    print("CUDA is not available. Using CPU.")




from datetime import datetime
from tickterial import Tickloader
import matplotlib.pyplot as plt
import numpy as np




correlations = []
if True:
    
    prevprice = 0
    prevnb = []
    prevna = []

    deltaprice = []
    deltabin = []
    bias = 0
    base = 0
    pbias = 0
    nbias = 0
    for hour in range(0,24):
        tickloader = Tickloader()
        period = datetime(hour=hour, day=24,month=6, year=2024)
            
        print(period.ctime())
        
        ticks = list()
        if data := tickloader.download('XAUUSD', period):
            for tick in data:
                ticks.append(tick)
            
            nb, binb, pb = plt.hist(np.diff([i["bid"] for i in ticks[0:]]), bins=10, alpha=0.7,)
            na, binda, pa = plt.hist(np.diff([i["ask"] for i in ticks[0:]]), bins=10, color="red", alpha=0.7,)
            plt.show()
            
        
        if(len(ticks) < 50):
            continue
        # current_price = np.mean([i["bid"] for i in ticks[0:]])
        current_price = ticks[-1]["bid"]
        
        if prevprice > 0:
            if abs(prevnb[-1] - prevna[-1]) > 0:
                if((current_price - prevprice < 0) == (prevnb[-1] - prevnb[0] > 0)):
                    bias += 1
                    pbias+=1
                else:
                    bias -= 1
                    nbias+=1
                    
                base+=1
                    
                deltaprice.append(current_price - prevprice > 0)
                deltabin.append(prevnb[-1] - prevnb[0] > 0)
                    
                
        prevnb = nb
        prevna = na
        prevprice = current_price
    
    # print("delt aprice: ", deltaprice)
    # print("delta bin: ", deltabin)
    mat = correlation_matrix = np.corrcoef(deltaprice, deltabin)
    # print("corelation is:",mat[0,1] )
    print("\n\n\nportion is:", bias / base,"\n")
    # print("base is:", base)
    # print("bias is:", bias)
    print("pbase is:", pbias)
    print("nbias is:", nbias)
    
    
    correlations.append(deltaprice == deltabin)




print("Overall:", correlations)