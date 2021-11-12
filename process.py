log_file = open("um-server-01.txt")#this is a method that opens the file 'um-server-01.txt' saved as a variable 'log_file'


# def sales_reports(log_file):#def is a keyword for function. The name of the function is sales_reports, the parameter is the variable mentioned above
#     for line in log_file:# This is a for in loop that is going through the file log_file
#         line = line.rstrip()#.rstrip() with no parameters removes all the whitespace from the end of a string.
#         day = line[0:3]#saving the 1st and 4th index of each line to a variable called 'day'
#         if day == "Mon":# an IF statement looking for the string 'Tue' assuming it means Tuesday (Changed to Mon or Monday)
#             # print(line) # printing the line only if the IF statement above returns True


# sales_reports(log_file) #Calling the function with log_file as the parameter


def melon_log(log_file):
    for line in log_file:
        line = line.strip()
        line2 = line.split(' ')
        amount = int(line2[2])
        if amount > 10:
            print(line)
melon_log(log_file)
