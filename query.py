from movies import Movies

movies = Movies('./movies.txt')


def list_all ():



def list_name():



def list_cast():



input = ' '

    while input.lower() != 'q':
        print("q: quit")
        print("sn: search by name")
        print("sc: search by cast")
        print("list: print all the movie names")
        input.lower() = scan("")

        if(input == "list"):
            list_all()

        if (input == "sn"):
            list_name()

        if (input == "sc"):
            list_cast()











        




