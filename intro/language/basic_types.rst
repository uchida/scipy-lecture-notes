基本的な型
==========

..  Basic types
    ============

数値型
------

..  Numerical types
    ----------------

整数::

    >>> 1 + 1
    2
    >>> a = 4

..
    Integer variables::
    
        >>> 1 + 1
        2
        >>> a = 4

浮動小数点数::

    >>> c = 2.1

..
    floats ::
    
        >>> c = 2.1

複素数（Python の組み込み型です!）::

    >>> a=1.5+0.5j
    >>> a.real
    1.5
    >>> a.imag
    0.5

..
    complex (a native type in Python!) ::
    
        >>> a=1.5+0.5j
        >>> a.real
        1.5
        >>> a.imag
        0.5

そして, ブール値::

    >>> 3 > 4
    False
    >>> test = (3 > 4)
    >>> test
    False
    >>> type(test)
    <type 'bool'>

..
    and booleans::
    
        >>> 3 > 4
        False
        >>> test = (3 > 4)
        >>> test
        False
        >>> type(test)
        <type 'bool'>


Python シェルは基本的な算術演算 ``+``, ``-``, ``*``, ``/``, ``%``
（剰余）がそのまま使えるため電卓代わりに使うこともできます::

    >>> 7 * 3.
    21.0
    >>> 2**10
    1024
    >>> 8%3
    2

..
    A Python shell can therefore replace your pocket calculator, with the
    basic arithmetic operations ``+``, ``-``, ``*``, ``/``, ``%`` (modulo)
    natively implemented::
    
        >>> 7 * 3.
        21.0
        >>> 2**10
        1024
        >>> 8%3
        2

.. warning:: 整数での除算
    ::

	>>> 3/2
	1

    **うまくやるには**: 浮動小数点数を使いましょう::

	>>> 3/2.
	1.5

	>>> a = 3
	>>> b = 2
	>>> a/b
	1
	>>> a/float(b)
	1.5

..
    .. warning:: Integer division
        ::
    
    	>>> 3/2
    	1
    
        **Trick**: use floats:: 
    
    	>>> 3/2.
    	1.5
    
    	>>> a = 3
    	>>> b = 2
    	>>> a/b
    	1
    	>>> a/float(b)
    	1.5

* スカラー型：int, float, complex, bool::

    >>> type(1)
    <type 'int'>
    >>> type(1.)
    <type 'float'>
    >>> type(1. + 0j )
    <type 'complex'>

    >>> a = 3
    >>> type(a)
    <type 'int'>

..
    * Scalar types: int, float, complex, bool::
    
        >>> type(1)
        <type 'int'>
        >>> type(1.)
        <type 'float'>
        >>> type(1. + 0j )
        <type 'complex'>
    
        >>> a = 3
        >>> type(a)
        <type 'int'>


* 型変換::

    >>> float(1)
    1.0

..
    * Type conversion::
    
        >>> float(1)
        1.0

コンテナ
--------

..  Containers
    ------------

Python は多くの効率よいコンテナ型を提供していて, これらはオブジェクトの集まりを記録できます.

..
    Python provides many efficient types of containers, in which collections of
    objects can be stored.

リスト
~~~~~~

..  Lists
    ~~~~~

リストは順序つきのオブジェクトの集まりです, 要素となるオブジェクトは異なる型を取ることができます.
例::

    >>> l = [1, 2, 3, 4, 5]
    >>> type(l)
    <type 'list'>

..
    A list is an ordered collection of objects, that may have different
    types. For example ::
    
        >>> l = [1, 2, 3, 4, 5]
        >>> type(l)
        <type 'list'>

* インデクス指定：リストが含む個々のオブジェクトにアクセス::

    >>> l[2]
    3

  負のインデクスは端から数えます::

    >>> l[-1]
    5
    >>> l[-2]
    4

  .. warning::
   
      **インデクスは 0 から始まります** （C のように）1 から（Fortran や Matlab のように）ではありません!

