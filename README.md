# JPG Injector
injector for injecting text, png and exe into a jpg file with python

This static class allows us to place text, png photos and exe on jpg photos. There are no discernible differences in the JPG photo apart from the size.

NOTE: JPGs injected with this program cannot be restored with this program. So if you are going to inject to an important JPG photo, make sure you have a copy of the photo.

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
