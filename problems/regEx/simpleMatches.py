import re

# matching a url
# match s or no s = (s|)
reURL = re.compile(r"https*?://(www\.|)\w*?\.\w+")
urls = """http://www.google.com
          https://www.amazon.com
          http://io9.com
       """

for match in reURL.finditer(urls):
    print(match.group(0))
