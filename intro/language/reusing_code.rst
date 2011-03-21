コードの再利用：スクリプトとモジュール
======================================

.. Reusing code: scripts and modules
.. =================================

これまでの内容では, 命令は全てインタプリタに打ち込んできました.
全体が長い命令となる場合には, その方針を変えて, （テキストエディタを使って）
**スクリプト** や **モジュール** と呼ぶテキストファイルに書くことにします.
テキストエディタは好みのもの（Python 用の構文ハイライト機能があるものがいいでしょう）か
Python の科学ライブラリ一式に付属しているエディタ
（例えば, Python(x,y) に付属する Scite）を使いましょう.

.. For now, we have typed all instructions in the interpreter. For longer
.. sets of instructions we need to change tack and write the code in text
.. files (using a text editor), that we will call either **scripts** or
.. **modules**. Use your favorite text editor (provided it offers syntax
.. highlighting for Python), or the editor that comes with the Scientific
.. Python Suite you may be using (e.g., Scite with Python(x,y)). 

スクリプト
----------

.. Scripts
.. -------

最初の **スクリプト** を書いてみましょう, 
スクリプトは呼び出す度に連続した命令が実行されます.

.. Let us first write a **script**, that is a file with a sequence of
.. instructions that are executed each time the script is called.

命令は例えばインタプリタからコピーペーストしてもかまいません
（ただし, インデントの規則は忘れないように!）.
Python ファイルの拡張子は **.py** です.
**test.py** という名前のファイルに以下の行を書き写すか, コピーペーストしましょう.

::

    message = "Hello how are you?"
    for word in message.split():
        print word

.. Instructions may be e.g. copied-and-pasted from the interpreter
.. (but take care to respect indentation rules!). The extension for Python
.. files is **.py**. Write or copy-and-paste the following lines in a file
.. called **test.py** ::

..     message = "Hello how are you?"
..     for word in message.split():
..         print word

では, スクリプトをインタラクティブに IPython インタプリタ内部から実行してみましょう.
これは, 科学技術計算用のスクリプトの最も一般的使い方でしょう.

.. Let us now execute the script interactively, that is inside the Ipython
.. interpreter. This is maybe the most common use of scripts in scientific
.. computing. 

	* IPython でスクリプトを実行する構文は ``%run script.py`` です．
      例

    .. * in Ipython, the syntax to execute a script is ``%run
    ..   script.py``. For example, 

.. sourcecode:: ipython

    In [1]: %run test.py
    Hello
    how
    are
    you?

    In [2]: message
    Out[2]: 'Hello how are you?'

スクリプトが実行されるとスクリプト内の変数が定義され, インタプリタ内の名前空間で
アクセスできるようになります．

.. The script has been executed. Moreover the variables defined in the
.. script (such as ``message``) are now available inside the interpeter's
.. namespace.

他のインタプリタでもスクリプトを実行することができます
（例えば, デフォルトの Python インタプリタでは ``execfile`` 等）.

.. Other interpreters also offer the possibility to execute scripts (e.g.,
.. ``execfile`` in the plain Python interpreter, etc.).

また, ターミナル上（Linux/Mac のターミナル Windows のコマンドプロンプト）
で実行することで **独立したプログラム** としても実行できます.
例えば, test.py ファイルが置かれたディレクトリにいる場合,
端末でこれを実行します.

.. It is also possible In order to execute this script as a **standalone
.. program**, by executing the script inside a shell terminal (Linux/Mac
.. console or cmd Windows console). For example, if we are in the same
.. directory as the test.py file, we can execute this in a console:

.. sourcecode:: bash 

    epsilon:~/sandbox$ python test.py
    Hello
    how
    are
    you?


独立したスクリプトはコマンドライン引数をとることもできます.

.. Standalone scripts may also take command-line arguments

``file.py`` に::

    import sys
    print sys.argv

.. In ``file.py``::

..     import sys
..     print sys.argv

と書いておくと

::

    $ python file.py test arguments
    ['file.py', 'test', 'arguments']

.. note:: 

	オプションの構文解析は行いません. `optparse` モジュールを使って下さい.

