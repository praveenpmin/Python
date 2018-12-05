
from sklearn import svm
from sklearn import datasets
# Load dataset
iris = datasets.load_iris()
clf = svm.LinearSVC()
# learn from the data
clf.fit(iris.data, iris.target)
# predict for unseen data
clf.predict([[ 5.0,  3.6,  1.3,  0.25]])
# Parameters of model can be changed by using the attributes ending with an underscore
print(clf.coef_ )
