# -*- coding: utf-8 -*-

"""
Created on Sunday Sept 23, 2018

@author: alian
"""

####################################################################################################
# Python 3.6      Alianna J. Maren   Creation date: Sept. 23, 2018
#
# For bug-fixes and latest releases: 
#   alianna#aliannajmaren.com
#   alianna.maren@northwestern.edu
#
# Pulled from GitHub: 
# Original file 2D-CVM-OO_basic-config-vars_V-and-V_1-1_2018-09-23.py 
#
# Computing configuration variables for the Cluster Variation Method
#
# Tutorial and test program using object-oriented Python to create and populate a
#   list of nodes for a 2-D CVM grid.
# This program has extensive printouts enabling V&V for the configuration variables. 
####################################################################################################
# Import the following Python packages

import random
import itertools
import numpy as np
import pylab
import matplotlib
from math import exp
from math import log
from matplotlib import pyplot as plt
from random import randrange, uniform #(not sure this is needed, since I'm importing random)


####################################################################################################
#
# About this code: 
#
# This code works with a single Python object, Node. 
# It creates a 2-D grid of Nodes, initially populated with 0-value activations
#   and 0-values for the next-nearest neighbor weights 'w' (in the same row only).
#
# Then, it creates a set of pre-defined values for certain Nodes, and then
#   computes the actual w-values associated with each of these Nodes. 
# Then it prints the updated Node activations and w-values. 
#
####################################################################################################



####################################################################################################
####################################################################################################
#
# Object definitions
#
####################################################################################################
####################################################################################################


# ================================================================================================ # 
# ------------------------------------------------------------------------------------------------ #    
#  The 'node' class
# ------------------------------------------------------------------------------------------------ #
# ================================================================================================ #   

class Node(object):
    """__init__() functions as the class constructor"""    
    def __init__(self, nodeNum=None, row=None, col=None, activ=None, wLeft=None, wRight=None):
        self.nodeNum = nodeNum
        self.row = row
        self.col = col
        self.activ = activ
        self.wLeft = wLeft
        self.wRight = wRight



####################################################################################################
####################################################################################################
#
# Procedure to welcome the user and identify the code
#
####################################################################################################
####################################################################################################

def printWelcome ():

    print() 
    print()
    print()
    print(" ******************************************************************************")   
    print(" ******************************************************************************")
    print()
    print(" Welcome to the Object-Oriented 2-D Cluster Variation Method")
    print(" Version 1.1, 09/23/2018, A.J. Maren")
    print(' This version computes the configuration values for an initial grid')
    print(' There are no thermodynamic computations or free energy minimization steps in this code')
#    print(" This version computes the behavior of a perturbed unitArray,")
#    print("  based on minimizing the free energy both before and after perturbation.")
#    print() 
#    print(" By changing parameters in the main code, the user can select:'")
#    print("   x1 value - relative proportion of A (on) vs. B (off) nodes")
#    print("     y, w, and z configuration values for a given x, and")
#    print("   perturbPrcnt - the percentage of nodes in the unitArray that")
#    print("     will be flipped from one state to another.")
    print() 
    print(" For comments, questions, or bug-fixes, contact: alianna.maren@northwestern.edu")
    print(" Alternate email address: alianna@aliannajmaren.com")
    print()
    print("   NOTE: In these calculations, x1 = A (node activation values are at value 1),")
    print("                            and x2 = B (node activation values are at value 0).")
    print()
    print(" ******************************************************************************")
    print()
    return()



####################################################################################################
####################################################################################################
#
# Procedure to print the debug printing status
#
####################################################################################################
####################################################################################################

def printDebugPrintStatus ():

    if not debugPrintOff:
        print()
        print("******************************************")
        print("  Debug printing in effect during this run")
        print("******************************************")
        print()   
    else: 
        print()
        print("******************************************")
        print("  Debug printing is off during this run")
        print("******************************************")
        print()  

    return()



####################################################################################################
####################################################################################################
#
# Print procedure to describe the grid  
#
####################################################################################################
####################################################################################################

