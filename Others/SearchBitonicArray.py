'''
Given a Bitonic array, find if a given ‘key’ is present in it. An array is considered bitonic if it is monotonically increasing and then monotonically decreasing. Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].

Write a function to return the index of the ‘key’. If the ‘key’ is not present, return -1.

Example 1:

Input: [1, 3, 8, 4, 3], key=4
Output: 3
'''

def search_bitonic_array(arr, key):
  max_el = find_max(arr)

  if key > arr[max_el] or (key < arr[0] and key < arr[len(arr) - 1]):
    return -1

  index = binary_search(arr, 0, max_el, key, True)
  if index != -1:
    return index
  return binary_search(arr, max_el + 1, len(arr) - 1, key, False)



def find_max(arr):
  start, end = 0, len(arr) - 1

  while start < end:
    mid = (end + start) // 2
    if arr[mid] > arr[mid + 1]:
      end = mid
    else:
      start = mid + 1

  return start



def binary_search(arr, start, end, key, direction):
  while start <= end:
    mid = (start + end) // 2

    if arr[mid] == key:
      return mid
    elif key < arr[mid]:
      if direction:
        end = mid - 1
      else:
        start = mid + 1
    else:
      if direction:
        start = mid + 1
      else:
        end = mid - 1
        
  return -1



def main():
  print(search_bitonic_array([1, 3, 8, 4, 3], 4))
  print(search_bitonic_array([3, 8, 3, 1], 8))
  print(search_bitonic_array([1, 3, 8, 12], 12))
  print(search_bitonic_array([10, 9, 8], 10))


main()
