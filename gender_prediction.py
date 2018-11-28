from sklearn import tree 
from sklearn.metrics import accuracy_score
from sklearn import svm
from sklearn import neighbors


# training dataset
# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

#decision tree
clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

prediction = clf.predict([[190,70,43]])

print(prediction)


#svm

clf = svm.SVC()
clf = clf.fit(X,Y)
prediction = clf.predict([[190,70,43]])

print(prediction)


#kneighbors

clf = neighbors.KNeighborsClassifier()
clf = clf.fit(X,Y)
prediction = clf.predict([[190,70,43]])

print(prediction)
