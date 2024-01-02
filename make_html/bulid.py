'''
A script to build the website with the same header and footer for all the files
'''

import os


# At this point in the code we have all the files content, now we will create the website
creation_location = "../website"


# Getting the footer and header from the listed files
wrapper = []

try:
    wrapper.append(open("./parts/wrappers/header.html", "r").read())
    print("The header file was read")

except FileNotFoundError:
    print("Could not read the header file")

try:
    wrapper.append(open("./parts/wrappers/footer.html", "r").read())
    print("The footer file was read")

except FileNotFoundError:
    print("Could not read the footer file")

# List of all the files that we are going to create
indexs = []

# Looping through the list of pages and getting their content
for root, dirs, files in os.walk("./parts/indexs"):
    for name in files:
        try:
            indexs.append([name,open(os.path.join(root, name), "r").read()])
            print(f"The content of {name} was read")
        except FileNotFoundError:
            print(f"Could not read the content of {name}")

# Creating the build dir is does not exist
if not os.path.isdir(creation_location):
    os.mkdir(creation_location)

# Printing to the user that we are in the building stage
print("\nBuilding the webpages",end='\n\n')

# Making the files
for file_combo in indexs:
    # The name and the file content from the file_combo
    name = file_combo[0]
    content = file_combo[1]

    # Creating the files
    try:
        file = open(os.path.join(creation_location,name),"w")
        file.write(wrapper[0])   # The header
        file.write(content)   # The content of that specific webpage
        file.write(wrapper[1])   # The footer
        file.close()
        print(f"File {name} wes created successfully")

    except FileNotFoundError:
        print(f"Could not create '{name}' - FileNotFoundError")
    except PermissionError:
        print(f"Could not create '{name}' - PermissionError")
    except Exception as e:
        print(f"Could not create '{name}' - {type(e).__name__}")
