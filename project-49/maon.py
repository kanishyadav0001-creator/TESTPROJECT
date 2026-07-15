import pandas as pd
import matplotlib.pyplot as plt


data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'July_Births': [12, 15, 11, 9, 1, 9, 21],
    'August_Births': [17, 5, 2, 11, 1, 8, 29]
}
df = pd.DataFrame(data)

plt.figure(figsize=(10, 5)) 


plt.plot(df['Day'], df['July_Births'], 
         marker='D', linestyle='dashed', linewidth=2, color='blue', label='July')

plt.plot(df['Day'], df['August_Births'], 
         marker='o', linestyle='solid', linewidth=2, color='orange', label='August')

plt.title('Birth Rate Comparison: July vs. August')
plt.xlabel('Days of the Week')
plt.ylabel('Number of New Births')

plt.legend()

plt.grid(True)
plt.show()