def num_steps(coordinates):
    #keep track of steps
    steps = 0

    #loop through coordinates, minimum steps from point
    #to point will be the absolute value of the difference
    #of consecutive coordinates
    for i in range(len(coordinates)-1):
       current_x, current_y = coordinates[i]
       next_x, next_y = coordinates[i+1]

       x_steps = abs(current_x - next_x)
       y_steps = abs(current_y - next_y)

       steps += max(x_steps, y_steps)

    return steps
