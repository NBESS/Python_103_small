# Print a 5x5 square of "*"

# Setup
shape_item = ''
lenght_of_shape = 5
count = 0

# Do the work
# Have shape item print desired length

while count < lenght_of_shape:
    shape_item = shape_item + '*'
    count += 1
    # Provide the output
    print(shape_item,flush=True)