..
    * Indexing: accessing individual objects contained in the list::
    
        >>> l[2]
        3
    
      Counting from the end with negative indices::
    
        >>> l[-1]
        5
        >>> l[-2]
        4
    
    .. warning::
    
        **Indexing starts at 0** (as in C), not at 1 (as in Fortran or Matlab)!

* スライス：規則正しく並んだ要素からなる部分リストを得る

  ::

    >>> l
    [1, 2, 3, 4, 5]
    >>> l[2:4]
    [3, 4]

  .. Warning::
   
      ``l[start:stop]`` はインデクス ``start<= i <stop`` を満す ``i``
      である（ ``i`` は ``start`` から ``stop-1`` までの値をとる）ことに注意しましょう.
      したがって,  ``l[start:stop]`` は ``(stop-start)`` 個の要素を持ちます.

**スライス構文** ： `l[start:stop:stride]`

全てのスライスのパラメータは必須ではありません::

    >>> l[3:]
    [4, 5]
    >>> l[:3]
    [1, 2, 3]
    >>> l[::2]
    [1, 3, 5]

..
    * Slicing: obtaining sublists of regularly-spaced elements
    
    ::
    
        >>> l
        [1, 2, 3, 4, 5]
        >>> l[2:4]
        [3, 4]
    
    .. Warning::
    
        Note that ``l[start:stop]`` contains the elements with indices ``i``
        such as  ``start<= i < stop`` (``i`` ranging from ``start`` to
        ``stop-1``). Therefore, ``l[start:stop]`` has ``(stop-start)`` elements.
    
    **Slicing syntax**: `l[start:stop:stride]`
    
    All slicing parameters are optional::
    
        >>> l[3:]
        [4, 5]
        >>> l[:3]
        [1, 2, 3]
        >>> l[::2]
        [1, 3, 5]

リストは *変更可能 (mutable)* なオブジェクトなので変更できます::

    >>> l[0] = 28
    >>> l
    [28, 2, 3, 4, 5]
    >>> l[2:4] = [3, 8] 
    >>> l
    [28, 2, 3, 8, 5]

.. Note::

    リストの要素は異なる型を持ちえます::

	>>> l = [3, 2, 'hello']
	>>> l
	[3, 2, 'hello']
	>>> l[1], l[2]
	(2, 'hello')

    リストの要素があらゆる型, サイズをとりうるために,
    リストの i 番目の要素へのアクセスは複雑さ O(i) となります.
    要素が全て同じ型を持つ数値データの集まりに対しては
    **Numpy** モジュールが提供している,
    固定サイズのデータがメモリ上に順序よく並んだデータの集まり
    **array** 型を使うとより効率的です.
    Numpy の array を使うとi番目の要素へのアクセスは要素が規則正しく並んでいるため
    複雑さ O(1) となります.

..
    Lists are *mutable* objects and can be modified::
    
        >>> l[0] = 28
        >>> l
        [28, 2, 3, 4, 5]
        >>> l[2:4] = [3, 8] 
        >>> l
        [28, 2, 3, 8, 5]
    
    .. Note::
    
        The elements of a list may have different types::
    
    	>>> l = [3, 2, 'hello']
    	>>> l
    	[3, 2, 'hello']
    	>>> l[1], l[2]
    	(2, 'hello')
    
        As the elements of a list can be of any type and size, accessing the
        i `th` element of a list has a complexity O(i). For collections of
        numerical data that all have the same type, it is **more efficient** to use
        the **array** type provided by the **Numpy** module, which is a sequence
        of regularly-spaced chunks of memory containing fixed-sized data istems.
        With Numpy arrays, accessing the i`th` element has a complexity of O(1)
        because the elements are regularly spaced in memory.


Python はリストを変更する, 照会するための多くの関数を提供します.
ここでは少数の例を挙げますが, 詳しくは
http://docs.python.org/tutorial/datastructures.html#more-on-lists [*]_
を見てください.

..
    Python offers a large panel of functions to modify lists,
    or query them. Here are a few examples; for more details, see
    http://docs.python.org/tutorial/datastructures.html#more-on-lists