..     Don't implement option parsing yourself. Use modules such as
..     `optparse`.


モジュールからオブジェクトをインポートする
------------------------------------------

.. Importing objects from modules
.. ------------------------------

.. sourcecode:: ipython

    In [1]: import os

    In [2]: os
    Out[2]: <module 'os' from '/usr/lib/python2.6/os.pyc'>

    In [3]: os.listdir('.')
    Out[3]:
    ['conf.py',
     'basic_types.rst',
     'control_flow.rst',
     'functions.rst',
     'python_language.rst',
     'reusing.rst',
     'file_io.rst',
     'exceptions.rst',
     'workflow.rst',
     'index.rst']

さらに：

.. And also:

.. sourcecode:: ipython

    In [4]: from os import listdir

略記でインポート：

.. Importing shorthands:

.. sourcecode:: ipython

    In [5]: import numpy as np

.. warning:: 

    ::
    
      from os import * 

    **してはいけません.**

    * コードが読みにくく, 理解しづらくなります： シンボルがどこから来たかわかりますか?

    * 名前と文脈から機能を予測することが不可能になります
      （ヒント： `os.name` は OS の名前）,
      さらに tab 補完の恩恵を受けるのに便利です.

    * 命名できる変数名が制限されます： `os.name` を `name` に上書きするなどすれば
	
    * モジュール間の名前の衝突を生みます

    * 未定義のシンボルを静的に調べることが不可能になります

.. .. warning:: 

..     ::
    
..       from os import * 

..     **Do not do it.**

..     * Makes the code harder to read and understand: where do symbols come 
..       from?

..     * Makes it impossible to guess the functionality by the context and
..       the name (hint: `os.name` is the name of the OS), and to profit
..       usefully from tab completion.

..     * Restricts the variable names you can use: `os.name` might override 
..       `name`, or vise-versa.

..     * Creates possible name clashes between modules.

..     * Makes the code impossible to statically check for undefined
..       symbols.

モジュールはこのように階層的にコードをまとめるのに有効です::

    >>> import numpy as np # data arrays
    >>> np.linspace(0, 10, 6)
    array([  0.,   2.,   4.,   6.,   8.,  10.])
    >>> import scipy # scientific computing

.. Modules are thus a good way to organize code in a hierarchical way. Actually,
.. all the scientific computing tools we are going to use are modules::

..     >>> import numpy as np # data arrays
..     >>> np.linspace(0, 10, 6)
..     array([  0.,   2.,   4.,   6.,   8.,  10.])
..     >>> import scipy # scientific computing

Python(x,y) の中のソフトウェア IPython(x,y) 起動時に以下のインポートを実行します::

    >>> import numpy	
    >>> import numpy as np
    >>> from pylab import *
    >>> import scipy

つまり, これらのモジュールの再インポートは不要です.

.. In Python(x,y) software, Ipython(x,y) execute the following imports at startup::


..     >>> import numpy	
..     >>> import numpy as np
..     >>> from pylab import *
..     >>> import scipy

.. and it is not necessary to re-import these modules.

モジュールを作る
----------------

.. Creating modules
.. -----------------

いくつかのオブジェクト（変数,関数,クラス）が定義され, 何度も再利用したくなるような
より大きな, まとまったプログラム（単純なスクリプトに比べて）を書きたい場合,
自分自身の **モジュール** を作成します.

`demo.py` に書かれた `demo` モジュールを作ってみましょう：

.. If we want to write larger and better organized programs (compared to
.. simple scripts), where some objects are defined, (variables, functions,
.. classes) and that we want to reuse several times, we have to create our
.. own **modules**. 

.. Let us create a module `demo` contained in the file `demo.py`:

   .. literalinclude:: demo.py

このファイルには, 私達が定義した二つの関数 `print_a` と `print_b` があります.
インタプリタから `print_a` 関数を呼び出したい仮定します.
ファイルをスクリプトとして実行することもできますが, `print_a` 関数にアクセスしたいだけなので,
**モジュールとしてインポート** しましょう.
構文は以下です.

