関数を定義する
==============

..  Defining functions
    =====================

関数定義
--------

..  Function definition
    -------------------

.. sourcecode:: ipython

    In [56]: def test():
       ....:     print('in test function')
       ....:     
       ....:     

    In [57]: test()
    in test function

.. Warning:: 

    関数ブロックは制御フローブロックと同様にインデントされる必要があります. 

..
    .. Warning:: 
    
        Function blocks must be indented as other control-flow blocks.

return 文
---------

..  Return statement
    ----------------

関数は *オプションとして* 値を返すことができます. 

..  Functions can *optionally* return values.

.. sourcecode:: ipython

    In [6]: def disk_area(radius):
       ...:     return 3.14 * radius * radius
       ...: 

    In [8]: disk_area(1.5)
    Out[8]: 7.0649999999999995

.. Note:: デフォルトでは, 関数は ``None`` を返します. 

.. .. Note:: By default, functions return ``None``.

.. Note:: 関数定義構文の注解：

    * ``def`` キーワード；

    * 続けて関数の **名前**, そして

    * 丸括弧の間に関数の引数を与え, 続けてコロン

    * 関数の本体；

    * そしてオプションとして値を返すために ``return object`` する

..
    .. Note:: Note the syntax to define a function:
    
        * the ``def`` keyword;
    
        * is followed by the function's **name**, then
    
        * the arguments of the function are given between brackets followed
          by a colon.
    
        * the function body ;
    
        * and ``return object`` for optionally returning values.


引数
----

..  Parameters
    ----------

必須の引数（固定引数）

.. Mandatory parameters (positional arguments)

.. sourcecode:: ipython

    In [81]: def double_it(x):
       ....:     return x * 2
       ....: 

    In [82]: double_it(3)
    Out[82]: 6

    In [83]: double_it()
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)

    /Users/cburns/src/scipy2009/scipy_2009_tutorial/source/<ipython console> in <module>()

    TypeError: double_it() takes exactly 1 argument (0 given)

オプションの引数（キーワード引数または名前付き引数）

.. Optional parameters (keyword or named arguments)

.. sourcecode:: ipython

    In [84]: def double_it(x=2):
       ....:     return x * 2
       ....: 

    In [85]: double_it()
    Out[85]: 4

    In [86]: double_it(3)
    Out[86]: 6

キーワード引数は *デフォルトの値* を持つことができます. 

.. Keyword arguments allow you to specify *default values*.

.. warning:: 

   デフォルトの値は関数が呼び出されたときではなく, 定義されたときに評価されます. 

..
    .. warning:: 
    
       default values are evaluated when the function is defined, not when
       it is called.

.. sourcecode:: ipython

    In [124]: bigx = 10

    In [125]: def double_it(x=bigx):
       .....:     return x * 2
       .....: 

    In [126]: bigx = 1e9  # Now really big

    In [128]: double_it()
    Out[128]: 20

python のスライスを実装した, より複雑な例：

.. More involved example implementing python's slicing:

.. sourcecode:: ipython

    In [98]: def slicer(seq, start=None, stop=None, step=None):
       ....:     """Implement basic python slicing."""
       ....:     return seq[start:stop:step]
       ....: 

    In [101]: rhyme = 'one fish, two fish, red fish, blue fish'.split()

    In [102]: rhyme
    Out[102]: ['one', 'fish,', 'two', 'fish,', 'red', 'fish,', 'blue', 'fish']

    In [103]: slicer(rhyme)
    Out[103]: ['one', 'fish,', 'two', 'fish,', 'red', 'fish,', 'blue', 'fish']

    In [104]: slicer(rhyme, step=2)
    Out[104]: ['one', 'two', 'red', 'blue']

    In [105]: slicer(rhyme, 1, step=2)
    Out[105]: ['fish,', 'fish,', 'fish,', 'fish']

    In [106]: slicer(rhyme, start=1, stop=4, step=2)
    Out[106]: ['fish,', 'fish,']

キーワード引数はどんな順序で書いても問題ありません：

.. The order of the keyword arguments does not matter:

.. sourcecode:: ipython

    In [107]: slicer(rhyme, step=2, start=1, stop=4)
    Out[107]: ['fish,', 'fish,']

しかし, 関数定義と同じ順序で書くこと方がいい習慣とされます.

..  but it is good practice to use the same ordering as the function's
    definition.

*キーワード引数* は多くの引数を持つ関数を定義するのにとても便利な機能です, 
とりわけ, 多くの値がデフォルトの値を持つような関数で特に便利です. 

..
    *Keyword arguments* are a very convenient feature for defining functions
    with a variable number of arguments, especially when default values are
    to be used in most calls to the function.

値渡し
------

..  Passed by value
    ---------------

