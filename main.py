from opencv import *

def switch(argument):
    if argument == 1:
        videoCap()
    elif argument == 2:
        detectFinger()
    elif argument == 3:
        detectPos()
    elif argument == 4:
        detectSym()

def Menu():
    while True:
        print("--- Menu ---")
        print("1.Test Camera\n2.Detect Finger\n3.Detect Position of Finger\n4.Detect Symbol\n5.Exit")
        ans = int(input("Select: "))
        switch(ans)
        if ans == 5:
            print("Goodbye")
            break
        elif ans > 5:
            print("Please enter in 1 - 5")

def main():
    Menu()

if __name__ == '__main__':
    main()