def printGridOverview ():

    print()
    print("The grid layout that we will use is for a (currently 1-D) CVM grid")
    print("  This grid has dimensions of ", gridRows, "rows and ", gridColumns, " columns.")
    print("  The two rows create a single zig-zag chain for the 1-D CVM.")
    print("The grid prints do not show the wrap-arounds.")    
    print()
    return () 



####################################################################################################
####################################################################################################
#
# Print procedure to identify the grid is before pattern activation assignments  
#
####################################################################################################
####################################################################################################

def printGridInitialIdentification ():

    # Print the initial value assignments
    print ()
    print ("-------------------------------------------------------")
    print ("  *** Initial assignment of 0 for all activations   ***")  
    print ("-------------------------------------------------------")    
    print ()
    return () 



####################################################################################################
####################################################################################################
#
# Print procedure to identify the grid is before pattern activation assignments  
#
####################################################################################################
####################################################################################################

def printGridPatternIdentification ():

    # Print the node value assignments after the pre-determined pattern has been imposed
    #  and the new configuration variable values have been computed. 
    print ()
    print ("-------------------------------------------------------")
    print ("  *** Pre-determined initial node value assignments ***")  
    print ("-------------------------------------------------------")    

    return () 



####################################################################################################
####################################################################################################
#
# Debug print procedure to print the grid node values  
#
####################################################################################################
####################################################################################################

def printGridNodeValues (gridNodeList): 

    # Print the initial value assignments
    x=0
    for i in range(gridRows): 
        print ()
        print ("Row ", i)
        print (" Col:   Activation:    wLeft      wRight    nodeNum")
        for j in range(gridColumns):
            thisRow   = gridNodeList[x].row
            thisCol   = gridNodeList[x].col
            thisActiv = gridNodeList[x].activ
            thisWLeft = gridNodeList[x].wLeft
            thisWRight= gridNodeList[x].wRight
            thisNum   = gridNodeList[x].nodeNum        
            if j<10:
                print ("   ", thisCol, "       ", thisActiv, "         ", thisWLeft, "         ", thisWRight, "       ", thisNum)
            else:
                print ("  ", thisCol, "       ", thisActiv, "         ", thisWLeft, "         ", thisWRight, "       ", thisNum)                
            x = x+1
        print()   
    return ()  



####################################################################################################
####################################################################################################
#
# Debug print the grid, showing physical relationships between the nodes  
#
####################################################################################################
####################################################################################################

def printGrid (gridNodeList): 
   
    print()
    print("This is a visual depiction of the grid layout")
    print ("(showing wrap-around of first column to far right)")
    print ()
    x = 0
    for i in range(gridRows):
        if i % 2 == 0:
            evenNum = True # Even 
        else:
            evenNum = False # Odd
        print("Row ", i, ":  ", end="")
        if evenNum == False: print ("  ", end="")
        for j in range(gridColumns): 
            if gridNodeList[x].activ==0:
                print ("-  ", end="")
            else:
                print ("X  ", end="")
    # Print the wrap-around
            x = x+1
        if gridNodeList[x-gridColumns].activ==0:
            print ('o  ', end='')
        else:
            print ('x  ', end='')           
        print ('  ')       
    return()




####################################################################################################
####################################################################################################
#
# Procedure to print the details after computing a set of w-Left values
#
####################################################################################################

def printDetailWLeftComputation (gridNodeList):
       
