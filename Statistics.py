import csv
import urllib.request as urllib
import codecs
import pprint


def make_dict_from_csv():
    url = 'http://data.kk.dk/dataset/76ecf368-bf2d-46a2-bcf8-adaf37662528/resource/9286af17-f74e-46c9-a428-9fb707542189/download/befkbhalderstatkode.csv'
    ftpstream = urllib.urlopen(url)
    csvfile = csv.reader(codecs.iterdecode(ftpstream, 'utf-8'))
    next(csvfile)

    res = {}

    for line in csvfile:
        res.setdefault(int(line[0]), {}).setdefault(int(line[1]), {}).setdefault(int(line[2]), {})[int(line[3])] = int(line[4])
    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(res)
    return res



