import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Dataset.csv")

print("Original dataset shape:", df.shape)
print(df.isnull().sum())

df_clean = df.dropna()
print("Dataset shape after removing null values:", df_clean.shape)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Titanic Survival Classification Analysis', fontsize=16)

sns.countplot(ax=axes[0, 0], data=df_clean, x='Survived', palette='Set1')
axes[0, 0].set_title('Overall Survival Count (0 = Dead, 1 = Survived)')
axes[0, 0].set_xticklabels(['Dead', 'Survived'])

sns.countplot(ax=axes[0, 1], data=df_clean, x='Sex', hue='Survived', palette='Pastel1')
axes[0, 1].set_title('Survival Breakdown by Gender')
axes[0, 1].legend(['Dead', 'Survived'])

sns.countplot(ax=axes[1, 0], data=df_clean, x='Pclass', hue='Survived', palette='Set2')
axes[1, 0].set_title('Survival Breakdown by Ticket Class')
axes[1, 0].set_xlabel('Passenger Class')
axes[1, 0].legend(['Dead', 'Survived'])

fig.delaxes(axes[1, 1])

plt.tight_layout()
plt.show()
