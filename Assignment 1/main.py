# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 19:56:40 2020

@author: Sid's Lap
"""
#%%
import numpy as np
import tensorflow as tf
from tensorflow import keras
import random
import sys
#%%
inFile = sys.argv[1]

input=[]
with open(inFile, 'r') as filehandle:
	for line in filehandle:
		line = line[:-1]
		input.append(line)


#%%
def fizzbuzz1(i):
    if i % 15 ==0:
        return ("FizzBuzz")
    elif i % 5==0:
       return ("Buzz")
    elif i%3==0:
     return ("Fizz")
    else:
     return (str(i))
#%%
def fizzbuzz2(i):
    if i % 15 ==0:
        return [0,0,0,1]
    elif i % 5==0:
       return [0,0,1,0]
    elif i%3==0:
     return [0,1,0,0]
    else:
     return [1,0,0,0]
#%%

def decimal_to_binary(i):
  binrep=np.zeros(10)
  j=9;
  while(i!=0):
    binrep[j]=i%2;
    i=int(i/2);
    j=j-1;
  return binrep
#%%
def prediction_fizzbuzz(i, pred): 
    return [str(i), "fizz", "buzz", "fizzbuzz"][pred.argmax()]

#%%
input = np.array(list(map(int, input))) 
m=len(input);
f1=open('software1.txt','w');
f2=open('software2.txt','w');
model = tf.keras.models.load_model('./model/model_final.h5')
errors=0;
correct=0;
for i in range(m):
    f1.write(fizzbuzz1(input[i])); 
    f1.write('\n');
    x = decimal_to_binary(input[i])
    y = model.predict(np.array(x).reshape(-1,10))
    f2.write(prediction_fizzbuzz(input[i],y)); 
    f2.write('\n');
    
    
f1.close()
f2.close()
