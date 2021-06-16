import schedule
import time
import webbrowser
import datetime

def open_link(link):
    webbrowser.open(link)


def dsd():
    print("running")
    open_link('https://us04web.zoom.us/j/79599887604?pwd=OUNhSGJ6dmU1dlJaejdrelhzREduQT09')
def adc():
    print("running")
    open_link('https://us04web.zoom.us/j/74871911316?pwd=T3AzYmVjSW5FTjE1R0NuclJlWXBKZz09')
def cs():
    print("running")
    open_link('https://us04web.zoom.us/j/6657325252?pwd=M1ozSG4vTjgwNStoRVZlKzZyc0lqUT09')
def emt():
    print("running")
    open_link('https://us04web.zoom.us/j/4051632980?pwd=MmZrWGw2UnMyQ3VHUWtBcFV0Sk1Xdz09')
def ac():
    print("running")
    open_link('https://us04web.zoom.us/j/5546372849?pwd=Qk1IOWd3bzltSlkrMjU1RElGUkVSQT09')
def ccna():
    print("running")
    open_link('https://us04web.zoom.us/j/75841646905?pwd=L1pRVUFPTnVVcTBzZVhlbW9wcG9oZz09')


schedule.every().monday.at("10:05").do(dsd)
schedule.every().monday.at("10:58").do(cs)
schedule.every().monday.at("11:58").do(emt)
schedule.every().monday.at("13:58").do(adc)
schedule.every().monday.at("14:58").do(ac)
schedule.every().tuesday.at("09:58").do(ac)
schedule.every().tuesday.at("11:05").do(adc)
schedule.every().tuesday.at("11:58").do(dsd)
schedule.every().tuesday.at("14:03").do(emt)
schedule.every().wednesday.at("10:00").do(cs)
schedule.every().wednesday.at("11:00").do(adc)
schedule.every().wednesday.at("11:58").do(ac)
schedule.every().wednesday.at("13:58").do(dsd)
schedule.every().thursday.at("10:00").do(adc)
schedule.every().thursday.at("11:00").do(dsd)
schedule.every().thursday.at("12:00").do(cs)
schedule.every().thursday.at("13:58").do(emt)
schedule.every().thursday.at("14:58").do(ac)
schedule.every().friday.at("10:12").do(ac)
schedule.every().friday.at("10:58").do(emt)
schedule.every().friday.at("12:02").do(adc)
schedule.every().friday.at("13:58").do(cs)
schedule.every().saturday.at("10:06").do(dsd)
schedule.every().saturday.at("10:58").do(emt)
schedule.every().saturday.at("11:58").do(cs)
schedule.every().saturday.at("14:45").do(ccna)


while 1:
    schedule.run_pending()
    time.sleep(1)

