### Dependencies
* matplotlib              3.2.2


`main.py` and `main_counter.py` are almost identical, the difference is that `main.py` uses some dictionaries and increment oprators to count the number of letters where as `main_counter.py` uses the Counter which has the same purpose and exisists in collections library. You can specify in `run.py` which one you want to use. just import the one that you want in `run.py` and then run it to see the results.
Surprisingly, `main.py` works faster!

If you want to save the results as an image, you can also specify the name of the image as an optional argument to the `LetterFrequency` class in `run.py`

Books were downloaded from www.gutenberg.org