関数内部の変数に変更を加えることはできるでしょうか?
多くの言語 (C, Java, ...) では「値渡し (passing by value)」
と「参照渡し (passing by reference)」を区別します [*]_ . 
Python ではこのような区別はいくぶん不自然で, 
変数が変更されるのかについては少々わかりにくいところがあります. 
しかし, 幸運なことに明解な規則があります. 

..
    Can you modify the value of a variable inside a function? Most languages
    (C, Java, ...) distinguish "passing by value" and "passing by reference".
    In Python, such a distinction is somewhat artificial, and it is a bit
    subtle whether your variables are going to be modified or not.
    Fortunately, there exist clear rules.

関数の引数はオブジェクトの参照が値として渡されます. 
関数に変数を渡すとき, Python は変数を参照しているオブジェクト（ **値** ）を渡します. 
変数自身は渡しません. 

..
    Parameters to functions are refereence to objects, which are passed by
    value. When you pass a variable to a function, python passes the
    reference to the object to which the variable refers (the **value**).
    Not the variable itself.

もし **値** が変化不可能 (immutable) なら, 関数は呼び出し元の変数を変更しません. 
もし **値** が変更可能 (mutable) なら, 関数は呼び出し元の変数をインプレースに変更する可能性があります::

    >>> def try_to_modify(x, y, z):
    ...     x = 23
    ...     y.append(42)
    ...     z = [99] # new reference
    ...     print(x)
    ...     print(y)
    ...     print(z)
    ...     
    >>> a = 77    # immutable variable
    >>> b = [99]  # mutable variable
    >>> c = [28]
    >>> try_to_modify(a, b, c)
    23
    [99, 42]
    [99]
    >>> print(a)
    77
    >>> print(b)
    [99, 42]
    >>> print(c)
    [28]

..
    If the **value** is immutable, the function does not modify the caller's
    variable.  If the **value** is mutable, the function may modify the
    caller's variable in-place::
    
        >>> def try_to_modify(x, y, z):
        ...     x = 23
        ...     y.append(42)
        ...     z = [99] # new reference
        ...     print(x)
        ...     print(y)
        ...     print(z)
        ...     
        >>> a = 77    # immutable variable
        >>> b = [99]  # mutable variable
        >>> c = [28]
        >>> try_to_modify(a, b, c)
        23
        [99, 42]
        [99]
        >>> print(a)
        77
        >>> print(b)
        [99, 42]
        >>> print(c)
        [28]

関数はローカルな変数テーブルを持っています, 
それは *ローカルな名前空間* と呼ばれます. 

.. functions have a local variable table. called a *local namespace*.

変数 ``x`` は *foo* 関数の中でのみ存在します. 

.. the variable ``x`` only exists within the function *foo*.


グローバル変数
--------------

..  global variables
    ----------------

関数の外で宣言された変数は関数内部で呼び出すことができます：

..  variables declared outside the function can be referenced within the
    function:

.. sourcecode:: ipython

    In [114]: x = 5

    In [115]: def addx(y):
       .....:     return x + y
       .....: 

    In [116]: addx(10)
    Out[116]: 15

しかし, これらのグローバル変数は関数の中で変更することはできません, 
ただし **global** と宣言すれば可能になります. 

..  but these "global" variables cannot be modified within the function,
    unless declared **global** in the function.

これは動きません：

.. this doesn't work:

.. sourcecode:: ipython

    In [117]: def setx(y):
       .....:     x = y
       .....:     print('x is %d' % x)
       .....:     
       .....:     

    In [118]: setx(10)
    x is 10

    In [120]: x
    Out[120]: 5

これは動きます：

.. this works:

.. sourcecode:: ipython

    In [121]: def setx(y):
       .....:     global x
       .....:     x = y
       .....:     print('x is %d' % x)
       .....:     
       .....:     

    In [122]: setx(10)
    x is 10

    In [123]: x
    out[123]: 10


可変な引数
----------

..  variable number of parameters
    -----------------------------

引数の特別な形式：
  * \*args：任意の固定引数が入ったタプル
  * \**kwargs：任意のキーワード引数が入った辞書

..
    special forms of parameters:
      * \*args: any number of positional arguments packed into a tuple
      * \**kwargs: any number of keyword arguments packed into a dictionary

.. sourcecode:: ipython

    In [35]: def variable_args(*args, **kwargs):
       ....:     print 'args is', args
       ....:     print 'kwargs is', kwargs
       ....: 

    In [36]: variable_args('one', 'two', x=1, y=2, z=3)
    args is ('one', 'two')
    kwargs is {'y': 2, 'x': 1, 'z': 3}

.. **

ドキュメンテーション文字列 (docstring)
--------------------------------------

