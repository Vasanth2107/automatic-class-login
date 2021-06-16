import schedule
import time
import webbrowser
import datetime

def open_link(link):
    webbrowser.open(link)


def class1():
    print("running")
    open_link('link')
def class2():
    print("running")
    open_link('link')
def class3():
    print("running")
    open_link('link')
def class4():
    print("running")
    open_link('link')
def class5():
    print("running")
    open_link('link')
def class6():
    print("running")
    open_link('link')


schedule.every().monday.at("10:00").do(class1)
schedule.every().monday.at("11:00").do(class2)
schedule.every().monday.at("12:00").do(class3)
schedule.every().monday.at("13:00").do(class4)
schedule.every().monday.at("14:00").do(class5)
schedule.every().tuesday.at("09:00").do(class1)
schedule.every().tuesday.at("11:00").do(class2)
schedule.every().tuesday.at("12:00").do(class3)
schedule.every().tuesday.at("14:00").do(class4)
schedule.every().wednesday.at("10:00").do(class5)
schedule.every().wednesday.at("11:00").do(class4)
schedule.every().wednesday.at("12:00").do(class3)
schedule.every().wednesday.at("13:00").do(class1)
schedule.every().thursday.at("10:00").do(class3)
schedule.every().thursday.at("11:00").do(class1)
schedule.every().thursday.at("12:00").do(class5)
schedule.every().thursday.at("13:00").do(class2)
schedule.every().thursday.at("14:00").do(class6)
schedule.every().friday.at("10:00").do(class4)
schedule.every().friday.at("11:00").do(class2)
schedule.every().friday.at("12:00").do(class1)
schedule.every().friday.at("13:00").do(class6)
schedule.every().saturday.at("10:00").do(class2)
schedule.every().saturday.at("11:00").do(class3)
schedule.every().saturday.at("12:00").do(class4)
schedule.every().saturday.at("14:00").do(class6)


while 1:
    schedule.run_pending()
    time.sleep(1)

