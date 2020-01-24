#!/usr/bin/python

import sys



def rock_paper_scissors(n):
    result = []
    rps = ['rock', 'paper', 'scissors']

    # recursive helper function for adding lists by n

    def rps_helper(arr, n):
        #base case
        if n == 0:
            return result.append(arr)
        #adds string to arr
        for i in rps:
            #add each play to the array
            rps_helper(arr + [i], n-1)
        
    rps_helper([], n)
    return result


print(rock_paper_scissors(5))



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')