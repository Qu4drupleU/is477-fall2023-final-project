import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load the dataset
df = pd.read_csv('data/winequality-red.csv', delimiter=';')

# 1. Computing summary statistics
summary_stats = df.describe()
summary_stats.to_csv('results/summary_statistics.csv')

# 2. Simple analytical task: Predicting wine quality using a linear regression model
# Selecting a few features for simplicity
features = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides']
X = df[features]
y = df['quality']

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating and training the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predicting and evaluating the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Saving the model's performance
with open('results/model_performance.txt', 'w') as file:
    file.write(f'Mean Squared Error: {mse}\n')

# 3. Creating a simple visualization: Histogram of Wine Quality
plt.hist(df['quality'], bins=10, color='blue', alpha=0.7)
plt.title('Histogram of Wine Quality')
plt.xlabel('Quality')
plt.ylabel('Frequency')
plt.savefig('results/wine_quality_histogram.png')
plt.show()
