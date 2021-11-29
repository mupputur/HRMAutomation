
class FileOperations:

    def __init__(self, filename):
        self.filename = filename

    def file_read(self):
        try:
            fobj = open(self.filename, 'r')
            data = fobj.read()
            fobj.close()
            return data
        except Exception as e:
            print("unable to found a file. {}".format(str(e)))

    def file_write(self, data):
        fobj = open(self.filename , 'w')
        fobj.write(data)
        fobj.close()

    def file_append(self, data):
        fobj = open(self.filename , 'a+')
        fobj.write(data)
        fobj.close()


class FileActions(FileOperations):

    def __init__(self, filename):
        self.filename = filename
        FileOperations.__init__(self, self.filename)

if __name__ == "__main__":
    filepath = "sample.txt"
    sobj = FileActions(filepath)
    sobj.file_write("Hello World welcome to python")
    print(sobj.file_read())
    sobj.file_append("\n Added the new data")
    print("---------------------------------------------")
    print(sobj.file_read())
