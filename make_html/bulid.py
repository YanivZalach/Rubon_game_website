'''
A script to build the website with the same header and footer for all the files
'''

import os


# At this point in the code we have all the files content, now we will create the website
creation_location = "../website"


# Getting the footer and header from the listed files
wrapper = []

# List of all the files that we are going to create
indexs = []

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


# Printing to the user that we created the file string
print("\nCreating the file strings",end='\n\n')

# Making the file strings
for file_combo in indexs:
    # The name and the file content from the file_combo
    name = file_combo[0]
    content = file_combo[1]

    # Creating the file strings
    try:
        file_combo[1] = wrapper[0] + content + wrapper[1]
        print(f"File string {name} wes created successfully")

    except Exception as e:
        print(f"Could not create '{name}' - {type(e).__name__}")


# Printing to the user that we are adding the personal stylesheet
print("\nAdding personal stylesheet",end='\n\n')

# Adding personal stylesheet (stylesheet name: {name}_style.css)
for file_combo in indexs:
    # The name and the file content from the file_combo
    name = file_combo[0]
    content = file_combo[1]

    # Adding the stylesheet
    try:
        # Locating the place to add the stylesheet: `<!-- Insert stylesheet -->`
        add_index = content.find('<!-- Insert stylesheet -->')
        # Getting the file name without the end
        file_name = name[ : name.find('.') ]
        # Adding to the content
        file_combo[1]=content[:add_index] +f'<link rel="stylesheet" href="css/{file_name}_style.css">\n' + content[add_index:]
        print(f"Added the stylesheet to {name}")

    except Exception as e:
        print(f"Could not find the index comment in '{name}' - {type(e).__name__}")
    


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
        file.write(content)   # The content of that specific webpage
        file.close()
        print(f"File {name} wes created successfully")

    except FileNotFoundError:
        print(f"Could not create '{name}' - FileNotFoundError")
    except PermissionError:
        print(f"Could not create '{name}' - PermissionError")
    except Exception as e:
        print(f"Could not create '{name}' - {type(e).__name__}")