.. In this file, we defined two functions `print_a` and `print_b`. Suppose
.. we want to call the `print_a` function from the interpreter. We could
.. execute the file as a script, but since we just want to have access to
.. the function `print_a`, we are rather going to **import it as a module**.
.. The syntax is as follows.

.. sourcecode:: ipython

    In [1]: import demo


    In [2]: demo.print_a()
    a

    In [3]: demo.print_b()
    b

モジュールをインポートすることで, そのオブジェクトに ``module.object`` 構文でアクセスすることができます.
オブジェクトの名前の前にモジュールの名前を忘れないで下さい, そうしないと Python は命令を理解してくれません.

.. Importing the module gives access to its objects, using the
.. ``module.object`` syntax. Don't forget to put the module's name before the
.. object's name, otherwise Python won't recognize the instruction.


内観

.. Introspection

.. sourcecode:: ipython

    In [4]: demo?
    Type:               module
    Base Class: <type 'module'>
    String Form:        <module 'demo' from 'demo.py'>
    Namespace:  Interactive
    File:               /home/varoquau/Projects/Python_talks/scipy_2009_tutorial/source/demo.py
    Docstring:
        A demo module.


    In [5]: who
    demo

    In [6]: whos
    Variable   Type      Data/Info
    ------------------------------
    demo       module    <module 'demo' from 'demo.py'>

    In [7]: dir(demo)
    Out[7]: 
    ['__builtins__',
    '__doc__',
    '__file__',
    '__name__',
    '__package__',
    'c',
    'd',
    'print_a',
    'print_b']
 

    In [8]: demo.
    demo.__builtins__      demo.__init__          demo.__str__
    demo.__class__         demo.__name__          demo.__subclasshook__
    demo.__delattr__       demo.__new__           demo.c
    demo.__dict__          demo.__package__       demo.d
    demo.__doc__           demo.__reduce__        demo.print_a
    demo.__file__          demo.__reduce_ex__     demo.print_b
    demo.__format__        demo.__repr__          demo.py
    demo.__getattribute__  demo.__setattr__       demo.pyc
    demo.__hash__          demo.__sizeof__        

main の名前空間にオブジェクトをインポートする

.. Importing objects from modules into the main namespace

.. sourcecode:: ipython

    In [9]: from demo import print_a, print_b

    In [10]: whos
    Variable   Type        Data/Info
    --------------------------------
    demo       module      <module 'demo' from 'demo.py'>
    print_a    function    <function print_a at 0xb7421534>
    print_b    function    <function print_b at 0xb74214c4>

    In [11]: print_a()
    a

.. warning:: 

	**モジュールのキャッシュ**

	モジュールはキャッシュされます：`demo.py` を変更して
	変更前のセッションで再インポートした場合, 変更前のモジュールがインポートされます.

	解決法：

    .. **Module caching**

    ..  Modules are cached: if you modify `demo.py` and re-import it in the
    ..  old session, you will get the old one.

    .. Solution:

    .. sourcecode :: ipython

        In [10]: reload(demo)


'__main__' とモジュールのロード
-------------------------------

.. '__main__' and module loading
.. ------------------------------

ファイル `demo2.py` ：

.. File `demo2.py`:

.. literalinclude:: demo2.py

インポートする：

.. Importing it:

.. sourcecode:: ipython

    In [11]: import demo2
    b

    In [12]: import demo2

実行する：

.. Running it:

.. sourcecode:: ipython

    In [13]: %run demo2
    b
    a


スクリプトそれともモジュール? ソースコートのまとめ方
----------------------------------------------------

.. Scripts or modules? How to organize your code
.. ---------------------------------------------

.. Note:: 確かな経験則

    * コードの再利用性を高めるために, 
      多く呼び出される命令の集まりは関数の内部に書くべきです.

    * いくつかのスクリプトから呼び出される関数（もしくはソースコードの一部分）はモジュールの中に書くべきです,
      そうすると異なるスクリプトから呼び出されるのはそのモジュールだけになります
      （異なるスクリプトに関数をコピーペーストするのはやめましょう!）

.. .. Note:: Rule of thumb