# Optional list-print code: identify what the node number is as well as the node activation, and left and right nodes
# This updates the wRight values given that certain nodes now have an activation of "1"

    x = 0
    print ()
    print ("------------------------------------------------------")
    print ("  *** Invoking debug print after computing w-Right ***")
    print ()
    print ('      A value of 1 for x-wLeft means that the node  ')
    print ('        to the immediate left of the x-node has  ')
    print ('        a value of 1.  ')
    print ('      The values for x-1.activ and for x-wLeft')    
    print ('        should be the same.') 
    print ('      The values for x-1.activ should correspond to ')    
    print ('        the node to the immediate left of the x-node.')
    print ()
    print ('      The value for i in q=ttlCols*i corresponds to the ')         
    print ('        row number.  ')   
    print ('      The value for q corresponds to the first node in  ') 
    print ('        that row.  ')       
    print ("------------------------------------------------------")   
    print ()
    print ("  x       row       col     q=ttlCols*i (x)activ  (x-1)activ  (x)wLeft")
    for i in range(gridRows): 
        print ()
        print (" Row ", i)
        for j in range(gridColumns):
            q = gridColumns*i    # q denotes first node of the i-th row
            # test to see if at the beginning of row; if so, assign wLeft from last element on row
            if j==0:  # At the beginning node in the row
                wrapLeftAtCol0 = q+gridColumns-1
                print (" ", x, "      ", i, "       ", j, "          ", q, "         ", gridNodeList[x].activ, "        ", gridNodeList[wrapLeftAtCol0].activ, "          ", gridNodeList[x].wLeft)
            else:
            # Deal with all nodes after the first column of that row    
                print (" ", x, "      ", i, "       ", j, "          ", q, "         ", gridNodeList[x].activ, "        ", gridNodeList[x-1].activ, "          ", gridNodeList[x].wLeft)
            x = x+1        
    print ()        

    return()    



####################################################################################################
####################################################################################################
#
# Procedure to print the details after computing a set of w-Right values 
#
####################################################################################################

def printDetailWRightComputation (gridNodeList):

# Optional list-print code: identify what the node number is as well as the node activation, and left and right nodes
# This updates the wRight values given that certain nodes now have an activation of "1"

    x = 0
    print ()
    print ("------------------------------------------------------")
    print ("  *** Invoking debug print after computing w-Right ***")
    print ()
    print ('      A value of 1 for x-wRight means that the node  ')
    print ('        to the immediate right of the x-node has  ')
    print ('        a value of 1.  ')
    print ('      The values for x+1.activ and for x-wRight')    
    print ('        should be the same.') 
    print ('      The values for x+1.activ should correspond to ')    
    print ('        the node to the immediate right of the x-node.')
    print ()
    print ('      The value for i in q=ttlCols*i corresponds to the ')         
    print ('        row number.  ')   
    print ('      The value for q corresponds to the first node in  ') 
    print ('        that row.  ')       
    print ("------------------------------------------------------")    
    print ()
    print ("  x       row       col     q=ttlCols*i (x)activ  (x+1)activ  (x)wRight")
    for i in range(gridRows): 
        print ()
        print (" Row ", i)
        for j in range(gridColumns):
            q = gridColumns*i    # q denotes first node of the i-th row
            # test to see if at the end of row; if so, assign wRight from first element on row
            if j==gridColumns-1:  # At the last node in the row
                print (" ", x, "      ", i, "       ", j, "          ", q, "         ", gridNodeList[x].activ, "        ", gridNodeList[q].activ, "          ", gridNodeList[x].wRight)
            else:
            # Deal with all nodes leading up to the final column of that row    
                print (" ", x, "      ", i, "       ", j, "          ", q, "         ", gridNodeList[x].activ, "        ", gridNodeList[x+1].activ, "          ", gridNodeList[x].wRight)
            x = x+1        
    print ()

    return ()    
    


####################################################################################################
####################################################################################################

# >>>>>>> Actual Working Functions Start HERE <<<<<< #

####################################################################################################
####################################################################################################
#
# Function to obtain the array size specifications (currently DEFINED for the user; not a choice)
#
# Note: The code is ONLY set up to work with a grid consisting of an EVEN number of rows
#
####################################################################################################
####################################################################################################

def obtainGridSizeSpecs ():

    gridColumns = 12
    gridRows = 2   

# Alternate code to use later - allow users to specify grid size
#    x = input('Enter gridColumns: ')
#    gridColumns = int(x)
#    print 'gridColumns is', gridColumns  
          
#    x = input('Enter gridRows: ')
#    gridRows = int(x)
#    print 'gridRows is', gridRows

                          
    gridSizeList = (gridColumns, gridRows, unitVal, wLeft, wRight)  
    return (gridSizeList)  



