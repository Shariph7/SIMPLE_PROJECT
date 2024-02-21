# Shutting Down the Computer using Python Code
import os
import subprocess
def shutdown_computer():
    if os.name == 'nt':
        # For Windows operating system
        os.system('shutdown /s /t 0')
    elif os.name == 'posix':
        # For Unix/Linux/Mac operating systems
        os.system('sudo shutdown now')
    else:
        print('Unsupported operating system.')

# Calling the shutdown_computer() function to initiate shutdown
shutdown_computer()