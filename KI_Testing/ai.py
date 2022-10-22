import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf
from sklearn.metrics import accuracy_score

df = pd.read_csv('./KI_Testing/Churn.csv')

X = pd.get_dummies(df.drop(['Churn', 'Customer ID'], axis=1))
y = df['Churn'].apply(lambda x: 1 if x== 'Yes' else 0)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

X_train.head()
y_train.head()

print(str(X_train))
print(str(y_train))

## funzt nicht, falsche Versionen aktuell
