#liufeng9
#section 0201

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn import tree

import pydotplus
from sklearn.externals.six import StringIO

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
from scipy import integrate

#########################1-1

def z(x,y):
    return (x-y)**2

def fg(x):
    if x > 0 and x < 1:
        return 1
    else:
        return 0
    
def fh(y):
    if y > 0 and y < 1:
        return 1
    else:
        return 0
    
def ff(x,y):
    a=z(x,y)
    b=fg(x)
    c=fh(y)
    return a*b*c
    
def bound_x(self):
    return [-np.inf,np.inf]

def bound_y():
    return [-np.inf,np.inf]

fo = open("/Users/fengheliu/Desktop/hw_writeup.txt", "a+")
fo.write("1-1\n"+"expectations  "+str(integrate.nquad(ff,[bound_x, bound_y])))

def fff(x,y):
    return ((x-y)**2)**2

def ffff(x,y):
    a=fff(x,y)
    b=fg(x)
    c=fh(y)
    return a*b*c

fo.write("\n1-1\n"+"\nVariance "+str(integrate.nquad(ffff,[bound_x, bound_y])[0]-(integrate.nquad(ff,[bound_x, bound_y])[0])**2))


################################ 2-1
def read_data(f1,f2,y1,y2):
    hl1=[]
    hl2=[]
    a=[]
    final=[]
    line=f1.readline()
    line_2=f2.readline()
    while line:
        hl1.append(line.strip('\n'))
        
        line=f1.readline()
    a = [y1 for _ in range(len(hl1))]  
    while line_2:
        hl2.append(line_2.strip('\n'))
        
        line_2=f2.readline()
    b = [y2 for _ in range(len(hl2))]  
   
    hl1.extend(hl2)
    a.extend(b)
    final.append(hl1)
    final.append(a)
    return final
    
    f1.close()
    f2.close()

f=open("/Users/fengheliu/Desktop/clean_real.txt","r+")
f1=open("/Users/fengheliu/Desktop/clean_fake.txt","r")


def combine_data(file1,file2,class1,class2):
    a=read_data(file1,file2,class1,class2)
    X=a[0]
    y=a[1]
    newlist=[]
    for i in range(len(X)):
        newlist.append([X[i],y[i]])
    random.shuffle(newlist)
    newlist=np.array(newlist)
    X_new=newlist[:,0]
    y_new=newlist[:,-1]
    return (X_new,y_new)
    
X_shuffled,y_shuffled=combine_data(f,f1,"read","fake")

def vectorize(dataset):
    tfidf=TfidfVectorizer()
    vec_list=tfidf.fit_transform(dataset).toarray()
    word=tfidf.get_feature_names()
    dictionary=tfidf.vocabulary_
    return (vec_list,dictionary,word)


X=vectorize(X_shuffled)[0]
y=y_shuffled
dictionary=vectorize(X_shuffled)[1]
word=vectorize(X_shuffled)[2]
split=int(len(X)*0.7)
split2=int(len(X)*0.85)
X_train, X_test, X_val, y_train, y_test,y_val = X[:split],X[split:split2],X[split2:],y[:split],y[split:split2],y[split2:] 


def classify_accuracy(criterion,max_depth):
    count=0
    clf=tree.DecisionTreeClassifier(criterion=criterion,max_depth=max_depth)
    clf = clf.fit(X_train,y_train)
    e=clf.predict(X_val)
    for i in range(len(y_val)):
        if y_val[i]!=e[i]:
            count+=1
    return 1-(count/len(y_val))

x=range(10,100,4)


def graph(criterion,max_depth):
    list1=map(lambda x:classify_accuracy(criterion,x),max_depth)
    f=plt.figure()
    plt.plot(max_depth,list(list1))
    plt.title(criterion)
    f.savefig("/Users/fengheliu/Desktop/%s.pdf" % criterion)
    
graph("gini",x)
graph("entropy",x)
        

############################ 2-3 
            
clf=tree.DecisionTreeClassifier(criterion="gini",max_depth=34)
clf = clf.fit(X_train,y_train)
dot_data = StringIO()
tree.export_graphviz(clf,
                        out_file=dot_data,
                        feature_names=word,
                        class_names=["real","fake"],
                    
                        filled=True,rounded=True,
                        impurity=False,max_depth=2)

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())

graph.write_pdf("/Users/fengheliu/Desktop/viz.pdf")


####################################2-4
def ent(x):
    prob=pd.value_counts(x)/len(x)
    return (sum(prob*(-1)*np.log2(prob)))



def info_gain(dictionary,a):
    data=pd.DataFrame(dictionary)
    pro=pd.value_counts(data["class"])/len(data["class"])
    entropy=sum(pro*(-1)*np.log2(pro))
    pro1=data.groupby([a]).apply(lambda x:ent(x["class"]))
    pro2=pd.value_counts(data[a])/len(data[a])
    entropy_gain=sum(pro1*pro2)
    return entropy-entropy_gain

def compute_information_gain(feature_name,feature_value):
    pre_dic={}
    feature_tif=X_train[:,int(dictionary[feature_name])]
    a=[]
    pre_dic["class"]=y_train
    for i in range(len(feature_tif)):
        if feature_tif[i]<feature_value or feature_tif[i]==feature_value:
            a.append("true")
        else:
            a.append("false")
    pre_dic[feature_name]=a
    
    data=pd.DataFrame(pre_dic)
    return info_gain(data,feature_name)

test_list=[["trump",0.056],["trumps",0.164],["hillary",0.069],["trump",0.051],["the",0.042]]


fo.write("\n2-4")
for i in range(len(test_list)):
    results="\n"+test_list[i][0]+str(test_list[i][1])+" information gain is "+str(compute_information_gain(test_list[i][0],test_list[i][1]))+"\n"
    fo.write(results)

  
fo.close()

        






