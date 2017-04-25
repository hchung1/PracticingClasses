###############
###Fibonacci###
###############

#


class fib(object):
    def number(self):
        x=1;



        ######################
        #######Python 2#######
        ######################
        try:
            print "This is for the Fibonacci sequence." ##Will fail with Python3 (print needs parentheses)
            while (x == 1):
                try:
                    self.loop = int(raw_input("How many loops for Fibonacci? Must be greater than 2. >>")) #Fail upon any non-numbers
                    if (self.loop-2 >0):
                        x = 0; ##Break the loop upon success of if statement right above
                except:  #Upon crashing
                    print "The input needs to be an integer."
        ######################



        ######################
        #######Python 3#######
        ######################
        except: #Code made for Python2 crashes..... Your using Python3
            print ("This is for the Fibonacci sequence.") ##Regardless, Python 2 and 3 will work with this statement
            while (x == 1):
                try:
                    self.loop = int(input("How many loops for Fibonacci? Must be greater than 2. >>"))#Fail upon any non-numbers
                    if (self.loop-2 > 0):
                        x = 0; ##Break the loop upon success of if statement right above
                except:#Upon crashing
                    print ("The input needs to be an integer.")
        ######################


    def lists(self):
        start_list=[0,1];a=0;x=1;y=1;pos = 0;
        while (a == 0):
            for i in range(0, self.loop-1):
                temp = start_list[x] + start_list[y]
                x+=1;y+=1;pos+=1;
                start_list.append(temp)
                if (pos==self.loop-2):
                    print(start_list)
                    a=1




##################################################
#This calls a class...This is not part of a class#
##################################################
s=1;
while s == 1:  #have a loop break by CTRL + C or CTRL + Z
    hello = fib()
    hello.number()
    hello.lists()
##################################################



    ###############
    ###Continue?###
    ###############
    try:   #Runable with Python2
        go = raw_input("Continue? Type 'No' or 'N' to quit. >>")
        if ((go == "NO") or (go == "No") or (go == "no") or (go == "N") or (go == "n")):
            s=0; #Break tthe loop
    except: #Runable with Python3 and 2, but this will never run with Python to thanks to the one above
        go = input("Continue? Type 'No' or 'N' to quit. >>")
        if ((go == "NO") or (go == "No") or (go == "no") or (go == "N") or (go == "n")):
            s=0; #Break tthe loop
    ###############
