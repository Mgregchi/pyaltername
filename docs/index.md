## PYALTERNAME

Simple and easy way to name, rename,search and manage your files.

## Installations

## You can install with :
```markdown
- pip install pyaltername
- pipwin install pyaltername
```

## Example
- Generate a Name for a file .

```python

from pyaltername import Generic

filename = "Image.png"
path = r"C:/Users"

'''
do your work
data = some_data
'''

generic_name = Generic.name(filename = filename, path = path)

with open(generic_name, "wb") as file:
    file.write(data)
file.close()

```



### Clone and join the move.

### What you can do :

- Submit pull request.
- Clone and make it better.
- Report a bug.
- Provide helpful feedback.


### Support or Contact

Having trouble with the project? Check out our [documentation](https://github.com/Mgregchi/pyaltername/) or [Create an Issue](https://github.com/Mgregchi/pyaltername/issues/) and you’ll get help to sort it out.


### Resources
- [Documentation](https://github.com/Mgregchi/pyaltername/)
- [Issues](https://github.com/Mgregchi/pyaltername/issues/)
- [Wiki](https://github.com/Mgregchi/pyaltername/wiki/)