要素の追加と削除::

    >>> l = [1, 2, 3, 4, 5]
    >>> l.append(6)
    >>> l
    [1, 2, 3, 4, 5, 6]
    >>> l.pop()
    6
    >>> l
    [1, 2, 3, 4, 5]
    >>> l.extend([6, 7]) # extend l, in-place
    >>> l
    [1, 2, 3, 4, 5, 6, 7]
    >>> l = l[:-2]
    >>> l
    [1, 2, 3, 4, 5]

..
    Add and remove elements::
    
        >>> l = [1, 2, 3, 4, 5]
        >>> l.append(6)
        >>> l
        [1, 2, 3, 4, 5, 6]
        >>> l.pop()
        6
        >>> l
        [1, 2, 3, 4, 5]
        >>> l.extend([6, 7]) # extend l, in-place
        >>> l
        [1, 2, 3, 4, 5, 6, 7]
        >>> l = l[:-2]
        >>> l
        [1, 2, 3, 4, 5]


`l` の逆順::

    >>> r = l[::-1]
    >>> r
    [5, 4, 3, 2, 1]

..
    Reverse `l`::
    
        >>> r = l[::-1]
        >>> r
        [5, 4, 3, 2, 1]

リストの結合と繰り返し:: 

    >>> r + l
    [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]
    >>> 2 * r
    [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]

..
    Concatenate and repeat lists:: 
    
        >>> r + l
        [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]
        >>> 2 * r
        [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]

r のソート（インプレース：上書きされる）::

    >>> r.sort()
    >>> r
    [1, 2, 3, 4, 5]

..
    Sort r (in-place)::
    
    >>> r.sort()
    >>> r
    [1, 2, 3, 4, 5]


.. Note:: **メソッドとオブジェクト指向プログラミング**

    ここで ``r.method()`` という表記法 (``r.sort(), r.append(3), l.pop()``) は
    オブジェクト指向プログラミングのはじめての例です.
    オブジェクト `r` は ``list`` なので **.** の表記で使える
    *method* 関数を所持しています.
    このチュートリアルでは **.** の表記以上の OOP の知識は不要です.

..
    .. Note:: **Methods and Object-Oriented Programming**
    
        The notation ``r.method()`` (``r.sort(), r.append(3), l.pop()``) is our
        first example of object-oriented programming (OOP). Being a ``list``, the
        object `r` owns the *method* `function` that is called using the notation
        **.**. No further knowledge of OOP than understanding the notation **.** is
        necessary for going through this tutorial.  


.. note:: **メソッドを見つける：**

    IPython を起動した上で：tab-補完（tab を押す）

    .. sourcecode:: ipython

        In [28]: r.
        r.__add__           r.__iadd__          r.__setattr__
        r.__class__         r.__imul__          r.__setitem__
        r.__contains__      r.__init__          r.__setslice__
        r.__delattr__       r.__iter__          r.__sizeof__
        r.__delitem__       r.__le__            r.__str__
        r.__delslice__      r.__len__           r.__subclasshook__
        r.__doc__           r.__lt__            r.append
        r.__eq__            r.__mul__           r.count
        r.__format__        r.__ne__            r.extend
        r.__ge__            r.__new__           r.index
        r.__getattribute__  r.__reduce__        r.insert
        r.__getitem__       r.__reduce_ex__     r.pop
        r.__getslice__      r.__repr__          r.remove
        r.__gt__            r.__reversed__      r.reverse
        r.__hash__          r.__rmul__          r.sort

..
    .. note:: **Discovering methods:**
    
        In IPython: tab-completion (press tab)
    
        .. sourcecode:: ipython
    
            In [28]: r.
            r.__add__           r.__iadd__          r.__setattr__
            r.__class__         r.__imul__          r.__setitem__
            r.__contains__      r.__init__          r.__setslice__
            r.__delattr__       r.__iter__          r.__sizeof__
            r.__delitem__       r.__le__            r.__str__
            r.__delslice__      r.__len__           r.__subclasshook__
            r.__doc__           r.__lt__            r.append
            r.__eq__            r.__mul__           r.count
            r.__format__        r.__ne__            r.extend
            r.__ge__            r.__new__           r.index
            r.__getattribute__  r.__reduce__        r.insert
            r.__getitem__       r.__reduce_ex__     r.pop
            r.__getslice__      r.__repr__          r.remove
            r.__gt__            r.__reversed__      r.reverse
            r.__hash__          r.__rmul__          r.sort




