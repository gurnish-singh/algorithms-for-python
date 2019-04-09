training_data=[['green',3,'mango'],
                ['yello',3,'mango'],
               ['red',1,'grape'],
               ['red',1,'grape'],
                ['yellow',3,'lemon']
               ]
#column labels
header=['color','diameter','label']
def unique(rows,col):
    #find the unique value for a column in the dataset
    return set([row[col]  for row in rows])
'''set([1,1,2,2,3,4,5,5])
{1, 2, 3, 4, 5}
unique(training_data,0) returns all unique colors'''
def class_count(rows):
    #counts the numbers of labels in a dataset
    counts={}#dictionary
    for row in rows:
        label=row[-1]
        if label not in counts:
            counts[label]=0
        counts[label]+=1
        return counts
def is_numeric(value):
    #simply checks if value is numeric
    return isinstance(value,int) or isinstance(value,float)
class question:
    ''' this class records a column number and a column value'''
    def __init__(self,column,value):
        self.column=column
        self.value=value
    def match(self,example):
        val=example(self.column]
        if is_numeric(val):
              return val>=self.value
        else:
              return value==self.value
    def __repr__(self):
              #to print the question in readable format
        condition='=='
        if is_numeric(self.value):
            condition='>='
        return 'Is %s %s %s?'%(header[self.column],condition,str(self.value))
    def partition(rows,column):
            '''for each row in the dataset check if it matches the
              question if it does add it to true rows else false rows'''
        true_rows,false_rows=[],[]
        for row in rows:
              if question.match(row):
                  true_rows.append(row)
              else:
                  false_rows.append(row)
        return true_rows,false_rows
# let's partition the training dataset wheather the rows are red
#true_rows,false_rows=partition(training_data,question(0,'red'))
#all red roww in true_row,and everytinh else in false_rows
def gini(rows):
    #calculate the gini impurity for a list of rows
    count=class_count(rows)# count is a dictionary
    impurity=1
    for i in counts:
        prob_of_i=count[i]/float(len(rows))
        impurity-=prob_of_i**2
    return impurity
def info_gain(left,right,current_uncertanity):
    ''' information gain=
            the uncertanity of the of the startnig mode - weighted gini impurity
            of the child node'''
    p=float(len(left))/(len(left)+len(right))
    return current_uncertanity-p*gini(left)-(1-p)*gini(right)
def find_best_split(rows):
    ''' find the best question to ask by iterating over feature or value
and by calculating information gain'''
    best_gain=0#keep track of best info_gain
    best_question=None
    curret_uncertanity=gini(rows)
    n_features=len(rows[0])-1#number of columns
    for col in range n_features:
        values=set([row[col] for row in rows])#unqique values in a specific column
        for val in values:
            question=Question(col,val)
            #try splitin the dataset
            true_rows,false_rows=parttition(rows,question)
            if len(true_rows)==0 or len(false_rows)==0:
                continue
            gain_info_gain(true_rows,false_rows,current_uncertanity)
            if gain>=best_gain:
                best_gain,best_question=gain,question
    return best_gain,best_question
class leaf:
    ''' a leaf node classifies data.
this holds a dictionary of class(eg. mango)->
number of times it appers in the rows from the training data that reach this leaf'''
    def __init__(self,rows):
        self.predictions=class_count(rows)
class decision_node:
    # a decision ode askes a question
    def __init__(self,question,true_branch,false_branch):
        self.question=question
        self.true_branch=true_branch
        self.false_branch=false_branch
        
    
              


              
              
