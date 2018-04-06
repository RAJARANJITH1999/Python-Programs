from sklearn.naive_bayes import GaussianNB
import numpy as np
import pandas as pd

x=np.array([["raja","yuvi","uday"],[12,23,432],["india","china","german"]])

'''clf=GaussianNB()
clf.fit(x,y)
GuassianNB()
print(clf.predict([[-0.8,-1]]))

from sklearn.metrics import accuracy_score
print(accuracy_score(pred,labels_test))'''


data=pd.DataFrame(x)
print(data)
