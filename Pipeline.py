import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA

data = pd.read_csv('https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv')

myLabel = LabelEncoder()
data['smoker'] = myLabel.fit_transform(data['smoker'])
data['sex'] = myLabel.fit_transform(data['sex'])
data['region'] = myLabel.fit_transform(data['region'])

print(data.head())

y = data['charges'].values
X = data.drop('charges', axis=1).values
print(X)

algo = LinearRegression()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
algo.fit(X_train, y_train)
print(algo.score(X_train, y_train))

pipe = Pipeline(steps=[("scaler", StandardScaler()),
                       ("pca", PCA(n_components=3)),
                       ("linear", LinearRegression())])
pipe.fit(X_train, y_train)
print(pipe.score(X_test, y_test))
