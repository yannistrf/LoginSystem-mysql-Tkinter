# LoginSystem with GUI (Tkinter) and mysql database

### Description
Following the Client-Server architecture over a TCP connection,
a user can create an account and get authenticated by the server.
The client sends the information to the server and then the server
communicates with the database and gives the appropriate response.
Besides the login and register functionality there isn't anything
else ... yet.

### Run
To test the application you need to have a mysql service running somewhere,
the mysql-connector python module installed on the server (pip install mysql-connector-python)
and then run the Server/demo_db.py script. This script will create a new database
and a table in which some names-passwords will be stored. Just don't forget
to change your database login creadentials inside the script.

Now, we have a database running with some names and passwords already stored
inside of it. We can proceed by running the Server/server.py script to setup
the server to handle incoming requests.

And finally we can now run the Client/app.py to prompt the users to login/register.

Feel free to mess with the application, changing the port that the server is listening
or its ip address. Of course the client, server and mysql-service can be all three of
them different computers on different networks so go ahead and experiment. However, be
careful in case you expose the app to the internet as it's not considered safe.