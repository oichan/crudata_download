#coding:utf-8
import sys
import os
import re
import urllib
import urllib2
def match(html):
    pattern = r'<a href="(.*)">(.*)</a>'
    matchs = re.finditer(pattern, html)
    url = [match.groups()[1] for match in matchs]
    return url

def main(crudata):
    url = "https://crudata.uea.ac.uk/cru/data/hrg/cru_ts_3.23/crucy.1506241137.v3.23/countries/"+crudata
    response = urllib.urlopen(url)
    html = response.read()
    csv_list = match(html)
    for filename in csv_list:
        download_name=crudata+filename
        filename=url+filename
        urllib.urlretrieve(filename, download_name)
    print csv_list

if __name__ == "__main__":
    argvs = sys.argv
    if os.path.isdir(argvs[1])==False:
        os.makedirs(argvs[1])
    main(argvs[1]+"/")
