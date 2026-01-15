# Write a Python program to write multiple strings into a file.
f=open("new.txt","w")
write=["heelooo","\nkem chheeeee","\nhehhehehe"]
f.writelines(write)
f.close()