..     * Sets of instructions that are called several times should be
..       written inside **functions** for better code reusability.

..     * Functions (or other bits of code) that are called from several
..       scripts should be written inside a **module**, so that only the
..       module is imported in the different scripts (do not copy-and-paste
..       your functions in the different scripts!).

.. Note:: **離れたディレクトリからモジュールをインポートするには?**

	主に OS によって変わりますが, 多くの方法があります.
	``import mymodule`` 文が実行されると, 
 	`mymodule` があるディレクトリのリストから探されます.
	このは環境変数 **PYTHONPATH** で指定されたディレクトリリストと
	インストール場所に依存したデフォルトのパス
	（例えば, `/usr/lib/python` ） を含みます.

	その Python が探すディレクトリリストは `sys.path` 変数で与えられます

.. .. Note:: **How to import a module from a remote directory?**

..     ..

..     Many solutions exist, depending mainly on your operating system. When
..     the ``import mymodule`` statement is executed, the module `mymodule`
..     is searched in a given list of directories. This list includes a list
..     of installation-dependent default path (e.g., `/usr/lib/python`) as
..     well as the list of directories specified by the environment variable
..     **PYTHONPATH**. 

..     The list of directories searched by Python is given by the `sys.path`
..     variable 

    .. sourcecode:: ipython	

        In [1]: import sys
        
        In [2]: sys.path
        Out[2]: 
        ['',
         '/usr/bin',
         '/usr/local/include/enthought.traits-1.1.0',
         '/usr/lib/python2.6',
         '/usr/lib/python2.6/plat-linux2',
         '/usr/lib/python2.6/lib-tk',
         '/usr/lib/python2.6/lib-old',
         '/usr/lib/python2.6/lib-dynload',
         '/usr/lib/python2.6/dist-packages',
         '/usr/lib/pymodules/python2.6',
         '/usr/lib/pymodules/python2.6/gtk-2.0',
         '/usr/lib/python2.6/dist-packages/wx-2.8-gtk2-unicode',
         '/usr/local/lib/python2.6/dist-packages',
         '/usr/lib/python2.6/dist-packages',
         '/usr/lib/pymodules/python2.6/IPython/Extensions',
         u'/home/gouillar/.ipython']
     
	モジュールはこの検索パスの中に置かれていないといけません, つまり以下の方法を取れます：

	* 既に定義された検索パスの中（例えば '/usr/local/lib/python2.6/dist-packages） に
	  モジュールを書く. （Linux では）シンボリックリンクを使えば他の場所に置くことができます.

	* **PYTHONPATH** 環境変数を変更して, ユーザが定義したモジュールを含むディレクトリを含むようにする.
	  Linux/Unix では以下の行をシェルの起動ファイル（例えば /etc/profile .profile）に加えましょう.

    .. Modules must be located in the search path, therefore you can:

    .. * write your own modules within directories already defined in the
    ..   search path (e.g. '/usr/local/lib/python2.6/dist-packages'). You
    ..   may use symbolic links (on Linux) to keep the code somewhere else.

    .. * modify the environment variable **PYTHONPATH** to include the
    ..   directories containing the user-defined modules. On Linux/Unix, add
    ..   the following line to a file read by the shell at startup (e.g.
    ..   /etc/profile, .profile)

    ::

	export PYTHONPATH=$PYTHONPATH:/home/emma/user_defined_modules

	Windows では, http://support.microsoft.com/kb/310519 で環境変数の扱い方が説明されています.

    .. On Windows, http://support.microsoft.com/kb/310519 explains how to
    .. handle environment variables.

	* または, Python スクリプトの中で `sys.path` 変数を変更する

    .. * or modify the `sys.path` variable itself within a Python script.

    ::

	import sys
	new_path = '/home/emma/user_defined_modules'
	if new_path not in sys.path:
	    sys.path.append(new_path)

	この方法は （ユーザによって変わるパスを設定するため）
    ソースコードの可搬性が悪くなること, 
	ディレクトリからモジュールをインポートする度 sys.path を変更しなければならないこと, 
	という二点から変更が少なくすむ, 頑強な方法とはいえません.

    .. This method is not very robust, however, because it makes the code
    .. less portable (user-dependent path) and because you have to add the
    .. directory to your sys.path each time you want to import from a module in
    .. this directory.

