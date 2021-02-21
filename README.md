# Titanic-Data-Analysis
A step by step guide to data analysis of the **Titanic** data set (source:[Kaggle](https://www.kaggle.com/)) using Python
### The project involves basic exploratory data analysis (EDA) of the Titanic data set and extracting relevant information from various fields (read as columns in dataframes). 
#### Contents
1 Downloading and cleaning the dataset
2 Analysis and visualization of the data
3  Storytelling about data findings

1 **Downloading and cleaning the dataset** - Any data analysis project in Python begins with the downloading of necessary libraries nemrly **Pandas**, **numpy**, **mathplotlib** and **seaborn** to name a few followed by the download and reading of the dataset file as [dataframe](https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html#dataframe) in Python. The resource offers both the training data (**train.csv**) and test data (**test.csv**). In this case we use the train data to draw the inferences for model implementation on test data.

In order to analyse, you will need to have a basic understanding of the data:
* No of rows  = 891
* No. of columns = 12
* PassengerId - A unique identification Id for each passenger
* Survived - A categorical variable where '0' represents death and '1' represents survival
* Pclass - Travel class of the passenger (1,2 or 3)
* Name - Name 
* Sex - Gender 
* Age - Age 
* Sibsp - Number of siblings or partners accompanying the passenger
* Parch - Number of Parents or children accompanying the passenger
* Ticket - Ticket number
* Fare 
* Cabin 
* Embarked - Embarkment port where **C** is Cherbourg, **S** is Southampton and **Q** is Queenstown

The first step involved in the cleaning of the dataset is to check the number of missing values (read nulls) in each of the column and is done using the **isnull()** function. 

![isnull](https://user-images.githubusercontent.com/77699950/108626623-66c08c80-7451-11eb-8f20-18f9097ead7e.png)


#### Prerequisites
 * Any Python IDE. For this analysis Jupyter notebook (server version 5.2.2) with Python (3.6.9) is used.


