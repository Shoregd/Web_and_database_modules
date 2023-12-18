STRAIGHT UP

As a Maker
So that I can let people know what I am doing
I want to post a message (peep) to chitter

As a maker
So that I can see what others are saying
I want to see all peeps in reverse chronological order

As a Maker
So that I can better appreciate the context of a peep
I want to see the time at which it was made

As a Maker
So that I can post messages on Chitter as me
I want to sign up for Chitter

--- NOUNS ---
peeps,message,users,time,name,email

--- TABLE LAYOUT ---

RECORD | PROPERTIES

peeps  | message, time

users  | name,email

--- DATA TYPES ---

Peeps:
    * id: SERIAL
    * message:text
    * post_time: date
    * post_time: time 
    * user_id: foreign key

Users:
    * id: SERIAL
    * name: text
    * email: text

--- RELATIONSHIPS ---

User can have many peeps. Peeps can only have one user. Peeps belong to users. Peeps have the foreign key

SQL located in chitter_app.sql and chitter_test.sql

--- CLASS BREAKDOWN ---

Peep - Model Class
    * __init__: inputs id,message,post_date,time,user_id stored in self.attributes. Returns nothing. No side effects
    * __repr__: No inputs. Returns a string of the Peep object i.e 'Peep(1,'Test Message','2023-11-10','11:15:30',1)'. No side effects
    * __eq__: Allows for object testing

User - Model Class
    * __init__: inputs id,name,email stored in self.attributes. Returns nothing. No side effects.
    * __repr__: No inputs. Returns string of User object i.e 'User(1,'User name','User email')'. No side effects
    * __eq__: Allows for object testing

ChitterRepository - Repository Class
    * __init__: establishes database connection. Takes connection as input. Returns nothing. Establishes database connection.

    * list_users(): Takes no inputs. returns list of User objects.
    * add_user(): Inputs will be username, useremail.
    Will validate the user to ensure that the username or email is not already in use. Will return an error message if this is the case, otherwise will return a message stating the user has been added under the provided username. Side effects will be that a user is added to the users table in the database. 
    Will use _is_user_valid() to validate and generate the errors(if there are any) executes 'INSERT INTO users (name,email) VALUES (%s,%s)',[username,useremail]

    * _is_user_valid(): Will take username,useremail as input variables then check these against the currently stored usernames and user emails returning True if it doesn't match any or with an error message explaining the matches.
    i.e Valid user returns True
    Username aleady used returns 'Username has been taken. Please try another.'
    username and email used returns 'Username and Email has been taken. Please try another.'
    email used returns 'Email has been taken. Please try another.'

    * sign_in() Will let a user sign in if they provide a username and email that exists in the system. Takes username and useremail as inputs. Returns True and the username if the credentials pass or returns False and None if not.

    *sign_out() Takes no inputs. Returns False and None. No side effects.

    *add_peep(): Will create a new peep(message). Inputs message and userid. Returns nothing. Side effects will add a new item to the peeps table in the database. Function will get the date and time for the additional values.
    executes 'INSERT INTO peeps (message,post_date,post_time,user_id) VALUES(%s,%s,%s,%s)',[message,postdate,posttime,userid]

    *list_peeps(): Will return a list of peep objects but with the username instead of the user_id. No Inputs. No side effects
    executes '''SELECT 
                      peeps.id,
                      peeps.message,
                      peeps.post_date,
                      peeps.post_time,
                      users.name
                FROM peeps
                JOIN users ON users.id = peeps.user_id
                '''
    * get_user_id(): Takes username as input. Returns integer value of user ID. No side effects. Lets the user get the user ID of the supplied username.
    executes 'SELECT id from users WHERE users.name = %s',[username]
--- ROUTE LAYOUT ---

GET /
    Main page that contains the current peeps in the system and a button sign in.
    If already signed in. It will have a form to create a post at the top of the page.

GET /sign_in
    FORM page to fill out username and email to submit to sign in. Will also have a button to create a new user

POST /sign_in
    Submits the form details and checks if the user is correct. If they are it signs them in and returns to the main page. If incorrect it returns to the /sign_in page this time with error messages that the username or email is incorrect.

GET /sign_up
    FORM page to fill out NEW username and email to submit to create the account and sign in.

POST /sign_up
    Will return the user to the main page signed in if the credentials are valid otherwise it will return to the /sign_up page and inform the user which credentials need changing.

POST /peep
    Will take the data from the form if it is not blank and post the peep to the main page.