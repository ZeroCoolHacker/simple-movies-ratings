# Movies Ratings (Omni Apps Task)

This is a Movies Ratings Listing

## Building

It is best to use the python `virtualenv` tool to build locally:

```bash
> virtualenv venv
> source venv/bin/activate
> git clone https://github.com/ZeroCoolHacker/simple-movies-ratings .
```
Then you navigate to the base directory of the project and install the requirements in your virtual environment

```bash
> cd simple-movies-ratings
> pip install -r requirements.txt
```
And finally you migrate the database, create a super user, run tests, and run the server
```bash
> python manage.py migrate
> python manage.py createsuperuser
> python manage.py test
> python manage.py runserver
```

## Building with Docker
First run `docker-compose` to build the container:

```bash
docker-compose build
```

Then, run the following command to create the superuser:

```bash
docker-compose run --rm web python manage.py migrate
docker-compose run --rm web python manage.py test
docker-compose run --rm web python manage.py createsuperuser
```

Finally, the Docker container can be launched with the following command:

```bash
docker-compose up
```

The server should be responding at localhost:8000


## Overview

- [x] Create Suitable Models
- [x] Filtered Results via javascript
- [x] Customized Admin Views
- [x] Used latest syntax
- [x] Written TestCases for all possible scenerios
- [x] Minimize the number of queries for admin list views

## Licensing
This Project is Licensed under [GLWTPL](LICENSE)



