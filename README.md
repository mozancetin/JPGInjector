# JPG Injector
injector for injecting text, png and exe into a jpg file with python

# Usage

```python
from Injector import *

"""
injectionPath -> injection path of JPG file
pngPath -> target PNG file path
savePath -> path to save
"""

# Hide text
Injector.HideString(injectionPath, text)

# Get text from injected JPG
Injector.GetString(injectionPath)

# Hide PNG file
Injector.HidePhoto(pngPath, injectionPath)

# Get PNG from injected JPG
Injector.GetPhoto(injectionPath, savePath)

# Hide exe
Injector.HideExe(targetExePath, injectionPath)

# Get exe
Injector.GetExe(injectionPath, savePath)
```
