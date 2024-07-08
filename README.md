# Hamon Application
 This documentation is the explaination of what the the function f() does and how can we improve the same function.

 ### what does it do?

```python
def f(s):

  r = {}

  for i in s:

     if i in r:

         r[i] += 1

     else:

         r[i] = 0

  return r
```

This function accepts string or list as an input and give the count of characters or elements of the list as output in a form dictionary.

#### Example: - 
When you pass a string **Mohammed Shafi** to this function, each character in the string will be iterated using for loop, each time this charcter will be stored in i, Then it will check this character is already in **r** dictionary as a key using if condition, if it is found in r dictionary, corresponding value in the dictionary will be added to 1. in our case (Mohammed Shafi), in first iteration it won't find it, so, else block will be executed, it will assign value 0 for the corresponding character in our dictionary.
in the next iteration it will calculate o, it will be also get value 0.
then when it reaches to lowercase m, it will again treated as 0, since variables in python is case sensitive, but in the very next iteration, if block will be executed, instead of else, because we have already "m" in our dictionary, it will add 1 to the exting value 0, m value will be 1 in dictionary r.
this iteration will be last until all the characters are finished.
this is also the case for list as input.

### Code Quality Improvement
In the current code the counting value will be wrong, you may need to change the value in else block as below.

```python
     else:

         r[i] = 1
```

we can also do the same thing using python's built in function called count, it will be lesser complex than this one and better readability.

```python
def f(s):

  r = {}

  for i in s:

    r[i] = s.count(i)

  return r
```
We can add or remove if block here,

Here in each iteration it will check how many times the charater appeared in the string (if it is a list, it will check the elements of the list for the same).
when we add if block into this, it won't go through all charater or elements.

### Unit Test Cases

I have added unit test code for current code and my updated one using unittest module in python.
It will check 3 test cases for now, we can add more if want.

In the first case it will check for normal string, then for special characters and finally for a list of values.

#### Test Case Result



I will fail for the current code since it won't give the desired result.



But The updated code will passed since it give the desired result for the given values in the test cases.

### Summary

f() function will calculate elements of the list or characters of the string, we can also improve the code as i mentioned.
