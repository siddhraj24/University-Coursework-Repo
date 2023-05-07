
import os
# defining function for directory space calculation


def directory_space(path):
    # initialize the totaSum variable to zero
    directorySum = 0
    # iterate over all the files for the given path using os module
    for files in os.listdir(path):
        # join the given path to the file in the list to get the file path
        filePath = os.path.join(path, files)
        # check whether the file on the given filepath is file or directory and add the size to the directorySum
        if os.path.isfile(filePath):
            directorySum += os.path.getsize(filePath)
        # Using recursion to get the size of all files in directory
        elif os.path.isdir(filePath):
            directorySum += directory_space(filePath)
    return directorySum


# Get the current working directory and pass it to the directory_space function
size = directory_space(os.getcwd())
print("Directory size in bytes is:", size)


'''Answer to the questions:
# 1.Coding the assignment in Python was easy, since it is my primary language in which I code. The syntax was very simple, easy to 
    read and implement. It has rich library suppory that reduces the need to write additional code and saves time.
    Python is simple, flexible and dynamically typed and therefore we had to write less lines of code.

# 2.If some language does not support recursion, we can achieve the same results through iteration or use some data structure or 
   ADT that can be used to achieve same result.For Exampl,to implement a recursive function, you can write an iterative version 
   using a loop.
   The disadvantage of using iteration instead of recursion is that it can use up more memory when input size is large
   as a separate memory space is required for each iteration. Also,some algorithms are recursive in nature and are difficult
   or inefficient to implement using iteration.'''
