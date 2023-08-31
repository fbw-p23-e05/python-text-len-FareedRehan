# length() in Python

## Task

### Input --> Output 1
text = str(input("Enter hello world: ", ))
text = "hello world"
result = len(text)
print(result)
if result % 2 == 0:
    print(text, "--> even")
else:
    print(text, "--> odd")
    
### Input --> Output 2
text = str(input("Enter 'hello planet': ", ))
text = "hello planet"
result = (len(text))
print(result)
if result % 2 == 0:
    print(text, "--> even")
else:
    print(text, "--> odd")
    
### Input--> Output 3
text = str(input("Enter quotation marks: ", ))
text = '""'
result = (len(text))
print(result)
if result % 2 == 0:
    print(text, "--> even")
else:
    print(text, "--> odd")


