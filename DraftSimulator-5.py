import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
import numpy as np
from numpy import log as ln
import math


#draft counter
count = 1


#read csvs using pandas
df_sreek = pd.read_csv('sreek.csv', index_col='Position')
df_sammy = pd.read_csv('sammy.csv', index_col='Position')
df_robel = pd.read_csv('robel.csv', index_col='Position')
df_parsa = pd.read_csv('parsa.csv', index_col='Position')
df_madhav = pd.read_csv('madhav.csv', index_col='Position')
df_ben = pd.read_csv('ben.csv', index_col='Position')
df_arjun = pd.read_csv('arjun.csv', index_col='Position')

#draft score that everyone starts with
sreek_score = 100.0
sammy_score = 100.0
robel_score = 100.0
parsa_score = 100.0
madhav_score = 100.0
ben_score = 100.0
arjun_score = 100.0


#used pandas and numpy for logarithmic regression 
#df = pd.read_csv("MasterList.csv")
#x = np.arange(1, 43, 1)
#y = np.array(df.TrueVBD)
#plt.scatter(x, y)
#plt.savefig("plot.png")
#fit = np.polyfit(np.log(x), y, 1)
#print(fit) 
#y2 = 9.84435213 - 2.51900962*ln(x)
#plt.plot(x,y2, 'r')
#plt.savefig("plot.png")

#calculation 
def calc(x):
  value = 9.84435213 - 2.51900962*ln(x)
  return value



#draft for each team
def sreek():
  position = input("Enter position: ")
  name = input("Enter name: ")
  vbd = float(input("Enter VBD: "))
  df_sreek.loc[position, 'Name'] = name
  df_sreek.loc[position, 'VBD'] = vbd
  df_sreek.to_csv('sreek.csv')
  change = calc(count) - vbd
  global sreek_score
  sreek_score = sreek_score - (4*change)
  df_sreek.loc['QB','Score'] = sreek_score
  df_sreek.to_csv('sreek.csv')
def sammy():
  position = input("Enter position: ")
  name = input("Enter name: ")
  vbd = float(input("Enter VBD: "))
  df_sammy.loc[position, 'Name'] = name
  df_sammy.loc[position, 'VBD'] = vbd
  df_sammy.to_csv('sammy.csv')
  change = calc(count) - vbd
  global sammy_score
  sammy_score = sammy_score - (4*change)
  df_sammy.loc['QB','Score'] = sammy_score
  df_sammy.to_csv('sammy.csv')
def robel():
  position = input("Enter position: ")
  name = input("Enter name: ")
  vbd = float(input("Enter VBD: "))
  df_robel.loc[position, 'Name'] = name
  df_robel.loc[position, 'VBD'] = vbd
  df_robel.to_csv('robel.csv')
  change = calc(count) - vbd
  global robel_score
  robel_score = robel_score - (4*change)
  df_robel.loc['QB','Score'] = robel_score
  df_robel.to_csv('robel.csv')
def parsa():
  position = input("Enter position: ")
  name = input("Enter name: ")
  vbd = float(input("Enter VBD: "))
  df_parsa.loc[position, 'Name'] = name
  df_parsa.loc[position, 'VBD'] = vbd
  df_parsa.to_csv('parsa.csv')
  change = calc(count) - vbd
  global parsa_score
  parsa_score = parsa_score - (4*change)
  df_parsa.loc['QB','Score'] = parsa_score
  df_parsa.to_csv('parsa.csv')
def madhav():
  position = input("Enter position: ")
  name = input("Enter name: ")
  vbd = float(input("Enter VBD: "))
  df_madhav.loc[position, 'Name'] = name
  df_madhav.loc[position, 'VBD'] = vbd
  df_madhav.to_csv('madhav.csv')
  change = calc(count) - vbd
  global madhav_score
  madhav_score = madhav_score - (4*change)
  df_madhav.loc['QB','Score'] = madhav_score
  df_madhav.to_csv('madhav.csv')
def ben():
  position = input("Enter position: ")
  name = input("Enter name: ")
  vbd = float(input("Enter VBD: "))
  df_ben.loc[position, 'Name'] = name
  df_ben.loc[position, 'VBD'] = vbd
  df_ben.to_csv('ben.csv')
  change = calc(count) - vbd
  global ben_score
  ben_score = ben_score - (4*change)
  df_ben.loc['QB','Score'] = ben_score
  df_ben.to_csv('ben.csv')
def arjun():
  position = input("Enter position: ")
  name = input("Enter name: ")
  vbd = float(input("Enter VBD: "))
  df_arjun.loc[position, 'Name'] = name
  df_arjun.loc[position, 'VBD'] = vbd
  df_arjun.to_csv('arjun.csv')
  change = calc(count) - vbd
  global arjun_score
  arjun_score = arjun_score - (4*change)
  df_arjun.loc['QB','Score'] = arjun_score
  df_arjun.to_csv('arjun.csv')

#snake draft
def firstround():
  global count
  arjun()
  count+=1
  print("------Pick Number: " + str(count) + " ------")
  ben()
  count+=1
  print("------Pick Number: " + str(count) + " ------")
  madhav()
  count+=1
  print("------Pick Number: " + str(count) + " ------")
  parsa()
  count+=1
  print("------Pick Number: " + str(count) + " ------")
  robel()
  count+=1
  print("------Pick Number: " + str(count) + " ------")
  sammy()
  count+=1
  print("------Pick Number: " + str(count) + " ------")
  sreek()
  count+=1
def secondround():
  global count
  print("------Pick Number: " + str(count) + " ------")
  sreek()
  count+=1
  print("------Pick Number: " + str(count) + " ------")
  sammy()
  count+=1
  print("------Pick Number: " + str(count) + " ------")
  robel()
  count+=1
  print("------Pick Number: " + str(count) + " ------")
  parsa()
  count+=1
  print("------Pick Number: " + str(count) + " ------")
  madhav()
  count+=1
  print("------Pick Number: " + str(count) + " ------")
  ben()
  count+=1
  print("------Pick Number: " + str(count) + " ------")
  arjun()
  count+=1

  