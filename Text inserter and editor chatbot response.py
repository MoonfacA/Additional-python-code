def insert_line_in_middle(file_path, index, value):
    with open(file_path, "r") as f:
        contents = f.readlines()
        contents.insert(index, value)

    with open(file_path, "w") as f:
        f.write("".join(contents))

# Usage example:
file_path = "Code.txt"
index_to_insert = 4  # Line number where you want to insert
text_to_insert = "New line inserted\n"# This should be a variable# it should be instructed to
#Open a text document, copy last line and run file editor
insert_line_in_middle(file_path, index_to_insert, text_to_insert)
#Replace "myfile.txt" with the actual file path,
#adjust the index_to_insert, and provide the text_to_insert according to your requirements.
#This code will insert the specified line into the middle of the file without overwriting existing content