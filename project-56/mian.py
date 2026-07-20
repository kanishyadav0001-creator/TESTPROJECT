import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 


data = pd.read_csv('Bestsellers with categories.csv') 
print(data.head(5)) 

print("\n* Null Values Summary *")
print(data.isnull().sum()) 

print("\n* Frequency of categories for feature Genre *") 
print(data['Genre'].value_counts()) 


print("\n* Median of Genre *") 

categories = data['Genre'].dropna().unique().tolist()

data['Genre'] = pd.Categorical(data['Genre'], categories=categories, ordered=True) 
median_value = np.median(data['Genre'].cat.codes) 
median_text = categories[int(median_value)] 
print("Median Value of Genre -", median_text) 

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.countplot(x='Genre', data=data, order=data['Genre'].value_counts().index, palette='winter') 
plt.title('Bar Chart of Genre')


plt.subplot(1, 2, 2)
data['Genre'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['#4E79A7', '#F28E2B'])
plt.ylabel('') # Removes the overlapping 'Genre' vertical label
plt.title('Pie Chart of Genre')

plt.tight_layout()
plt.show()