文字列
~~~~~~

..  Strings
    ~~~~~~~

異なる文字列構文（シングルクオート, ダブルクオート, 3重のクオート）::

    s = 'Hello, how are you?'
    s = "Hi, what's up"
    s = '''Hello, 
           how are you'''
    s = """Hi,
	   what's up?'''

..
    Different string syntaxes (simple, double or triple quotes)::
    
        s = 'Hello, how are you?'
        s = "Hi, what's up"
        s = '''Hello, 
               how are you'''
        s = """Hi,
    	   what's up?'''

.. sourcecode:: ipython

    In [1]: 'Hi, what's up?'
    ------------------------------------------------------------
       File "<ipython console>", line 1
	 'Hi, what's up?'
               ^
    SyntaxError: invalid syntax

改行文字は ``\n`` で tab 文字は ``\t`` です. 

文字列はリストのように要素が集まったものです. 
そのためインデクスやスライスを同じ構文や規則で使うことができます. 

..
    The newline character is ``\n``, and the tab characted is
    ``\t``.
    
    Strings are collections as lists. Hence they can be indexed and sliced,
    using the same syntax and rules.
    
インデクス指定::

    >>> a = "hello"
    >>> a[0]
    'h'
    >>> a[1]
    'e'
    >>> a[-1]
    'o'

..
    Indexing::
    
        >>> a = "hello"
        >>> a[0]
        'h'
        >>> a[1]
        'e'
        >>> a[-1]
        'o'

（負のインデクスは右端から数えることに対応することを忘れずに. ）

..
    (Remember that Negative indices correspond to counting from the right
    end.)

スライス::

    >>> a = "hello, world!"
    >>> a[3:6] # 3rd to 6th (excluded) elements: elements 3, 4, 5
    'lo,'
    >>> a[2:10:2] # Syntax: a[start:stop:step]
    'lo o'
    >>> a[::3] # every three characters, from beginning to end 
    'hl r!'

..
    Slicing::
    
    
        >>> a = "hello, world!"
        >>> a[3:6] # 3rd to 6th (excluded) elements: elements 3, 4, 5
        'lo,'
        >>> a[2:10:2] # Syntax: a[start:stop:step]
        'lo o'
        >>> a[::3] # every three characters, from beginning to end 
        'hl r!'

アクセントや特殊な記号は [*]_ Unicode 文字列で扱うことができます（
http://docs.python.org/tutorial/introduction.html#unicode-strings [*]_
を見ましょう）.

..
    Accents and special characters can also be handled in Unicode strings (see
    http://docs.python.org/tutorial/introduction.html#unicode-strings).

文字列は **変化不可能なオブジェクト (immutable)** なので文字を変更することはできません. 
とはいえ, 元の文字列から新しい文字列を作ることはできます.

..
    A string is an **immutable object** and it is not possible to modify its
    characters. One may however create new strings from an original one.

.. sourcecode:: ipython

    In [53]: a = "hello, world!"
    In [54]: a[2] = 'z'
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call
    last)

    /home/gouillar/travail/sgr/2009/talks/dakar_python/cours/gael/essai/source/<ipython
    console> in <module>()

    TypeError: 'str' object does not support item assignment
    In [55]: a.replace('l', 'z', 1)
    Out[55]: 'hezlo, world!'
    In [56]: a.replace('l', 'z')
    Out[56]: 'hezzo, worzd!'

文字列は上で見た ``a.relace`` のような多くの便利なメソッドを持っています.
``a.`` がオブジェクト指向の表記法であることと
新しいメソッドを探すのに tab 補完か ``help(str)`` が使えることは覚えておきましょう.

