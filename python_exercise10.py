# Print a square the size of user's input

# Setup 
# Create variables to be used 

shape_item = ''
user_request = int(input('How big is the square? '))
count = 0

# Perform the task

while count < user_request:
    shape_item =  user_request * '*'
    count += 1
    # Output the result
    print(shape_item)

