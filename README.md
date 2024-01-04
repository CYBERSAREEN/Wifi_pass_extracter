# Windows Wi-Fi Profile Explorer
A Python script leveraging the subprocess and optparse modules to interact with Windows Wi-Fi profiles. This utility provides essential functionalities:
<br>
Show Profiles:
<br>
Utilize the -s or --show option to display a list of all saved Wi-Fi profiles. <br>
Retrieve Wi-Fi Passwords:<br>
<br>
Specify a Wi-Fi network's name using the -n or --name option to extract and display its password.<br>
Current Network Information:<br>
<br>
Activate the -c or --current option to showcase details, including the password, of the currently connected Wi-Fi network.<br>
Note: The script utilizes Windows-specific commands (netsh wlan) to extract information about Wi-Fi profiles. Ensure compatibility with your operating system.<br>
