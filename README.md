# Pinder
Swipe right on a new peering relationship


## Installation

1. Check out the code
2. cd into `<root>/pinder/`
3. Run `./manage.py migrate`
4. Load the sample data with:

        ./manage.py loaddata users/fixtures/initial_data.json
        ./manage.py loaddata peering_requests/fixtures/initial_data.json
5. Run the development server with `./manage.py runserver`
6. Open your browser and visit http://localhost:8000/api/