モジュールに関するさらなる情報は http://docs.python.org/tutorial/modules.html [*]_ を見てください.

.. See http://docs.python.org/tutorial/modules.html for more information
.. about modules.

パッケージ
----------

.. Packages
.. --------

多くのモジュールを含むディレクトリは **パッケージ** と呼ばれます.
パッケージはサブモジュール（これもサブモジュールを持ちます）を含むモジュールです.
`__init__.py` と呼ばれる特別なファイルがそのディレクトリがパッケージであること,
どのモジュールがインポートできるかを Python に教えます.

.. A directory that contains many modules is called a **package**. A package
.. is a module with submodules (which can have submodules themselves, etc.).
.. A special file called `__init__.py` (which may be empty) tells Python
.. that the directory is a Python package, from which modules can be
.. imported.

::

    sd-2116 /usr/lib/python2.6/dist-packages/scipy $ ls
    [17:07]
    cluster/        io/          README.txt@     stsci/
    __config__.py@  LATEST.txt@  setup.py@       __svn_version__.py@
    __config__.pyc  lib/         setup.pyc       __svn_version__.pyc
    constants/      linalg/      setupscons.py@  THANKS.txt@
    fftpack/        linsolve/    setupscons.pyc  TOCHANGE.txt@
    __init__.py@    maxentropy/  signal/         version.py@
    __init__.pyc    misc/        sparse/         version.pyc
    INSTALL.txt@    ndimage/     spatial/        weave/
    integrate/      odr/         special/
    interpolate/    optimize/    stats/
    sd-2116 /usr/lib/python2.6/dist-packages/scipy $ cd ndimage
    [17:07]
    
    sd-2116 /usr/lib/python2.6/dist-packages/scipy/ndimage $ ls
    [17:07]
    doccer.py@   fourier.pyc   interpolation.py@  morphology.pyc   setup.pyc
    doccer.pyc   info.py@      interpolation.pyc  _nd_image.so
    setupscons.py@
    filters.py@  info.pyc      measurements.py@   _ni_support.py@
    setupscons.pyc
    filters.pyc  __init__.py@  measurements.pyc   _ni_support.pyc  tests/
    fourier.py@  __init__.pyc  morphology.py@     setup.py@

IPython から：

.. From Ipython:

.. sourcecode:: ipython

    In [1]: import scipy

    In [2]: scipy.__file__
    Out[2]: '/usr/lib/python2.6/dist-packages/scipy/__init__.pyc'

    In [3]: import scipy.version

    In [4]: scipy.version.version
    Out[4]: '0.7.0'
    
    In [5]: import scipy.ndimage.morphology

    In [6]: from scipy.ndimage import morphology

    In [17]: morphology.binary_dilation?
    Type:	    function
    Base Class: <type 'function'>
    String Form:	<function binary_dilation at 0x9bedd84>
    Namespace:  Interactive
    File:	    /usr/lib/python2.6/dist-packages/scipy/ndimage/morphology.py
    Definition: morphology.binary_dilation(input, structure=None,
    iterations=1, mask=None, output=None, border_value=0, origin=0,
    brute_force=False)
    Docstring:
        Multi-dimensional binary dilation with the given structure.
        
        An output array can optionally be provided. The origin parameter
        controls the placement of the filter. If no structuring element is
        provided an element is generated with a squared connectivity equal
        to one. The dilation operation is repeated iterations times.  If
        iterations is less than 1, the dilation is repeated until the
        result does not change anymore.  If a mask is given, only those
        elements with a true value at the corresponding mask element are
        modified at each iteration.



よい習慣
--------

.. Good practices
.. --------------

