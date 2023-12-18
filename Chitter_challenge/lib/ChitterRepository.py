from lib.User import User
from lib.Peep import Peep
import datetime
class ChitterRepository:
    def __init__(self,connection):
        self._connection = connection
    
    def add_user(self,username,useremail):
        validuser,errors = self._is_valid(username,useremail)
        if validuser:
            self._connection.execute('INSERT INTO users (name,email) VALUES (%s,%s)',[username,useremail])
            return f'User {username} has been added.'
        return errors
    def list_users(self):
        rows = self._connection.execute('SELECT * from users')
        user_list = []
        for row in rows:
            data = User(row['id'],row['name'],row['email'])
            user_list.append(data)

        return user_list
    
    def _is_valid(self,username,useremail):
        rows = self._connection.execute('SELECT * from users WHERE users.name = %s OR users.email = %s',[username,useremail])
        error_message = ['has been taken. Please try another.']
        if len(rows) == 0:
            return True,None
        
        if rows[0]['name'] == username:
            error_message.insert(0,'Username')
        if rows[0]['email'] == useremail:
            if error_message[0] == 'Username':
                error_message.insert(1,'and Email')
            else:
                error_message.insert(0,'Email')

        return False, ' '.join(error_message)

    def sign_in(self,username,useremail):
        userdoesntexists,errors = self._is_valid(username,useremail)

        if not userdoesntexists and 'Username' in errors:
            return True, username
        
        return False, None
    
    def sign_out(self):
        return False, None
    
    def add_peep(self,message,userid):
        postdate = datetime.date.today()
        posttime = datetime.datetime.now().strftime("%H:%M:%S")
        self._connection.execute('''INSERT INTO peeps (message,post_date,post_time,user_id)
                                 VALUES (%s,%s,%s,%s)
                                 ''',[message,postdate,posttime,userid]
                                 )
    def list_peeps(self):
        rows = self._connection.execute('''SELECT 
                      peeps.id,
                      peeps.message,
                      peeps.post_date,
                      peeps.post_time,
                      users.name
                FROM peeps
                JOIN users ON users.id = peeps.user_id
                ''')
        
        peep_list = []
        for row in rows:
            data = Peep(row['id'],row['message'],row['post_date'],row['post_time'],row['name'])
            peep_list.append(data)
        
        
        return sorted(peep_list, key= lambda x: x.post_time, reverse=True)
    
    def get_user_id(self,username):
        rows = self._connection.execute('SELECT id FROM users WHERE users.name = %s',[username])
        

        return rows[0]['id']