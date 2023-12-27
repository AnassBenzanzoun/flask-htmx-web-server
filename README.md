## Flask-htmx Search App

This is a simple Flask application that allows users to search through a dataset loaded from a JSON file.
it's a simple project designed to learn how htmx works and to test how many loaded data
can htmx handle before breaking</br>

ps: tried with over 3k elements and still runs pretty smoothly.. it is also dynamic because the search bar is designed to query the backend each time the user type something

## Project Structure

app.py # Main application file generate_data.py # Script to generate the data requirements.txt # Project dependencies templates/ # HTML templates index.html # Home page search_result.html # Search results page venv/ # Python virtual environment

## Setup and Running

1. Clone the repository:

```sh
git clone https://github.com/AnassBenzanzoun/flask-htmx-web-server.git
```

2. Navigate into the cloned repository:

cd flask-htmx-web-server

3. Create a virtual enviroment and activate it:

python3 -m venv venv
source venv/bin/activate

4. install the dependencies:

pip install -r requirements.txt

5. run the app

python app.py

The application will be accessible at http://localhost:5000.
