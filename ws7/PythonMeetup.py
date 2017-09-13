# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 13:45:33 2017

@author: Juhani Rantaniemi, Johan Salmelin
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ----- Datatypes ------

# ----- Tuple ------ #

#Immutable
solarpanels = (1, 2, 3) #IDs
powers = (3, 4, 5.1) #kW
efficiency = (0.7, 0.6, 0.65)
invertertypes = ("SMA", "LGA", "GE")

#Selection
solarpanels[0] #1

#Mathematical operations
sum(powers) #12.1

# ----- List ----- #
#Mutable
yearlysales = [2345, 4567, 5678]
yearlysales.append(6789) #[2345, 4567, 5678, 6789]

#Selection and mathematical operations the same


# ----- Numpy arrays ----- #

#Creation
solardata1 = np.array([solarpanels, powers, efficiency])
print (solardata1)

#Selection
solardata1[0,0] #first datapoint
solardata1[:,0] #first column
solardata1[[0,1],:] #first and second row
print (solardata1.T) #Transposed array

#Add and delete row
new_row1 = np.array([(10, 10, 10)])
solardata1 = np.concatenate((solardata1, new_row1), axis=0)
print (solardata1)

solardata1 = np.delete(solardata1, 3, axis=0)
print (solardata1)

#Add and delete column
new_col1 = np.array([(11,), (11,), (11,)])
solardata1 = np.concatenate((solardata1, new_col1), axis=1)
print (solardata1)
solardata1 = np.delete(solardata1, 3, axis=1)
print (solardata1)
#Array manipulations: https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.array-manipulation.html

# ---- Numpy Structured arrays ---- #

#Creation
transposed_data = list(zip(solarpanels, powers, efficiency, invertertypes))
solardata2 = np.array(transposed_data, dtype= 
                      [("SolarPanelId", "int"),
                       ("Power", "float"),
                       ("Efficiency", "float"),
                       ("InvType", "U20")])

#or
"""
np.core.records.fromarrays(numpy_array_name, 
                           names="SolarPanelId, Power, Efficiency, InvType",
                           formats = 'i8, f8, f8, U8')
"""

#Selection
solardata2["InvType"] #array(['SMA', 'LGA', 'GE']
solardata2[["SolarPanelId", "InvType"]] #array([(1, 'SMA'), (2, 'LGA'), (3, 'GE')]

#Mathematical operations - works also with np.array
np.mean(solardata2["Power"]) #4.0333
np.min(solardata2["SolarPanelId"]) #1
solardata2["Power"]*2 #array([  6. ,   8. ,  10.2])
solardata2["Power"]*solardata2["Efficiency"] #array([ 2.1  ,  2.4  ,  3.315])
#More operations: https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.math.html

#Add & Delete
new_row=np.array([(4, 3.33, 0.7, "Panasonic")], dtype= 
                      [("SolarPanelId", "int"),
                       ("Power", "float"),
                       ("Efficiency", "float"),
                       ("InvType", "U20")])
print (new_row)
solardata2 = np.concatenate((solardata2, new_row), axis=0)
solardata2 = np.delete(solardata2, 3, axis=0)
print (solardata2)

#Conditional operations - works also with np.array
solardata2["Power"]>3.5 #array([False,  True,  True], dtype=bool)
solardata2[solardata2["Power"]<3.5]#array([(1,  3.  ,  0.7, 'SMA'), (4,  3.33,  0.7, 'Panasonic')]
solardata2[(solardata2["Power"]==3) & (solardata2["Efficiency"]==0.7)] #array([(1,  3.,  0.7, 'SMA')]

#Numpy vs. Pandas -performance
#http://gouthamanbalaraman.com/blog/numpy-vs-pandas-comparison.html


# ----- Pandas ------

#--- Series (columns) ---
pd.Series(np.random.randn(5))
datetimerange = pd.Series(pd.date_range('1.1.2017', periods=24, freq='H'))
print(datetimerange)

#Timezone conversions
from datetime import datetime
utcdaterange = datetimerange.dt.tz_localize('EET').dt.tz_convert('UTC')
print(utcdaterange)

#---- Dataframes (Matrices) ----

#From structured array
solardata_df = pd.DataFrame(solardata2)

#From file
path="H:\spring\pworkshop\MeetupHeatingData.csv"
heatdata_df=pd.read_csv(path, sep=";", header=0, decimal=",")
heatdata_df
heatdata_df.head()

#Handling missing data:
heatdata_df=heatdata_df.fillna(method="ffill")

#Access data
heatdata_df["Heating"]

#Mathematical operations.
heatdata_df["Temperature"].mean()

#Adding new column:
heatdata_df["DateTime"] = pd.to_datetime(heatdata_df["DateTime"]) #Change column to datetime-format
heatdata_df["Hours"]=heatdata_df["DateTime"].dt.hour #Create new column of the hours
heatdata_df["Heatingx2"]=heatdata_df["Heating"]*2
del heatdata_df["Heatingx2"]

#Merges / Joins:
pd.merge(heatdata_df, solardata_df[["SolarPanelId","InvType"]],   how="inner", left_on="Hours", right_on="SolarPanelId").head()
#https://blog.codinghorror.com/a-visual-explanation-of-sql-joins/

#Draw  charts:
plt.plot(heatdata_df["Temperature"], heatdata_df["Heating"], 'ro')
plt.show()

#Read mode: https://pandas.pydata.org/pandas-docs/stable/dsintro.html



# ----- PuLP ------

