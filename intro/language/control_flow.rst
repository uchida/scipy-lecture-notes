制御フロー
==========

..  Control Flow
    ============

コードが実行される順序を制御します.

.. Controls the order in which the code is executed.

if/elif/else
------------

.. sourcecode:: ipython
  
    In [1]: if 2**2 == 4:
       ...:     print('Obvious!')
       ...: 
    Obvious!

**ブロックの範囲はインデントで決まります**

.. **Blocks are delimited by indentation**


以下の行を Python インタプリタで打ち込んで下さい, ただし 
**インデントの深さに注意してください**
IPython はコラム記号 ``:`` の後に自動的にインデントを深くします;
インデントを減らすにはバックスペースキーでスペース4つ分移動します.
論理ブロックを抜けるためには2回エンターキーを押します.

..
    Type the following lines in your Python interpreter, and be careful to
    **respect the indentation depth**. The Ipython shell automatically
    increases the indentation depth after a column ``:`` sign; to
    decrease the indentation depth, go four spaces to the left with the
    Backspace key. Press the Enter key twice to leave the logical block.

.. sourcecode:: ipython

    In [2]: a = 10
    
    In [3]: if a == 1:
       ...:     print(1)
       ...: elif a == 2:
       ...:     print(2)
       ...: else:
       ...:     print('A lot')
       ...: 
    A lot

インデントはスクリプトを書く場合も必須です.
練習問題として, 上の行の内容を同じインデントで
``condition.py`` というスクリプトに打ち込んで
IPython から ``run condition.py``
としてスクリプトを実行してみましょう.

..
    Indentation is compulsory in scripts as well. As an exercise, re-type the
    previous lines with the same indentation in a script ``condition.py``, and
    execute the script with ``run condition.py`` in Ipython.

for/range
----------

インデクスで反復する：

.. Iterating with an index:

.. sourcecode:: ipython

    In [4]: for i in range(4):
       ...:     print(i)
       ...: 
    0
    1
    2
    3

しかし多くの場合, 値に対して反復した方が読みやすいでしょう：

.. But most often, it is more readable to iterate over values:

.. sourcecode:: ipython

    In [5]: for word in ('cool', 'powerful', 'readable'):
       ...:     print('Python is %s' % word)
       ...: 
    Python is cool
    Python is powerful
    Python is readable


while/break/continue
---------------------

典型的な C 形式の while ループ（Mandelbrot の問題）：

.. Typical C-style while loop (Mandelbrot problem):

.. sourcecode:: ipython

    In [6]: z = 1 + 1j

    In [7]: while abs(z) < 100:
       ...:     z = z**2 + 1
       ...:     

    In [8]: z
    Out[8]: (-134+352j)

**より進んだ機能**

.. **More advanced features**

``break`` for/while ループの中から抜ける：

.. ``break`` out of enclosing for/while loop:

.. sourcecode:: ipython

    In [9]: z = 1 + 1j

    In [10]: while abs(z) < 100:
       ....:     if z.imag == 0:
       ....:         break
       ....:     z = z**2 + 1
       ....:     
       ....:     


``continue`` ループの反復を進める::

    >>> a = [1, 0, 2, 4]
    >>> for element in a:
    ...     if element == 0:
    ...         continue
    ...     print 1. / element
    ...     
    1.0
    0.5
    0.25

..
    ``continue`` the next iteration of a loop.::
    
        >>> a = [1, 0, 2, 4]
        >>> for element in a:
        ...     if element == 0:
        ...         continue
        ...     print 1. / element
        ...     
        1.0
        0.5
        0.25


条件式
------

..  Conditional Expressions
    -----------------------

* `if オブジェクト`

  真と評価されるもの：
    * 0 でない値
    * 長さが 0 でないシーケンス

  偽と評価されるもの：
    * 0 となる値
    * 空のシーケンス

..
    * `if object`
    
      Evaluates to True:
        * any non-zero value
        * any sequence with a length > 0
    
      Evaluates to False:
        * any zero value
        * any empty sequence
    
* `a == b`

  論理的に等価かどうか調べる：

  .. sourcecode:: ipython

    In [19]: 1 == 1.
    Out[19]: True

..
    * `a == b`
    
    Tests equality, with logics:

..   .. sourcecode:: ipython

..     In [19]: 1 == 1.
..     Out[19]: True

* `a is b`

  同一性を調べる：2つのオブジェクトが同じか

  .. sourcecode:: ipython

    In [20]: 1 is 1.
    Out[20]: False

    In [21]: a = 1

    In [22]: b = 1

    In [23]: a is b
    Out[23]: True

