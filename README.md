# Summer-Project

My project for summer 2022

This project was built because I was bored during the summer and and I wanted to learn something new.

To run this project:

1. First, you're going to need to download python and then django. You can do this by following the guide at https://docs.djangoproject.com/en/4.0/topics/install/ 

2. Next, it is recommended that you set up a virtual environment, which can be done with this tutorial: https://docs.python.org/3/tutorial/venv.html

3. Finally, enter the command `python -m pip install -r requirements.txt` (if on Linux/Apple) or `py -m pip install  -r requirements.txt` (if on Windows).

## Running the Development Site

Running the development site is as easy as running any django site!

```bash
# Run migrations
python mysite/manage.py migrate

# Run the dev server
python mysite/manage.py runserver
```

### Environment Variables

| variable      | type | default     | description                                    |
| ------------- | ---- | ----------- | ---------------------------------------------- |
| SECRET_KEY    | str  | None        | The django secret key                          |
| DEBUG         | str  | 'true'      | Set "true" to debug, "false" to turn off debug |
| ALLOWED_HOSTS | list | 'localhost' | A comma-separated list of allowed hosts        |
| DATABASE_NAME | str  | 'db'        | The name of the sqlite database                |

## Endpoints

These are the pages you can access:

### /

This is the homepage

### /resume

This is my resume

### /polls

This is the polls app

### /admin

This is the default admin panel

## Contributing

Before committing, please format your code with `python black`:

```bash
pip install black
python -m black {source_file_or_directory}
```
