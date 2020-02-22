import yagmail
import datetime


def send_email(to_mail_list, subject, contents):
    yag = yagmail.SMTP(user="kevinzhu@algologic.info", password="Qt2FL56LTsEApByt", host='smtp.exmail.qq.com')
    yag.send(to_mail_list, subject, contents)
    print('[{ts}] Sent out email to: {mail_list}'.format(ts=datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                                                         mail_list=to_mail_list))
