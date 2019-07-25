import numpy as np


def dir_vec(A,B):
  return B-A

def norm_vec(A,B):
  return omat@dir_vec(A,B)

def perp_foot(A,B,C):
  m = dir_vec(B,C)
  n = norm_vec(B,C)
  p = np.zeros(2)
  p[0] = m@A
  p[1] = n@B
  #Intersection
  N=np.vstack((m,n))
  P=np.linalg.inv(N)@p
  return P

#Generate line points
def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

def get_coord(r,theta):
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

#Centre and Radius  of the circumcircle
def ccircle(A,B,C):
  p = np.zeros(2)
  n1 = dir_vec(B,A)
  p[0] = 0.5*(np.linalg.norm(A)**2-np.linalg.norm(B)**2)
  n2 = dir_vec(C,B)
  p[1] = 0.5*(np.linalg.norm(B)**2-np.linalg.norm(C)**2)
  #Intersection
  N=np.vstack((n1,n2))
  O=np.linalg.inv(N)@p
  r = np.linalg.norm(A -O)
  return O,r

def icentre(A,B,C):
  p = np.zeros(2)
  t = norm_vec(B,C)
  n1 = t/np.linalg.norm(t)
  t = norm_vec(C,A)
  n2 = t/np.linalg.norm(t)
  t = norm_vec(A,B)
  n3 = t/np.linalg.norm(t)
  p[0] = n1@B- n2@C
  p[1] = n2@C- n3@A
  N=np.vstack((n1-n2,n2-n3))
  I=np.matmul(np.linalg.inv(N),p)
  r = np.abs(n1@(I-B))
  #Intersection
  return I,r

def line_intersect(n1,c1,n2,c2):
  N=np.vstack((n1,n2))
  p = np.zeros(2)
  p[0] = c1
  p[1] = c2
  P=np.linalg.inv(N)@p
  return P
#Intersection

def line_seg_intersect(A,B,C,D):
  n1=omat@(A-D)
  n2=omat@(B-C)
  c1 =  n1@A
  c2 =  n2@B
  P=line_intersect(n1,c1,n2,c2)
  return P
#Intersection

def circ_chord(m,R,O):
  return R - 2*(m.T@(R-O))/(np.linalg.norm(m)**2)*m


#A = np.array([-2,-2]) 
#B = np.array([1,3]) 
dvec = np.array([-1,1]) 
omat = np.array([[0,1],[-1,0]]) 
#AB =np.vstack((A,B)).T

#print (dir_vec(A,B))
#print (norm_vec(A,B))



