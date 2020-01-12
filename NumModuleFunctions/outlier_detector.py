import pandas as pd
import numpy as np 

#df = pd.DataFrame({'Name':pd.Series(['foo'] * 100), 
#        'Age':np.append(np.random.normal(10, 1 ,99), 35)})

#Step 1: User will be prompted to input the name of the dataframe and then the 
#column of that dataframe they desire to clean
    #Ex: df is a pandas dataframe.
    #"Age" is a column in the df pandas dataframe
    #The user would input df, the name of the dataframe, and "Age", the column within df

#Step 2: At this point the name of the dataframe and its column is stored as a string. 

#Step 3: outlier function will identify the lower boun
     

def outlier_detect ():
    import pandas as pd #Imports pandas module
    import numpy as np #Loads numpy module
    #Take in the name of the user's dataframe that they would like to clean 
    data_frame = input("Hello! What is the name of your dataframe?\n") 
    #Prints the name of the user's dataframe they would like to clean
    print("\nOk! We are cleaning the", data_frame,"dataframe") 
    #Prompts the user to identify 
    print("\nWhich column of", data_frame, "would you like to clean?") 
    #The column of the user's dataframe they will clean
    col = input() 
    #Prints the user's dataframe and it's column that will be cleaned
    print ("Detecting for outliers in the", col, "column of", data_frame)
    #Converts name of the dataframe from a string to a variable
    df = globals()[data_frame]
    #Third quartile
    QR3 = np.percentile(df["Age"], .75)
    #First quartile
    QR1 = np.percentile(df["Age"], .25) 
    #Find IQR by subtracting third and first quartile
    IQR =  QR3 - QR1 
    #Upper boundary outlier: #Outlier: Values greater than Q3 + (IQR * 1.5) 
    upper = QR3 + (IQR * 1.5)
    #Lower boundary outlier: Values less than Q3 - (IQR * 1.5)
    lower = QR1 - (IQR * 1.5)
    outlier_index = df.index[(df[col] < lower) | (df[col] > upper)].tolist()
    outlier_val = df[col].loc[(df[col] < lower) | (df[col] > upper)]
    outlierdf = pd.DataFrame({'Index': outlier_index, 
                        'Value':outlier_val}) 
    print("You have", len(outlierdf), "outliers in the", col, "column")
    return outlierdf
