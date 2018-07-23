# -*- coding: utf-8 -*-


# a list of class objects to mimic a C type array of structures
# tested with Python24       vegaseat       30sep2005
class Node(object):
    """__init__() functions as the class constructor"""
    def __init__(self, col=None, activ=None, wLeft=None, wRight=None):
        self.col = col
        self.activ = activ
        self.wLeft = wLeft

totalColumns = 4
        
print()
# Establish the initial Row 1 of nodes
row1NodeList = []
row1NodeList.append(Node(0, 1, 0, 0))
row1NodeList.append(Node(1, 1, 0, 0))
row1NodeList.append(Node(2, 1, 0, 0))
row1NodeList.append(Node(3, 0, 0, 0))
row1NodeList.append(Node(4, 1, 0, 0))

# Redefine the last node (the wrap-around) to have the same value as the first
row1NodeList[totalColumns].activ = row1NodeList[0].activ

# Establish the initial Row 2 of nodes
row2NodeList = []
row2NodeList.append(Node(0, 1, 0, 0))
row2NodeList.append(Node(1, 0, 0, 0))
row2NodeList.append(Node(2, 0, 0, 0))
row2NodeList.append(Node(3, 0, 0, 0))
row2NodeList.append(Node(4, 1, 0, 0))

# Redefine the last node (the wrap-around) to have the same value as the first
row2NodeList[totalColumns].activ = row2NodeList[0].activ


# For Row 1: 
# Find the activation of the node on the left of each given node
#   Note that for the first node in the list (x=0), we find the left-most neighbor 
#     via wrap-around: we look at node in the last column BEFORE the wrap-around. 
x = 0
for node in row1NodeList: 
    if x==0:
        if row1NodeList[totalColumns-1].activ==0:
            row1NodeList[x].wLeft=0
        else:
            row1NodeList[x].wLeft=1
    else:
        if row1NodeList[x-1].activ==0:
            row1NodeList[x].wLeft=0
        else:
            row1NodeList[x].wLeft=1  
    x = x+1

# Find the activation of the node on the right of each given node
#   Note that for the last node in the list (x=totalColumns-1), we find the right-most neighbor 
#     via wrap-around: we look at node in the last column (the one that contains the wrap-around).
x = 0
for node in row1NodeList: 
    if x<totalColumns:
        if row1NodeList[x+1].activ==0:
            row1NodeList[x].wRight=0
        else:
            row1NodeList[x].wRight=1
    else:
        if row1NodeList[0].activ==0:
            row1NodeList[x].wRight=0
        else:
            row1NodeList[x].wRight=1  
    x = x+1    
    
# For Row 1: do the same as previously for Row 1    
x = 0
for node in row2NodeList: 
    if x==0:
        if row2NodeList[totalColumns-1].activ==0:
            row2NodeList[x].wLeft=0
        else:
            row2NodeList[x].wLeft=1
    else:
        if row2NodeList[x-1].activ==0:
            row2NodeList[x].wLeft=0
        else:
            row2NodeList[x].wLeft=1  
    x = x+1

# Find the activation of the node on the right of each given node
#   Note that for the last node in the list (x=totalColumns-1), we find the right-most neighbor 
#     via wrap-around: we look at node in the last column (the one that contains the wrap-around).
x = 0
for node in row2NodeList: 
    if x<totalColumns:
        if row2NodeList[x+1].activ==0:
            row2NodeList[x].wRight=0
        else:
            row2NodeList[x].wRight=1
    else:
        if row2NodeList[0].activ==0:
            row2NodeList[x].wRight=0
        else:
            row2NodeList[x].wRight=1  
    x = x+1     
    
    
print() 
print ('Row 1:')
x = 0
print (' Col:   Activation:    wLeft      wRight')
for node in row1NodeList:
    if x<totalColumns:
        print ('  ', x, '       ', row1NodeList[x].activ, '         ', row1NodeList[x].wLeft, '         ', row1NodeList[x].wRight)
    x = x+1

print() 
print ('Row 2:')
x = 0
print (' Col:   Activation:    wLeft      wRight')
for node in row2NodeList:
    if x<totalColumns:
        print ('  ', x, '       ', row2NodeList[x].activ, '         ', row2NodeList[x].wLeft, '         ', row1NodeList[x].wRight)
    x = x+1    
    

print ()
print ('Horizontal print of both rows (showing wrap-around of first column to far right)')
x = 0
print ('  ', end='')
for node in row1NodeList: 
    if x<totalColumns:
        if row1NodeList[x].activ==0:
            print ('-  ', end='')
        else:
            print ('X  ', end='')
    else:
        if row1NodeList[x].activ==0:
            print ('o  ', end='')
        else:
            print ('x  ', end='')           
    x = x+1
print ('  ') 
x = 0
print ('    ', end='')
for node in row2NodeList: 
    if x<totalColumns:
        if row2NodeList[x].activ==0:
            print ('-  ', end='')
        else:
            print ('X  ', end='')
    else:
        if row2NodeList[x].activ==0:
            print ('o  ', end='')
        else:
            print ('x  ', end='')           
    x = x+1

    

