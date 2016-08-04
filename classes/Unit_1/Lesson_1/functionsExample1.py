import collections

number_list = [1,1,2,2,2,2,3,3,4,4,5,5,5,5,5,5,6,7,8,8,8,8,9,9,9,9]
count_dict = collections.defaultdict(int)
for i in number_list:
    count_dict[i] += 1