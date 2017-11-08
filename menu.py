while True:
    print("Welcome to the Future!\nPlease make your selection \
    ")
    print("Menu\n\t1) First\n\t2) Second")
    r = raw_input("Selection: ")
    if int(r) == 1:
        print("You win!")
        break
    elif int(r) == 2:
        print("You lose!")
        break
    else:
        print("Fail\n")
