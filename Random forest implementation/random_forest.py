# Random forest implementation (ensemble learning) to predict whether the agent will
# vote for me or not in the ai wolf game

#importing necessary libraries

import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier #For random forest
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import metrics
import matplotlib.pyplot as plt

target = "Vote(Yes/No)"  # Target variable is whether the target agent voted for us or not

train_df= pd.read_csv("training data.csv")

x = train_df.drop(target, axis=1).values
y = train_df[[target]].values
y=y.ravel() #Converting to 1D array

# Splitting the dataset into train 70% and test 30%
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3) 


forest_model=RandomForestClassifier(n_estimators=100)

forest_model.fit(X_train,y_train)



# Training data statistics*************************************************************************

y_predtrain = forest_model.predict(X_train)

print("Training accuracy of random forest on takeda dataset :",metrics.accuracy_score(y_train, y_predtrain))

print("The confusion matrix of training dataset: ")
print(confusion_matrix(y_train, y_predtrain))


# Plotting the confusion matrix
cm = confusion_matrix(y_train, y_predtrain)

fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(cm)
ax.grid(False)
ax.xaxis.set(ticks=(0, 1), ticklabels=('Predicted 0s', 'Predicted 1s'))
ax.yaxis.set(ticks=(0, 1), ticklabels=('Actual 0s', 'Actual 1s'))
ax.set_ylim(1.5, -0.5)
for i in range(2):
    for j in range(2):
        ax.text(j, i, cm[i, j], ha='center', va='center', color='red')
plt.show()


# Test data statistics******************************************************************


y_pred=forest_model.predict(X_test)

print("Test accuracy of random forest on takeda dataset :",metrics.accuracy_score(y_test, y_pred))

print("The confusion matrix of test dataset: ")
print(confusion_matrix(y_test, y_pred))

# Plotting the confusion matrix

cm = confusion_matrix(y_test, y_pred)

fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(cm)
ax.grid(False)
ax.xaxis.set(ticks=(0, 1), ticklabels=('Predicted 0s', 'Predicted 1s'))
ax.yaxis.set(ticks=(0, 1), ticklabels=('Actual 0s', 'Actual 1s'))
ax.set_ylim(1.5, -0.5)
for i in range(2):
    for j in range(2):
        ax.text(j, i, cm[i, j], ha='center', va='center', color='red')
plt.show()



