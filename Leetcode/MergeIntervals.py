from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    if len(intervals) == 1:
        return intervals
    
    result = []
    sorted(intervals, key = lambda x: x[0])
    print(intervals)
    result.append(intervals[0])
    
    
    for i in range(1, len(intervals)):
        #print(result[-1][0],intervals[i][0],result[-1][1])
        if intervals[i][0] <= result[-1][1]:
            result[-1][1] = intervals[i][1]  
        else:
            result.append(intervals[i])
    
    return result


merge([[1,4],[0,4]])