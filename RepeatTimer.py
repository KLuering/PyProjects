import time

def countdown(minutes):
    while True:
        for i in range(minutes, 0, -1):
            print(f"{i} minutes left")
            time.sleep(60)  # sleep for 60 seconds (1 minute)
        print("Time's up!")
        
if __name__ == "__main__":
    countdown(5)  # replace 5 with the number of minutes you want to count down from
