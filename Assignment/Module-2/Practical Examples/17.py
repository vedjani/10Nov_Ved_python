# 17) Write a Python program to convert two lists into one dictionary using a for loop.
key=["id","name","city","number","subject","loction"]
velue=[101,"ved","morbi",9510450418,"python","rajkot"]
dit={}
for i in range(len(key)):
    dit[key[i]]=velue[i]

print("dictionary",dit)
print(type(dit))