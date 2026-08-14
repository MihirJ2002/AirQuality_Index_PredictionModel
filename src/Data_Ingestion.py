# Import Data Mainpulation Libraries
import numpy as np 
import pandas as pd 

def data_loader():
    df = pd.read_excel('C:\\AirQuality_Index_PredictionModel\\data\\AirQualityUCI.xlsx')
    
    return df