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
    #counts the numbers of examples in a dataset
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
    def match((self,example):
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
              
              
