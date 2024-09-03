Core Features

Create Note: Allow API consumers to create a new note with a title and body.

Fetch Note by ID: Enable fetching of a note using its primary key.

Query Notes by Title Substring: Implement functionality to query notes based on a substring present in the note's title, returning all matching notes.

Update Note: Provide the ability to update the title and body of an existing note identified by its primary key.

Delete Notes: Remove notes from the database.


Installatoion Process:

1.> Get clone of repositories by these : git clone https://github.com/mkumar2112/Simple-Note.git

2.> Makemigrations in terminal : python manage.py makemigrations

3.> Migrate in terminal : python manage.py migrate

4.> Runserver : python manage.py runserver

Now your api is ready to work


Urls for local:

1.> Get all Notes -> http://127.0.0.1:8000/notes

2.> Get Note by Id -> http://127.0.0.1:8000/notes/<id>

3.> Get Note by subscripting title -> http://127.0.0.1:8000/notes?title=<Searching_value>

4.> Post Note -> http://127.0.0.1:8000/notes

5.> Update Note by Put or patch Method -> http://127.0.0.1:8000/notes/<id>

6.> Delete Note -> http://127.0.0.1:8000/notes/<id>
