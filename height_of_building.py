def tallest_building_height(buildings):
    max_floor_count = 0
    # determind longest string
    longest_string = 0

    for floor in buildings:
        if len(floor) > longest_string:
            longest_string = len(floor)
    # TODO:
    # create list that keeps track of num of # 
    # signs that have occured repeatedly in one column
    floor_streak = [0] * longest_string
    # loop through each string in the input list
    for floor in buildings:
        # loop through each char in the current string
        for idx, char in enumerate(floor):
            # if the char is equal to "#"
            if char == "#":
                floor_streak[idx] += 1
                if floor_streak[idx] > max_floor_count:
                    max_floor_count = floor_streak[idx]
            else: 
                floor_streak[idx] = 0
    # return max_floor_count * 20 as a string formatted like... "heightm"
    return str(max_floor_count * 20) + "m"





# Questions:
# how do I count the height?
# how do we group the strings that make up one image?
# can buildings overlap?
# max input?
# how do we split the buildings?


'''
Example:
[
"   "
" # "
]
should return 20m
'''