import os

file_name = "/var/log/restartLog.txt"
date = os.popen('date').read()
text = "Restart happened in: "+date

def append_new_line(file_name, text_to_append):
    """Append given text as a new line at the end of file"""
    # Open the file in append & read mode ('a+')
    with open(file_name, "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("")
        # Append text at the end of file
        file_object.write(text_to_append)


append_new_line(file_name,text)
