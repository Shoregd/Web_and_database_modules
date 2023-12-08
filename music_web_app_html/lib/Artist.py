class Artist:
    def __init__(self,id,name,genre):
        self.id = id
        self.name = name
        self.genre = genre
    def __repr__(self):
        
        return f'Artist({self.id}, {self.name}, {self.genre})'
    
    def __eq__(self, other):
        
        return self.__dict__ == other.__dict__
    
    def isvalid(self):
        if self.name == None or self.name == '':
            return False
        elif self.genre == None or self.genre == '':
            return False
        
        return True

    def generate_errors(self):
        error_list=[]

        if self.name == None or self.name =='':
            error_list.append("Name can't be blank")
        if self.genre == None or self.name == '':
            error_list.append("Genre can't be blank")
        
        if len(error_list)==0:
            return None
        
        return ',\n'.join(error_list)
