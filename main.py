# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

#append to the exiting text
# with open("my_file.txt", mode="a") as file:
#     file.write("\n New text.")

#creating a new txt file
with open("new_file.txt", mode="w") as file:
    file.write("New text.")
