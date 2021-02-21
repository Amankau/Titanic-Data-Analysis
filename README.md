# Titanic-Data-Analysis
A step by step guide to data analysis of the **Titanic** data set (source:[Kaggle](https://www.kaggle.com/)) using Python
### The project involves basic exploratory data analysis (EDA) of the Titanic data set and extracting relevant information from different variables.
#### Contents
1. Downloading and cleaning the dataset
2. Analysis and visualization of the data
3. Storytelling about data findings

1 **Downloading and cleaning the dataset** - Any data analysis project in Python begins with the downloading of necessary libraries namely **Pandas**, **Plotly**, **numpy**, **mathplotlib** and **seaborn** to name a few followed by the download and reading of the dataset file as [dataframe](https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html#dataframe) in Python. The data source offers both the training data (**train.csv**) and test data (**test.csv**). In this case we use the train data to draw the inferences for model implementation on test data.

In order to analyse, a basic understanding of the data is important:
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

The first step involved in the cleaning of the dataset is to check the number of missing values (read nulls) in each of the columns, done using the **isnull()** function, to impute the data using suitable estimates.

![isnull](https://user-images.githubusercontent.com/77699950/108626623-66c08c80-7451-11eb-8f20-18f9097ead7e.png)

The data shows that the number of null values in the **Age** and **Cabin** columns is remarkably high. In this case the nulls in the Age column were replaced by the median of Age for both Males and Females respectively. For the **Cabin** column we chose to ignore the missing data.

1 **Analysis and visualization of the data** - After building a basic understanding of each variable, we can try to draw the inferences and find the relationship between them. The simplest way to do this is by generating visualizations.

We started with the calculation of Survived and dead (unfortunately) passengers followed by the grouping on the basis of different variables

![Graph1](https://user-images.githubusercontent.com/77699950/108627402-b6a15280-7455-11eb-9c15-4c2cee88c425.png)

On the basis of **Sex**

![Graph2](https://user-images.githubusercontent.com/77699950/108627415-c91b8c00-7455-11eb-85e8-6c1e02cdb134.png)

On the basis of **Passenger Class**

![Graph3](https://user-images.githubusercontent.com/77699950/108627641-f7e63200-7456-11eb-8dd6-0ff8ea0167b7.png)

On the basis of **Number of siblings or spouses**

![Graph4](https://user-images.githubusercontent.com/77699950/108627883-084adc80-7458-11eb-8c07-807760cb69b3.png)

On the basis of **Number of parents and children**

![Graph5](https://user-images.githubusercontent.com/77699950/108628005-aa6ac480-7458-11eb-82ce-83b5a3d768e1.png)

On the basis of **Embarkment port**

![Graph6](https://user-images.githubusercontent.com/77699950/108628144-80fe6880-7459-11eb-9018-5ed4a224b5a4.png)

On the basis of **Age** 
![Graph7](https://user-images.githubusercontent.com/77699950/108628320-92944000-745a-11eb-8c91-dbcc6280a279.png)

3. **Data Storytelling** - Finally our findings can be broken down as follows:
Out of the 891 Passengers only approximately 38% of the passengers survived with a 74% survival chance of Females in comparison to ~19% in males. Furthermore, the passenger class played an important role as passengers from class 1 and class 3 had a  better chance of survival than class 2. Also the age distribution of the passengers from 0.42 to 80 shows that almost all the children under the age of 1 survived but a correlation of Age with Passenger class and Sex seems important. More number of passengers not accompanied with either children, parents,siblings or spouses also survived.







#### Prerequisites
 * Any Python IDE. For this analysis Jupyter notebook (server version 5.2.2) with Python (3.6.9) is used.


