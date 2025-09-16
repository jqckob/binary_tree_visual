# Binary Tree Visualizer
## Description
Binary Tree Visualizer is a program to demonstrate basic bainary tree operation, such as:
 *Adding nodes
 *Deleting Nodes
 *Searching for value

## Features:
 () Node Reoresentation: Each node is as a circle with its key value.
 () Dynamic Visualization: Lines connects parent nodes to their children, showing the tree structure clearly
 () Random Tree Generation: Youn can test the progrsm with randomly generated nodes to see different tree configuration.
## Implementation Details:
1. Node Class:
    Each node is stores its value and references to its left and right children.
2. Adding Nodes
    Nodes are added recursively acoording to binary search tree rules:
    *Values smaller then parent go to the left subtree
    *Values greater or equal go to the right subtree
3. Visuakization:
    *Nodes are drawn on a Tkinter Canvas
    *Lines connect each parent to its children
    *Horizontal spacing (dx) was initially adjusted to reduce overlapping at deeper levels
## Challenges:
*Overlapping nodes: At deeper levels, some nodes overlapped and brancges crossed, making the tree hard to read.
*Initial Fix: Adjusted the horizontal spacing  by dividing dx by a gradually increasing variable size per layer. This reduce overlap slightly but was not a perfect solution
## Future Improvments:
*Implementing node positioning to center parent node over their subtrees and eliminate overlapping.
*Improve visual aesthetics, includiing colors, line thickness etc.
*Add ineractive features such as inserting, dleting, or searching nodes via CUI buttons.
##Examples:
## NOTES
Testes with 12-20 nodes with random values in the range 0-100
Works best for small to medium-sized trees 

