# Author: Damian Archer
# Course: Machine Learning COS 575
# Date: 9-6-23
# Assignment: Lab 2
from filter_even import filter_even
from numpy_exercise import create_md_array, find_highest


nums_list_1 = [1,2,3,4,5,6,7,8,9,10]
nums_list_2 = [3,4,6,8,8,1,2]

if __name__ == '__main__':
    # filter list exercise
    print("filtering nums lists for even numbers:")
    print(filter_even(nums_list_1))
    print(filter_even(nums_list_2),'\n')

    # numpy exercise
    print("creating random 3x4 md_array:")
    md_array = create_md_array(3,4)
    print("finding highest number in md_array:")
    print(find_highest(md_array))

    # data visualization exercise
    import data_visualization


