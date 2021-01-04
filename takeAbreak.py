import datetime
import webbrowser
import time



def breaktime(user):
    session = 8 #
    now = datetime.datetime.now()
    StartTime = now.strftime("%H:%M:%S")
    #print(f"The current time is {StartTime}, your next break will be at {}")
    seconds = int(user * 60)
    print(seconds)
    while session != 0:
        time.sleep(seconds)
        print("Break time!")
        webbrowser.get("firefox").open("https://www.bing.com")
        session = session - 1


user = int(input("How long will your work session be in minutes? "))

breaktime(user)

print("Your study session is now offically over!")
