import numpy as np
from sklearn.ensemble import RandomForestClassifier

 # For this sample:
 # col1 = address (or passport_id)
 # col2 = sybil (sybil = true or non-sybil = false)
 # col3... = stamp inputs either true or false

train_data = pd.read_csv('sample1.csv')

 # Extract boolean attribute columns
inputs = train_data.iloc[:, 2:].values

# Extract labels
labels = np.where(train_data['sybil'], 1, 0)

# Train a Random Forest classifier
model = RandomForestClassifier()
model.fit(inputs, labels)

feature_importance = model.feature_importance
feature_importance_df = pd.DataFrame({'Feature': data.columns[2:], 'Importance': feature_importance})
feature_importance_df.to_csv('feature_importance.csv', index=False)

### PLEASE NOTE: these scores should be used in tandem with a final prediction feature! Ie. once a minimum threshold
### score has been met, the user is able to receive a positive or negative prediction outcome. Just because a high
### importance score is returned for a particular stamp, does not mean it is of positive correlation to non-sybil 
### outcome prediction.
