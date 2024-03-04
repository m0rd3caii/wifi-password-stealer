import subprocess

# Obtener los perfiles de red inalambrica
output_profiles = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

# Filtrar solo los nombres de los perfiles de usuario
profiles = [line.split(":")[1].strip() for line in output_profiles if "All User Profile" in line]

# Obtener las contraseñas de los perfiles
for profile in profiles:
    try:
        output_password = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', profile, 'key=clear']).decode('utf-8').split('\n')
        password_lines = [line.split(":")[1].strip() for line in output_password if "Key Content" in line]
        print("{:<30}| {:<}".format(profile, password_lines[0] if password_lines else ""))
    except subprocess.CalledProcessError:
        print("Error al obtener la contraseña para el perfil:", profile)
