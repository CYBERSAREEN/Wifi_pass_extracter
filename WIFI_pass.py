''' 
This is the windows based module which extract saved Wifi - passwords from the saved pass list adddressing the name and security key saved by the user during connection establishment  
'''
""" 
Architectural structure or guide for the contrcution of this wifi pass extractor
"""

import subprocess as sb #>>> in order to make anything work on terminal, we need to call this module 
import optparse as opt #>>> in order to take arguments from the user 

parser = opt.OptionParser() # the class is bieng called

# It will return the user entering something in a certain way storing its value to the variables.

parser.add_option("-s","--show",action = 'store_true' ,dest = "show",help=" Will show all the saved network interfaces")
parser.add_option("-n","--name",dest = "name",help=" Will allocate the 'NAME OF ACCESS POINT'")
parser.add_option("-c","--current",action = 'store_true',dest = "current",help=" Will show the password of the current connected network")
parser.add_option("-e","--export",action = 'store_true',dest = "export",help=" Will export all the password creating a pass folder")


# We need to make the parser understand that how the code will work and where to innitialise the value/string added to it 
(options,arguments) = parser.parse_args() #it will act as function 


# Ask the user to input the name of the saved access point
name = options.name 

# Display the details of the specified Wi-Fi profile (including the key)
def result_concluder(x): #>>> here the x is taken to be replaced by other interlinking variables 
    result = sb.check_output(['netsh', 'wlan', 'show', 'profile', x, 'key=clear'], text=True)

# This is the simple string based program which finds the "key content" in the output and then finds whats written in next to it 
    password = ""
    for line in result.split('\n'):
        if 'Key Content' in line:
            password = line.split(':')[1].strip()
            break

    print(f"Wi-Fi Password for {x}: {password}")

# Display the list of saved Wi-Fi profiles
if options.show:
    sb.call(['netsh', 'wlan', 'show', 'profiles'])

# Display the password for the saved network 
elif options.name:
    result_concluder(options.name)

# Export all profiles creating a file pass on the directory
elif options.export:
    sb.call(['mkdir','pass'])
    sb.call(['netsh', 'wlan', 'export', 'profile','folder=pass','key=clear'])

# Display the password for the current connected ACCESS POINT
elif options.current:
    current_profile = sb.check_output(['netsh', 'wlan', 'show', 'interfaces'], text=True)

    profile_name = ""
    for line in current_profile.split('\n'):
        if 'Profile' in line:
            profile_name = line.split(':')[1].strip()
            break


# Basic python string based program that will extract the name of profile and then calls out the function result_concluder replacing the x value with prifile name. 
    if profile_name:
        result_concluder(profile_name)
    else:
        print("Not currently connected to a Wi-Fi network.")

        
        
