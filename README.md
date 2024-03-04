# WiFi password stealer
```ruby
██╗    ██╗██╗███████╗██╗    ███████╗████████╗███████╗ █████╗ ██╗     ███████╗██████╗ 
██║    ██║██║██╔════╝██║    ██╔════╝╚══██╔══╝██╔════╝██╔══██╗██║     ██╔════╝██╔══██╗
██║ █╗ ██║██║█████╗  ██║    ███████╗   ██║   █████╗  ███████║██║     █████╗  ██████╔╝
██║███╗██║██║██╔══╝  ██║    ╚════██║   ██║   ██╔══╝  ██╔══██║██║     ██╔══╝  ██╔══██╗
╚███╔███╔╝██║██║     ██║    ███████║   ██║   ███████╗██║  ██║███████╗███████╗██║  ██║
 ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝    ╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝
```                                                                                   

### Powershell Example:
```ps1
PS> .\win-passwd-stealer.ps1

Perfil1 | Contraseña1
Perfil2 | Contraseña2
```
### Python Example:

### Step 1:
Install pyinstaller to make it an executable.

```py
pip install pyinstaller
```
### Step 2:
```py
pyinstaller --onefile win-pass-stealer.py
```
## Step 3:
Use it:

```py
.\win-pass-stealer.exe
Perfil1 | Contraseña1
Perfil2 | Contraseña2
```
Or just use it without making it executable

```py
python3 get_wifi_passwords.py
Perfil1 | Contraseña1
Perfil2 | Contraseña2
```
