class Album:
    def __init__(self,id,title,release_year,artist_id):
        self.id = id
        self.title = title
        self.release_year = release_year
        self.artist_id = artist_id
    def __repr__(self):
        return f'Album({self.id}, {self.title}, {self.release_year}, {self.artist_id})'
    def __eq__(self,other):
        return self.__dict__ == other.__dict__
    def isvalid(self):
        if self.title == None or self.title == '':
            return False
        elif self.release_year == None or self.release_year =='':
            return False
        elif self.artist_id == None or self.artist_id == '':
            return False
        
        return True
    def generate_errors(self):
        error_list = []
        if self.title == None or self.title == '':
            error_list.append("Title can't be blank")
        if self.release_year == None or self.release_year =='':
            error_list.append("Release year can't be blank")
            
        
        if self.artist_id == None or self.artist_id == '':
            error_list.append("Artist id can't be blank")
        
        if len(error_list) == 0:
            return None
        else:
            return ', \n'.join(error_list)
            