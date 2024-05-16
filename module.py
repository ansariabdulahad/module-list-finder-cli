index = 0
count = 0

def Finder(name) :
    global index
    global count
    list = ["ahad", "hamza", "noor", "samad", "ahAd", "ahad"]
    data = list[index].lower()

    if data == name :
        count = count + 1

    index = index + 1
    length = len(list)
    if index < length : 
        Finder(name)
    else :
        if count != 0 :
            print(f"{name} matched for {count} times")
        else :
            print("Index out of range")