####################################################################################################
####################################################################################################
#
# Function to obtain the initial node specifications 
#
####################################################################################################
####################################################################################################

def obtainInitialNodeSpecs (): 

    initialNodeVal = 0  
    initialWLeft = 0 
    initialWRight = 0 

    initialNodeSpecsList = (initialNodeVal, initialWLeft, initialWRight)  
    return (initialNodeSpecsList)  



####################################################################################################
####################################################################################################
#
# Function to assign initial values (0) to nodes and their config variables 
#
####################################################################################################
####################################################################################################

def createInitialGridNodeList ():

    initialGridNodeList = []
    x=0
    for i in range(gridRows):
        for j in range(gridColumns):
            initialGridNodeList.append(Node(x, i, j, 0, 0, 0))
            x = x+1
    
    printGridNodeValues (initialGridNodeList)

    return (initialGridNodeList)  
   


####################################################################################################
####################################################################################################
#
# Function to give nodes the activation values according to a specified pattern 
#
####################################################################################################
####################################################################################################


def assignInitialNodeActivations (gridNodeList): 
# This assigns activations of '1" to certain nodes
    x=0
    for i in range(gridRows): 
        for j in range(gridColumns):
            if i==0: # Turn on some nodes in Row 0 
                if j<3:  # Assign value of "1" to first three nodes in Row 1  (nodes 0 .. 2)            
                    gridNodeList[x].activ = 1
                if j>3: # In the second set of four columns (columns 4 .. 7)
                    if j<7: # Assign value of "1" to nodes 4 .. 6 in Row 1 
                        gridNodeList[x].activ = 1
                if j>7: # In the third set of four columns (columns 8 .. 11)
                    if j<11: # Assign value of "1" to nodes 8 .. 10 in Row 1 
                        gridNodeList[x].activ = 1                    
            if i==1: # Turn on some nodes in Row 1 
                if j<1:  # Assign value of "1" to zeroth node in Row 1   
                    gridNodeList[x].activ = 1  
                if j>3: # In the second set of four columns
                    if j<5: # Assign value of "1" to fourth node in Row 1   
                        gridNodeList[x].activ = 1                
                if j>7: # In the third set of four columns
                    if j<9: # Assign value of "1" to eighth node in Row 1   
                        gridNodeList[x].activ = 1 
            x = x+1 

    return(gridNodeList)



####################################################################################################
####################################################################################################
#
# Function to update the w-config variables to the left of each node 
#
####################################################################################################
####################################################################################################
      
def updateWLeftConfigVars (gridNodeList):
    # This updates the wLeft values given that certain nodes now have an activation of "1"
    x = 0
    for i in range(gridRows): 
        for j in range(gridColumns):
            q = gridColumns*i    # q denotes first node of the i-th row
            if j==0:
                # test to see if at the beginning of row; if so, assign wRight from last element on row
                if gridNodeList[q-1].activ==0:
                    gridNodeList[x].wLeft=0
                else:
                    gridNodeList[x].wLeft=1
            else:
                if gridNodeList[x-1].activ==0:
                    gridNodeList[x].wLeft=0
                else:
                    gridNodeList[x].wLeft=1  
            x = x+1
 
    return (gridNodeList)



####################################################################################################
####################################################################################################
#
# Function to update the w-config variables to the right of each node 
#
####################################################################################################
####################################################################################################

def updateWRightConfigVars (gridNodeList):
    
# This updates the wRight values given that certain nodes now have an activation of "1"
    x = 0
    for i in range(gridRows): 
        for j in range(gridColumns):
            q = gridColumns*i    # q denotes first node of the i-th row
            # test to see if at the end of row; if so, assign wRight from first element on row
            if j==gridColumns-1:
                if gridNodeList[q].activ==0:
                    gridNodeList[x].wRight=0
                else:
                    gridNodeList[x].wRight=1
            else:
                if gridNodeList[x+1].activ==0: 
                    gridNodeList[x].wRight=0                
                else:    
                    if gridNodeList[x+1].activ==0:
                        gridNodeList[x].wRight=0
                    else:
                        gridNodeList[x].wRight=1  
            x = x+1        

    return (gridNodeList)



