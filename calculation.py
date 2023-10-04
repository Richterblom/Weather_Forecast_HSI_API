"""
Did the calculation function in its own .py just to make things simpler
"""
def hsical(temp, humid):

    # print((0.81 * temp) + ((0.01 * humid) * ((0.99 * temp) - 14.3)) + 46.3)
    return (0.81 * temp) + ((0.01 * humid) * ((0.99 * temp) - 14.3)) + 46.3
