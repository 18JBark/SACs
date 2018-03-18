#Made by Jack Bark
#This program allows the user to enter and read the meanings of different words based on the language (file) entered
#Date: 15/3/2018
#The file used is called lang.txt
#The file is formatted as 'users language' - 'Other language'

File = open("lang.txt", 'r+')

#Loads the file to be read, then returns it for other functions to use
def LoadLanguage():
    print('Load language')
    File = open('lang.txt', 'r+')
    return File

#Displays all files to be read
def DisplayAllWords(File):
    print('Display all')
    print(File.read())
    return

#Enters data specified by the user
#Uses the SaveFile function
def EnterNewData(File):
    print('Enter new term')
    Yourlang = input('Enter word in your language: ')
    Othlang = input('Enter word in other language: ')
    SaveFile(Yourlang, Othlang, File)
    return

#Deletes the line specified by the data entered by the user
def DeleteData(File):
    word = input('Enter a word: ')
    print("Are you sure you wish to delete this record? (Yes/No) ")
    userResponse = input(": ")
    if userResponse == "Yes":
            if word in File:
                for line in File:
                    if word in line:
                        line.strip(line)
    return

#Searches for the term specified by the user and then prints the line it is on
def SearchTerm(File):
    word = input('Enter a word: ')
    with open(File) as f:
        if word in f:
            for line in f:
                if word in line:
                    print('Word : Translation')
                    print(line)
    return

#Saves file by writing all data entered to it
def SaveFile(Yourlang, Othlang, File):
    File.write(Yourlang)
    File.write(' : ')
    File.write(Othlang)
    File.write('\n')
    return

#The main menu for the program, it loops if the data entered is not acceptable
while True:
    print('Please enter the number of the option you wish to see:')
    print('     1. Display all')
    print('     2. Enter new term')
    print('     3. Search and display meaning')
    print('     4. Delete term')
    print('     5. Exit')
    menuOption = input('Selection: ')
    if menuOption == '1':
        DisplayAllWords(File)

    elif menuOption == '2':
        EnterNewData(File)

    elif menuOption == '3':
        SearchTerm(File)

    elif menuOption == '4':
        DeleteData(File)

    elif menuOption == '5':
        exit(0)
    else:
        print('Menu option doesnt exist')
        menuOption = 0