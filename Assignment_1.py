# Assignment 1 :
# Four Example of String

str1 = "This is First Example of String."
str2 = "This is Second Example of String."
str3 = "This is Thired Example of String."
str4 = "This is Fourth Example of String."

print(str1 + "\n" + str2 + "\n" + str3 + "\n" + str4 + "\n")



# Four Example of Lists and its Opreations
list1 = [1, 2, 3, 4]  # This is a list of Integers
list2 = [1.1, 2.2, 3.3, 4.4]  # This is a list of Floats 
list3 = ["Hello", 'there', "viola", "gargi"] # This a list of char and string ###
list4 = ["hello", 2, 4.4]   ### This is a example of lists with diffrent datatype ###

print(list1,list2,list3,list4)
print(list1[1:3]) # Slicing of the list1
list2[2] = 5.5 # reassigning the value in list2 at index 2
print(list2)



print("\n")
# Four Example of Dictionary and its Opreations
Dict1 = {"Name" : "Gargi", "Age" : 20, "Gender" : "Female"}
Dict2 = {int : 8, float : 9.2, True : 1, False : 0}
Dict3 = {'a' : 5, 'b' : 77, 'c' : 12, 'd' : 90, 'e' : 1}
Dict4 = {'A' : 67, 'B' : 36, 'A' : 33, 'C' : 7}

print(Dict4) # it removes the duplicats and prints the latest value assign
print(Dict1["Name"]) # accessing the element in dictionary using key word
print(Dict3.get('d')) # accessing with get function
Dict2[float] = 6.7 # reassigining the value
print(Dict2)
