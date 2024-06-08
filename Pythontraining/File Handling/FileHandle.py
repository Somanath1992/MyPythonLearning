# Example 1: Writing Date into text file
file = open("C:/Users/Admin/PycharmProjects/MySeleniumLearning/Pythontraining/File Handling/myfile.txt", 'w')
file.write("This is my first statement...")
file.write("\nThis is my second statement...")
file.write("\nThis is my third statement...")
file.write("\nThis is my fourth statement...")
file.close()
print("Program completed")

# Example 2: Reading data from text file
file1 = open("C:/Users/Admin/PycharmProjects/MySeleniumLearning/Pythontraining/File Handling/myfile.txt", 'r')
# print(file1.readline())
print(file1.read())
file1.close()


# Example 3: Appending data from text file
file2 = open("C:/Users/Admin/PycharmProjects/MySeleniumLearning/Pythontraining/File Handling/myfile.txt", 'a')
file2.write("\nThis is my fifth line")
file2.write("\nThis is my sixth line")
file2.close()
print("append program completed")
