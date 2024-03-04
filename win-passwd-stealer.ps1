# Obtener los perfiles de red inalámbrica
$profiles = netsh wlan show profiles | Select-String "All User Profile" | ForEach-Object { $_.ToString().Split(":")[1].Trim() }

# Obtener las contraseñas de los perfiles
foreach ($profile in $profiles) {
    try {
        $password_lines = netsh wlan show profile $profile key=clear | Select-String "Key Content" | ForEach-Object { $_.ToString().Split(":")[1].Trim() }
        if ($password_lines) {
            Write-Host "$profile | $($password_lines[0])"
        } else {
            Write-Host "$profile | No se encontró contraseña"
        }
    } catch {
        Write-Host "Error al obtener la contraseña para el perfil: $profile"
    }
}
