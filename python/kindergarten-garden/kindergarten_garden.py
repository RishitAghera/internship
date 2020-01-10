stud = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]

plants = {"R": "Radishes", "C" : "Clover", "G" : "Grass", "V" : "Violets"}
class Garden:
    def __init__(self, diagram, students=stud):
        self.students=sorted(students)
        self.diagram=diagram.split()
        
    def plants(self,students):
        index=self.students.index(students)
        return [plants[self.diagram[i][j]] for i in range(2) for j in range(2*index,2*(index+1))]
        
        

    
