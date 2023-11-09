"""
Program Name: Multiprocessing_Ehlert.py
Author: Tony Ehlert
Date: 11/9/2023

Program Description: This program creates a list of 1,000,000 random integers between 0-10(inclusive) and utilizes
multiprocessing to determine if each number in the list is greater than 5 and returns the result of the process and
also counts how many of the integers were greater than five.
"""
from multiprocessing import Pool
import random
import time
import multiprocessing as mp


def greater_than_5(int):
    """
    This function accepts an integer and determines if it is greater than five.  It returns one if it is greater than
    five and zero if it is less than or equal to five
    :param int: int to be checked
    :return: 1 if greater than 5, else zero
    """
    if int > 5:
        return 1
    else:
        return 0


if __name__ == '__main__':
    #### Create a list of 1,000,000 random integers between 0-10 with 0 and 10 included.
    rand_ints_list = [random.randrange(0, 11, 1) for _ in range(1000000)]

    #### pass this list into a multiprocessing process that determines whether each item in the list is greater than 5.
    # create variable to store number of cpus on device (mp.cpu_count will pull number of cpus on current device)
    num_processors = mp.cpu_count()
    # print(num_processors)

    # create a Pool of processes
    p = Pool(processes=num_processors)

    start = time.time()
    #### Return an appropriate output from the process that indicates whether the item is greater than 5.
    # use map() function to apply greater_than_5 function to rand_ints_list
    result = p.map(greater_than_5, rand_ints_list)
    # print(type(result))
    # print(len(result))

    # result = []
    # for i in range(len(rand_ints_list)):
    #     print(rand_ints_list[i])
    #     result.append(greater_than_5(rand_ints_list[i]))

    end = time.time()
    #### In your main, count how many of the items were greater than 5.  You should get something like 450,000
    print('\n# of times an integer was greater than five: ' + str(sum(result)))
    print('\nProgram/Processing time = ' + str(end - start) + ' seconds')
