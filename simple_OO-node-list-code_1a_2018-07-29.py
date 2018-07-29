# -*- coding: utf-8 -*-


# Tutorial and test program using object-oriented Python to create and populate a
#   list of nodes.

# Python 3.6      Alianna J. Maren   Creation date: July 27, 2018
# For bug-fixes and latest releases: 
#   alianna#aliannajmaren.com
#   alianna.maren@northwestern.edu

# This code works with a single Python object, Node. 
# It creates a 1-D grid of Nodes, initially populated with 0-value activations
#   and 0-values for the next-nearest neighbor weights 'w' (in the same row only).
# It prints out this initial 0-valued grid. 
#
# Then, it creates a set of pre-defined values for certain Nodes, and then
#   computes the actual w-values associated with each of these Nodes. 
# Then it prints the updated Node activations and w-values. 

class Node(object):
    """__init__() functions as the class constructor"""    
    def __init__(self, nodeNum=None, row=None, col=None, activ=None, wLeft=None, wRight=None):
        self.nodeNum = nodeNum
        self.row = row
        self.col = col
        self.activ = activ
        self.wLeft = wLeft
        self.wRight = wRight

    

wLeft = 0 
wRight = 0 
totalRows = 2
totalColumns = 8    
unitVal = 0


NodeList = []
x=0
for i in range(totalRows):
    for j in range(totalColumns):
        NodeList.append(Node(x, i, j, 0, 0, 0))
        x = x+1

# Print the initial value assignments
print()
print("This is the grid layout for a (currently 1-D) CVM grid")
print("  This grid has dimensions of ", totalRows, "rows and ", totalColumns, " columns.")
print("  The two rows create a single zig-zag chain for the 1-D CVM.")
print()
print("These are the node values before assigning certain nodes an activation of 1")
print()
print("This print does not show the wrap-arounds.")
print()

debugPrintOff = True
if not debugPrintOff:
    print()
    print("******************************************")
    print("  Debug printing in effect during this run")
    print("******************************************")
    print()    

debugPrintOff = False
if not debugPrintOff:
    x = 0
    print ()
    print ("-----------------------------------------------------")
    print ("  *** Initial assignment of 0 for all activations ***")  
    print ("-----------------------------------------------------")    
    print ()
    x=0
    for i in range(totalRows): 
        print ()
        print ("Row ", i)
        print (" Col:   Activation:    wLeft      wRight    nodeNum")
        for j in range(totalColumns):
            thisRow   = NodeList[x].row
            thisCol   = NodeList[x].col
            thisActiv = NodeList[x].activ
            thisWLeft = NodeList[x].wLeft
            thisWRight= NodeList[x].wRight
            thisNum   = NodeList[x].nodeNum        
            print ("  ", thisCol, "       ", thisActiv, "         ", thisWLeft, "         ", thisWRight, "       ", thisNum)
            x = x+1
    print()
    

# This assigns activations of '1" to certain nodes
x=0
for i in range(totalRows): 
    for j in range(totalColumns):
        if i==0: # Turn on some nodes in Row 0 
            if j<3:  # Assign value of "1" to first three nodes in Row 1              
                NodeList[x].activ = 1
            if j>3: # In the second set of four columns (columns 4 .. 7)
                if j<7: 
                    NodeList[x].activ = 1
        if i==1: # Turn on some nodes in Row 1 
            if j<1:  # Assign value of "1" to zeroth node in Row 1   
                NodeList[x].activ = 1  
            if j>3: # In the second set of four columns
                if j<5: # Assign value of "1" to fourth node in Row 1   
                    NodeList[x].activ = 1                
        x = x+1        




debugPrintOff = True
if not debugPrintOff:
    x = 0
    print ()
    print ("---------------------------------------------------------")
    print ("  *** After assigning activation of 1 to select nodes ***")
    print ("  *** Values for wLeft and wRight not yet computed    ***")      
    print ("---------------------------------------------------------")    
    print ()
    x=0
    for i in range(totalRows): 
        print ()
        print ("Row ", i)
        print (" Col:   Activation:    wLeft      wRight    nodeNum")
        for j in range(totalColumns):
            thisRow   = NodeList[x].row
            thisCol   = NodeList[x].col
            thisActiv = NodeList[x].activ
            thisWLeft = NodeList[x].wLeft
            thisWRight= NodeList[x].wRight
            thisNum   = NodeList[x].nodeNum        
            print ("  ", thisCol, "       ", thisActiv, "         ", thisWLeft, "         ", thisWRight, "       ", thisNum)
            x = x+1
    print()


# This updates the wLeft values given that certain nodes now have an activation of "1"
x = 0
for i in range(totalRows): 
    for j in range(totalColumns):
        q = totalColumns*i    # q denotes first node of the i-th row
        if j==0:
            # test to see if at the beginning of row; if so, assign wRight from last element on row
            if NodeList[q-1].activ==0:
                NodeList[x].wLeft=0
            else:
                NodeList[x].wLeft=1
        else:
            if NodeList[x-1].activ==0:
                NodeList[x].wLeft=0
            else:
                NodeList[x].wLeft=1  
        x = x+1

