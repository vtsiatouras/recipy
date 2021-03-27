import os

from scrapy import cmdline

from recipes.settings import LOGS_DIRECTORY


def initiate_crawl():
    # Set up log directory
    try:
        os.mkdir(LOGS_DIRECTORY)
    except FileExistsError:
        pass
    # The execution method below is not recommended, for testing purposes only
    cmdline.execute("scrapy crawl akispetretzikis -o petretzikis_results.csv --set delimiter=\",\"".split())
    cmdline.execute("scrapy crawl skarmoutsos -o skarmoutsos_results.csv --set delimiter=\",\"".split())
    cmdline.execute("scrapy crawl suntagesme -o suntagesme_results.csv --set delimiter=\",\"".split())



if __name__ == '__main__':
    initiate_crawl()