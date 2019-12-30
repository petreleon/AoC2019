
def param_mode(instruction, index_of_param):
    return instruction // (100 * 10 ** index_of_param) % 10


def position(list_, mode, relative_index, location):
    if mode == 0:
        return list_[location]
    if mode == 1:
        return location
    if mode == 2:
        return list_[location] + relative_index


def machine(input_, output_, list_, position_index=0):
    relative = 0
    compute_index = position_index

    while list_[compute_index] % 100 != 99:
        opcode = list_[compute_index] % 100
        before_change = list_[compute_index]

        (first_param, second_param, third_param) = tuple(map(lambda param_index:
                                                             position(list_,
                                                                      param_mode(list_[compute_index],
                                                                                 param_index),
                                                                      relative,
                                                                      compute_index + 1 + param_index),
                                                             range(3)))
        if opcode == 5:
            if list_[first_param]:
                compute_index = list_[second_param]
            else:
                compute_index += 3

        if opcode == 6:
            if not list_[first_param]:
                compute_index = list_[second_param]
            else:
                compute_index += 3

        if opcode == 1:
            list_[third_param] = list_[first_param] + list_[second_param]
            # i+=4
            if third_param != compute_index:
                compute_index += 4
        if opcode == 2:
            list_[third_param] = list_[first_param] * list_[second_param]
            # i+=4
            if third_param != compute_index:
                compute_index += 4
        if opcode == 3:
            list_[first_param] = int(input_())

            compute_index += 2
        if opcode == 4:
            output_(list_[first_param])
            compute_index += 2
            #return compute_index

        if opcode == 7:
            if list_[first_param] < list_[second_param]:
                list_[third_param] = 1
            else:
                list_[third_param] = 0
            # i+=4
            if third_param != compute_index:
                compute_index += 4

        if opcode == 8:
            if list_[first_param] == list_[second_param]:
                list_[third_param] = 1
            else:
                list_[third_param] = 0
            # i+=4
            if third_param != compute_index:
                compute_index += 4

        if opcode == 9:
            relative += list_[first_param]
            compute_index += 2

    return compute_index
