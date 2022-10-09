from klimov import *

class TestQuestion():
    ''' one test element: two alternatives (strings) to choose from.'''
    def __init__(self, a1, a2):
        self.a1 = a1 # alternative 1
        self.a2 = a2 # alternative 2

def list_from_choices():
    ''' in the imported module with the listed data there should be a test_choices list
    transfer this list into a list of objects of the TestQuestion type'''
    list_test = []
    for choice in test_choices:
        question = TestQuestion(choice[1], choice[2])
        list_test.append(question)
    return list_test

class ProfessionType():
    ''' each "job type" has a text description, and it also remembers which answers correspond to this type '''
    def __init__(self, description):
        self.description = description
        self.data = []
    def add_answer(self, list_index, answer_num):
        ''' it assigns a specific answer to a specific question to a given job type.
        The questions are identified by their number in the source! '''
        self.data.append((list_index - 1, answer_num)) # are numbered starting from 1 - this way it is easier to transfer them from sources
        # but in our data structure, the numbering starts from 0. This is taken into account here and we subtract 1 from the resulting index.

    def check(self, list_answers):
        ''' checks against the current list to see which answers are included in this job type.
        list_questions is a list format (id, answer_number, answer_text).
        check makes a list of these answers (which can be shown on the screen)
        Returns the number of responses corresponding to this job type.'''
        self.answers = []
        for answer in list_answers:
            id = answer[0]
            answer_number = answer[1]
            if (id, answer_number) in self.data: 
                # on such a length of data and this search should work sufficiently fast
                self.answers.append(answer[2])
        return len(self.answers)

    def normal(self, list_answers):
        ''' Normalizes the result: returns the percentage of the maximum scored.
            Normalization is needed if the answers are unevenly distributed by type (as in the Holland test).
            This method will call check first! Therefore, use either check or normal in the application, but not both.'''
        qty = self.check(list_answers)
        total =  len(self.data)
        if total > 0:
            return 100 * qty / total
        else:
            return 0

def list_from_types():
    ''' the imported module with the listed data must contain prf_types, prf_type_answers lists
    using this information, a list with ProfessionType class instances is created '''
    list_proftypes = []
    for i, type_descr in enumerate(prf_types):
        currtype = ProfessionType(type_descr) # the instance stores the description of the job type
        for answer in prf_type_answers[i]:
            # add which answers correspond to this type
            currtype.add_answer(answer[0], answer[1])
        list_proftypes.append(currtype) # all the instances are in one list
    return list_proftypes

