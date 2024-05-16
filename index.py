import module

def App() :
    print("-----List Finder CLI App-----")
    name = input("Enter your name to find...\n")
    module.Finder(name)
App()