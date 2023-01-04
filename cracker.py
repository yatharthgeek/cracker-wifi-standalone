import os
def cracker():
    wordlist= input("wordlist file path(drag&drop): ")
    cap=input("cap file path(drag&drop): ")
    while True:
        link=int(input("start attack ? 1(for yes) 2(for no) : "))
        if link==1:
            cmd="sudo aircrack-ng -w "+wordlist+" "+cap
            os.system(cmd)
            link=link+1

        elif link==2:
            break
        else:
            print("incorrect input")
            

cracker()