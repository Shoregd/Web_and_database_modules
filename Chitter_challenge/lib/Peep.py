class Peep:
    def __init__(self,id,message,post_date,post_time,user_id):
        self.id = id
        self.message = message
        self.post_date = post_date
        self.post_time = post_time
        self.user_id = user_id
    def __repr__(self):
        return f'Peep({self.id}, {self.message}, {self.post_date}, {self.post_time}, {self.user_id})'
    def __eq__(self,other):
        return self.__dict__ == other.__dict__