import pandas as pd
from sklearn.metrics import mean_absolute_error as MAE
from sklearn.model_selection import train_test_split as TTS
from sklearn.tree import DecisionTreeRegressor

def Get_Mae(max_leafs,predictions):
    train_X,val_X,train_y,val_y=TTS(X,y,random_state=1)

    Utr_Burnout_Model=DecisionTreeRegressor(max_leaf_nodes=max_leafs,random_state=1)

    Utr_Burnout_Model.fit(train_X,train_y)

    val_predictions=Utr_Burnout_Model.predict(predictions)

    print("The BurnOut Predictions are:")
    print(val_predictions)


#Get the whole table from the csv
Burnout_Data=pd.read_csv("group_data.csv")

#What value es gonna
y=Burnout_Data.Academic_Burnout_Index

#print(Burnout_Data.columns)

print(y)


#Get names AND values from the csv except 1st and last column
X=Burnout_Data.iloc[:, 1:-1]

print(X)
Galia=pd.read_csv("galia.csv")

galia_x=Galia.iloc[:,1:]
print(galia_x)
input()
Get_Mae(5,galia_x)




