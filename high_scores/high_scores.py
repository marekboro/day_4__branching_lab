def latest(scores):
    return scores[-1]



def personal_best(scores):
    return max(scores)



def personal_top_three(scores):
    resulting_list = []
    

    while len(resulting_list) <3:
        resulting_list.append(personal_best(scores))
        scores.remove(personal_best(scores))
    return resulting_list

