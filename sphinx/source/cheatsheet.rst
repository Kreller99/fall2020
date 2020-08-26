Commandline Cheatsheet
======================
In this cheatsheet you will find important and hard to remember terminal commands.

Docker Commands
---------------

--------------------------------
Week 35 - Introduction to python 
--------------------------------

.. code::
   
   $ docker run -it --rm ubuntu  // creates and runs a simple ubuntu container with interactive access and removal after use. 
   $ docker run -it --rm python bash // same as above, but now a python image. starts in a bash terminal.
   $ docker run -it --rm -v ${PWD}:/docs python bash  // same as above, but now sharing files from the current directory to/from /docs folder in the container.
 

-----------------------------------------------------
Week 36 - Data Structures: Sequences & comprehensions
-----------------------------------------------------


.. code::







---------------
Sphinx commands
---------------

.. code::
   
   $ docker run --rm -v ${PWD}:/docs sphinx /bin/sh -c 'cd sphinx/; make html'

