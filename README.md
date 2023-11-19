# Uncomment

## How it works

This function allow you to uncomment a python file. It will not damage your code in any way, it will just remove all the comment, and suppress the big vertical spaces in your code if you have some.

## Advice to use it

You should only use this function on text python file. Maybe later, there will be an update that could allow you to directly put your python file in it, but for the moment it is not the case. So before to put your python file the function, you need to change it into a text file

## Example of how you need to implement it

First you need to copy the "uncomment.py" to your directory where are saved your file that you want to uncomment.

```python
filename="test.txt"
uncomment(filename)
# or you can simply put the filename directly in it
uncomment(test.txt)
```

## Result

This implementation should create a "new_test.txt" file, and from there you just need to change it into a python file to be able to use it.

```
your_directory/
├── test.txt
├── new_test.txt
└── uncomment.py
```

