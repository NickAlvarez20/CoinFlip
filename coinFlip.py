import random

coin = ["H","T"]

def flip(no):
    i=1
    h = 0
    t = 0
    result = ""
    while i <= no:
        if(random.choice(coin) == "H"):
            h+=1
            result+="H"
        else:
            t+=1
            result+="T"
        i+=1

    print "No of Heads : %s" %h
    print "No of Tails : %s" %t
    print "Result : %s" %result

def userInput():
    while True:
        x = raw_input("Enter number")

        try:
            number = int(x)
            if number > 0:
                return number
            else:
                print "Enter a valid number"
        except ValueError:
            print "Enter a number"

def main():
    no = userInput()
    flip(no)

if __name__ == "__main__":
    main()