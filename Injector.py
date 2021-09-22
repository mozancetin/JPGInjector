import PIL.Image
import io

class Injector:

    @staticmethod
    def HideString(path, text):
        with open(path, "ab") as f:
            f.write(str.encode(text))

    @staticmethod
    def GetString(path):
        with open(path, "rb") as f:
            content = f.read()
            offset = content.index(bytes.fromhex('FFD9'))
            f.seek(offset + 2)
            text = f.read().decode('utf-8')
        return text

    @staticmethod
    def HidePhoto(targetPath, injectionPath):
        img = PIL.Image.open(targetPath)
        byte_arr = io.BytesIO()
        img.save(byte_arr, format='PNG')

        with open(injectionPath, 'ab') as f:
            f.write(byte_arr.getvalue())

    @staticmethod
    def GetPhoto(injectionPath, savePath):
        with open(injectionPath, "rb") as f:
            content = f.read()
            offset = content.index(bytes.fromhex('FFD9'))

            f.seek(offset + 2)

            new_img = PIL.Image.open(io.BytesIO(f.read()))
            new_img.save(savePath)

    @staticmethod
    def HideExe(targetExePath, injectionPath):
        with open(injectionPath, 'ab') as f, open(targetExePath, 'rb') as e:
            f.write(e.read())

    @staticmethod
    def GetExe(injectionPath, savePath):
        with open(injectionPath, 'rb') as f:
            content = f.read()
            offset = content.index(bytes.fromhex('FFD9'))
            f.seek(offset + 2)

            with open(savePath, 'wb') as e:
                e.write(f.read())
