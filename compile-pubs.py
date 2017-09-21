import csv
import itertools as i
from pprint import pprint
import json
from io import StringIO

def parse():
    with open("./citations.csv", 'rb') as f:
        txt = f.read()
        buf = StringIO(txt.decode('utf-8', errors='ignore'))

        reader = csv.reader(buf)
        next(reader)
        for line in reader:
            try:
                authors, typ, title, publication, vol, num, pages, year, publisher = line
            except:
                continue

            if vol and num:
                publication = "%s %s (%s)" % (publication, vol, num)
            if pages:
                publication = "%s pp. %s" % (publication, pages)
            if year:
                publication = "%s, %s" % (publication, year)
            if publisher:
                publication = "%s, %s" % (publication, publisher)

            yield dict(authors=authors,
                    title=title,
                    publication=publication,
                    publisher=publisher,
                    year=year,
                    type=typ)
    return

pubs = sorted(list(parse()), key=lambda x: (x["type"], x["year"]), reverse=1)
data = dict()

for typ, papers in i.groupby(pubs, key=lambda x: x["type"]):
    data[typ] = []
    for year,papers in i.groupby(papers, key=lambda x: x["year"]):
        if not year:
            year = "Others"
        data[typ].append(dict(year=year, papers=list(papers)))

print(json.dumps(data, indent=1))
