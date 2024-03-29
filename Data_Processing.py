import pandas as pd
import ydata_profiling


df = pd.read_csv("Crop_recommendation.csv")   #读取数据集

df = pd.get_dummies(df)    #使用独热编码
df.to_csv('Process_crop_recommendation.csv',index=False)   #将独热编码后的数据集输出为文件Process_crop_recommendation.csv