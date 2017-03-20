# temp convert through f and c

#keep asking the temp 
end = False
while not end:
    temp = input("please input the temp you want to convert (such as 35C/88F) \n" )
    if temp[-1].upper() == "C":
        F = 32 + eval(temp[0:-1])*1.8
        print("the F temp is {:.2f} F".format(F))
    elif temp[-1].upper() == "F":
        C = (eval(temp[0:-1]) - 32.0)/1.8
        print("the C temp is {:.2f} C".format(C))
    else:
        print("It is not a temp")
        end = True 


        