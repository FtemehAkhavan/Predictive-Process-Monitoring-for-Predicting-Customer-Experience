#!/usr/bin/env python
# coding: utf-8

# # decision tree

# In[2]:


import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation


# # cluster0

# In[3]:


df = pd.read_csv('C:\\Users\\Administrator\\thesis\\BPI Challenge 2016\\feature selection\\cluster0 feature selected.csv')
df


# In[ ]:


y=df.Complaint


# In[ ]:


df.drop(['Complaint','CustomerID'], axis=1, inplace=True)


# In[ ]:


X=df
X


# In[71]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)


# In[72]:


# Create Decision Tree classifer object
clf = DecisionTreeClassifier()

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)


# In[73]:


from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred )


# In[74]:


print("Accuracy:",metrics.accuracy_score(y_test, y_pred))


# In[75]:


X.columns


# In[76]:


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


# In[77]:


node_counts = clf.tree_.node_count
node_counts


# In[78]:


depth = clf.tree_.max_depth
depth


# In[79]:


text_representation = tree.export_text(clf)
print(text_representation)


# In[1]:


from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, y_pred)


# In[81]:


from sklearn.metrics import classification_report
print (classification_report(y_test, y_pred))


# In[54]:


#import numpy as np 
#from sklearn.tree import _tree

#def find_rules(tree, features):
 #   dt= tree.tree_
  #  def visitor(node, depth):
   #     indent= ' ' * depth
    #    if dt.feature[node]!=_tree.Tree_UNDEFINED:
     #       print('{}if<{}> <= {}:'. format(indent, features[node], round(dt.threshold[node],2)))
      #      visitor(dt.children_left[node], depth + 1)
       #     print('{}else:'. format(indent))
        #    visitor(dt.children_left[node], depth + 1)
       # else:
        #    print('{}return {}:'. format(indent, dt.value[node]))
   # visitor(0,1)


# In[55]:


#find_rules(clf, X.columns)


# In[16]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[17]:


import matplotlib.pyplot as plt


# In[18]:


from sklearn import tree
plt.figure(figsize=(75,30))
tree.plot_tree(clf,filled=True)


# In[57]:


#تابع کامپلکسیتی دو تا ورودی داره آلفا که نشون دهنده عمق هست و ایمپوریتی
path= clf.cost_complexity_pruning_path(X_train, y_train)
ccp_alphas, impurities = path.ccp_alphas, path.impurities


# In[58]:


clfs=[]
for ccp_alpha in ccp_alphas:
    clf=DecisionTreeClassifier(random_state=0, ccp_alpha=ccp_alpha )
    clf.fit(X_train, y_train)
    clfs.append(clf)
print("number of nodes in the last tree:{} with ccp_alpa: {}". format(clfs[-1].tree_.node_count, ccp_alphas[-10]))


# In[59]:


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


# In[60]:


clf=DecisionTreeClassifier(random_state=0, ccp_alpha=0.0000625)

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)


# In[61]:


print("Accuracy:",metrics.accuracy_score(y_test, y_pred))


# In[62]:


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


# In[63]:


node_counts = clf.tree_.node_count
node_counts


# In[64]:


depth = clf.tree_.max_depth
depth


# In[65]:


text_representation = tree.export_text(clf)
print(text_representation)


# In[ ]:




