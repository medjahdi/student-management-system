import os
import sys
import app
# Enable ANSI escape codes on Windows
if sys.platform == "win32":
    os.system("color")
app.main()
