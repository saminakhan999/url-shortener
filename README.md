# URL Shortener

URL? Short! [Try it out](https://url-short-url.herokuapp.com)

## Installation & Usage

### Installation

* Clone or fork the repo
* Navigate to the `url-shortener` folder at the command line 
* Run `pipenv shell` to enter a virtual environment and `pipenv install` to install the dependencies
* Run `python manage.py makemigrations` and then `python manage.py migrate` to apply the model to the database

### Usage

* run `python manage.py runserver` to run the development version of the app


### Deployment

* View the client live on [Heroku](https://url-short-url.herokuapp.com) 

## Changelog

* To see our changelog, run `git log --pretty="- %s"` in the command line

## Wins & Challenges

### Wins

* Creating a functional URL shortener using Django
* Worked very well together as a team

### Challenges

* Having to run 3 separate commands on the Heroku Procfile to fix a deployment issue
* The shortened URL is actually longer than the full URL... 
