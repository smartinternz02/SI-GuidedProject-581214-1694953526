import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('SmartBridge\House Price India.csv')

df = data
#print(df)
df.drop(["id"], axis=1, inplace=True)
df.drop(["Date"], axis=1, inplace=True)
df.drop(["Renovation Year"], axis=1, inplace=True)

print(df.isna().sum())
#As there is no missing values we don't have to handle missing values
df.isnull()
df.info()
df.describe().T
df.duplicated()
df.shape
df.columns

#print(df)

df.set_index("Price").head(10)

df.Price.sum()
df.corr()


df.plot()
plt.legend(['Number of bedrooms', 'Number of Bathrooms', 'Living Area', 'Lot Area', 'Number of Floors',
            'Waterfront Present', 'Number of views', 'Condition of the house', 'Grade of the house', 'Area of the house',
            'Area of the basement', 'Built Year', 'Postal Code', 'Lattitude', 'Longitude', 'Lin=ving Area Renovation', 'Lot Area REnovation',
            'Number of schools nearby', 'Distance from airport', 'Price'])

plt.figure(figsize=(12, 6))
sns.histplot(df["number of bathrooms"], color="black", linewidth=10)

pd.pivot_table(df,index="Price", values="Built Year").head(10).round()

df.loc[:,["number of bedrooms", "number of bathrooms", "Lattitude", "Longitude","Price"]].tail(10)

f = plt.figure(figsize=(12, 6))
ax=f.add_subplot(121)
sns.displot(data["number of bedrooms"], color="pink")
plt.title("number of bedrooms")

ax=f.add_subplot(122)
sns.displot(data["number of bathrooms"], color="b")
plt.title("number of bathrooms")
plt.suptitle("Distribution of Bedrooms and Bathrooms")

plt.figure(figsize=(12, 6))
sns.scatterplot(data=data, x="Number of schools nearby", y="Price", hue="Price")
plt.grid()
plt.title("Distribution of Prices by nearby Schools")

plt.figure(figsize=(12,4))
sns.scatterplot(data=data, x="Distance from the airport", y="Price", hue="Price")
plt.title("Distribution of Prices by Distance from the Airport")

sns.catplot(data=df, x="number of bedrooms", y="Price", palette="magma", hue="Price")
plt.title("Distribution of Prices by Number of Bedrooms")

plt.figure(figsize=(12,5))
sns.scatterplot(y="Built Year", x="Price", data=data, hue="Built Year")
plt.title("Distribution of Prices with Built Year")

plt.figure(figsize=(12, 6))
sns.histplot(df["number of bathrooms"], color="black", linewidth=10)

plt.figure(figsize=(10,5))
sns.heatmap(df.corr(), cmap="coolwarm", annot=True)

sns.pairplot(df)

plt.show()