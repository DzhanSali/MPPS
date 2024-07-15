import os
from send2trash import send2trash

def find_duplicates(folder):
    duplicates = [
        file
        for file in os.listdir(folder)
        # os.path.isfile(os.path.join(folder, file)) ensures that only files (not directories) are considered. 
        # Without this, directories named with the suffix "-1.mp3" would also be included incorrectly 
        # even though there aren't any in my case.
        if file.endswith("-1.mp3") and os.path.isfile(os.path.join(folder, file))
    ]
    return duplicates

# Usage of normpath: without it an error is thrown related to 
# mixed usage of forward and backward slashes in the file path on a Windows system 
# such as: "C:/Users/Lenovo Y510P/Music/Metal\\ACDC - Kick You When You're Down (128 kbps)-1.mp3" due to the usage of send2trash
def main():
    folder = 'C:/Users/Lenovo Y510P/Music/Metal'
    folder = os.path.normpath(folder)
    duplicates = find_duplicates(folder)
    acc = 0
    
    for duplicate in duplicates:
        acc = acc + 1
        file_path = os.path.join(folder, duplicate)
        file_path = os.path.normpath(file_path)
        send2trash(file_path)
        #print(duplicate)
    
    print(acc)

if __name__ == "__main__":
    main()
