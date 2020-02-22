import time
import datetime
from jqdatasdk import *
from utils.email import send_email


def get_stocks(filename):
    df_stocks = pd.read_csv(filename, encoding='gbk')
    return df_stocks


def get_daily_trading_data(stock_list, end_date, period='15m'):
    get_price(stock_list, count=15, end_date=datetime.datetime.now())
    pass


def calculating(df):
    target_stocks = []
    return target_stocks


def notify(to_mails=[]):
    pass


def main():
    mail_list = ['yanhuaxie@algologic.info', 'kevinzhu@algologic.info']
    stock_list = ['000905.XSHG']
    auth('18516227429', 'Mcgrady1')
    while True:
        spare = get_query_count()['spare']
        if spare > 10000:
            df = get_daily_trading_data(stock_list)
            result = calculating(df)
            if len(result) > 0:
                send_email(mail_list, subject='Qualified stocks @[{ts}]'.format(ts=datetime.datetime.now()),
                           contents=['Qualified stocks found are as follows:\n'] + result)
        else:
            send_email(mail_list, 'Balance not enough', ['Current balance = {}'.format(spare)])
            print('Exit due to lacking of jqData spare')
            return
