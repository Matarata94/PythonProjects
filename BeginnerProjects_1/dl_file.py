from urllib import request

goog_finance_url = 'http://chart.finance.yahoo.com/table.csv?s=GOOG&a=9&b=11&c=2016&d=10&e=11&f=2016&g=d&ignore=.csv'
def dl_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'goog_finance_url.csv'
    fx = open(dest_url,"w")
    for linee in lines:
        fx.write(linee + "\n")

    fx.close()

dl_stock_data(goog_finance_url)