..  docstrings
    ----------

関数が何をするのかとその引数についてのドキュメントを書くのに
一般的なとりきめとして：

..  documention about what the function does and it's parameters.  general
    convention:

.. sourcecode:: ipython

    In [67]: def funcname(params):
       ....:     """Concise one-line sentence describing the function.
       ....: 
       ....:     Extended summary which can contain multiple paragraphs.
       ....:     """
       ....:     # function body
       ....:     pass
       ....: 

    In [68]: funcname?
    Type:		function
    Base class:	<type 'function'>
    String form:	<function funcname at 0xeaa0f0>
    Namespace:	Interactive
    File:		/Users/cburns/src/scipy2009/.../<ipython console>
    Definition:	funcname(params)
    Docstring:
        Eoncise one-line sentence describing the function.

        Extended summary which can contain multiple paragraphs.

.. note:: **ドキュメンテーション文字列に関するガイドライン**


    標準化の目的のために, `docstring conventions 
    <http://www.python.org/dev/peps/pep-0257>`_ の Web ページ [*]_
    に python の docstring に関する意味論と取り決めが文書化されています. 

    また numpy や scipy モジュールも科学技術計算用の関数の文書化のために
    簡潔化された標準を定めています, 
    それらは,  ``引数`` 節や ``example`` 節等を含んでいて, 
    自分で書いた関数について参考にしたいと思うことでしょう. 
    http://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt
    と http://github.com/numpy/numpy/blob/master/doc/example.py#L37 を見てください.

..
    .. note:: **docstring guidelines**
    
    
        for the sake of standardization, the `docstring
        conventions <http://www.python.org/dev/peps/pep-0257>`_ webpage
        documents the semantics and conventions associated with python
        docstrings.
    
        also, the numpy and scipy modules have defined a precised standard
        for documenting scientific functions, that you may want to follow for
        your own functions, with a ``parameters`` section, an ``examples``
        section, etc. see
        http://projects.scipy.org/numpy/wiki/codingstyleguidelines#docstring-standard 
        and http://projects.scipy.org/numpy/browser/trunk/doc/example.py#l37
    
    functions are objects
    ---------------------
    functions are first-class objects, which means they can be:
      * assigned to a variable
      * an item in a list (or any collection)
      * passed as an argument to another function.

.. sourcecode:: ipython

    in [38]: va = variable_args

    in [39]: va('three', x=1, y=2)
    args is ('three',)
    kwargs is {'y': 2, 'x': 1}

メソッド
--------

..  methods
    -------

メソッドはオブジェクトと結びついた関数です. 
これまで **リスト**, **辞書**, **文字列** 等の例の中でみてきました. 

..  methods are functions attached to objects.  you've seen these in our
    examples on **lists**, **dictionaries**, **strings**, etc...

練習問題
--------

..  exercises
    ---------

.. topic:: 練習問題：クイックソート

    クイックソートアルゴリズムを実装しましょう, Wikipedia での定義::

	function quicksort(array)
	    var list less, greater
	    if length(array) < 2  
		return array  
	    select and remove a pivot value pivot from array
	    for each x in array
		if x < pivot + 1 then append x to less
		else append x to greater
	    return concatenate(quicksort(less), pivot, quicksort(greater))

:ref:`quick_sort`

..
    .. topic:: exercise: quicksort
    
        implement the quicksort algorithm, as defined by wikipedia::
    
    	function quicksort(array)
    	    var list less, greater
    	    if length(array) < 2  
    		return array  
    	    select and remove a pivot value pivot from array
    	    for each x in array
    		if x < pivot + 1 then append x to less
    		else append x to greater
    	    return concatenate(quicksort(less), pivot, quicksort(greater))
    
    .. :ref:`quick_sort`

.. topic:: 練習問題：Fibonacci 数列

    Fibonacci 数列の第1項から ``n`` 項までを表示する関数を書きましょう, 
    Fibonacci 数列の定義は：

    * ``u_0 = 1; u_1 = 1``
    * ``u_(n+2) = u_(n+1) + u_n``

:ref:`fibonacci`

..
    .. topic:: Exercise: Fibonacci sequence
    
        Write a function that displays the ``n`` first terms of the Fibonacci
        sequence, defined by:
    
        * ``u_0 = 1; u_1 = 1``
        * ``u_(n+2) = u_(n+1) + u_n``
    
    .. :ref:`fibonacci`

.. rubric:: Footnotes

.. [*] C や Java は値渡ししかないので参照渡しはない. ポインタの値渡しのことを参照渡しといっているのかな?
.. [*] 日本語訳 `ドキュメンテーション文字列の書き方のガイドライン <http://www.python.jp/doc/contrib/peps/pep-0257.txt>`_
