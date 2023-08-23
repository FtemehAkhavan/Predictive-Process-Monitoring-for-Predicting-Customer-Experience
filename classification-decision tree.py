#!/usr/bin/env python
# coding: utf-8

# # decision tree

import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation


df = pd.read_csv('dataset.csv')
df


y=df.Complaint


df.drop(['Complaint','CustomerID'], axis=1, inplace=True)


X=df
X


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)


# Create Decision Tree classifer object
clf = DecisionTreeClassifier()

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)


from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred )


print("Accuracy:",metrics.accuracy_score(y_test, y_pred))


X.columns


from sklearn.tree import export_graphviz
from six import StringIO  
from IPython.display import Image  
import pydotplus

dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True,feature_names = X.columns,class_names=['0','1','2','3','4','5'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('decision tree cluster0.png')
Image(graph.create_png())


node_counts = clf.tree_.node_count
node_counts

depth = clf.tree_.max_depth
depth

text_representation = tree.export_text(clf)
print(text_representation)


from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, y_pred)


from sklearn.metrics import classification_report
print (classification_report(y_test, y_pred))


get_ipython().run_line_magic('matplotlib', 'inline')


import matplotlib.pyplot as plt


from sklearn import tree
plt.figure(figsize=(75,30))
tree.plot_tree(clf,filled=True)

path= clf.cost_complexity_pruning_path(X_train, y_train)
ccp_alphas, impurities = path.ccp_alphas, path.impurities


clfs=[]
for ccp_alpha in ccp_alphas:
    clf=DecisionTreeClassifier(random_state=0, ccp_alpha=ccp_alpha )
    clf.fit(X_train, y_train)
    clfs.append(clf)
print("number of nodes in the last tree:{} with ccp_alpa: {}". format(clfs[-1].tree_.node_count, ccp_alphas[-10]))


train_scores = [clf.score(X_train, y_train) for clf in clfs]
test_scores = [clf.score(X_test, y_test) for clf in clfs]

fig, ax = plt.subplots(figsize=(15,10))
ax.set_xlabel("alpha")
ax.set_ylabel("accuracy")
ax.set_title("Accuracy vs alpha for training and testing sets")
ax.plot(ccp_alphas, train_scores, marker="o", label="train", drawstyle="steps-post")
ax.plot(ccp_alphas, test_scores, marker="o", label="test", drawstyle="steps-post")
ax.legend()
plt.show()


clf=DecisionTreeClassifier(random_state=0, ccp_alpha=0.0000625)

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)


print("Accuracy:",metrics.accuracy_score(y_test, y_pred))


from sklearn.tree import export_graphviz
from six import StringIO  
from IPython.display import Image  
import pydotplus

dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True,feature_names = X.columns,class_names=['0','1','2','3','4','5'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('decision tree cluster0.png')
Image(graph.create_png())


node_counts = clf.tree_.node_count
node_counts


depth = clf.tree_.max_depth
depth


text_representation = tree.export_text(clf)
print(text_representation)




