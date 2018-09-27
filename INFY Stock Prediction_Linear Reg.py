
# coding: utf-8

# In[5]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn import preprocessing;
from sklearn import linear_model;

data = pd.read_csv('C:/Users/DELL/Desktop/intern/INFY.csv')


# In[6]:


print(data)


# In[7]:


from sklearn import cross_validation;


# In[8]:


def prepare_data(df,forecast_col,forecast_out,test_size):
    label = df[forecast_col].shift(-forecast_out);#creating new column called label with the last 5 rows are nan
    X = np.array(df[[forecast_col]]); #creating the feature array
    X = preprocessing.scale(X) #processing the feature array
    X_lately = X[-forecast_out:] #creating the column i want to use later in the predicting method
    X = X[:-forecast_out] # X that will contain the training and testing
    label.dropna(inplace=True); #dropping na values
    y = np.array(label)  # assigning Y
    X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(X, y, test_size=test_size) #cross validation 

    response = [X_train,X_test , Y_train, Y_test , X_lately];
    return response;


# In[9]:


forecast_col = 'Close'#choosing which column to forecast
forecast_out = 5 #how far to forecast 
test_size = 0.2; #the size of my test set


# In[11]:


X_train, X_test, Y_train, Y_test , X_lately =prepare_data(data,forecast_col,forecast_out,test_size); #calling the method were the cross validation and data preperation


# In[12]:


learner = linear_model.LinearRegression();


# In[13]:


learner.fit(X_train,Y_train); #training the linear regression model


# In[19]:


score=learner.score(X_test,Y_test);#testing the linear regression model
print(score)


# In[18]:


forecast= learner.predict(X_lately);
print(forecast)


# In[28]:


def mean_absolute_percentage_error(y_true, y_pred): 
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100


# In[31]:


mean_absolute_percentage_error(X_test,Y_test)

