# Print a range of numbers based on a start and end point determined by a user's input


# Setup
start_point = int(input('Start from: '))
end_point = int(input('End on: '))



# Do the work
desired_range = start_point
# Use a while loop to count all numbers included in range
while desired_range < end_point:
    desired_range += 1
    # Output result
    print(desired_range)


