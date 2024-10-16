import pyjokes
import multiprocessing
import os

print('hello world')

# Module - It is a way to use code written by others in our own program.

# External module
joke = pyjokes.get_joke()
print(joke)

# Internal module
# OS module

print(multiprocessing.cpu_count())