.. Note:: **よい習慣**

    * **インデント：選択の余地なし!**

    Python ではインデントは強制されます.
    どのコマンドブロックもコロンに続いて,
    前のコロンの行より一段インデントが深くなります.
    なので ``def f():`` や ``while:`` の後にインデントしなければいけません.
    この論理ブロックが終ったときには, インデントが浅くなります
    （そして新しいブロックに入るとまた深くなります）.

    インデントを厳格に扱うことは他の言語で論理ブロックを示す文字
    ``{`` や ``;`` を取り除く効果があります.
    不適切なインデントはこのようなエラーを起こします.

    .. sourcecode:: ipython

        ------------------------------------------------------------
        IndentationError: unexpected indent (test.py, line 2)

    はじめはインデントに少し混乱するかもしれませんが, はっきりとインデントと
    余計な文字列がないことによって他の言語と比べて読みやすい, 
    とてもいいソースコードになります.

    * **インデントの深さ**

    テキストエディタでは, インデントのスペースの数を任意の正の数(1, 2, 3, 4, ...) にできるかもしれません.
    しかし, **インデントはスペース4つ分** がよい習慣とされています.
    エディタの設定で ``Tab`` キーをインデントのための4文字分のスペースに割り当てることができるでしょう.
    Python(x,y) の ``Scite`` エディタは既にそう設定されています.

    * **スタイルガイド**

    **長い行** ： 80文字以上に渡る長い行は書いてはいけません.
    長い行は ``\`` 文字で分割することができます::

        >>> long_line = "Here is a very very long line \
        ... that we break in two parts."
 
    **スペース**

    うまくスペースを入れてソースコードを書きましょう：カンマの後や算術演算子の周りに空白を入れましょう::

        >>> a = 1 # yes
        >>> a=1 # too cramped
 
    「きれいな」ソースコードを書くための
    いくつかの規則が `Style Guide for Python Code <http://www.python.org/dev/peps/pep-0008>`_ [*]_
    に与えられています（みんなで同じ規則を使う, という意味でも重要です）.

    * オブジェクトには **意味のある名前** をつけましょう

.. .. Note:: **Good practices**

    .. * **Indentation: no choice!**

    .. Indenting is compulsory in Python. Every commands block following a
    .. colon bears an additional indentation level with respect to the
    .. previous line with a colon. One must therefore indent after 
    .. ``def f():`` or ``while:``. At the end of such logical blocks, one
    .. decreases the indentation depth (and re-increases it if a new block
    .. is entered, etc.)

    .. Strict respect of indentation is the price to pay for getting rid of
    .. ``{`` or ``;`` characters that delineate logical blocks in other
    .. languages. Improper indentation leads to errors such as

    .. .. sourcecode:: ipython

    ..     ------------------------------------------------------------
    ..     IndentationError: unexpected indent (test.py, line 2)

    .. All this indentation business can be a bit confusing in the
    .. beginning. However, with the clear indentation, and in the absence of
    .. extra characters, the resulting code is very nice to read compared to
    .. other languages.

    .. * **Indentation depth**: 

    .. Inside your text editor, you may choose to
    .. indent with any positive number of spaces (1, 2, 3, 4, ...). However,
    .. it is considered good practice to **indent with 4 spaces**. You may
    .. configure your editor to map the ``Tab`` key to a 4-space
    .. indentation. In Python(x,y), the editor ``Scite`` is already
    .. configured this way.        

    .. * **Style guidelines**

    .. **Long lines**: you should not write very long lines that span over more
    .. than (e.g.) 80 characters. Long lines can be broken with the ``\``
    .. character ::

    ..     >>> long_line = "Here is a very very long line \
    ..     ... that we break in two parts."

    .. **Spaces**

    .. Write well-spaced code: put whitespaces after commas, around arithmetic
    .. operators, etc.:: 

    ..     >>> a = 1 # yes
    ..     >>> a=1 # too cramped

    .. A certain number of rules
    .. for writing "beautiful" code (and more importantly using the same
    .. conventions as anybody else!) are given in the `Style Guide for Python
    .. Code <http://www.python.org/dev/peps/pep-0008>`_.

    .. * Use **meaningful** object **names**

.. rubric:: 脚注

.. [*] 日本語訳 http://www.python.jp/doc/release/tutorial/modules.html
.. [*] 日本語訳 http://oldriver.org/python/pep-0008j.html
