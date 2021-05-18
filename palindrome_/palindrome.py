# program: palindrome.py
# takes in a string return true if the input is a pal; false if not
def checkUserInput(string):
    # copy the string and compared it with the string reversed
    tempRev = list(string)
    tempRev.reverse()
    if list(string) == tempRev:
        return True
    else:
        return False

def main():
    tempStr = input("Enter a string:: ")
    if checkUserInput(tempStr):
        print("%s is a palindrome" % tempStr)
    else:
        print("%s is not a palindrome" % tempStr)

if __name__ == '__main__':
    main()