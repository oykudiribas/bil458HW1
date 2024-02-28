# Print Downward Triangle Star Pattern Code

# Assign the desired number of rows for the downward triangle
number = 7

def downward_triangle_star_pattern(number):
    # Loop through the range from the desired number to 0 (not included) in decreasing order
    for i in range(number, 0, -1):
        # Adjust spaces and the number of stars for each row
        print(" " * (number - i) + "* " * i)

# Call the function with the assigned number of rows
downward_triangle_star_pattern(number)

