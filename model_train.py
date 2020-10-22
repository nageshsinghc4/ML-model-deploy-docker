from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

#Load iris Dataset¶
iris_dict = load_iris()
X = iris_dict['data']
y = iris_dict['target']



# shuffle arrays since y values are in order
from sklearn.utils import shuffle
X_new, y_new = shuffle(X, y, random_state=0)

# Divide samples into train and test
n_samples_train = 120 # number of samples for training (--> #samples for testing = len(y_new) - 120 = 30)
X_train = X_new[:n_samples_train, :]
y_train = y_new[:n_samples_train]

X_test = X_new[n_samples_train:, :]
y_test = y_new[n_samples_train:]

#Fit logistic regression model¶
clf = LogisticRegression()
clf.fit(X_train, y_train)

#predict
y_pred = clf.predict(X_test)

#Metrics¶

from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_pred)

#Save model
import pickle
with open('iris_trained_model.pkl', 'wb') as f:
    pickle.dump(clf, f)


with open('iris_trained_model.pkl', 'rb') as f:
    clf_loaded = pickle.load(f)

clf_loaded
