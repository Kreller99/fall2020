Week 48 - Problem-Solving with python
=====================================




.. note: 
        Øvelse: give kode med python2 fra introduction to Data Science
.. note:
        Emnerne Data Science, Machine learning og Tensorflow.
        Er aflyst, og bliver erstattet af nogle andre. 


..
        Supervised and Unsupervised Learning
        ------------------------------------


        Supervised Learning
                In supervised learning we learn from labeled data.
                Supervised learning is a very powerful learning method, but it can be very costly to create labeled data sets.

        Unsupervised Learning 
                In unsupervised learning we don't have labeled data, so we must learn about data points based on their relation to other data points.
                Unsupervised learning is open for a wider range of problems than supervised learning, but the insights we can gain are less powerfull.

Materials
---------

..
        * `K-Means Clustering in Python: A Practical Guide <https://realpython.com/k-means-clustering-python/>`_

Exercises
---------

..        -------------------------
        Ex 1: Tjek dit cpr-nummer
        -------------------------

        Dit CPR-nummer består af 10 cifre. De 6 første er din fødselsdato, din måned og de sidste to cifre i dit fødselsår: ddmmåå  fx 150949.

        De tre første efter stregen er et såkaldt løbenummer, fra 000-399 i forrige årtusinde.

        Det sidste ciffer er et kontrolciffer, fx 1.

        Du kan tjekke dit eget CPR-nummer efter denne fremgangsmåde, hvor hvert ciffer ganges med en konstant i denne rækkefølge 4,3,2,7,6,5,4,3,2

        Alle produkterne (cpr ciffer og konstant) summeres, så ved cpr nummeret 150949-0941 får man: 

        * 4 + 15 + 0 + 63 + 24 + 45 +0 + 27 + 8 = 186 


        | Summen divideres med 11: 
        | 186 : 11 = 16,0909...
        | Det hele tal 16 ganges med konstanten 11
        | 16 * 11 = 176. 
        | Der er altså 186 –176 = 10 til rest.
        | NB! Hvis divisionen med 11 går op, og der ikke er nogen rest, gives automatisk kontrol-ciffer 0!

        | Kontrolnummeret findes ved at trække denne rest (her 10) fra konstanten 1111 – 10 = 1 
        | Dette nummer - 150949-xxxx

..
        * `Machine learning tutorials <https://realpython.com/tutorials/machine-learning/>`_
        * `Build a Recommendation Engine With Collaborative Filtering <https://realpython.com/build-recommendation-engine-collaborative-filtering/>`_
        * `Three Ways of Storing and Accessing Lots of Images in Python <https://realpython.com/storing-images-in-python/>`_
        * `Recommender Systems in Python <https://www.datacamp.com/community/tutorials/recommender-systems-python>`_
        * `Ultimate Guide to Getting Started with TensorFlow <https://www.kdnuggets.com/2018/09/ultimate-guide-tensorflow.html>`_
        * `TicaTacToe <https://towardsdatascience.com/tic-tac-toe-learner-ai-208813b5261>`_

