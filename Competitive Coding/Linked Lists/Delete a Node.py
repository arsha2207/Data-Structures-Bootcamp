#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'deleteNode' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER position
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def deleteNode(llist, position):
    # Write your code here
    if position == 0:
        return llist.next

    count = 0
    ptr = llist

    while count < position - 1 and ptr is not None and ptr.next is not None:
        ptr = ptr.next
        count += 1

    if ptr is not None and ptr.next is not None:
        ptr.next = ptr.next.next

    return llist


llist_count = int(input())

llist = SinglyLinkedList()

for _ in range(llist_count):
    llist_item = int(input())
    llist.insert_node(llist_item)

position = int(input())

llist1 = deleteNode(llist.head, position)

print_singly_linked_list(llist1, ' ')

