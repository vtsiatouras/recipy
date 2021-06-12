<p align="center">
  <img src="https://github.com/VangelisTsiatouras/recipy/blob/main/readme_assets/logo.png"/>
</p>

<p align="center">
  <a href="https://www.python.org/" target="_blank">
      <img src="https://img.shields.io/badge/Python-3.7%20%7C%203.8%20%7C%203.9-blue.svg?logo=python&logoColor=white" alt="Python">
  </a>
  <a href="https://www.djangoproject.com/" target="_blank">
      <img src="https://img.shields.io/badge/Django-3.2-589636.svg?logo=django&logoColor=white" alt="Django">
  </a>
  <a href="https://reactjs.org/" target="_blank">
      <img src="https://img.shields.io/badge/React-17.0-brightgreen.svg?logo=react&logoColor=white" alt="React">
  </a>
  <a href="https://www.postgresql.org/" target="_blank">
      <img src="https://img.shields.io/badge/PostgreSQL-12.5-008bb9.svg?logo=postgresql&logoColor=white" alt="PostgreSQL">
  </a>
</p>


A crawler framework that scrapes data from famous Greek cuisine sites.

Current target sites:

- [akispetretzikis.com](https://akispetretzikis.com)
- [dimitrisskarmoutsos.gr](https://www.dimitrisskarmoutsos.gr)
- [suntages.me](https://www.syntages.me/syntages)
- [sintagesmamas.com](https://www.sintagesmamas.com)
- [argiro.gr](https://www.argiro.gr)

## Installation

### DjangoREST & Scrapy Installation from source


This section contains the installation instructions in order to set up a local development environment. The instructions
have been validated for Ubuntu 20.04.

First, install all required software with the following command:

```bash
sudo apt update
sudo apt install git python3 python3-pip python3-dev postgresql postgresql-contrib 
```

The project dependencies are managed with [pipenv](https://docs.pipenv.org/en/latest/). You can install it with:

```bash
pip install --user pipenv
```

`pipenv` should now be in your `PATH`. If not, logout and log in again. Then install all dependencies with:

```bash
pipenv install --dev
```

Then you can enable the python environment with:

```bash
pipenv shell
```

All commands from this point forward require the python environment to be enabled.

### Environment variables

The project uses environment variables in order to keep private data like user names and passwords out of source
control. You can either set them at system level, or by creating a file named `.env` at the root of the repository. 
The required environment variables for development are:

* `RECIPY_DATABASE_USER`: The database user
* `RECIPY_DATABASE_PASSWORD`: The database user password 
* `RECIPY_DATABASE_HOST`: The database host. _For local development use_
 `localhost`
* `RECIPY_DATABASE_NAME`: The database name.

### Local Development
In order to run the project on your workstation, you must create a database named according to the value of the
`RECIPY_DATABASE_NAME` environment variable, at the host that is specified by the
`RECIPY_DATABASE_HOST` environment variable. You can create the database by running:

```
sudo -u postgres psql
postgres=# CREATE DATABASE recipy_development_db;
```

After you create the database, you can populate it with the initial schema by running:

```bash
python manage.py migrate
```

Now you can run the web server, exposing the API:

```bash
python manage.py runserver
```

The API is available at http://127.0.0.1:8000/api/v1/

The documentation Swagger page of the API is available at http://127.0.0.1:8000/api/swagger

Also in order to populate the database with data you must run the crawlers. In order to do that, just simply run the following

```bash
cd crawlers
./deploy.sh
```

This will spawn a [Scrapyd](https://scrapyd.readthedocs.io/en/stable/) instance and will execute all the crawlers concurrently.

The Scrapyd management page is available at http://127.0.0.1:6800

If you want to run each crawler saperately run:
```bash
scrapy crawl <crawler-name>
```
## Installation using Docker (RECOMMENDED)
 
Initially, install [Docker Engine](https://docs.docker.com/engine/install/ubuntu/) (click the link to see
 instructions) & [Docker Compose](https://docs.docker.com/compose/install/) in order to build the project.
 
__Set up the `.env` at the root of the repository!__
* `RECIPY_DATABASE_USER`: The database user
* `RECIPY_DATABASE_PASSWORD`: The database user password 
* `RECIPY_DATABASE_HOST`: `db` _The host name __must__ be `db`_
* `RECIPY_DATABASE_NAME`: The database name.

Then just execute the following:

```bash
docker-compose up --build
```

Then you have the database, the API & the crawlers & the React frontend client up and running!

The database is exposed at jdbc:postgresql://localhost:5433/

The API, the Swagger page and the Scrapy page are available to the same addresses that referred above.
The React client is available at http://127.0.0.1:5000/

## Aditional Notes

The diagram below shows the structure and the main components of the ReciPy project.

<p align="center">
  <img src="https://github.com/VangelisTsiatouras/recipy/blob/main/readme_assets/RecipyDiagram.png"/>
</p>

The project is structured mainly by:
- The Crawlers component which gathers all the required data from the targeted websites
- A database in which those data are stored
- An API that is able to access the data and to provide them following the REST architecture
- And finally a web application, that is used as the User Interface, from which the users can search for recipes that exists in one of the targeted websites.

Below is an example of the management console of Scrapyd showing the status of each crawler process:

<p align="center">
  <img src="https://github.com/VangelisTsiatouras/recipy/blob/main/readme_assets/scrapyd.png"/>
</p>

The following endpoints were implemented in order to serve all the requests of the front-end application:

<p align="center">
  <img src="https://github.com/VangelisTsiatouras/recipy/blob/main/readme_assets/endpoint_getRecipes.png"/>
  <img src="https://github.com/VangelisTsiatouras/recipy/blob/main/readme_assets/endpoint_recipe_id.png"/>
  <img src="https://github.com/VangelisTsiatouras/recipy/blob/main/readme_assets/endpoint_sites.png"/>
</p>

Below is the Diagram of the respective schema that we used in order to store the various Recipes, Sites and Ingredients that were retrieved from the crawlers:

<p align="center">
  <img src="https://github.com/VangelisTsiatouras/recipy/blob/main/readme_assets/db_recipes.png"/>
</p>

Finally, the below screenshots display the frontend application.

Search page:

<p align="center">
  <img src="https://github.com/VangelisTsiatouras/recipy/blob/main/readme_assets/frontend.png"/>
</p>

Recipe detail page:

<p align="center">
  <img src="https://github.com/VangelisTsiatouras/recipy/blob/main/readme_assets/recipe_makaronada.png"/>
</p>
