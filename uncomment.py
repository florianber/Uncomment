import string 

def uncomment(filename):
    """
    You can only use this to comment python file 
    that are already changed in text file. This will 
    allow you to uncomment properly the python file you have 
    in order to let it like that or comment it again in 
    your own way.
    """
    # Variable Initialization
    file=open(filename,"r")
    new_file=""
    letter=False
    prec_line=0

    # Main loop to access the file
    for line in file:
        new_line=""

        # Allow to not have too many spaces between piece of code
        if line=="\n" and not prec_line:
            new_file+=line
            prec_line=1
        # Go through all characters in a line
        for char in line:
            
            # Verify if your line contain letters
            if char in string.ascii_letters:
                letter=True

            # Replace the comment sign by a line break
            elif char=="#"and letter:
                new_line+="\n"
                break
            
            # Don't car about the line entirely commented
            elif char=="#" and not letter:
                break

            new_line+=char
        
        # Add the line uncommented to the new file
        if letter:
            new_file+=new_line
            letter=False
            prec_line=0

    file.close()
    n_filename="new_"+filename
    
    file=open(n_filename,"w")
    file.write(new_file)
    file.close()
    


# Example on how to use it
filename="test.txt"
uncomment(filename)


