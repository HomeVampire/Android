# Please find the following string methods and try to explain their working principle
# along with examples.
# (a) capitalize
# (b) count
# (c) islower
# (d) join
def main():
    s=input("Enter a string input: ")
    print("===============================================================")
    print("1. To make 'first character of a string capital' \nwe use string_name.capitalize() function")
    print("The given data was:",s)
    print("After using string_name.capitalize() function\nThe output is: ",s.capitalize())
    print("===============================================================")
    print("2. To 'count occurance of a sub-string' in a string\nWe use string_name.count('sub_string') function")
    print("The given data was:",s)
    ss=input("Enter the substring you want to find: ")
    print("After using string_name.upper('sub_string') function\nThe output is: ",s.count(ss))
    print("===============================================================")
    print("3. To 'check a string' is in lower case\nWe use string_name.islower() function \nIt returns True or False")
    print("The given data was:",s)
    print("After using string_name.islower() function\nThe output is: ",s.islower())
    print("===============================================================")
    print("4. To 'join a string with iterable values' \nWe use string_name.join('strings'/'lists') function")
    print("The 1st string was:",s)
    ss=input("Enter 2nd string: ")
    print("After using string_name.join('strings'/'lists') function")
    print("Each character of 2nd string is concatenated to the front of 1st string: ",s.join(ss))
    print("===============================================================")

main()
