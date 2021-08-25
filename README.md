# hackathon-app-back-end

Install Python, put pip into directory (so it was usable in command line)
- make sure to add it to the PATH if on windows
- should see a version when entering a command of `python --version`

## Running the Django Server

1. Open the folder in a terminal (e.g. CMD)
1. Run `python -m venv myenv` to create a virtual environment
1. Activate the virtual environment
    - `.\myenv\Scripts\activate` on windows
    - Something different on Mac
1. Install dependencies with `pip install -r requirements.txt`
1. Go into the project folder with `cd backend`
1. Run the server with `python manage.py runserver`