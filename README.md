# recipy
A crawler framework that scrapes data from famous Greek cuisine sites.

Current target sites:

- [akispetretzikis.com](https://akispetretzikis.com)
- [dimitrisskarmoutsos.gr](https://www.dimitrisskarmoutsos.gr)
- [suntages.me](https://www.syntages.me/syntages)
- [sintagesmamas.com](https://www.sintagesmamas.com)

## Installation

Python 3.7+

```bash
sudo apt update
sudo apt install git python3 python3-pip python3-dev
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

## Execution

```bash
cd crawlers
python controller.py
```
For running each crawler saperately run:

`scrapy crawl <crawler-name> -o <output-file>.csv`