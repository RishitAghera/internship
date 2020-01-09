class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string=matrix_string
        # print(self.matrix_string)
    def row(self, index):
        self.index=list(map(int,(self.matrix_string.split('\n')[index-1].split())))
        return self.index

    def column(self, index):
        lst=[]
        for i in self.matrix_string.split('\n'):
        # print(i)
            lst.append(int(i.split(' ')[index-1]))
        return lst
# print(Matrix("1 2\n3 4").row(1))