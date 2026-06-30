
class TextFileManager:
    def __init__(self, filename, mode="a"):
        self.filename = self.construct_filename(filename)
        self.mode = mode
        self.file = None

    @staticmethod
    def construct_filename(filename) -> str:
        if not isinstance(filename, str):
            return "default.txt"
        return filename if filename.endswith(".txt") else f"{filename}.txt"
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file    
    
    def __exit__(self, exc_type, exc, tb):
        if self.file:
            self.file.close()

        if exc_type:
            print(f"An error was raised:{exc_type}\n{exc}\n\n{tb}")
            return False
        return True


with TextFileManager("hi") as file: #__enter__ being called
    file.write("test" + 234)
#__exit__


#     # Timing a block of code
# with open('my_file.txt', 'r') as file:
#     content = file.read()
#     print(content)