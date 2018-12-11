import time                                       #importing time module
qn=0
q=''
a=''
score=0
ans='y'
print("Enter 1 for admin page and 2 for user page")
ch=int(input("Enter your choice="))
high_score=[]                                       #for storing high score
if ch==1:
    questions=open("questions.txt",'a')            #opening the file in append mode
    questions.write("7.What is the capital of Kerela?")
    questions.write('\n')
    answers=open("answers.txt",'a')
    answers.write('\n')
    answers.write("A.Mumbai B.New Delhi C.Thiruvananthapuram D.Satara")
    answers.write('\n')
    questions.close()                                   #closing the file
    answers.close()
if ch==2:
    while ans=='y':
        name=input("Enter your name=")
        questions=open("questions.txt",'r')          #opening the file in read mode
        qt=questions.readlines()
        answers=open("answers.txt",'r')
        an=answers.readlines()
        while qn<len(qt):
            q=qt[qn]
            a=an[qn]
            print(q,a)
            choice=input("Enter your choice=")      #choosing an option
            if choice=='C':
                score+=1                            #increementing the score
                high_score.append(score)
            qn+=1                                   #increementing the counter
        print(max(high_score))                      #printing high score
        f=open("file.txt",'a')
        f.write(name + str(score))                  #storing the name of the user and its score
        f.write('\n')
        f.close()
        questions.close()                           #closing the file
        answers.close()
        qn=0
        score=0
        ans=input("Do you want to continue?[y/n]")
        if ans=='n':
            break                                   #coming out of the loop                          
    f=open("file.txt",'r')
    print(f.read())                                 #reading the file
