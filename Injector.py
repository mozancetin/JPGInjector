import PIL.Image
import io

class Injector:
    SEPARATOR = b'--INJECTED-DATA--'

    @staticmethod
    def HideString(path, text):
        with open(path, "ab") as f:
            f.write(Injector.SEPARATOR + str.encode(text, 'utf-8'))

    @staticmethod
    def GetString(path):
        with open(path, "rb") as f:
            content = f.read()

            offset = content.find(Injector.SEPARATOR)
            if offset == -1:
                raise ValueError("No injected data found.")

            f.seek(offset + len(Injector.SEPARATOR))
            text = f.read().decode('utf-8')
        return text

    @staticmethod
    def HidePhoto(targetPath, injectionPath):
        img = PIL.Image.open(targetPath)
        byte_arr = io.BytesIO()
        img.save(byte_arr, format='PNG')

        with open(injectionPath, 'ab') as f:
            f.write(Injector.SEPARATOR + byte_arr.getvalue())

    @staticmethod
    def GetPhoto(injectionPath, savePath):
        with open(injectionPath, "rb") as f:
            content = f.read()
            # Find the separator, not just FFD9
            offset = content.find(Injector.SEPARATOR)
            if offset == -1:
                raise ValueError("No injected photo found.")

            f.seek(offset + len(Injector.SEPARATOR))

            new_img = PIL.Image.open(io.BytesIO(f.read()))
            new_img.save(savePath)

    @staticmethod
    def HideExe(targetExePath, injectionPath):
        with open(injectionPath, 'ab') as f, open(targetExePath, 'rb') as e:
            f.write(Injector.SEPARATOR + e.read())

    @staticmethod
    def GetExe(injectionPath, savePath):
        with open(injectionPath, 'rb') as f:
            content = f.read()
             # Find the separator
            offset = content.find(Injector.SEPARATOR)
            if offset == -1:
                raise ValueError("No injected EXE found.")

            f.seek(offset + len(Injector.SEPARATOR))

            with open(savePath, 'wb') as e:
                e.write(f.read())