from prettytable import PrettyTable

class familytree(object):
    def __init__(self):
        self.generations = {}
        self.generationstraced = 0
        self.createtree()
        self.printtree()
        self.generations
    def printtree(self):
        for i,index in enumerate(self.generations):
            for g in self.generations[index]:
                 g.printt()
    def createtree(self):
        self.generationstraced = int(input(('How many generations do you want to track?')))
        for i in range(self.generationstraced):
            self.generations[f'Generation_{i+1}'] = []
        seed = Person('Chris', 'Unknown', 1, 2006, 'Unknown', 3, 'Nigerian', "Abdullah", self.generationstraced, self.generations,1)
        self.generations['Generation_1'].append(seed)


class Person(object):
    def __init__(self, name, gender, generation, dob, dod, Siblings, Ethnicity, Relationship, traces, familytree,kid):  # initializes the Person Class
        self.id=self
        if generation==1:
            self.kid='No Kid'
        else:
            self.kid=kid
        self.name = name
        self.gennumber = 0
        self.gender = 'Male' if gender == 1 or gender == 'Male' else 'Female'
        self.generation = generation
        self.dob = dob
        self.dod = dod
        self.siblings = Siblings
        self.ethnicity = Ethnicity
        self.relationship = Relationship
        self.generations = {}
        self.traces = traces
        self.familytree = familytree
        self.createtree(self.traces)
        
        


    def createtree(self, trace):
        if self.traces == 1 and self.generation != 1:
            return
        elif trace > 0:
            pass
        else:
            return
        self.traces = trace
        self.dad = Person('Unknown', 1, self.generation + 1, 'Unknown', 'Unknown', 'Unknown', 'Unknown',
                          'Father of ' + self.relationship, self.traces - 1, self.familytree,self.id)
        self.mom = Person('Unknown', 2, self.generation + 1, 'Unknown', 'Unknown', 'Unknown', 'Unknown',
                          'Mother of ' + self.relationship, self.traces - 1, self.familytree,self.id)
        self.parents = {'mom': self.mom, 'dad': self.dad}
        self.addparents()

    def addparents(self):
        pass
        self.familytree[f'Generation_{self.mom.generation}'].append(self.mom)
        self.familytree[f'Generation_{self.dad.generation}'].append(self.dad)

    def printt(self):
        table = PrettyTable()
        table.field_names = ["Attribute", "Value"]
        table.add_row(["Name", self.name])
        table.add_row(["Gender", self.gender])
        table.add_row(["Generation", self.generation])
        table.add_row(["Date of Birth", self.dob])
        table.add_row(["Date of Death", self.dod])
        table.add_row(["Siblings", self.siblings])
        table.add_row(["Ethnicity", self.ethnicity])
        table.add_row(["Relationship", self.relationship])
        table.add_row(["Traces", self.traces])
        table.add_row(["Address", self.id])
        table.add_row(["Kid", self.kid])
        #table.Address(["Traces", id(self)])
        #table.add_row(["Family Tree", self.familytree])
        print(table)
