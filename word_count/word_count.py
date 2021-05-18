import collections

def word_count(string):
    string = string.strip()
    temp = string.split(' ')
    [temp.remove(item) for item in temp if item in ",."]
    count = collections.Counter(temp)
    return len(count.keys())

def main():
    temp = input("Enter a string: ")
    num = word_count(temp)
    print("Num of words: ", num)

if __name__ == "__main__":
    main()