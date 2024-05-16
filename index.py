import module

def App() :
    print("-----List Finder CLI App-----")
    name = input("Enter your name to find...\n").strip().lower()
    module.Finder(name)
App()