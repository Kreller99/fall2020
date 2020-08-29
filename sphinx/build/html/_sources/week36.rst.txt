Week 36 - Data Structures: Sequences & comprehensions
=====================================================


Today we will work with data structures in python. You will by the end of these sessions be able to use Lists and Tuples, read and Write to Files and work with the for and while loop.

Learning goals
--------------

After this week you will be able to:
        
        - Work with lists, tuples
        - Loop over sequences with a for, foreach & while loops.  
        - Sort sequences using the build in sorted function and use its key parameter to perform custom sorting.  
        - Read from files using the build in "open" function. 
        - Use List comprehensions instead of list assignment and loops in you python code. 


Materials
---------

* `Lists and Tuples in Python <https://realpython.com/python-lists-tuples/>`_
* `Tuples in Python <https://www.datacamp.com/community/tutorials/python-tuples>`_
* `Python "for" Loops <https://realpython.com/python-for-loop/>`_
* `Python "while" Loops <https://realpython.com/python-while-loop/>`_
* `How to Use sorted() and sort() in Python <https://realpython.com/python-sort/>`_
* `Sorting key parameter explained <_static/sorted.png>`_
* `Reading and Writing Files in Python (Guide) <https://realpython.com/read-write-files-python/>`_
* `Comprehending Python’s Comprehensions <https://dbader.org/blog/list-dict-set-comprehensions-in-python>`_
* `Notebook on List Comprehensions <notebooks/list_comprehensions.ipynb>`_
* `Teaching notes <notebooks/lists_tuples_sorting_comp_files.ipynb>`_
* Download :download:`Code examples from teachings <code/week36/>`
  
Exercises
---------


---------------------------------
Ex 1: Build in functions on lists
---------------------------------

| Look at this list of pythons `build in functions <https://docs.python.org/3/library/functions.html>`_.
| Try all of these in the interpretor (on a list you create). e.g  :code:`len(a)`   
| Not all will work on lists, but try it out and see what works. 


-----------------
Ex 2: Sort a list
-----------------
`Solution <exercises/solution/02_lists/sorted_exercises.rst>`_

1. Create a list of strings with names in it. (l = ['Claus', 'Ib', 'Per'])
2. Sort this list by using the sorted() build in function.
3. Sort the list in reversed order. 
4. Sort the list on the lenght of the name.
5. Sort the list based on the last letter in the name.
6. Sort the list with the names where the letter 'a' is in the name first.

--------------------
Ex 2: Basic listcomp
--------------------
`Solutions <notebooks/list_comprehensions.ipynb>`_

1. Create a list of capital letters from the english alphabet.
2. Do the same, but exclude the 4 with the Unicode code point of 70, 75, 80 and 85.
3. Create a list of capital letters, but exclude every second between F & O
4. Create something that prints 

.. code:: python
   
   ['un-even and small', 2, 'un-even and small', 4, 
   'un-even and large', 6, 'un-even and large', 8, 
   'un-even and large']


-------------------
Ex 3: Deck of Cards
-------------------

1. Create a listcomp that produces a list of tuples containing all card in a deck. 

.. code:: python

   [('A','♠'), ('K','♣'), ... ] etc.

..   
        Solution:


        .. code:: python
   
                 numbers = list(range(2, 11)) + ['J', 'Q', 'K', 'A']
                [(i,chr(j)) for i in numbers for j in range(9824, 9828)]


-----------------------
List & Tuples exercises
-----------------------

* `List & tuple exercises <exercises/lists/lists.rst>`_

------
quizes
------
* `Lists and Tuples Quiz <https://realpython.com/quizzes/python-lists-tuples/>`_
* `"while" Loops Quiz <https://realpython.com/quizzes/python-while-loop/>`_
* `Reading and Writing Files in Python Quiz <https://realpython.com/quizzes/read-write-files-python/>`_