..
    Strings have many useful methods, such as ``a.replace`` as seen above.
    Remember the ``a.`` object-oriented notation and use tab completion or
    ``help(str)`` to search for new methods.

.. Note:: 

    Python はパターンを探したり, 
    フォーマットするといった進んだ文字列操作の方法を提供しています.
    時間的制限にためにその話題はここでは述べませんが,興味のある読者は
    http://docs.python.org/library/stdtypes.html#string-methods [*]_ と
    http://docs.python.org/library/string.html#new-string-formatting [*]_
    を参照して下さい.

..
    .. Note:: 
    
        Python offers advanced possibilities for manipulating strings,
        looking for patterns or formatting. Due to lack of time this topic is
        not addressed here, but the interested reader is referred to
        http://docs.python.org/library/stdtypes.html#string-methods and
        http://docs.python.org/library/string.html#new-string-formatting

* 文字列の置換::

    >>> 'An integer: %i; a float: %f; another string: %s' % (1, 0.1, 'string')
    'An integer: 1; a float: 0.100000; another string: string'

    >>> i = 102
    >>> filename = 'processing_of_dataset_%03d.txt'%i
    >>> filename
    'processing_of_dataset_102.txt'

..
    * String substitution::
    
        >>> 'An integer: %i; a float: %f; another string: %s' % (1, 0.1, 'string')
        'An integer: 1; a float: 0.100000; another string: string'
    
        >>> i = 102
        >>> filename = 'processing_of_dataset_%03d.txt'%i
        >>> filename
        'processing_of_dataset_102.txt'


辞書
~~~~

..
    Dictionnaries
    ~~~~~~~~~~~~~

辞書はハッシュテーブルを基にして **キー (key) を値 (value) に対応づけします** .
即ちこれは **順序づけられていない** コンテナです::

    >>> tel = {'emmanuelle': 5752, 'sebastian': 5578}
    >>> tel['francis'] = 5915 
    >>> tel
    {'sebastian': 5578, 'francis': 5915, 'emmanuelle': 5752}
    >>> tel['sebastian']
    5578
    >>> tel.keys()
    ['sebastian', 'francis', 'emmanuelle']
    >>> tel.values()
    [5578, 5915, 5752]
    >>> 'francis' in tel
    True

..
    A dictionnary is basically a hash table that **maps keys to values**. It
    is therefore an **unordered** container::
    
    
        >>> tel = {'emmanuelle': 5752, 'sebastian': 5578}
        >>> tel['francis'] = 5915 
        >>> tel
        {'sebastian': 5578, 'francis': 5915, 'emmanuelle': 5752}
        >>> tel['sebastian']
        5578
        >>> tel.keys()
        ['sebastian', 'francis', 'emmanuelle']
        >>> tel.values()
        [5578, 5915, 5752]
        >>> 'francis' in tel
        True

値を名前と関連づけて値を記録する（文字列に対して名前や時刻等を記録等）のに
とても便利なコンテナです.
より詳しくは
http://docs.python.org/tutorial/datastructures.html#dictionaries [*]_
を見ましょう.

..
    This is a very convenient data container in order to store values
    associated to a name (a string for a date, a name, etc.). See
    http://docs.python.org/tutorial/datastructures.html#dictionaries
    for more information.

辞書のキー, 値は各々異なる型を取ることができます::

    >>> d = {'a':1, 'b':2, 3:'hello'}
    >>> d
    {'a': 1, 3: 'hello', 'b': 2}

..
    A dictionnary can have keys (resp. values) with different types::
    
        >>> d = {'a':1, 'b':2, 3:'hello'}
        >>> d
        {'a': 1, 3: 'hello', 'b': 2}

さらに多くのコンテナ型
~~~~~~~~~~~~~~~~~~~~~~

..
    More container types
    ~~~~~~~~~~~~~~~~~~~~

* **タプル**

  タプルは要は変化不可能 (immutable) なリストです.
  タプルの要素はカンマで区切られ, 丸括弧に囲われて書かれます::
   
      >>> t = 12345, 54321, 'hello!'
      >>> t[0]
      12345
      >>> t
      (12345, 54321, 'hello!')
      >>> u = (0, 2)

