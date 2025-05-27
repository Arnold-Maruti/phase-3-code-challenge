from lib.models import article,author,magazine

# print(article.Article.find_by_id(2))
hr=author.Author(4,"jersey")
hr.save()

biggie=article.Article(2,"biggie",4,3)
biggie.save()

timesnewyork=magazine.Magazine(3,"timesnewyork","action")
timesnewyork.save()

print(hr.articles())