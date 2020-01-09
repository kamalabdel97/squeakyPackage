def outlier ():
    import numpy as np #Loads numpy module
    data_frame = input("Hello! What is the name of your dataframe?\n")
    print("\nOk! We are cleaning the", data_frame,"dataframe")
    print("\nWhich column of", data_frame, "would you like to clean?")
    col = input()
    print ("/nAwesome! Let's clean up the", col, "column in", data_frame)
    df = globals()[data_frame]
    QR3 = np.percentile(df[col], .75)  #Third quartile
    QR1 = np.percentile(df[col], .25) #First quartile
    IQR =  QR3 - QR1 #Find IQR by subtracting third and first quartile
    upper = QR3 + (IQR * 1.5) #Upper boundary outlier: #Outlier: Values greater than Q3 + (IQR * 1.5) 
    lower = QR1 - (IQR * 1.5) #Lower boundary outlier: Values less than Q3 - (IQR * 1.5)    
    extreme = df[col].loc[(df[col] > lower) & (df[col] < upper)]
    print("You have", len(extreme), "outliers in the", col, "column")
