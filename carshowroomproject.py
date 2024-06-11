class Carshowroom:
    def showroom(self):
        print('1.toyota','2.mahindra','3.mercedes')
        com=input("enter which company do you want:" )
        if com in ['toyota','1']:
            self.com=com
        elif com in ['mahindra','2']:
            self.com=com
        elif com in ['mercedes','3']:
            self.com=com
        else:
            print("enter valid company name")
    def model_name(self):
        if self.com in ['toyota','1']:
            model=input("enter which model do you want 1.innova crysta 2.fortuner 3.landcrusier")
            if model in ['innova crysta','1']:
                self.model=model
            elif model in ['fortuner','2']:
                self.model=model
            elif model in ['landcrusier','3']:
                self.model=model
            else:
                print("enter valid model name")
        elif self.com in ['mahindra','2']:
            model=input("enter which model do you want 1.scorpio 2.thar 3.bolero:")
            if model in ['scorpio','1']:
                self.model=model
            elif model in ['thar','2']:
                self.model=model
            elif model in ['bolero','3']:
                self.model=model
            else:
                print("enter a valid model name:")
        elif self.com in ['mercedes','3']:
            model=input("enter which model do you want 1.benz G-class 2.maybach S-class 3.benz C-class")
            if model in ['benz G-class','1']:
                self.model=model
            elif model in ['maybach','2']:
                self.model=model
            elif model in ['benz C-class','3']:
                self.model=model
            else:
                print("enter valid model name")
        else:
            print("enter valid company name")
    def varient(self):
        print("select which type of varient you want 1.petrol 2.diesel")
        var=input("enter varient type of car:")
        if var in ['petrol','1']:
            self.var=var
        elif var in ['diesel','2']:
            self.var=var
        else:
            print("enter valid varient type")
    def display(self):
        if self.com in ['toyota','1'] and self.model in ['innova crysta','1']:
            if self.var in ['petrol','1']:
                ex_showroom_price=40000
                tax=(ex_showroom_price)*25/100
            elif self.var in ['diesel','2']:
                ex_showroom_price=45000
                tax=(ex_showroom_price)*25/100
        elif self.com in ['toyota','1'] and self.model in ['fortuner','2']:
            if self.var in ['petrol','1']:
                ex_showroom_price=50000
                tax=(ex_showroom_price)*25/100
            elif self.var in ['diesel','2']:
                ex_showroom_price=55000
                tax=(ex_showroom_price)*25/100
        elif self.com in ['toyota','1'] and self.model in ['land crusier','3']:
            if self.var in ['petrol','1']:
                ex_showroom_price=60000
                tax=(ex_showroom_price)*25/100
            elif self.var in ['diesel','2']:
                ex_showroom_price=65000
                tax=(ex_showroom_price)*25/100
        if self.com in ['mahindra','2'] and self.model in ['scorpio','1']:
            if self.var in ['petrol','1']:
                ex_showroom_price=70000
                tax=(ex_showroom_price)*25/100
            elif self.var in ['diesel','2']:
                ex_showroom_price=75000
                tax=(ex_showroom_price)*25/100
        if self.com in ['mahindra','2'] and self.model in ['thar','2']:
            if self.var in ['petrol','1']:
                ex_showroom_price=80000
                tax=(ex_showroom_price)*25/100
            elif self.var in ['diesel','2']:
                ex_showroom_price=85000
                tax=(ex_showroom_price)*25/100
        if self.com in ['mahindra','2'] and self.model in ['bolero','3']:
            if self.var in ['petrol','1']:
                ex_showroom_price=90000
                tax=(ex_showroom_price)*25/100
            elif self.var in ['diesel','2']:
                ex_showroom_price=95000
                tax=(ex_showroom_price)*25/100
        if self.com in ['mercedes','3'] and self.model in ['benz G-class','1']:
            if self.var in ['petrol','1']:
                ex_showroom_price=80500
                tax=(ex_showroom_price)*25/100
            elif self.var in ['diesel','2']:
                ex_showroom_price=85700
                tax=(ex_showroom_price)*25/100
        if self.com in ['mercedes','3'] and self.model in ['maybach S-class','2']:
            if self.var in ['petrol','1']:
                ex_showroom_price=40070
                tax=(ex_showroom_price)*25/100
            elif self.var in ['diesel','2']:
                ex_showroom_price=45035
                tax=(ex_showroom_price)*25/100
        if self.com in ['mercedes','3'] and self.model in ['benz C-class','3']:
            if self.var in ['petrol','1']:
                ex_showroom_price=60500
                tax=(ex_showroom_price)*25/100
            elif self.var in ['diesel','2']:
                ex_showroom_price=70050
                tax=(ex_showroom_price)*25/100
        on_road_price=ex_showroom_price+(3*tax)
        print("on road price of car is:",on_road_price)
        
obj=Carshowroom()
obj.showroom()
obj.model_name()
obj.varient()
obj.display()