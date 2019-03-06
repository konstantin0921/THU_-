def produce_power_set(input_list):
    '''
        given a set of integers(with no repeats),
        generates the collection of all possible subsets

        input_list: a list of integers
        returns a list of all subsets
    '''
    if len(input_list) == 0:
        return [[]]

    first = input_list[0:1]
    smaller = produce_power_set(input_list[1:])
    new = []
    for s in smaller:
        new.append(s+first)

    return new + smaller




def test():
    t = [1,2,3,4]
    t2 = [1,2]
    print(produce_power_set(t2))
    print(produce_power_set(t))

test()



