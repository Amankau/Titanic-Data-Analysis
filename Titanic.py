
# coding: utf-8

# In[356]:


import pandas as pd


# In[357]:


import numpy as np


# In[358]:


import math


# In[359]:


import matplotlib.pyplot as plt


# In[360]:


import seaborn as sns


# In[ ]:


color = sns.color_palette()


# In[363]:


import sklearn


# In[364]:


titanic=pd.read_csv(r'/home/varun/Desktop/train.csv')


# In[365]:


titanic.head()


# In[366]:


titanic.describe()


# In[368]:


titanic.isnull().sum()


# In[369]:


len(titanic["PassengerId"])


# In[370]:


Passenger_info = titanic.groupby("Survived").size()


# In[371]:


Passenger_info


# In[372]:


height = Passenger_info
bars = ('Dead','Survived')
y_pos = np.arange(len(bars))
 

plt.bar(y_pos, height,color= ["red","blue"])
plt.title('Number of dead and survived passengers')
plt.ylabel('No. of Passengers')

 

plt.xticks(y_pos, bars)
 

plt.show()


# In[373]:


Gender= titanic.groupby("Sex").size()


# In[374]:


Gender


# In[375]:


Gender_info = titanic.groupby(["Sex","Survived"]).size()


# In[376]:


Gender_info


# In[377]:


Gender_survived = Gender_info[[1,3]]


# In[475]:


import numpy as np
data = [[577,314],
[468,81]]
X = np.arange(2)
width= 0.25
fig = plt.figure()
ax = plt.subplot(111)
ax.bar(X + 0.00, data[0], width, color = 'b' )
ax.bar(X + 0.25, data[1], width, color = 'r' )
ax.set_xticks(X+0.11)
ax.set_xticklabels( ('Male', 'Female') )
plt.ylabel('No of Passengers')
ax.legend( ("Total","Dead"))
plt.show()


# In[ ]:


Gender_survived


# In[380]:


percentage_Gender = (Gender_survived/Gender)*100


# In[381]:


percentage_Gender


# In[441]:


height = percentage_Gender
bars = ('Female','Male')
y_pos = np.arange(len(bars))
 

plt.bar(y_pos, height,color= ["green","red"])
plt.title('Percentage of Female and Male survied passengers')
plt.ylabel('Percentage')

 
# Create names on the x-axis
plt.xticks(y_pos, bars)
 
# Show graphic
plt.show()



# In[383]:


Pclass= titanic.groupby("Pclass").size()


# In[384]:


Pclass


# In[385]:


Pclass_detail = titanic.groupby(["Pclass","Survived"]).size()


# In[386]:


Pclass_detail


# In[387]:


Pclass_survived = Pclass_detail.loc[[(1,1),(2,1),(3,1)]]


# In[388]:


Pclass_survived


# In[442]:


height = Pclass_survived #[136,87,119]
bars = ('Class 1','Class 2','Class 3')
y_pos = np.arange(len(bars))
 

plt.bar(y_pos, height,color= ["green","red","blue"])
plt.title('Survivors in each Passenger class')
plt.ylabel('No. of Survivors')

 
# Create names on the x-axis
plt.xticks(y_pos, bars)
 
# Show graphic
plt.show()



# In[390]:


Passenger_Age = titanic.groupby("Age").size()


# In[443]:


titanic.Age.describe()


# In[446]:


Passenger_Age.plot(kind = "bar", figsize = (20,6))
plt.ylabel("Number of Passengers")
plt.xlabel("Age")
plt.title("Age distribution of Passengers")
plt.show()


# In[394]:


Age = titanic.groupby(["Survived","Age"]).size()


# In[395]:


Age.head()


# In[419]:


Survived_Age = Age[1]


# In[420]:


Survived_Age


# In[434]:


Survived_Age.plot(kind = "bar", figsize = (20,7))
plt.ylabel("Number of Passengers")
plt.xlabel("Age")
plt.title("Survived Passengers Age")
plt.show()


# In[438]:


Relative_Age = (Survived_Age/Passenger_Age)*100


# In[448]:


Relative_Age.plot(kind = "bar", figsize = (20,7))
plt.ylabel("Percentage")
plt.xlabel("Age")
plt.title("Age distribution of Survived Passengers")
plt.show()


# In[466]:


Sibling_survival = titanic.groupby(["Survived","SibSp"]).size()


# In[467]:


Sibling_survival


# In[469]:


Sibling_survival[1]


# In[470]:


Sib_Survived = Sibling_survival[1]


# In[471]:


Sib_Survived.plot(kind = "bar", figsize = (17,5))
plt.ylabel("Number of Passengers")
plt.xlabel("No of Siblings or partner")
plt.title("Age distribution of Passengers")
plt.show()


# In[398]:


Parch = titanic.groupby("Parch").size()


# In[399]:


Parch


# In[451]:


Parch = titanic.groupby(["Survived","Parch"]).size()


# In[452]:


Parch


# In[464]:


Parch_survived = Survived[1]


# In[463]:


Parch_survived


# In[459]:


Parch.plot(kind = "bar", figsize = (17,5))
plt.ylabel("Number of Passengers")
plt.xlabel("Parch")
plt.title("Age distribution of Passengers")
plt.show()


# In[460]:


Embarkment = titanic.groupby("Embarked").size()


# In[404]:


Embarkment


# In[405]:


Embarkment = titanic.groupby(["Embarked","Survived"]).size()


# In[406]:


Embarkment


# In[407]:


Embark_survived


# In[408]:


data = [[168,77,644],
[93,30,217]]
X = np.arange(3)
width= 0.25
fig = plt.figure()
ax = plt.subplot(111)
ax.bar(X + 0.00, data[0], width, color = 'b' )
ax.bar(X + 0.25, data[1], width, color = 'g' )

ax.set_xticks(X+0.11)
ax.set_xticklabels( ('C', 'Q', 'S') )
ax.legend( ("Total","Survived"))

plt.show()


# In[409]:


Percentage_port = (Embark_survived/Embarkment)*100


# In[410]:


Percentage_port


# In[411]:


Fare = titanic.groupby("Fare").size()


# In[412]:


len(Fare)


# In[413]:


Fare.describe()


# In[424]:


Fare_survival = titanic.groupby(["Survived","Fare"]).size()


# In[425]:


Fare_survival


# In[426]:


Fare_survival = Fare_survival[[1]]


# In[427]:


Fare_survival


# In[428]:


Fare_only_survived =Fare_survival[1]


# In[429]:


Fare_class = titanic.groupby(["Survived","Pclass","Fare"]).size()


# In[430]:


Fare_class


# In[431]:


Fare_class_survived =Fare_class[1]


# In[432]:


Fare_class_survived


# In[ ]:


Fare_class_survived[1].head()


# In[ ]:


Fare_class_survived[1].plot(kind = "bar", figsize = (20,7))
plt.ylabel("Number of Passengers")
plt.xlabel("Fare")
plt.title("Survived Passengers in Class 1")
plt.show()


# In[ ]:


Fare_class_survived[3].head()


# In[ ]:


Fare_class_survived[3].plot(kind = "bar", figsize = (20,7))
plt.ylabel("Number of Passengers")
plt.xlabel("Fare")
plt.title("Survived Passengers in Class 3")
plt.show()


# In[ ]:


Fare_class_survived[2].head()


# In[ ]:


Fare_class_survived[2].plot(kind = "bar", figsize = (20,7))
plt.ylabel("Number of Passengers")
plt.xlabel("Fare")
plt.title("Survived Passengers in Class 2")
plt.show()

