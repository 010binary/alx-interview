#!/usr/bin/python3
"""
trying to sovle the Lockboz
"""


def canUnlockAll(boxes):
    """
    first I get the lenght of the list in the box
    then I create a variable to store boxes that are open
    and then another for locked boxes
    """
    length_boxes = len(boxes)
    open_boxes = set([0])
    closed_boxes = set(boxes[0]).difference(set([0]))
    while len(closed_boxes) > 0:
        boxIdx = closed_boxes.pop()
        if not boxIdx or boxIdx >= length_boxes or boxIdx < 0:
            continue
        if boxIdx not in open_boxes:
            closed_boxes = closed_boxes.union(boxes[boxIdx])
            open_boxes.add(boxIdx)
    return length_boxes == len(open_boxes)
