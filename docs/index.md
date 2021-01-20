## PYALTERNAME

Simple and easy way to name, rename and search your files

### Installations

## You can install with :
```markdown
- pip install pyaltername
- pipwin install pyaltername
```

## Example
1. Generate a Name for a file .
```markdown
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


```
# Header 1
## Header 2
### Header 3


- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Clone and join the move

Want to make hte project better?.
Submit pull request.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
