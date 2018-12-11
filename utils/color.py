# Use with something like this:
# print Color.CYAN + "Jon is rad" + Color.RESET

class Color:
    """
        Used to change the color of output to screen.
        Print a given color before printing your message, then print RESET
        at the end of your message to reset the terminal back to normal.

        A more robust implementation would differentiate background and foreground
        as described here:

            http://www.vias.org/linux-knowhow/lnag_05_05_04.html
    """
    RED    = '\033[31m'
    GREEN  = '\033[32m'
    YELLOW = '\033[33m'
    BLUE   = '\033[34m'
    VIOLET = '\033[35m'
    CYAN   = '\033[36m'
    GRAY   = '\033[37m'
    DIM    = '\033[2m' # Not supported in MacOS Terminal. 
    RESET  = '\033[0;0m'