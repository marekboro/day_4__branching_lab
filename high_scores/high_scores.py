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
    scores.sort(reverse=True)
    return scores
    
    #resulting_list = scores
    #resulting_list.sort(reverse = True)
    #return resulting_list
    
def top_three(scores):
    to_return = []
    sorted_descending_order(scores)
    for i in range(0,3):
        to_return.append(scores[i])
    return to_return

def top_three_less_than_three_scores(scores):
    scores.sort(reverse=True)
    less_than_3_scores =[]

    less_than_3_scores.append(scores[0])
    less_than_3_scores.append(scores[1])
    less_than_3_scores.append(0)

    return less_than_3_scores
    #a_copy


#print(sorted_descending_order([1, 2, 3, 4, 5,]))

#the_numbers = [1,2,3,4,5,6,78,12]
#the_numbers.sort(reverse=True)
#print(the_numbers)
#print(#
