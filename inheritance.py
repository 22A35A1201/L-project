class Faculty:
    def __init__(self,f_name,department,f_id):
        self.f_name=f_name
        self.department=department
        self.f_id=f_id
    def print_info(self):
        print("faculty infornation =",self.f_name,self.department,self.f_id)

obj = Faculty("lavanya","IT",1201)
obj.print_info()

class IT(Faculty):
    pass
obj=IT("subhani","IT",1202)
obj.print_info()