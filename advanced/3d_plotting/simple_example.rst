簡単な例
========

.. A simple example
.. =================

.. warning:: `ipython -wthread` で起動して下さい

.. .. warning:: Start `ipython -wthread`

.. literalinclude:: simple_example.py

`np.mgrid[-10:10:100j, -10:10:100j]` は x, y 各方向-10から10までの間で100ステップの格子を作ります.

.. `np.mgrid[-10:10:100j, -10:10:100j]` creates an x,y grid, going from -10
.. to 10, with 100 steps in each directions.

.. image:: simple_example.png
    :align: center
    :scale: 50


