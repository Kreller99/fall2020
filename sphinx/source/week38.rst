Week 38 - Utilities and Modules
===============================

Today we will carry on the work with modules and more specific the 3rd party module BeautifulSoup for webscrabing. You will also work with persitance in your docker containers, meaning how you will "save" your installed modules done by pip install.

Learning goals
--------------
After this week you will be able to:
       
        - Use python build in modules.
        - Find and use 3rd party modules.
        - Save and Share your modules installed in a docker container.   
        - Work with the module BeautifullSoup for webscrabing.


Materials
---------
* `Slides <>`_  `(Notebook) <>`_
* `Docker Commands <cheatsheet.rst#week-38-utilities-and-modules>`_
* `Code examples from today <https://github.com/python-elective-kea/fall2020-code-examples-from-teachings/tree/master/w38>`_
* `Docker `_

Exercises
---------
------
Docker
------

Ex 1: Clone, build and run
**************************

* Clone this repository:
  
  * git clone https://github.com/python-elective-kea/clbo-alpine-dev-env.git

* Build an Image based on the repositorys Dockerfile.
  
  * docker build --tag clbo/python

* Run a container based on this image
  
  * docker run -it --rm -v ${PWD}:/docs clbo/python

        
Ex 2: Node app and docker
*************************

* `Build and run your image <https://docs.docker.com/get-started/part2/>`_

Ex 3: Create and run a 'Hello world' C application
***************************************************

Based on this docker image: https://hub.docker.com/_/gcc create and run a Hello World app, written i the C language.

The code you need is something like this:

.. code::
   
   #include <stdio.h>
   int main() {
       // printf() displays the string inside quotation
       printf("Hello, World!");
       return 0;
   } 
   

Ex 4: Docker'ise' your own projects
***********************************

This exercise should be done in groups.
* You should create a project that makes use of the requests module.
* You should push this project to a github account and all in the group should have push rights to this repository.
* The project should contain a Dockerfile that as a minimum has a :code:`pip install -r requirements.txt` line in it.
* All group members should clone the repository, build the image based on the Dockerfile, and run a container with the right modules installed.

When this setup is up and running each group member should: 

* install a new 3rd. party module in the container. 
* Create some simple (maybe even stupid) code that makes use of this module
* do a :code:`pip freeze > requirements.txt`
* Push the changes to github
* Pull the other group members changes and do a :code:`docker build --tag nameoftheimage:1.1 .`  

.. warning::
        It might be a good idea that each group member does this one at a time.

------
Python
------

Ex 5: Build a Web Scraper With Python
*************************************

* `Build a Web Scraper With Python <https://realpython.com/beautiful-soup-web-scraper-python/>`_

  * When this is done, extend your solution with the ability to download all images (logos) from the Monster website you just worked with. 