####################################################################################################
####################################################################################################
#
# Function to identify two nodes that can be swapped
    # Return: list containing node 1 row & column, and node 2 row & column
#
####################################################################################################
####################################################################################################

def identifyNodeSwap(gridNodeList):

# --------------------------------------------------------------------
# User Interaction
# --------------------------------------------------------------------    

    goodSwap = False # initialze whether we have a good swap
    
    print()
    print("You can select two nodes to swap; these should be one ON node and one OFF node")
    print()
    print("  First node:")
    print()
    # User picks a new row
    print("Select a row number between 0 and ", gridRows, "inclusive" )
    userRow = int(input("Please enter a row number: "))
    success = True
    if userRow>1:
        success = False
    if userRow<0:
        success = False   
    if success == True:
        print("Successful row pick")
        print()
    if success == False:
        newTry = 0
        while newTry < 3:
            newTry = newTry + 1
            userRow = int(input("Please select a row number that is either 0 or 1: "))
            if userRow < 2:
                if userRow > -1:
                    success = True
                    print("Successful row pick on new try: ", newTry, "with row number: ", userRow)
                    print()
                    break
                print("New try number: ", newTry)
    if success == False: 
        print("Oops! Looks like you're out of tries to select a row.")  
    
    # User picks a new column
    print("Select a column number between 0 and ", gridColumns, "inclusive" )    
    userCol = int(input("Please enter a column number: "))
    success = True
    if userCol>gridColumns:
        success = False
    if userCol<0:
        success = False   
    if success == True:
        print("Successful column pick")
        print()    
    if success == False:
        newTry = 0
        while newTry < 3:
            newTry = newTry + 1
            userCol = int(input("Please select a column number that is within range: "))
            if userCol < gridColumns:
                if userCol > -1:
                    success = True
                    print("Successful column pick on new try: ", newTry, "with column number: ", userCol)
                    print()
                    break
                print("New try number: ", newTry)
    if success == False: 
        print("Oops! Looks like you're out of tries to select a column.")  
       
    print()
    print("Your first node is at row ", userRow, " and column ", userCol)
    nodeNum = userRow*gridColumns + userCol
    node1Activ = gridNodeList[nodeNum].activ
    print("  This node has activation ", node1Activ)
    print()
    print("Now, please select a node that has a different activation.")
       
    
    # Starting user interaction for second node pick
    
    # User picks a new row
    print("Select a row number between 0 and ", gridRows, "inclusive" )
    userRow2 = int(input("Please enter a row number: "))
    success = True
    if userRow2>1:
        success = False
    if userRow2<0:
        success = False   
    if success == True:
        print("Successful row pick")
        print()
    if success == False:
        newTry = 0
        while newTry < 3:
            newTry = newTry + 1
            userRow2 = int(input("Please select a row number that is either 0 or 1: "))
            if userRow2 < 2:
                if userRow2 > -1:
                    success = True
                    print("Successful row pick on new try: ", newTry, "with row number: ", userRow2)
                    print()
                    break
                print("New try number: ", newTry)
    if success == False: 
        print("Oops! Looks like you're out of tries to select a row.")  
    
    # User picks a new column
    print("Select a column number between 0 and ", gridColumns, "inclusive" )    
    userCol2 = int(input("Please enter a column number: "))
    success = True
    if userCol2>gridColumns:
        success = False
    if userCol<0:
        success = False   
    if success == True:
        print("Successful column pick")
        print()    
    if success == False:
        newTry = 0
        while newTry < 3:
            newTry = newTry + 1
            userCol2 = int(input("Please select a column number that is within range: "))
            if userCol2 < gridColumns:
                if userCol > -1:
                    success = True
                    print("Successful column pick on new try: ", newTry, "with column number: ", userCol2)
                    print()
                    break
                print("New try number: ", newTry)
    if success == False: 
        print("Oops! Looks like you're out of tries to select a column.")  
    
    print()
    print("Your second node is at row ", userRow2, " and column ", userCol2)
    nodeNum2 = userRow2*gridColumns + userCol2
    node2Activ = gridNodeList[nodeNum2].activ
    print("  This node has activation ", node2Activ)
    print() 
    if node1Activ == node2Activ:
        print("Sorry, the two nodes have the same activation; closing program.") 
    else:
        print("The two nodes have different activations; we'll attempt the swap.") 
        goodSwap = True

    nodeSwapList = [0,0,0,0] # initialize the Node 1 row & column, and the Node 2 row & column, to 0
    if goodSwap:
        nodeSwapList[0] = userRow
        nodeSwapList[1] = userCol
        nodeSwapList[2] = userRow2
        nodeSwapList[3] = userCol2
        # print the nodes to be swapped
        print (' The 1st node to be swapped is at row ', userRow, ' and column ', userCol)
        print (' The 2nd node to be swapped is at row ', userRow2, ' and column ', userCol2) 
        
    return (nodeSwapList)



