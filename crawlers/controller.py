from scrapy import cmdline


def initiate_crawl():

    # The execution method below is not recommended, for testing purposes only
    cmdline.execute("scrapy crawl akispetretzikis -o petretzikis_results.csv --set delimiter=\",\"".split())
    # cmdline.execute("scrapy crawl skarmoutsos -o skarmoutsos_results.csv --set delimiter=\",\"".split())
    # cmdline.execute("scrapy crawl suntagesme -o suntagesme_results.csv --set delimiter=\",\"".split())
    # cmdline.execute("scrapy crawl argirobarbarigou -o argirobarbarigou_results.csv --set delimiter=\",\"".split())


if __name__ == '__main__':
    initiate_crawl()