# Optional list-print code: identify what the node number is as well as the node activation, and left and right nodes
# This updates the wRight values given that certain nodes now have an activation of "1"

debugPrintOff = True
if not debugPrintOff:
    x = 0
    print ()
    print ("----------------------------------------------------")
    print ("  *** Invoking debug print after computing w-Left***")
    print ("----------------------------------------------------")    
    print ()
    print ("  x       row       col     q=ttlCols*i (x)activ  (x-1)activ  (x)wLeft")
    for i in range(totalRows): 
        print ()
        print (" Row ", i)
        for j in range(totalColumns):
            q = totalColumns*i    # q denotes first node of the i-th row
            # test to see if at the beginning of row; if so, assign wLeft from last element on row
            if j==0:  # At the last node in the row
                wrapLeftAtCol0 = q+totalColumns-1
                print (" ", x, "      ", i, "       ", j, "          ", q, "         ", NodeList[x].activ, "        ", NodeList[wrapLeftAtCol0].activ, "          ", NodeList[x].wLeft)
            else:
            # Deal with all nodes after the first column of that row    
                print (" ", x, "      ", i, "       ", j, "          ", q, "         ", NodeList[x].activ, "        ", NodeList[x-1].activ, "          ", NodeList[x].wLeft)
            x = x+1        
print ()        



#-------------------

      


# This updates the wRight values given that certain nodes now have an activation of "1"
x = 0
for i in range(totalRows): 
    for j in range(totalColumns):
        q = totalColumns*i    # q denotes first node of the i-th row
        # test to see if at the end of row; if so, assign wRight from first element on row
        if j==totalColumns-1:
            if NodeList[q].activ==0:
                NodeList[x].wRight=0
            else:
                NodeList[x].wRight=1
        else:
            if NodeList[x+1].activ==0: 
                NodeList[x].wRight=0                
            else:    
                if NodeList[x+1].activ==0:
                    NodeList[x].wRight=0
                else:
                    NodeList[x].wRight=1  
        x = x+1        


# Optional list-print code: identify what the node number is as well as the node activation, and left and right nodes
# This updates the wRight values given that certain nodes now have an activation of "1"

debugPrintOff = True
if not debugPrintOff:
    x = 0
    print ()
    print ("----------------------------------------------------")
    print ("  *** Invoking debug print after computing w-Right***")
    print ("----------------------------------------------------")    
    print ()
    print ("  x       row       col     q=ttlCols*i (x)activ  (x+1)activ  (x)wRight")
    for i in range(totalRows): 
        print ()
        print (" Row ", i)
        for j in range(totalColumns):
            q = totalColumns*i    # q denotes first node of the i-th row
            # test to see if at the end of row; if so, assign wRight from first element on row
            if j==totalColumns-1:  # At the last node in the row
                print (" ", x, "      ", i, "       ", j, "          ", q, "         ", NodeList[x].activ, "        ", NodeList[q].activ, "          ", NodeList[x].wRight)
            else:
            # Deal with all nodes leading up to the final column of that row    
                print (" ", x, "      ", i, "       ", j, "          ", q, "         ", NodeList[x].activ, "        ", NodeList[x+1].activ, "          ", NodeList[x].wRight)
            x = x+1        
print ()




print()
print("----------------------------------------------------------------------")
print("  *** Node values after assigning certain nodes an activation of 1 ***")
print("----------------------------------------------------------------------")
x=0
for i in range(totalRows): 
    print ()
    print ("Row ", i)
    print (" Col:   Activation:    wLeft      wRight    nodeNum")
    for j in range(totalColumns):
        thisRow   = NodeList[x].row
        thisCol   = NodeList[x].col
        thisActiv = NodeList[x].activ
        thisWLeft = NodeList[x].wLeft
        thisWRight= NodeList[x].wRight
        thisNum   = NodeList[x].nodeNum        
        print ("  ", thisCol, "       ", thisActiv, "         ", thisWLeft, "         ", thisWRight, "       ", thisNum)
        x = x+1

print()
print()
print("This is a visual depiction of the grid layout")
print ("(showing wrap-around of first column to far right)")
print ()
x = 0
for i in range(totalRows):
    if i % 2 == 0:
        evenNum = True # Even 
    else:
        evenNum = False # Odd
    print("Row ", i, ":  ", end="")
    if evenNum == False: print ("  ", end="")
    for j in range(totalColumns): 
        if NodeList[x].activ==0:
            print ("-  ", end="")
        else:
            print ("X  ", end="")
# Print the wrap-around
        x = x+1
    if NodeList[x-totalColumns].activ==0:
        print ('o  ', end='')
    else:
        print ('x  ', end='')           
    print ('  ')       




