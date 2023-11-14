import time
import ctypes
import winsound

def study_timer(minutes):
    print(f"Starting study session for {minutes} minutes...")
    while minutes:
        for seconds in range(59, -1, -1):
            time.sleep(1)
            print(f'\r{minutes:02}:{seconds:02}', end='')
        minutes -= 1

    # Displaying an alert at the end of the timer
    ctypes.windll.user32.MessageBoxW(0, "Time's up! Take a break.", "Study Timer Alert", 0x40 | 0x1)
    # Playing an alarm sound
    winsound.Beep(2500, 1000)  # Frequency 2500Hz, Duration 1 second

def main():
    try:
        duration = int(input("Enter the duration for your study session (in minutes): "))
        study_timer(duration)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()