#instructions for installing PuLP:
#https://pythonhosted.org/PuLP/main/installing_pulp_at_home.html

#instructions for installing CBC:
#https://projects.coin-or.org/Cbc

from pulp import *
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file = 'MeetupOptimData.xlsx' # file must be in working directory

xl = pd.ExcelFile(file)
print(xl.sheet_names)

ex_data = xl.parse('PythonMeetupData')

TIME = ex_data['TIME'].values.tolist() # Get TIME values
SPOTPRICES = ex_data['SPOTPRICES'].values.tolist() # Get SPOT prices (€/MWh)

# Powers of devices
PX = 4 # kW
PY = 3
PZ = 2

# Energy capacities of devices
CX = 16 #kWh
CY = 15

# Upper bound of hourly consumption
UB = 8 #kW (kWh)

# Decision variables
X = pulp.LpVariable.dicts( "EV",TIME,0,1,LpInteger ) 
Y = pulp.LpVariable.dicts( "WH", TIME,0,1,LpInteger ) 
Z = pulp.LpVariable.dicts( "ER", TIME,0,1,LpInteger ) 

# Problem name and type
prob  = pulp.LpProblem( "SPOT OPTIMIZATION", pulp.LpMinimize )

# Objective function
prob += pulp.lpSum( [ SPOTPRICES[t]/1000*( PX*X[t] + PY*Y[t] + PZ*Z[t] ) for t in TIME ]  )

# Constraints
for t in TIME:
    prob += PX*X[t] + PY*Y[t] + PZ*Z[t]  <= UB # Upper bound is not exceeded
    
prob += pulp.lpSum( PX*X[t] for t in TIME[0:8] ) == CX # Electric Vehicle is fully charged at 8:00

for t in TIME[8:24]:
    prob += X[t] == 0 # Cannot charge EV after 8:00

prob += pulp.lpSum( PY*Y[t] for t in TIME) >= CY  # Water Heater gets at least 15 kWh/day so that 
                                                        # you can get warm water 
    
prob+= pulp.lpSum( Z[t] for t in TIME ) >= 21 # Electric radiator can be switched off only 3h per day


# Solve the problem
prob.solve()

# Print status of the problem
print("Status: ",pulp.LpStatus[prob.status])

# Function that prints values of decision variables
def printVar( Var ):
        for t in TIME:
            print(Var[t].name, "=", Var[t].varValue)
        print('---------------')

#Function that plots Spot prices and values of decision variables
def plotVar( Var1, Var2, Var3 ):
    f, axarr = plt.subplots(4,sharex=True)
    p1 = [0 for j in range(24)]
    p2 = [0 for j in range(24)]
    p3 = [0 for j in range(24)]
    for t in TIME:
        p1[int(t)] = Var1[t].varValue
        p2[int(t)] = Var2[t].varValue
        p3[int(t)] = Var3[t].varValue
    axarr[1].plot(p1)
    axarr[1].set_title("Electric vehicle battery charging")
    axarr[1].xaxis.set_ticks(np.arange(0, 24, 1))
    axarr[2].plot(p2)
    axarr[2].set_title("Water heater")
    axarr[2].xaxis.set_ticks(np.arange(0, 24, 1))
    axarr[3].plot(p3)
    axarr[3].set_title("Electric radiator")
    axarr[2].xaxis.set_ticks(np.arange(0, 24, 1))
    axarr[0].plot(SPOTPRICES,'b')
    axarr[0].set_title("Spot prices")
    axarr[0].xaxis.set_ticks(np.arange(0, 24, 1))
    f.tight_layout()
    f.subplots_adjust(top=0.95)
# Print and plot variables
printVar(X)
printVar(Y)
printVar(Z)
plotVar(X,Y,Z)
#Print value of objective function
print("Value of objective function:",value(prob.objective))



# ----- Concurrency ------
import timeit
import time
import numpy as np
from threading import Thread
import concurrent.futures

#Threading / Processing
def print_task(taskname):
    time.sleep(3)
    print("{}: Print task done".format(taskname))

if __name__ == '__main__':
    t=Thread(target=print_task, args=("Bob",))
    #t.setDaemon(False/True) Does thread Exit when called Exits or not
    t.start()
    #t.join()
    print ("Print task started")

#ThreadPoolExecutor & Multiprocessing
def math_task(x, y):
    results=[]
    for i in range(0, x): #Tee n kertaa
        results.append(i)
    if y==0:
        print(1+"a")
    return("Task Ok")

def start_with_Executor(data):
    msg_statuses = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_ID = {executor.submit(math_task, row[0], row[1]):row[1] for row in data}
        for future in concurrent.futures.as_completed(future_to_ID): # completed futures
            ID = future_to_ID[future]
            try:
                msg_status = future.result() # output
            except Exception as e:
                print("{} generated an exception: {}".format(ID, e))
                msg_status = -1
            msg_statuses.append([ID,msg_status])
    print (msg_statuses)

if __name__ == '__main__':
    #Create test data
    fact_nums=list(range(0, 1001)) # list of [1,2..1000]
    div_nums=list(range(-1000, 1)) # list of [-999, -998....0]
    data = np.column_stack((fact_nums,div_nums))
    
    #Start timing
    start_time = timeit.default_timer()
    
    #Run concurrency
    start_with_PoolExecutor(data)

    #Print execution time
    print ("Run-time: {} seconds".format(timeit.default_timer() - start_time))

#Read more on Grid Interpreter Lock.
#See also multiprocessing -library
