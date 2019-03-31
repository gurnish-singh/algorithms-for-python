import numpy
def check():
     for i in range(100):
         a = numpy.random.randint(0, 10,size=(4,4)).tolist()
         b = numpy.random.randint(0, 10,size=(4,4)).tolist()
         assert strassen(a,b,4) == straight(a,b)
         assert (numpy.array(strassen(a,b,4)) == numpy.dot(a,b)).all()
     print 'hooray!' 