..
    * `a is b`
    
      Tests identity: both objects are the same

..   .. sourcecode:: ipython

..     In [20]: 1 is 1.
..     Out[20]: False

..     In [21]: a = 1

..     In [22]: b = 1

..     In [23]: a is b
..     Out[23]: True

* `a in b`

  データの集まり `b` の中に `a` が含まれているか::

    >>> b = [1, 2, 3]
    >>> 2 in b
    True
    >>> 5 in b
    False

  
  `b` が辞書の場合, 辞書のキーに `a` が含まれているか調べます.

..
    * `a in b`
    
      For any collection `b`: `b` contains `a` ::
    
        >>> b = [1, 2, 3]
        >>> 2 in b
        True
        >>> 5 in b
        False
    
    
      If `b` is a dictionary, this tests that `a` is a key of `b`.


進んだ反復
----------

..  Advanced iteration
    -------------------------

あらゆるシーケンスに対する反復
--------------------------------

..  Iterate over any *sequence*
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* あらゆるシーケンスに対して反復できます（文字列, リスト, 辞書, ファイル, ...）

.. * You can iterate over any sequence (string, list, dictionary, file, ...)

  .. sourcecode:: ipython

    In [11]: vowels = 'aeiouy'

    In [12]: for i in 'powerful':
       ....:     if i in vowels:
       ....:         print(i),
       ....:         
       ....:         
    o e u

::

    >>> message = "Hello how are you?"
    >>> message.split() # returns a list
    ['Hello', 'how', 'are', 'you?']
    >>> for word in message.split():
    ...     print word
    ...     
    Hello
    how
    are
    you?

整数やインデクスでなく, あらゆるものに対してループできる言語は
（特に科学技術計算向きの言語では）少数です.
Python を使うことで, インデクスについて注意深く考えない為に起きる問題に
悩まされることはなくなり, 
まさに興味あるオブジェクトに対してループできるようになります.

..
    Few languages (in particular, languages for scienfic computing) allow to
    loop over anything but integers/indices. With Python it is possible to
    loop exactly over the objects of interest without bothering with indices
    you often don't care about.

.. warning:: 反復しているシーケンスを変更するのは危険です.

.. .. warning:: Not safe to modify the sequence you are iterating over.

反復回数を追跡する
~~~~~~~~~~~~~~~~~~

..  Keeping track of enumeration number
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

シーケンスの反復中に反復回数を追跡することはよくあります.

..  Common task is to iterate over a sequence while keeping track of the
    item number.

* 以下のような, カウンタ付きの while や for ループを使うこともできます：

  .. sourcecode:: ipython

    In [13]: for i in range(0, len(words)):
       ....:     print(i, words[i])
       ....:     
       ....:     
    0 cool
    1 powerful
    2 readable

..  * Could use while loop with a counter as above. Or a for loop:

..   .. sourcecode:: ipython

..     In [13]: for i in range(0, len(words)):
..        ....:     print(i, words[i])
..        ....:     
..        ....:     
..     0 cool
..     1 powerful
..     2 readable

* しかし, Python はそうするための **enumerate** を提供しています::

    >>> words = ('cool', 'powerful', 'readable')
    >>> for index, item in enumerate(words):
    ...     print index, item
    ...     
    0 cool
    1 powerful
    2 readable

..
    * But Python provides **enumerate** for this::
    
        >>> words = ('cool', 'powerful', 'readable')
        >>> for index, item in enumerate(words):
        ...     print index, item
        ...     
        0 cool
        1 powerful
        2 readable


辞書を使ったループ
~~~~~~~~~~~~~~~~~~~~~~~~~~

..  Looping over a dictionary
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

**iteritems** を使います:

.. Use **iteritems**:

.. sourcecode:: ipython

    In [15]: d = {'a': 1, 'b':1.2, 'c':1j}

    In [15]: for key, val in d.iteritems():
       ....:     print('Key: %s has value: %s' % (key, val))
       ....:     
       ....:     
    Key: a has value: 1
    Key: c has value: 1j
    Key: b has value: 1.2

リスト内包表記
-------------------

..  List Comprehensions
    -------------------

.. sourcecode:: ipython

	In [16]: [i**2 for i in range(4)]
	Out[16]: [0, 1, 4, 9]



.. topic:: 練習問題

    Wallis の公式を使って, Pi の値を計算しましょう：

    .. image:: pi_formula.png
	:align: center

.. :ref:`pi_wallis`

..
    .. topic:: Exercise
    
        Compute the decimals of Pi using the Wallis formula:
    
        .. image:: pi_formula.png
    	:align: center
    
    .. :ref:`pi_wallis`



