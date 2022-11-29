import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from pycaret.regression import *
import pickle
df=pd.read_csv("car data.csv")
df['current_year']=2022
df['years']=df['current_year']-df['Year']
df.drop('current_year',axis=1,inplace=True)
df.drop('Year',axis=1,inplace=True)
df.drop('Car_Name',axis=1,inplace=True)
df=pd.get_dummies(df, columns = ['Fuel_Type', 'Seller_Type','Transmission'],drop_first=True)
# setup(data =  df, target='Selling_Price', silent=True)
# cm = compare_models()
X=df.iloc[:,1:]
y=df.iloc[:,0]
X_train, X_test, y_train, y_test=train_test_split(X,y,train_size=0.75)
model=GradientBoostingRegressor().fit(X_train,y_train)
pred=model.predict(X_test)
file=open('grb.pkl','wb')
pickle.dump(model,file)
