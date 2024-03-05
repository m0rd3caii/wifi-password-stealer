# Get wireless network profiles
$profiles = netsh wlan show profiles | Select-String "All User Profile" | ForEach-Object { $_.ToString().Split(":")[1].Trim() }

# Get profile passwords
foreach ($profile in $profiles) {
    try {
        $password_lines = netsh wlan show profile $profile key=clear | Select-String "Key Content" | ForEach-Object { $_.ToString().Split(":")[1].Trim() }
        if ($password_lines) {
            Write-Host "$profile | $($password_lines[0])"
        } else {
            Write-Host "$profile | Password not found"
        }
    } catch {
        Write-Host "Error getting password for profile: $profile"
    }
}
