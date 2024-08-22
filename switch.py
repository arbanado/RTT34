def pressBrake():
    print("Pressing the brake")

def accelerate():
    print("Accelerating")

def decelerate():
    print("Decelerating")

def ignore():
    print("Ignoring the sign")

def handle_sign(sign):
    if sign == "Stop":
        pressBrake()
    elif sign == "Merge":
        accelerate()
    elif sign == "Exit":
        decelerate()
    else:
        ignore()

# Example usage
sign = "Merge"  # Replace with "Stop", "Merge", "Exit", or any other sign
handle_sign(sign)



