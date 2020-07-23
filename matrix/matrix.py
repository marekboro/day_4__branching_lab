class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string


    def row(self, index):
        list_of_strings = self.matrix_string.split(" ")
        list_of_numbers = []
        for i in list_of_strings:
            list_of_numbers.append(int(i))

        
        return list_of_numbers


    def column(self, index):
        pass
