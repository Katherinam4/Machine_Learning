# TASK1

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
#
# data = pd.read_csv('emails.csv')
# print(data.head())
#
# X = data.drop('Prediction', axis=1).values
# y = data['Prediction'].values
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
#
# algo = LogisticRegression(max_iter=500000, C=0.7)
# algo.fit(X_train, y_train)
# print(algo.score(X_test, y_test))

# TASK2

# import pandas as pd
# from sklearn.feature_selection import f_classif, SelectKBest
# from sklearn.model_selection import train_test_split
# from sklearn.svm import SVC
#
# data = pd.read_csv("emails.csv")
# print(data.head())
#
#
# X = data.drop('Prediction', axis=1).values
# y = data['Prediction'].values
#
# X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1, test_size=0.3)
# algo1 = SVC()
# algo1.fit(X_train, y_train)
# print(algo1.score(X_test, y_test))
#
# selector = SelectKBest(score_func=f_classif, k=4)
# X_new = selector.fit_transform(X, y)
# X_train, X_test, y_train, y_test = train_test_split(X_new, y, random_state=1, test_size=0.3)
# algo2 = SVC()
# algo2.fit(X_train, y_train)
# print(algo2.score(X_test, y_test))

