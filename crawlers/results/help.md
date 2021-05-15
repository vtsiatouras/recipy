# Workspace setup
## Create venv

`python -m venv venv`

## Enable it 

`source venv/bin/activate`

## Activate it on VSCode

CTRL + SHIFT + P >> select intepreter

# Scrapy setup

## Create project

`scrapy startproject postscrapy`

## Creatins spiders

Target dir: `spiders/`

## Running the crawler

`scrapy crawl posts -o posts.json`

## Scraping from shell

`scrapy shell <url>`


# Scraping petretzikis

## Getting the food title

`response.css("h1::text").get()`

or 

`response.css("title::text").get().split("|")[0]`

## Ingidients

Dump way

`items = list(filter(lambda x: x!='\n', response.css("li::text").getall()))[10:]`

XPath way: by coping the proper paths

`response.xpath('//*[@id="recipe"]/div[4]/div/div[1]/div[5]/div/div/div/ul/li[2]//text()').extract() `

Select items with id (geting the id)


geting the paths. 

`response.xpath("//div[@id='recipes_cont']/div[1]/div[1]/div[1]/a/@href").get() `
`response.xpath("//div[@id='recipes_cont']/div[1]/div[2]/div[1]/a/@href").get() `
`response.xpath("//div[@id='recipes_cont']/div[1]/div[3]/div[1]/a/@href").get() `

`response.xpath("//div[@id='recipes_cont']/div[2]/div[1]/div[1]/a/@href").get() `
`response.xpath("//div[@id='recipes_cont']/div[2]/div[2]/div[1]/a/@href").get() `
`response.xpath("//div[@id='recipes_cont']/div[2]/div[3]/div[1]/a/@href").get() `

`response.xpath("//div[@id='recipes_cont']/div[3]/div[1]/div[1]/a/@href").get() `
`response.xpath("//div[@id='recipes_cont']/div[3]/div[2]/div[1]/a/@href").get() `
`response.xpath("//div[@id='recipes_cont']/div[3]/div[3]/div[1]/a/@href").get() `

## recipies list

`response.xpath("//*[@class='v_box recipe-card']/a[1]/@href").getall()`
`response.xpath("//*[@class='v_box recipe-card']/*/img/@src").getall()`


 # Skarmoutsos

`response.xpath('//*[@id="recipesCategArea"]/div[*]/a[1]/span/text()').getall()`


# DB
Connect to postGress

`psql -h localhost -p 5432 -U recipy_user recipy_db`

`\d`