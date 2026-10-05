import pandas as pd
from sklearn.metrics import mean_absolute_error as MAE
from sklearn.model_selection import train_test_split as TTS
from sklearn.tree import DecisionTreeRegressor

# Function to check the mae of the predictions' validation
## Notes to self that should be fix but right now I dont care:
### - This is a bad practice in python al global values in a function should be passed in the parameters
### - Not to split nor create the regresor in every iteration since the state is always 1 is inefficient
def Get_Mae(max_leafs):
    
    #split all the data into values to train and values to validate chosen at random
    train_X,val_X,train_y,val_y=TTS(X,y,random_state=1)

    #Create the model with a max number of leafs(ramifications) and a seed
    Utr_Burnout_Model=DecisionTreeRegressor(max_leaf_nodes=max_leafs,random_state=1)

    #train the model with my Data
    Utr_Burnout_Model.fit(train_X,train_y)

    #The model uses lineal regresion to predict the y values (If used the same val values results should be acurate)
    val_predictions=Utr_Burnout_Model.predict(val_X)


    print("The BurnOut Predictions are:")
    print(val_predictions)

    #Get the diference between teh spected values and the real values
    mae=MAE(val_y,val_predictions)

    
    return (mae)

#Get the whole table from the csv
Burnout_Data=pd.read_csv("group_data.csv")

#What value is gonna be my goal or I will try to predict
y=Burnout_Data.Academic_Burnout_Index

#Uncomment to see all columns names
#print(Burnout_Data.columns)

print(y)


#Get names AND values from the csv except 1st and last column
X=Burnout_Data.iloc[:, 1:-1]

print(X)

#USER action
is_mae_acceptable=False
leafs_array=[5,10,20,40,80,100,200,500]

while(not is_mae_acceptable):

    for number in leafs_array:
        mae=Get_Mae(number);
        print("max_leaf_nodes: %d       mae: %d" %(number,mae))

    print("Is mae acceptable? y/n")
    answer=input()
    if answer=="y" or answer=="Y":
        is_mae_acceptable=True
    else:
        leafs_array=[]
        print("Insert the new 5 values you want to check next")
        for i in range(5):
            print("Value %i" %(i))
            value=int(input())
            leafs_array.append(value)




