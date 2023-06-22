import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

  # Import a sample table with exactly one half of available sample data; 
  # the import table should be structured:
  # col1 = the Passport blockchain address (or passport_id),
  # col2 = the label of sybil, non-sybil, airdrop etc to be translated to boolean,
  # col3 = has_dup_attempt - any stamp hash for this passport appears for 2+ unique passport addresses,
  # col4...col64 = the boolean returns of each stamp; default 0 false
  # an example can be found here https://docs.google.com/spreadsheets/d/1v_ux5InolURG2j2oET8e3WQWaeR_okh8WOPQh_EeRB4/edit#gid=0

train_data = pd.read_csv('sample1.csv')
train_input_data = data.iloc[:, 2:].values
train_labels = np.where(data['label'] == 'sybil', 1, 0)

model = LogisticRegression()
model.fit(train_input_data, train_labels)

  # input risk scores for the second sample to assess accuracy
test_data = pd.read_csv('sample2.csv')
test_input_data = new_users_data.iloc[:, 2:].values

risk_scores = model.predict_proba(test_input_data)[:, 1] * 100
output_data = pd.DataFrame({'address': test_data['address'], 'risk_score': risk_scores})
output_data.to_csv('test_output.csv', index=False)
