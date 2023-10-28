import subprocess
import sys
try:
    subprocess.run(['pyside6-uic', '.\\main.ui', '-o', '.\\modules\\ui_main.py'], check=True)
except subprocess.CalledProcessError as e:
    print("Error running pyside6-uic:", e)
    sys.exit(1)

with open("modules/ui_main.py") as f:
    content =  f.readlines()

content[26] = "from widgets import ManagementPage\n"
content[27] = "from widgets import TwitterDeck\n"

with open("modules/ui_main.py", "w") as f:
    f.writelines(content)
