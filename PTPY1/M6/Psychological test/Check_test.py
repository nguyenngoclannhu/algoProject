from klimov import *

def check_type_answers(questions, type_answers, types):
    ''' checks that there are no contradictions in the data: each answer occurs exactly 1 time'''
    l_types = len(types)
    isCorrect = l_types > 0 and len(type_answers) == l_types # the number of job descriptions is equal to the number of columns in the test table 
    if isCorrect:
        # checking that each type contains an equal number of answers is necessary for Klimov's test, but not necessary for Holland...
        total = len(questions) * 2 # there are twice as many answers as questions
        ta_quantity = total / l_types
        for column in type_answers:
            isCorrect = isCorrect and ta_quantity == len(column) # in each column of the test table is the necessary number of elements
    else:
        print('Not tested: l_types > 0 and len(type_answers) == l_types ')
    if isCorrect:
        for i in range(1, len(questions) + 1):
            for j in range(1, 2):
                check_qty = 0
                for k in range(l_types):
                    if (i, j) in type_answers[k]:
                        check_qty += 1
                isCorrect = 1 == check_qty # this pair was found 1 time
                if not isCorrect:
                    print('(', i, ',', j, ') found ', check_qty, 'times')
                    break
            if not isCorrect:
                break
    else:
        print('Not tested: the answers are unevenly distributed in the columns')
    print(isCorrect)

check_type_answers(test_choices, prf_type_answers, prf_types)

