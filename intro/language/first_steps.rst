最初の一歩
----------

..  First steps
    -------------

**iPython** シェル（機能拡張された Python 対話型シェル）を起動してみましょう：

* Linux/Mac のターミナルから
  または Windows のコマンドプロンプトから "ipython" と打ち込んで,
* **または**  Python(x,y) や EPD などの科学ライブラリ一式からインストールしている場合
  プログラムメニューから起動してみましょう.

..
    Start the **Ipython** shell (an enhanced interactive Python shell):
    
    * by typing "Ipython" from a Linux/Mac terminal, or from the Windows cmd shell,
    * **or** by starting the program from a menu, e.g. in the Python(x,y) or
      EPD menu if you have installed one these scientific-Python suites.

.. :ref:`pythonxy`

もし ipython が計算機にインストールされていない,
もしくはターミナルから "python" と打って使える Python デフォルトのシェルが利用できるとしても,
対話的な科学技術計算機能をはじめとする拡張機能をもった ipython シェルを利用することをお勧めします.

..
    If you don't have Ipython installed on your computer, other Python shells
    are available, such as the plain Python shell started by typing "python"
    in a terminal, or the Idle interpreter. However, we advise to use the
    Ipython shell because of its enhanced features, especially for
    interactive scientific computing.

インタプリタを起動したら::

    >>> print "Hello, world!"
    Hello, world!

と打ちこんでみましょう.

"Hello, world!" というメッセージが表示されるはずです.
実行しましたね, いままさに Python の学習がはじまりました, おめでとう!

..
    Once you have started the interpreter, type ::
    
        >>> print "Hello, world!"
        Hello, world!
    
    The message "Hello, world!" is then displayed. You just executed your
    first Python instruction, congratulations!

次に理解を深めて使えるようにするために,
下にのせた例を順を追って打ち込んでみましょう::

    >>> a = 3
    >>> b = 2*a
    >>> type(b)
    <type 'int'>
    >>> print b
    6
    >>> a*b
    18
    >>> b = 'hello'
    >>> type(b)
    <type 'str'>
    >>> b + b
    'hellohello'
    >>> 2*b
    'hellohello'

..
    To get yourself started, type the following stack of instructions ::
     
        >>> a = 3
        >>> b = 2*a
        >>> type(b)
        <type 'int'>
        >>> print b
        6
        >>> a*b
        18
        >>> b = 'hello'
        >>> type(b)
        <type 'str'>
        >>> b + b
        'hellohello'
        >>> 2*b
        'hellohello'

``a``, ``b`` の2つのオブジェクトは上で定義されています.
ただオブジェクトの型が代入される前に宣言されていないことに注意しましょう.
これと対照的に C ではこう書かなければいけません.

.. sourcecode:: c

    int a;
    a = 3;

..
    Two objects ``a`` and ``b`` have been defined above. Note that one does
    not declare the type of an object before assigning its value. In C,
    conversely, one should write:
    
    .. sourcecode:: c
    
        int a;
        a = 3;

加えて, オブジェクトの型は変わることがあります.
`b` は最初整数でしたが,  `hello` を代入されて文字列になりました.
整数の操作 (``b=2*a``) は Python の標準ライブラリでそのまま実行され,
文字列の加算や乗算はそれぞれ結合と繰り返しになります.

..
    In addition, the type of an object may change. `b` was first an integer,
    but it became a string when it was assigned the value `hello`. Operations
    on integers (``b=2*a``) are coded natively in the Python standard
    library, and so are some operations on strings such as additions and
    multiplications, which amount respectively to concatenation and
    repetition.



