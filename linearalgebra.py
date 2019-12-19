#write a python programme to find operations and linear algebraic operations of two 3x3 matrices by using numpy
#operations on matrices
import numpy as np
a=np.array(input('enter 3*3 matrix:'))
b=np.array(input('enter another 3*3 matrix:'))
c=np.add(a,b)
print 'addition of two matirces:\n',c
d=np.subtract(a,b)
print 'subtraction of two matrices:\n',d
e=np.multiply(a,b)
print 'element by element multiplication of two matrices:\n',e
f=np.dot(a,b)
print 'multiplication of two matrices:\n',f
g=np.divide(a,b)
print 'element by element division of two matrices:\n',g
h=np.linalg.inv(a)
print 'inverse of\n',a,'\n is:',h
j=np.linalg.eig(a)
print 'eigen vectors of\n',a,'\n is:',j
k=np.linalg.matrix_rank(a)
print 'rank of a matrix of\n',a,'\n is:',k
l=np.linalg.det(a)
print 'determinant of\n',a,'\n is:',l
m=np.linalg.eigvals(a)
print 'eigen values of\n',a,'\n is:',m
n=np.linalg.qr(a)
print 'qr decomposition of\n',a,'\n is:',n
o=np.linalg.matrix_power(a,3)
print 'matrix power of\n',a,'\n is:',o