.. * **Tuples**

..   Tuples are basically immutable lists. The elements of a tuple are written
..   between brackets, or just separated by commas::
  
  
..       >>> t = 12345, 54321, 'hello!'
..       >>> t[0]
..       12345
..       >>> t
..       (12345, 54321, 'hello!')
..       >>> u = (0, 2)

* **集合：** 順序つきでない, 一意な要素の集まり::

    >>> s = set(('a', 'b', 'c', 'a'))
    >>> s
    set(['a', 'c', 'b'])
    >>> s.difference(('a', 'b'))
    set(['c'])

..
    * **Sets:** non ordered, unique items::
    
        >>> s = set(('a', 'b', 'c', 'a'))
        >>> s
        set(['a', 'c', 'b'])
        >>> s.difference(('a', 'b'))
        set(['c'])

.. topic:: IPython をうまく使う秘訣

   * IPython では ``ls``, ``pwd``, ``cd`` 等のいくつかの Linux シェルコマンドが動きます.

   * オブジェクトや関数, その他に関するヘルプを得たければ ``help object``
     やただ単に help() と打ち込んでみましょう.

   * できるだけ **tab補完** しましょう：オブジェクトの名前（変数, 関数, モジュール）を打ち込んですぐ
     **Tab** キーを押すと IPython がマッチする利用可能な名前に補完してくれます.
     もしたくさんの名前が候補にあれば, 候補となる名前のリストを表示します.

   * **履歴** ： 以前に入力した命令に `上` の矢印キーを押すことで
     移れます（逆に `下` の矢印で次に進みます）.
     移動できる命令はカーソルの左側に入力された表現と一致する命令です
     （つまり, カーソルが1番右にある場合には
     全ての過去のコマンドを渡り歩くことができます）.

   * IPython の %logstart という「マジックコマンド」を使えばセッションを保存できます.
     そうすれば, あなたの打ち込む命令群は異なるセッションで
     スクリプトとして実行できるファイルとして保存されます.

     .. sourcecode:: ipython
      
         In [1]: %logstart commandes.log
         Activating auto-logging. Current session state plus future input
         saved.
         Filename       : commandes.log
         Mode           : backup
         Output logging : False
         Raw input log  : False
         Timestamping   : False
         State          : active

..
    .. topic:: A bag of Ipython tricks
    
        * Several Linux shell commands work in Ipython, such as ``ls``,
        * ``pwd``,
          ``cd``, etc.
    
        * To get help about objects, functions, etc., type ``help object``.
          Just type help() to get started.
    
        * Use **tab-completion** as much as possible: while typing the
          beginning of an object's name (variable, function, module), press 
          the **Tab** key and Ipython will complete the expression to match 
          available names. If many names are possible, a list of names is 
          displayed.
    
        * **History**: press the `up` (resp. `down`) arrow to go through all
          previous (resp. next) instructions starting with the expression on
          the left of the cursor (put the cursor at the beginning of the line
          to go through all previous commands) 
    
        * You may log your session by using the Ipython "magic command"
          %logstart. Your instructions will be saved in a file, that you can
          execute as a script in a different session.


.. .. sourcecode:: ipython

..     In [1]: %logstart commandes.log
..     Activating auto-logging. Current session state plus future input
..     saved.
..     Filename       : commandes.log
..     Mode           : backup
..     Output logging : False
..     Raw input log  : False
..     Timestamping   : False
..     State          : active

.. rubric:: Footnotes

.. [*] 日本語訳 http://www.python.jp/doc/release/tutorial/datastructures.html#tut-morelists
.. [*] あるいは日本語など
.. [*] 日本語訳 http://www.python.jp/doc/release/tutorial/introduction.html#unicode
.. [*] 日本語訳 http://www.python.jp/doc/release/library/stdtypes.html#string-methods
.. [*] 日本語訳 http://www.python.jp/doc/release/library/string.html
.. [*] 日本語訳 http://www.python.jp/doc/release/tutorial/datastructures.html#tut-dictionaries