####################################################################################################
####################################################################################################
#
# Function to actually perform the swap between two nodes and update their configuration values
    # Return: updated gridNodeList
#
####################################################################################################
####################################################################################################

def performNodeSwap (nodeSwapList, gridNodeList): 
    
    node1Row = nodeSwapList[0]
    node1Col = nodeSwapList[1]
    node2Row = nodeSwapList[2]
    node2Col = nodeSwapList[3]
    
    node1Position = node1Row*gridColumns + node1Col
    node2Position = node2Row*gridColumns + node2Col       

    node1Activ = gridNodeList[node1Position].activ
    node2Activ = gridNodeList[node2Position].activ 
    
    localDebugPrintOff = True # Turn this to 'False' to see confirmation of swap nodes
    if not localDebugPrintOff:
        print (' node1Position = ', node1Position, ' with activation ', node1Activ)        
        print (' node2Position = ', node2Position, ' with activation ', node2Activ)
    localDebugPrintOff = True     

    gridNodeList[node1Position].activ = node2Activ
    gridNodeList[node2Position].activ = node1Activ 
    
    localDebugPrintOff = True # Turn this to 'False' to see confirmation of swap nodes
    if not localDebugPrintOff:
        print (' node1Position = ', node1Position, ' now has activation ', gridNodeList[node1Position].activ)        
        print (' node2Position = ', node2Position, ' now has activation ', gridNodeList[node2Position].activ)
    localDebugPrintOff = True  

    # Now we need to update the configuration variables for the nodes.
    updateWLeftConfigVars (gridNodeList)    
    updateWRightConfigVars (gridNodeList) 

    return (gridNodeList)



####################################################################################################
####################################################################################################
# ------------------------------------------------------------------------------------------------ #
 #  main program starts here   
# ------------------------------------------------------------------------------------------------ #
####################################################################################################
####################################################################################################

def main():

# ================================================================================================ # 
# ------------------------------------------------------------------------------------------------ #    
#  Define and initialze global variables
# ------------------------------------------------------------------------------------------------ #
# ================================================================================================ #    
    global debugPrintOff
    global detailedDebugPrintOff
    global detailedAdjustMatrixPrintOff
    global beforeAndAfterAdjustedMatrixPrintOff
    global ZDebugPrintOff
    
    global blnkspc
    
    global gridColumns
    global gridRows
    global evenLayers
    global pairs

#  Initialze the grid parameters
    evenLayers = True

#  Initialze the debug print booleans
    debugPrintOff = True
    detailedDebugPrintOff = True
    ZDebugPrintOff = True
    detailedAdjustMatrixPrintOff = True
    beforeAndAfterAdjustedMatrixPrintOff = True #local variable; passed to computeConfigVariables
        #  It will determine whether we print the contents of the x-array at the
        #  beginning and end of the adjust-matrix step. 
    
# ================================================================================================ # 
# ------------------------------------------------------------------------------------------------ #    
#  Define lists
# ------------------------------------------------------------------------------------------------ #
# ================================================================================================ #      

    arraySizeList = list() # list of the grid size parameters (num rows, num columns) 
    initialNodeSpecsList = list() # list of the initial values to assign when creating a node
    gridNodeList = list() # list of all the nodes in the grid    
    nodeSwapList = list() # list containing row and column numbers of two nodes to swap; 4 list elements
    sysVarsList = list() # list of all the thermodynamic system variables   
   

