入出力
======

.. Input and Output
.. ================

もれなく紹介するために, ここでは Python の入出力についての情報について扱います.
ファイルの読み書きは後で Numpy のメソッドを使うので,
最初に読むときは飛ばしてもかまいません.

.. To be exhaustive, here are some informations about input and output in Python.
.. Since we will use the Numpy methods to read and write files, you may skip this
.. chapter at first reading.

ファイルには **文字列** を読み書きします （他の型も文字列に変換されます）
ファイルに書き込むには

.. We write or read **strings** to/from files (other types must be converted to
.. strings). To write in a file::

::

    >>> f = open('workfile', 'w') # opens the workfile file
    >>> type(f)
    <type 'file'>
    >>> f.write('This is a test \nand another test')
    >>> f.close()

ファイルから読み込むには

.. To read from a file

.. sourcecode:: ipython

    In [1]: f = open('workfile', 'r')

    In [2]: s = f.read()

    In [3]: print(s)
    This is a test 
    and another test

    In [4]: f.close()

より詳しくは http://docs.python.org/tutorial/inputoutput.html [*]_

.. For more details: http://docs.python.org/tutorial/inputoutput.html

ファイルに対して反復
~~~~~~~~~~~~~~~~~~~~

.. Iterating over a file
.. ~~~~~~~~~~~~~~~~~~~~~

.. sourcecode:: ipython

    In [6]: f = open('workfile', 'r')

    In [7]: for line in f:
    ...:     print line
    ...:     
    ...:     
    This is a test 

    and another test

    In [8]: f.close()

ファイルのモード
----------------

.. File modes
.. ----------

* 読み込みのみ： ``r``
* 書き込みのみ： ``w``

  * 新しいファイルが作られるか, 存在するファイル上書きされることに注意.

* ファイルに追記： ``a``
* 読み書き: ``r+``
* バイナリモード： ``b``

  * バイナリファイルのために使うことに注意, 特に Windows で.

.. * Read-only: ``r``
.. * Write-only: ``w``

..   * Note: Create a new file or *overwrite* existing file.

.. * Append a file: ``a``
.. * Read and Write: ``r+``
.. * Binary mode: ``b``

..   * Note: Use for binary files, especially on Windows.

.. rubric:: 脚注

.. [*] http://www.python.jp/doc/release/tutorial/inputoutput.html
