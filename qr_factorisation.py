# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 17:43:20 2019

@author: ashita
"""

import numpy as np
def main():
    m=int(input("enter m,rows"))
    n=int(input("enter n,columns"))
    print("enter elements of array with a space")
    entries = list(map(int, input().split()))
    a = np.array(entries).reshape(m,n) 
    print(a)
    q, r = qr(a)
    print('q:\n', q.round(6))
    print('r:\n', r.round(6))

def qr(a):
    m,n=a.shape
    Q = a[:,0] / np.sqrt(np.dot(a[:,0],a[:,0]))
    for j in range(1, n):
        q = a[:, j] - np.dot(Q, np.dot(Q.T, a[:, j]))
        r = np.sqrt(q.dot(q))
        Q = np.column_stack([Q, q / r])
    R=np.dot(Q.T,a)
    return Q,R

if __name__=="__main__":
    main()