# ================================================================================================ # 
# ------------------------------------------------------------------------------------------------ #    
#  Initialze lists
# ------------------------------------------------------------------------------------------------ #
# ================================================================================================ #      

    gridSizeList = obtainGridSizeSpecs ()
    gridColumns = gridSizeList[0]
    gridRows = gridSizeList [1]
    
    initialNodeSpecsList = obtainInitialNodeSpecs ()
    unitVal     = initialNodeSpecsList[0] 
    wLeft       = initialNodeSpecsList[1] 
    wRight      = initialNodeSpecsList[2]  
    
    gridNodeList = []     # initialize to an empty list



# ================================================================================================ # 
# ================================================================================================ # 
#   
#  Start __main__ (actual computations)
#  
# ================================================================================================ # 
# ================================================================================================ # 

    printWelcome()
    printDebugPrintStatus ()
    printGridOverview () 

# Construct the initial list of nodes for the grid, populating with initial values  
    initialGridNodeList = createInitialGridNodeList ()
    localDebugPrintOff = True  # Turn this to 'False' to see the initial assignment of zero-values
    if not localDebugPrintOff:
        printGridInitialIdentification ()   
        printGridNodeValues (initialGridNodeList) 
        # Print the visual grid
        printGrid (initialGridNodeList) 
    localDebugPrintOff = True    
   
    
# Change the activation values of the grid nodes according to a pre-set pattern; 
#  compute the configuration variables    
    gridNodeList = assignInitialNodeActivations (initialGridNodeList) 
    updateWLeftConfigVars (gridNodeList)
    # This allows the user to see the details of computing the left-w config values
    localDetailedDebugPrintOff = True # Turn this to 'False' to see the details
    if not localDetailedDebugPrintOff:
        printDetailWLeftComputation (gridNodeList)        
    localDetailedDebugPrintOff = True

    updateWRightConfigVars (gridNodeList)
    # This allows the user to see the details of computing the right-w config values
    localDetailedDebugPrintOff = True # Turn this to 'False' to see the details
    if not localDetailedDebugPrintOff:
        printDetailWRightComputation (gridNodeList)        
    localDetailedDebugPrintOff = True


    localDebugPrintOff = False # Turn this to 'False' to see the initial pattern assignment
    if not localDebugPrintOff:
        printGridPatternIdentification ()   
        printGridNodeValues (gridNodeList)       
    localDebugPrintOff = True
    # Print the visual grid
    # Note: we'll print this grid regardless of debug print status
    printGrid (gridNodeList) 


# User can now swap any two nodes, subject to the condition that one must go from 1 => 0 
#  and the other from 0 => 1
    # Obtain the Node 1 row & column and the Node 2 row and column of two nodes to swap
    nodeSwapList = identifyNodeSwap (gridNodeList)
    


    # Before making the swap, print the previous visual grid
    print ()
    print (' The previous grid was:')
    printGrid (gridNodeList)     

    # Perform the actual swap
    gridNodeList = performNodeSwap (nodeSwapList, gridNodeList)
    goodSwap = True
    if nodeSwapList[0] == 0:
        if nodeSwapList[1] == 0:       
            if nodeSwapList[0] == 0:
                if nodeSwapList[1] == 0: goodSwap = False    


    if not goodSwap:
        print ()
        print ('Node selections do not give a good swap; closing program.')
    else: 
        # Print the new visual grid
        print ()
        print ('The new grid is:')
        printGrid (gridNodeList)  
    print ()
    print (' Thank you and goodbye!')
    
    

####################################################################################################
# Obtain unit array size in terms of array_length (M) and layers (N)
####################################################################################################                

    
####################################################################################################
# Conclude specification of the MAIN procedure
####################################################################################################                
    
if __name__ == "__main__": main()

####################################################################################################
# End program
####################################################################################################      