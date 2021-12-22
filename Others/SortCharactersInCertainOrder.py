"""
Sort a string of characters based on a given order.
Ex: string = "aabbcc"
    order = "bca"
    
Output: "bbccaa"
"""

from collections import Counter
def charSort(string, order):
    count = dict(Counter(string))
    
    res = ""
    for char in order:
        if char in count:
            res += char * count[char]
    return res
