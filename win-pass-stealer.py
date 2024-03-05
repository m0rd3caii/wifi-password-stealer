import subprocess

# Get wireless network profiles
output_profiles = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

# Filter only user profile names
profiles = [line.split(":")[1].strip() for line in output_profiles if "All User Profile" in line]

# Get profile passwords
for profile in profiles:
    try:
        output_password = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', profile, 'key=clear']).decode('utf-8').split('\n')
        password_lines = [line.split(":")[1].strip() for line in output_password if "Key Content" in line]
        print("{:<30}| {:<}".format(profile, password_lines[0] if password_lines else ""))
    except subprocess.CalledProcessError:
        print("[!]Error getting password for profile:", profile)
