#coding:utf-8
import re
import urllib
import urllib2
def match(html):
    pattern = r'<a href="(.*)">(.*)</a>'
    matchs = re.finditer(pattern, html)
    url = [match.groups()[1] for match in matchs]
    return url

if __name__ == "__main__":
    url = "https://crudata.uea.ac.uk/cru/data/hrg/cru_ts_3.23/crucy.1506241137.v3.23/countries/pre/"
    response = urllib.urlopen(url)
    html = response.read()
    csv_list = match(html)
    for filename in csv_list:
        download_name="pre/"+filename
        filename=url+filename
        urllib.urlretrieve(filename, download_name)
    print csv_list
