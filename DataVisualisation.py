import pandas as pd
import matplotlib.pyplot as plt
 
data=pd.read_excel("D:\Dhanya\VisualisationAssignment\population.xlsx", index_col= 0)#Reading data from excel file  
data1= data.drop(['Unnamed: 5'],  axis=1)
print(data1)

def line_plot(data):                                                     #Definig function to plot line plot         
    data = data
    plt.figure(figsize = (16,10))
    plt.plot(data.columns, data.loc['Afghanistan'], label='Afghanistan')
    plt.plot(data.columns, data.loc['Albania'], label='Albania')
    plt.plot(data.columns, data.loc['Angola'], label='Angola')
    plt.plot(data.columns, data.loc['Argentina'], label='Argentina')
    plt.legend()
    plt.xlabel("Years")
    plt.ylabel("Population")
    plt.title('Population')
    plt.show()
    return()


line_plot(data1)                                                        #Calling function to plot line


def pi_plot(pop_2010):                                                  #Defing Fuction for pi plot
    plt.figure(figsize = (16,10))
    plt.pie(pop_2010, labels=pop_2010.index, autopct='%1.1f%%')
    plt.title('World Population by Country (2010)')
    plt.axis('equal')
    plt.show()
    return()

pop_2010 = pd.to_numeric(data1['2010'].str.replace(',', ''))            #converting the population values in the '2010' column of the data1 DataFrame to numeric values. 
pi_plot(pop_2010)                                                       #The str.replace(',', '') method is used to remove any commas in the population values before conversion.


def bar_plot(data):                                                     #Defing Fuction for bar plot
    plt.figure(figsize = (16,10))
    plt.bar(data1.index, data1["2002"])
    plt.show()
    return()
 

bar_plot(data1)