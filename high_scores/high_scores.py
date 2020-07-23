def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    resulting_list = []

    while len(resulting_list) < 3:
        resulting_list.append(personal_best(scores))
        scores.remove(personal_best(scores))
    return resulting_list


def sorted_descending_order(scores):
    resulting_list = scores
    resulting_list.sort(reverse = True)
    return resulting_list
    


#print(sorted_descending_order([1, 2, 3, 4, 5,]))

#the_numbers = [1,2,3,4,5,6,78,12]
#the_numbers.sort(reverse=True)
#print(the_numbers)
#print(#
