NumPy：数値データの作成と操作
================================================

.. NumPy: creating and manipulating numerical data 
.. ================================================

.. only:: latex

    :authors: Emmanuelle Gouillart, Didrik Pinte, Gaël Varoquaux

.. topic:: 配列：科学技術計算の基本的な道具

    .. image:: simple_histo.jpg
       :align: right 

    **並んだ離散的なデータ** の頻繁な操作：

    * 実験やシミュレーションでの離散化された時間

    * 測定機器に記録された信号

    * 画像のピクセル

    **Numpy** モジュールは以下を可能にします.
    
    * 上のようなデータの集まりの作成を1度ですませる
    
    * データ配列のバッチ処理を実現（要素に対するループは不要）
    
    データ配列 := ``numpy.ndarray``

.. .. topic:: The array: the basic tool for scientific computing

..     .. image:: simple_histo.jpg
..        :align: right 

..     Frequent manipulation of **discrete sorted datasets** :
 
..     * discretized time of an experiment/simulation

..     * signal recorded by a measurement device

..     * pixels of an image, ...

..     The **Numpy** module allows to 

..     * create such datasets in one shot

..     * realize batch operations on data arrays (no loops on their items)

..     Data arrays := ``numpy.ndarray``

Numpy データ配列作成
--------------------

.. Creating NumPy data arrays
.. --------------------------

入門によさそうな短い例

.. A small introductory example::

::

    >>> import numpy as np
    >>> a = np.array([0, 1, 2])
    >>> a
    array([0, 1, 2])
    >>> print a
    [0 1 2]
    >>> b = np.array([[0., 1.], [2., 3.]])
    >>> b
    array([[ 0.,  1.],
           [ 2.,  3.]])

実際には要素を1つ1つ入力することは少ないでしょう.

    * 1つとばしの値::

        >>> import numpy as np
        >>> a = np.arange(10) # de 0 a n-1
        >>> a
        array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        >>> b = np.arange(1., 9., 2) # syntax : start, end, step
        >>> b
        array([ 1.,  3.,  5.,  7.])


      または点の数を指定::

        >>> c = np.linspace(0, 1, 6)
        >>> c
        array([ 0. ,  0.2,  0.4,  0.6,  0.8,  1. ])
        >>> d = np.linspace(0, 1, 5, endpoint=False)
        >>> d
        array([ 0. ,  0.2,  0.4,  0.6,  0.8])


    * よく使う配列のコンストラクタ::

        >>> a = np.ones((3,3))
        >>> a
        array([[ 1.,  1.,  1.],
               [ 1.,  1.,  1.],
               [ 1.,  1.,  1.]])
        >>> a.dtype
        dtype('float64')
        >>> b = np.ones(5, dtype=np.int)
        >>> b
        array([1, 1, 1, 1, 1])
        >>> c = np.zeros((2,2))
        >>> c
        array([[ 0.,  0.],
               [ 0.,  0.]])
        >>> d = np.eye(3)
        >>> d
        array([[ 1.,  0.,  0.],
               [ 0.,  1.,  0.],
               [ 0.,  0.,  1.]])

.. In practice, we rarely enter items one by one...

..     * Evenly spaced values::

..         >>> import numpy as np
..         >>> a = np.arange(10) # de 0 a n-1
..         >>> a
..         array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
..         >>> b = np.arange(1., 9., 2) # syntax : start, end, step
..         >>> b
..         array([ 1.,  3.,  5.,  7.])

..       or by specifying the number of points::

..         >>> c = np.linspace(0, 1, 6)
..         >>> c
..         array([ 0. ,  0.2,  0.4,  0.6,  0.8,  1. ])
..         >>> d = np.linspace(0, 1, 5, endpoint=False)
..         >>> d
..         array([ 0. ,  0.2,  0.4,  0.6,  0.8])

..     * Constructors for common arrays::

..         >>> a = np.ones((3,3))
..         >>> a
..         array([[ 1.,  1.,  1.],
..                [ 1.,  1.,  1.],
..                [ 1.,  1.,  1.]])
..         >>> a.dtype
..         dtype('float64')
..         >>> b = np.ones(5, dtype=np.int)
..         >>> b
..         array([1, 1, 1, 1, 1])
..         >>> c = np.zeros((2,2))
..         >>> c
..         array([[ 0.,  0.],
..                [ 0.,  0.]])
..         >>> d = np.eye(3)
..         >>> d
..         array([[ 1.,  0.,  0.],
..                [ 0.,  1.,  0.],
..                [ 0.,  0.,  1.]])


データのグラフィカルな表示：matplotlib と Mayavi
------------------------------------------------

.. Graphical data representation : matplotlib and Mayavi
.. -----------------------------------------------------

これでデータ配列を学びました, 次は可視化です.
**Matplotlib** は2次元の作図パッケージです.
関数は以下のようにしてインポートします.

.. Now that we have our first data arrays, we are going to visualize them.
.. **Matplotlib** is a 2D plotting package. We can import its functions as below::

::

    >>> import pylab
    >>> # or
    >>> from pylab import * # imports everything in the namespace

python(x,y) に付属する IPython か（Linux で） ``ipython -pylab`` として
IPython を起動すると ``from pylab import *`` を行うことなく
全ての pylab の関数やオブジェクトがインポートされます.
このチュートリアルでは ``from pylab import *`` か
``ipython -pylab`` を行なっているものとして扱います,
その結果として ``pylab.function()`` と書かずに直接 ``function`` と書きます.
    
.. If you launched Ipython with python(x,y), or with ``ipython
.. -pylab`` (under Linux), all the functions/objects of pylab are already
.. imported, without needing ``from pylab import *``. In the remainder of this
.. tutorial, we assume you have already run ``from pylab import *`` or ``ipython
.. -pylab``: as a consequence, we won't write ``pylab.function()`` but directly
.. ``function``.

**1次元の曲線の描画**

.. **1D curve plotting**

.. sourcecode:: ipython

    In [6]: a = np.arange(20)
    In [7]: plot(a, a**2) # line plot
    Out[7]: [<matplotlib.lines.Line2D object at 0x95abd0c>]
    In [8]: plot(a, a**2, 'o') # dotted plot
    Out[8]: [<matplotlib.lines.Line2D object at 0x95b1c8c>]
    In [9]: clf() # clear figure
    In [10]: loglog(a, a**2)
    Out[10]: [<matplotlib.lines.Line2D object at 0x95abf6c>]
    In [11]: xlabel('x') # a bit too small
    Out[11]: <matplotlib.text.Text object at 0x98923ec>
    In [12]: xlabel('x', fontsize=26) # bigger
    Out[12]: <matplotlib.text.Text object at 0x98923ec>
    In [13]: ylabel('y')
    Out[13]: <matplotlib.text.Text object at 0x9892b8c>
    In [14]: grid()
    In [15]: axvline(2)
    Out[15]: <matplotlib.lines.Line2D object at 0x9b633cc>

.. image:: plot.png
   :align: center 
   :scale: 80
   

**2次元配列** （画像のような）

.. **2D arrays** (such as images)   

.. sourcecode:: ipython

    In [48]: # 30x30 array with random floats btw 0 and 1
    In [49]: image = np.random.rand(30,30) 
    In [50]: imshow(image)
    Out[50]: <matplotlib.image.AxesImage object at 0x9e954ac>
    In [51]: gray()
    In [52]: hot()
    In [53]: imshow(image, cmap=cm.gray)
    Out[53]: <matplotlib.image.AxesImage object at 0xa23972c>
    In [54]: axis('off') # we remove ticks and labels    

.. image:: imshow.png
   :align: center
   :scale: 80

matplotlib には他にも多くの機能があります：色の選択, マーカーのサイズ, 
LaTeX のフォント, 図の取り込み, 頻度分布等.

.. There are many other features in matplotlib: color choice, marker size,
.. latex font, inclusions within figures, histograms, etc.

より多くの情報は：

    * matplotlib documentation
      http://matplotlib.sourceforge.net/contents.html

    * an example gallery with corresponding sourcecode
      http://matplotlib.sourceforge.net/gallery.html

.. To go further :

    * matplotlib documentation
      http://matplotlib.sourceforge.net/contents.html

    * an example gallery with corresponding sourcecode
      http://matplotlib.sourceforge.net/gallery.html

**3次元作図**

.. **3D plotting**

3次元可視化のためには **Mayavi** パッケージを使います.
**ipython -pylab -wthread** のオプションで **iPython を再起動** して速やかに例を実行しましょう：

.. For 3D visualization, we use another package: **Mayavi**. A quick example:
.. start with **relaunching iPython** with these options:
.. **ipython -pylab -wthread**

.. sourcecode:: ipython

    In [59]: from enthought.mayavi import mlab
    In [60]: mlab.figure()
    get fences failed: -1
    param: 6, val: 0
    Out[60]: <enthought.mayavi.core.scene.Scene object at 0xcb2677c>
    In [61]: mlab.surf(image)
    Out[61]: <enthought.mayavi.modules.surface.Surface object at 0xd0862fc>
    In [62]: mlab.axes()
    Out[62]: <enthought.mayavi.modules.axes.Axes object at 0xd07892c>

.. image:: surf.png
   :align: center
   :scale: 60

mayavi/mlab のウィンドウは対話的に開きます：ドラッグして画像を回転する, マウスホイールで拡大等.

.. The mayavi/mlab window that opens is interactive : by clicking on the left mouse button
.. you can rotate the image, zoom with the mouse wheel, etc.

.. image:: potential.jpg
   :align: center
   :scale: 60

Mayavi についての詳しい情報は：

.. For more information on Mayavi :

http://code.enthought.com/projects/mayavi/docs/development/html/mayavi/index.html

インデクス指定
--------------

.. indexing 
.. --------

配列の要素は他の python のシーケンス (``list``, ``tuple``) と同じようにアクセスできます.

.. The items of an array can be accessed the same way as other Python sequences
.. (``list``, ``tuple``) ::

    >>> a = np.arange(10)
    >>> a
    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    >>> a[0], a[2], a[-1]
    (0, 2, 9)

警告! 他の Python のシーケンス（さらには C/C++ ）と同様にインデクスは 0 から始まります.
Fortran や Matlab ではインデクスは 1 から始まります.

.. Warning! Indexes begin at 0, like other Python sequences (and C/C++).
.. In Fortran or Matlab, indexes begin with 1.

.. For multidimensional arrays, indexes are tuples of integers::

多次元配列に対しては, インデクスは整数のタプルとなります
::

    >>> a = np.diag(np.arange(5))
    >>> a
    array([[0, 0, 0, 0, 0],
           [0, 1, 0, 0, 0],
           [0, 0, 2, 0, 0],
           [0, 0, 0, 3, 0],
           [0, 0, 0, 0, 4]])
    >>> a[1,1]
    1
    >>> a[2,1] = 10 # third line, second column
    >>> a
    array([[ 0,  0,  0,  0,  0],
           [ 0,  1,  0,  0,  0],
           [ 0, 10,  2,  0,  0],
           [ 0,  0,  0,  3,  0],
           [ 0,  0,  0,  0,  4]])
    >>> a[1]
    array([0, 1, 0, 0, 0])

以下のことに注意しましょう：

 * 2次元では次元の最初が行に対応し, 2番目が列に対応します.
 * 2次元以上の配列 ``a`` に対しては `a[0]` は未指定の次元の全ての要素として解釈されます.

.. Note that:

.. * In 2D, the first dimension corresponds to lines, the second to columns.
.. * for an array ``a`` with more than one dimension,`a[0]` is interpreted by
..   taking all elements in the unspecified dimensions.

スライス
--------

.. Slicing
.. -------

インデクス指定のように Python におけるシーケンスのスライスと似ています

.. Like indexing, it's similar to Python sequences slicing::

::

    >>> a = np.arange(10)
    >>> a
    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    >>> a[2:9:3] # [start:end:step]
    array([2, 5, 8])

最後のインデクスは含まれないことに注意!

.. Note that the last index is not included!::

::

    >>> a[:4]
    array([0, 1, 2, 3])

``start:end:stop`` はインデクスの集まりを表わす ``slice`` オブジェクトです.
``slice`` は明示的に作ることができます

.. ``start:end:step`` is a ``slice`` object which represents the set of indexes
.. ``range(start, end, step)``. A ``slice`` can be explicitly created::

::

    >>> sl = slice(1, 9, 2)
    >>> a = np.arange(10)
    >>> b = 2*a + 1
    >>> a, b
    (array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), array([ 1,  3,  5,  7,  9, 11, 13, 15, 17, 19]))
    >>> a[sl], b[sl]
    (array([1, 3, 5, 7]), array([ 3,  7, 11, 15]))

slice の3つの要素は必須ではありません：デフォルトでは `start` は0で
`end` は最後で `step` は 1 です

.. All three slice components are not required: by default, `start` is 0, `end` is the
.. last and `step` is 1::

::

    >>> a[1:3]
    array([1, 2])
    >>> a[::2]
    array([0, 2, 4, 6, 8])
    >>> a[3:]
    array([3, 4, 5, 6, 7, 8, 9])

もちろん, 多次元配列に対しても使えます

.. Of course, it works with multidimensional arrays::

::

    >>> a = np.eye(5)
    >>> a
    array([[ 1.,  0.,  0.,  0.,  0.],
           [ 0.,  1.,  0.,  0.,  0.],
           [ 0.,  0.,  1.,  0.,  0.],
           [ 0.,  0.,  0.,  1.,  0.],
           [ 0.,  0.,  0.,  0.,  1.]])
    >>> a[2:4,:3] #3rd and 4th lines, 3 first columns
    array([[ 0.,  0.,  1.],
           [ 0.,  0.,  0.]])

スライスによって指定した全ての要素を簡単に変更できます

.. All elements specified by a slice can be easily modified::

::

    >>> a[:3,:3] = 4
    >>> a
    array([[ 4.,  4.,  4.,  0.,  0.],
           [ 4.,  4.,  4.,  0.,  0.],
           [ 4.,  4.,  4.,  0.,  0.],
           [ 0.,  0.,  0.,  1.,  0.],
           [ 0.,  0.,  0.,  0.,  1.]])

Numpy のインデクス指定, スライスを簡単に図でまとめると...

.. A small illustrated summary of Numpy indexing and slicing...

.. image:: numpy_indexing.png
   :align: center

スライス操作は元の配列の **ビュー (view)** を作ります, 
**ビュー** は単なる配列のデータへのアクセス法です.
なので, 元の配列はメモリ上でコピーされません.
**ビューが変更されると元の配列はこのように変更されます**

.. A slicing operation creates a **view** on the original array, which is just a way of
.. accessing array data. Thus the original array is not copied in memory. *When
.. modifying the view, the original array is modified as well**::

::

    >>> a = np.arange(10)
    >>> a 
    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    >>> b = a[::2]; b
    array([0, 2, 4, 6, 8])
    >>> b[0] = 12
    >>> b
    array([12,  2,  4,  6,  8])
    >>> a # a a été modifié aussi !
    array([12,  1,  2,  3,  4,  5,  6,  7,  8,  9])

この挙動をはじめて見たらおどろくでしょう...
しかし, これによって多くのメモリが節約されるのです.

.. This behaviour can be surprising at first sight... but it allows to save a lot
.. of memory.


配列のシェイプを操作する
------------------------

.. Manipulating the shape of arrays
.. ---------------------------------

配列のシェイプは ``ndarray.shape`` メソッドで取得できます.
このメソッドは配列の次元をタプルで返します.

.. th shape of an array can be retrieved with the ``ndarray.shape`` method which
.. returns a tuple with the dimensions of the array::

::

    >>> a = np.arange(10)
    >>> a.shape
    (10,)
    >>> b = np.ones((3,4))
    >>> b.shape
    (3, 4)
    >>> b.shape[0] # the shape tuple elements can be accessed
    3
    >>> # an other way of doing the same
    >>> np.shape(b)
    (3, 4)

さらに1番目の次元の長さは ``np.alen``
（リストに対する ``len`` からのアナロジー）
で求めることができます,
そして全要素の数は ``ndarray.size`` で取得できます.

.. Moreover, the length of the first dimension can be queried with ``np.alen`` (by
.. analogy with ``len`` for a list) and the total number of elements with
.. ``ndarray.size``::

::

    >>> np.alen(b)
    3
    >>> b.size
    12

いくつかの Numpy の関数は配列からシェイプの異なる配列を作れます.

.. Several NumPy functions allow to create an array with a different shape, from
.. another array::

::

    >>> a = np.arange(36)
    >>> b = a.reshape((6, 6))
    >>> b
    array([[ 0,  1,  2,  3,  4,  5],
           [ 6,  7,  8,  9, 10, 11],
           [12, 13, 14, 15, 16, 17],
           [18, 19, 20, 21, 22, 23],
           [24, 25, 26, 27, 28, 29],
           [30, 31, 32, 33, 34, 35]])

``ndarray.reshape`` はコピーではなく, ビューを返します

.. ``ndarray.reshape`` returns a view, not a copy::

::

    >>> b[0,0] = 10
    >>> a 
    array([10,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
           17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
           34, 35])

異なる要素数の配列も ``ndarray.resize`` で作ることができます

.. An array with a different number of elements can also be created with ``ndarray.resize``::

::

    >>> a = np.arange(36)
    >>> a.resize((4,2))
    >>> a
    array([[0, 1],
           [2, 3],
           [4, 5],
           [6, 7]])
    >>> b = np.arange(4)
    >>> b.resize(3, 2)
    >>> b
    array([[0, 1],
           [2, 3],
           [0, 0]])

小さな配列をタイル張りのように繰り返してできる大きな配列は

.. A large array can be tiled with a smaller one::

::

    >>> a = np.arange(4).reshape((2,2))
    >>> a
    array([[0, 1],
           [2, 3]])
    >>> np.tile(a, (2,3))
    array([[0, 1, 0, 1, 0, 1],
           [2, 3, 2, 3, 2, 3],
           [0, 1, 0, 1, 0, 1],
           [2, 3, 2, 3, 2, 3]])

練習問題：単純な配列作成
------------------------

.. Exercises : some simple array creations
.. ---------------------------------------

いろいろなコンストラクタ, インデクス指定, スライス, 単純な演算 (+/-/x/:) を使って
いろいろなパターンの大きな配列を作ることができます.

.. By using miscellaneous constructors, indexing, slicing, and simple operations
.. (+/-/x/:), large arrays with various patterns can be created.

**例** ： この配列を作成しましょう

.. **Example** : create this array::

::

    [[ 0  1  2  3  4]
     [ 5  6  7  8  9]
     [10 11 12 13  0]
     [15 16 17 18 19]
     [20 21 22 23 24]]

**解答**

.. **Solution**

::

    >>> a = np.arange(25).reshape((5,5))
    >>> a[2, 4] = 0

**練習問題** ：以下の配列を最も単純な解答で作成せよ.

.. **Exercises** : Create the following array with the simplest solution::

::

    [[ 1.  1.  1.  1.]
     [ 1.  1.  1.  1.]
     [ 1.  1.  1.  2.]
     [ 1.  6.  1.  1.]]

    [[0 0 0 0 0]
     [2 0 0 0 0]
     [0 3 0 0 0]
     [0 0 4 0 0]
     [0 0 0 5 0]
     [0 0 0 0 6]]

実際のデータ：ファイルを読み書きする
------------------------------------

.. Real data: read/write arrays from/to files
.. ------------------------------------------

たいていの場合, 実験やシミュレーションで得られた結果はファイルに書き出されます.
Numpy の配列として処理するためこれらの結果を Python に読み込まれなければいけません.
また, 結果をファイルに保存する必要もあるでしょう.

.. Often, our experiments or simulations write some results in files. These results
.. must then be loaded in Python as NumPy arrays to be able to manipulate them. We
.. also need to save some arrays into files.

**正しいフォルダに移動する**

.. **Going to the right folder**


..
    >>> import os, os.path 
    >>> os.chdir('/home/gouillar/sandbox')

フォルダの階層を移動する： 

    * iPython のコマンドを使いましょう： ``cd``, ``pwd``, tab-補完

      .. sourcecode:: ipython
       
        In [1]: mkdir python_scripts
       
        In [2]: cd python_scripts/ 
        /home/gouillar/python_scripts
       
        In [3]: pwd
        Out[3]: '/home/gouillar/python_scripts'
       
        In [4]: ls
       
        In [5]: np.savetxt('integers.txt', np.arange(10))
       
        In [6]: ls
        integers.txt

    * os（OS のルーチン）と os.path（パスの管理）モジュール

      ::
   
        >>> import os, os.path  
        >>> current_dir = os.getcwd()
        >>> current_dir
        '/home/gouillar/sandbox'
        >>> data_dir = os.path.join(current_dir, 'data')
        >>> data_dir
        '/home/gouillar/sandbox/data'
        >>> if not(os.path.exists(data_dir)):
        ...     os.mkdir('data')
        ...     print "created 'data' folder"
        ...     
        >>> os.chdir(data_dir) # or in Ipython : cd data

.. To move in a folder hierarchy:

..     * use the iPython commands: ``cd``, ``pwd``,
..       tab-completion.

.. .. sourcecode:: ipython
 
..   In [1]: mkdir python_scripts
 
..   In [2]: cd python_scripts/ 
..   /home/gouillar/python_scripts
 
..   In [3]: pwd
..   Out[3]: '/home/gouillar/python_scripts'
 
..   In [4]: ls
 
..   In [5]: np.savetxt('integers.txt', np.arange(10))
 
..   In [6]: ls
..   integers.txt


.. 

    .. * os (system routines) and os.path (path management) modules::

..   >>> import os, os.path  
..   >>> current_dir = os.getcwd()
..   >>> current_dir
..   '/home/gouillar/sandbox'
..   >>> data_dir = os.path.join(current_dir, 'data')
..   >>> data_dir
..   '/home/gouillar/sandbox/data'
..   >>> if not(os.path.exists(data_dir)):
..         ...     os.mkdir('data')
..         ...     print "created 'data' folder"
..         ...     
..   >>> os.chdir(data_dir) # or in Ipython : cd data

IPython は os モジュールとその統合された機能によってシェルのように使うことができます.

.. IPython can actually be used like a shell, thanks to its integrated features and
.. the os module.

**ファイルにデータ配列を書き込む**

.. **Writing a data array in a file**

::

    >>> a = np.arange(100)
    >>> a = a.reshape((10, 10))

         

* テキストファイルに書き込む（ASCII 文字列として）::

    >>> np.savetxt('data_a.txt', a)

.. * Writing a text file (in ASCII)::

..     >>> np.savetxt('data_a.txt', a)

* バイナリファイルとして書き込む（この形式では拡張子を ``.npy``
  とすることを推奨します）::

    >>> np.save('data_a.npy', a)

.. * Writing a binary file (``.npy`` extension, recommended format) ::

..    >>> np.save('data_a.npy', a)

**ファイルからデータ配列を読み込む**

.. **Loading a data array from a file**

* テキストファイルから読み込む::

    >>> b = np.loadtxt('data_a.txt')

.. * Reading from a text file::

..     >>> b = np.loadtxt('data_a.txt')

* バイナリファイルから読み込む::

    >>> c = np.load('data_a.npy')

.. * Reading from a binary file::

..     >>> c = np.load('data_a.npy')

.. topic:: matlab のデータファイルを読む

    ``scipy.io.loadmat`` : matlab 形式の .mat ファイルが辞書として保存されます.

.. .. topic:: To read matlab data files

..     ``scipy.io.loadmat`` : the matlab structure of a .mat file is stored as a
..     dictionary.

**画像を開く, 保存する：imread と imsave**

.. **Opening and saving images: imsave and imread**

::

  >>> import scipy
  >>> from pylab import imread, imsave, savefig
  >>> lena = scipy.lena()
  >>> imsave('lena.png', lena, cmap=cm.gray)
  >>> lena_reloaded = imread('lena.png')
  >>> imshow(lena_reloaded, cmap=gray)
  <matplotlib.image.AxesImage object at 0x989e14c>
  >>> savefig('lena_figure.png')

.. image:: lena_figure.png
   :align: center
   :width: 60

**リストからファイルを選ぶ**

.. **Selecting a file from a list**

`a` の各行を異なるファイルに保存する.

.. Each line of ``a`` will be saved in a different file::

::

    >>> for i, l in enumerate(a):
    ...     print i, l
    ...     np.savetxt('line_'+str(i), l)
    ...     
    0 [0 1 2 3 4 5 6 7 8 9]
    1 [10 11 12 13 14 15 16 17 18 19]
    2 [20 21 22 23 24 25 26 27 28 29]
    3 [30 31 32 33 34 35 36 37 38 39]
    4 [40 41 42 43 44 45 46 47 48 49]
    5 [50 51 52 53 54 55 56 57 58 59]
    6 [60 61 62 63 64 65 66 67 68 69]
    7 [70 71 72 73 74 75 76 77 78 79]
    8 [80 81 82 83 84 85 86 87 88 89]
    9 [90 91 92 93 94 95 96 97 98 99]

``line`` で始まる全てのファイルを取得するために, パターンに対応するパス全てに適合する
``glob`` モジュールを使います.

.. To get a list of all files beginning with ``line``, we use the ``glob`` module
.. which matches all paths corresponding to a pattern. Example::

    >>> import glob
    >>> filelist = glob.glob('line*')
    >>> filelist
    ['line_0', 'line_1', 'line_2', 'line_3', 'line_4', 'line_5', 'line_6', 'line_7', 'line_8', 'line_9']
    >>> # Note that the line is not always sorted
    >>> filelist.sort()
    >>> l2 = np.loadtxt(filelist[2])

注意：配列は Excel/Calc ファイルや HDF5 ファイル等からも作成できます
（ただし, 追加のモジュール xlrd, pytables などが必要です. 
これらについてはここで述べません.）.

.. Note: arrays can also be created from Excel/Calc files, HDF5 files, etc.
.. (but with additional modules not described here: xlrd, pytables, etc.).

配列に対する簡単な数学的, 統計的操作
------------------------------------

.. Simple mathematical and statistical operations on arrays
.. --------------------------------------------------------

いくつかの配列に対する操作は Numpy でそのまま使えます（そしてこれらは一般にとても効率的です）.

.. Some operations on arrays are natively available in NumPy (and are generally
.. very efficient)::

::

    >>> a = np.arange(10)
    >>> a.min() # or np.min(a)
    0
    >>> a.max() # or np.max(a)
    9
    >>> a.sum() # or np.sum(a)
    45

操作は全ての要素でなく, 軸に沿って行うこともできます.

.. Operations can also be run along an axis, instead of on all elements::

    >>> a = np.array([[1, 3], [9, 6]])
    >>> a
    array([[1, 3],
           [9, 6]])
    >>> a.mean(axis=0) # the array contains the mean of each column 
    array([ 5. ,  4.5])
    >>> a.mean(axis=1) # the array contains the mean of each line
    array([ 2. ,  7.5])

他にも多くの操作があります. そのうちいくつかはこのコースの中でみかけるでしょう.

.. Many other operations are available. We will discover some of them in this
.. course.

.. note::

    
    配列に対する算術演算子は個々の要素に対して演算されます.
    特に積は（ **Matlab と違い** ）行列の積ではありません!
    行列の積は ``np.dot`` によって計算できます::

        >>> a = np.ones((2,2))
        >>> a*a
        array([[ 1.,  1.],
               [ 1.,  1.]])
        >>> np.dot(a,a)
        array([[ 2.,  2.],
               [ 2.,  2.]])

.. .. note::

..     Arithmetic operations on arrays correspond to operations on each individual
..     element. In particular, the multiplication is not a matrix multiplication
..     (**unlike Matlab**)! The matrix multiplication is provided by ``np.dot``::

..         >>> a = np.ones((2,2))
..         >>> a*a
..         array([[ 1.,  1.],
..                [ 1.,  1.]])
..         >>> np.dot(a,a)
..         array([[ 2.,  2.],
..                [ 2.,  2.]])

**例** ： 酔歩を使った拡散のシミュレーション

.. **Example** : diffusion simulation using a random walk algorithm

.. image:: random_walk.png
   :align: center 

右か左に動く酔っ払いは  ``t`` 後に原点から代表的な距離として, どれだけ離れているでしょう?

.. What is the typical distance from the origin of a random walker after ``t`` left
.. or right jumps?

.. image:: random_walk_schema.png
   :align: center

::

    >>> nreal = 1000 # number of walks
    >>> tmax = 200 # time during which we follow the walker
    >>> # We randomly choose all the steps 1 or -1 of the walk
    >>> walk = 2 * ( np.random.random_integers(0, 1, (nreal,tmax)) - 0.5 )
    >>> np.unique(walk) # Verification : all steps are 1 or -1
    array([-1.,  1.])
    >>> # We build the walks by summing steps along the time
    >>> cumwalk = np.cumsum(walk, axis=1) # axis = 1 : dimension of time
    >>> sq_distance = cumwalk**2
    >>> # We get the mean in the axis of the steps
    >>> mean_sq_distance = np.mean(sq_distance, axis=0) 

.. sourcecode:: ipython

    In [39]: figure()
    In [40]: plot(mean_sq_distance)
    In [41]: figure()
    In [42]: plot(np.sqrt(mean_sq_distance))

.. image:: diffuse.png
   :align: center
   :scale: 70

距離が時間の平方根で増えていくことがわかります!

.. We find again that the distance grows like the square root of the time!

**演習問題** ： フランスの女性研究者の数に関する統計（INSEE のデータ）

.. **Exercise** : statistics on the number of women in french research (INSEE data)

1. ``data`` ディレクトリの ``organisms.txt`` と ``women_percentage.txt`` を入手しましょう

.. 1. Get the following files ``organisms.txt`` and ``women_percentage.txt``
..    in the ``data`` directory. 

2. ``np.loadtxt`` を使って ``women_percentage.txt`` を開き, 配列 ``data`` を作成しましょう.
   この配列はどんなシェイプでしょうか?

.. 2. Create a ``data`` array by opening the ``women_percentage.txt`` file
..    with ``np.loadtxt``. What is the shape of this array? 

3. 列は 2006 から 2001 までの年に対応します.
   これらの年に対応する整数の配列 ``year`` を作成しましょう.

.. 3. Columns correspond to year 2006 to 2001. Create a ``years`` array with
..    integers corresponding to these years.

4. 行は研究機関に対応します. 各機関の名前は ``organisms.txt`` に保存されています.
   このファイルを開いて配列 ``organisms`` を作成しましょう.
   ただし,  ``np.loadtxt`` はデフォルトで浮動小数点数の配列を作ることに注意して下さい, 
   そして文字列を使うことを指定しなければなりません：
   ``organisms = np.loadtxt('organisms.txt, dtype=str)``

.. 4. The different lines correspond to the research organisms whose names are
..    stored in the ``organisms.txt`` file. Create a ``organisms`` array by
..    opening this file. Beware that ``np.loadtxt`` creates float arrays by default,
..    and it must be specified to use strings instead: ``organisms =
..    np.loadtxt('organisms.txt', dtype=str)``

5. ``data`` の行数が organisms の行数と等しいことをチェックしましょう.

.. 5. Check that the number of lines of ``data`` equals the number of lines of the
..    organisms.

6. 全ての組織, 年度の中での最大女性の割合を求めましょう.

.. 6. What is the maximal percentage of women in all organisms, for all years taken
..    together? 

7. 各々の組織における女性の割合の平均値の配列を作りましょう.
   つまり, 軸(axis) 1 に対しての平均を求めましょう.

.. 7. Create an array with the temporal mean of the percentage of women for each
..    organism? (i.e. the mean of ``data`` along axis 1).

8. 2004年に女性の割合が最も高い組織を求めましょう. （ヒント：np.argmax）

.. 8. Which organism had the highest percentage of women in 2004? (hint: np.argmax)

9. 2006 年の各組織の女性の割合の頻度分布を作りましょう.
   （ヒント：np.histgram, また matplotlib の bar か plot で可視化できます.）

.. 9. Create a histogram of the percentage of women the different organisms in 2006
..    (hint: np.histogram, then matplotlib bar or plot for visulalization)

10. 各年度の女性が最も多い組織を要素とする配列を作成しましょう.

.. 10. Create an array that contains the organism where the highest women's
..     percentage is found for the different years.

**解答** :ref:`stat_recherche`

.. **Answers** :ref:`stat_recherche`

ファンシーインデクス指定
------------------------

.. Fancy indexing
.. --------------

Numpy の配列はスライスだけでなく,
ブール値や整数の配列（ **マスク (masks)** ）を使って
インデクス指定することができます.
この方法を *ファンシーインデクス指定 (fancy indexing)* と呼びます.

.. Numpy arrays can be indexed with slices, but also with boolean or integer arrays
.. (**masks**). This method is called *fancy indexing*.

**マスク** ::

    >>> np.random.seed(3)
    >>> a = np.random.random_integers(0, 20, 15)
    >>> a
    array([10,  3,  8,  0, 19, 10, 11,  9, 10,  6,  0, 20, 12,  7, 14])
    >>> (a%3 == 0)
    array([False,  True, False,  True, False, False, False,  True, False,
            True,  True, False,  True, False, False], dtype=bool)
    >>> mask = (a%3 == 0)
    >>> extract_from_a = a[mask] #one could directly write a[a%3==0]
    >>> extract_from_a # extract a sub-array with the mask
    array([ 3,  0,  9,  6,  0, 12])

.. **Masks** ::

..     >>> np.random.seed(3)
..     >>> a = np.random.random_integers(0, 20, 15)
..     >>> a
..     array([10,  3,  8,  0, 19, 10, 11,  9, 10,  6,  0, 20, 12,  7, 14])
..     >>> (a%3 == 0)
..     array([False,  True, False,  True, False, False, False,  True, False,
..             True,  True, False,  True, False, False], dtype=bool)
..     >>> mask = (a%3 == 0)
..     >>> extract_from_a = a[mask] #one could directly write a[a%3==0]
..     >>> extract_from_a # extract a sub-array with the mask
..     array([ 3,  0,  9,  6,  0, 12])

配列の一部をビューではなく, コピーとして抽出します.

.. Extracting a sub-array using a mask produces a copy of this sub-array, not a view::

::

    >>> extract_from_a = -1
    >>> a
    array([10,  3,  8,  0, 19, 10, 11,  9, 10,  6,  0, 20, 12,  7, 14])

マスクによるインデクス指定は配列の一部に新しい値を代入するのに便利です.

.. Indexing with a mask can be very useful to assign a new value to a sub-array::

::

    >>> a[mask] = 0 
    >>> a
    array([10,  0,  8,  0, 19, 10, 11,  0, 10,  0,  0, 20,  0,  7, 14])

整数配列を利用したインデクス指定

.. **Indexing with an array of integers** ::

::

    >>> a = np.arange(10)
    >>> a[::2] +=3 #to avoid having always the same np.arange(10)...
    >>> a
    array([ 3,  1,  5,  3,  7,  5,  9,  7, 11,  9])
    >>> a[[2, 5, 1, 8]] # or a[np.array([2, 5, 1, 8])]
    array([ 5,  5,  1, 11])

インデクス指定は整数配列を使ってもでき, 同じインデクスが何回か繰り返されていても使えます.

.. Indexing can be done with an array of integers, where the same index is repeated
.. several time::

::

    >>> a[[2, 3, 2, 4, 2]]
    array([5, 3, 5, 7, 5])

このようなインデクス指定を使って新しい値を代入することもできます.

.. New values can be assigned with this kind of indexing::

::

    >>> a[[9, 7]] = -10
    >>> a
    array([  3,   1,   5,   3,   7,   5,   9, -10,  11, -10])
    >>> a[[2, 3, 2, 4, 2]] +=1
    >>> a
    array([  3,   1,   6,   4,   8,   5,   9, -10,  11, -10])

整数配列によるインデクス指定で新しい配列を作った場合, 
新しい配列は整数配列と同じシェイプになります.

.. When a new array is created by indexing with an array of integers, the new array
.. has the same shape than the array of integers::

::

    >>> a = np.arange(10)
    >>> idx = np.array([[3, 4], [9, 7]])
    >>> a[idx]
    array([[3, 4],
           [9, 7]])
    >>> b = np.arange(10) 

    >>> a = np.arange(12).reshape(3, 4)
    >>> a
    array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11]])
    >>> i = np.array([0, 1, 1, 2])
    >>> j = np.array([2, 1, 3, 3])
    >>> a[i, j]
    array([ 2,  5,  7, 11])

    >>> i = np.array([[0, 1], [1, 2]])
    >>> j = np.array([[2, 1], [3, 3]])
    >>> i
    array([[0, 1],
           [1, 2]])
    >>> j
    array([[2, 1],
           [3, 3]])
    >>> a[i, j]
    array([[ 2,  5],
           [ 7, 11]])

.. image:: numpy_fancy_indexing.png
   :align: center

**練習問題**

.. **Exercise** 

女性研究者の数の問題と同じ統計を取りましょう. 
（配列 ``data`` と ``organisms`` を使います）

.. Let's take the same statistics about the percentage of women in the research
.. (``data`` and ``organisms`` arrays)

1. ``data`` の要素が 30% より高ければ 1 低ければ 0 となるような ``data``
   と同じサイズの配列 ``sup30`` を作りましょう.

.. 1. Create a ``sup30`` array of the same size than ``data`` with a value of 1 if
..    the value of ``data`` is greater than 30%, 0 otherwise.

2. 各年度毎の女性の割合が最大となる組織を含む配列を作成しましょう.

.. 2. Create an array containing the organisme having the greatest percentage of
.. women of each year.

**解答** :ref:`stat_recherche`

.. **Answers** :ref:`stat_recherche`
    


ブロードキャスト
----------------

.. Broadcasting
.. ------------


``numpy`` の配列に対する基本演算は同じサイズの配列の各要素に対して行なわれます.
しかし, ``numpy`` がサイズの異なる配列を同じサイズの配列に変換できれば,
異なるサイズの配列に対しても演算を行うことができます.
この変換を **ブロードキャスト (broadcast)** と呼びます.

.. Basic operations on ``numpy`` arrays (addition, etc.) are done element by
.. element, thus work on arrays of the same size. Nevertheless, it's possible to do
.. operations on arrays of different sizes if ``numpy`` can transform these arrays
.. so that they all have the same size: this conversion is called **broadcasting**.

以下の画像はブロードキャストの例を示しています：
    
.. The image below gives an example of broadcasting:

.. image:: numpy_broadcasting.png
   :align: center

画像は IPython では以下を実行することに対応します.

.. which gives the following in Ipython::

::

    >>> a = np.arange(0, 40, 10)
    >>> b = np.arange(0, 3)
    >>> a = a.reshape((4,1)) # a must be changed into a vertical array
    >>> a + b
    array([[ 0,  1,  2],
           [10, 11, 12],
           [20, 21, 22],
           [30, 31, 32]])


実は以前にもブロードキャストを使っていました!

.. We actually already used broadcasting without knowing it!::

::

    >>> a = np.arange(20).reshape((4,5))
    >>> a
    array([[ 0,  1,  2,  3,  4],
           [ 5,  6,  7,  8,  9],
           [10, 11, 12, 13, 14],
           [15, 16, 17, 18, 19]])
    >>> a[0] = 1 # we assign an array of dimension 0 to an array of dimension 1
    >>> a[:3] = np.arange(1,6)
    >>> a
    array([[ 1,  2,  3,  4,  5],
           [ 1,  2,  3,  4,  5],
           [ 1,  2,  3,  4,  5],
           [15, 16, 17, 18, 19]])

ファンシーインデクス指定とブロードキャストを同時に使うこともできます.
上と同じ例を取り上げてみましょう.

.. We can even use fancy indexing and broadcasting at the same time. Take again the
.. same example as above::

::

    >>> a = np.arange(12).reshape(3,4)
    >>> a
    array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11]])
    >>> i = np.array( [ [0,1],                        
    ...              [1,2] ] )
    >>> a[i, 2] # same as a[i, 2*np.ones((2,2), dtype=int)]
    array([[ 2,  6],
           [ 6, 10]])

ブロードキャストは少々不思議に思えるでしょう,
しかし入力データより出力データが多い問題を解くような場合
自然に使うことができます.

.. Broadcasting seems a bit magical, but it is actually quite natural to use it
.. when we want to solve a problem whose output data is an array with more
.. dimensions than input data.

**例** ： ルート 66 での各街 (Chicago, Springfield, Saint-Louis, Tulsa,
Oklahoma City, Amarillo, Santa Fe, Albucquerque, Flagstaff and Los Angeles)
間の距離（マイル）を表わす配列を作ってみましょう.

.. **Example**: let's construct an array of distances (in miles) between cities of
.. Route 66: Chicago, Springfield, Saint-Louis, Tulsa,
.. Oklahoma City, Amarillo, Santa Fe, Albucquerque, Flagstaff and Los
.. Angeles. 

::

    >>> mileposts = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544,
    ...        1913, 2448])
    >>> ditance_array = np.abs(mileposts - mileposts[:,np.newaxis])
    >>> ditance_array
    array([[   0,  198,  303,  736,  871, 1175, 1475, 1544, 1913, 2448],
           [ 198,    0,  105,  538,  673,  977, 1277, 1346, 1715, 2250],
           [ 303,  105,    0,  433,  568,  872, 1172, 1241, 1610, 2145],
           [ 736,  538,  433,    0,  135,  439,  739,  808, 1177, 1712],
           [ 871,  673,  568,  135,    0,  304,  604,  673, 1042, 1577],
           [1175,  977,  872,  439,  304,    0,  300,  369,  738, 1273],
           [1475, 1277, 1172,  739,  604,  300,    0,   69,  438,  973],
           [1544, 1346, 1241,  808,  673,  369,   69,    0,  369,  904],
           [1913, 1715, 1610, 1177, 1042,  738,  438,  369,    0,  535],
           [2448, 2250, 2145, 1712, 1577, 1273,  973,  904,  535,    0]])


.. image:: route66.png
   :align: center
   :scale: 60

.. warning:: よい習慣

    これまでの例でよい（あるいはよくない）習慣を書き留めてきました：

    * 明示的な変数名を使う（変数説明のコメント不要）

    * カンマや ``==`` 等の後に空白を入れる.
      「美しい」ソースコードを書くための（そしてより重要な点として,
      誰もが同じ記法を使うという重要性のための!）規則が
      `Style Guide for Python Code <http://www.python.org/dev/peps/pep-0008>`_ [*]_ と
      `Docstring Conventions <http://www.python.org/dev/peps/pep-0257>`_ [*]_
      （こちらはヘルプの為の文字列を扱うための規則）にあります.

    * いくつかの例外を除いて変数名とコメントは英語で書きましょう.

.. .. warning:: Good practices

..     In the previous example, we can note some good (and bad) practices:

..     * Give explicit variable names (no need of a comment to explain what is in
..       the variable)

..     * Put spaces after commas, around ``=``, etc. A certain number of rules
..       for writing "beautiful" code (and more importantly using the same
..       conventions as anybody else!) are given in the `Style Guide for Python
..       Code <http://www.python.org/dev/peps/pep-0008>`_ and the `Docstring
..       Conventions <http://www.python.org/dev/peps/pep-0257>`_ page (to manage
..       help strings).

..     * Except some rare cases, write variable names and comments in english.

多くの格子やネットワークを扱う問題ではブロードキャストを使うことができます.
例えば, 10x10の格子の原点からの距離を計算したければこうします

.. A lot of grid-based or network-based problems can also use broadcasting. For instance,
.. if we want to compute the distance from the origin of points on a 10x10 grid, we
.. can do::

::

    >>> x, y = np.arange(5), np.arange(5)
    >>> distance = np.sqrt(x**2 + y[:, np.newaxis]**2)
    >>> distance
    array([[ 0.        ,  1.        ,  2.        ,  3.        ,  4.        ],
           [ 1.        ,  1.41421356,  2.23606798,  3.16227766,  4.12310563],
           [ 2.        ,  2.23606798,  2.82842712,  3.60555128,  4.47213595],
           [ 3.        ,  3.16227766,  3.60555128,  4.24264069,  5.        ],
           [ 4.        ,  4.12310563,  4.47213595,  5.        ,  5.65685425]])

``pylab.imshow`` 関数を使って配列の距離の値を色で表示できます
（構文は ``pylab.imshow(distance)`` です.
他のオプションについてはヘルプを見てください.）

.. The values of the distance array can be represented in colour, thanks to the
.. ``pylab.imshow`` function (syntax: ``pylab.imshow(distance)``. See help for
.. other options).

.. image:: distance.png
    :align: center
    :scale: 70

**注目** ： ``numpy.ogrid`` 関数を2つの「代表的次元」を与えて使うことで
前の例での x, y ベクトルを直接作りだすことができます.

.. **Remark** : the ``numpy.ogrid`` function allows to directly create vectors x
.. and y of the previous example, with two "significant dimensions"::

::

    >>> x, y = np.ogrid[0:5, 0:5]
    >>> x, y
    (array([[0],
           [1],
           [2],
           [3],
           [4]]), array([[0, 1, 2, 3, 4]]))
    >>> x.shape, y.shape
    ((5, 1), (1, 5))
    >>> distance = np.sqrt(x**2 + y**2)

    
これからわかるように ``np.ogrid`` はネットワークの計算を扱うのにとても便利です.
一方 ``np.mgrid`` は完全なインデクスを持つ行列を直接提供します.
これはブロードキャストの恩恵を受けられない（もしくは受けたない）場合に使うことができます.

.. So, ``np.ogrid`` is very useful as soon as we have to handle computations on a
.. network. On the other hand, ``np.mgrid`` directly provides matrices full of
.. indices for cases where we can't (or don't want to) benefit from broadcasting::

    >>> x, y = np.mgrid[0:4, 0:4]
    >>> x
    array([[0, 0, 0, 0],
           [1, 1, 1, 1],
           [2, 2, 2, 2],
           [3, 3, 3, 3]])
    >>> y
    array([[0, 1, 2, 3],
           [0, 1, 2, 3],
           [0, 1, 2, 3],
           [0, 1, 2, 3]])

 
総合練習問題：Lena の縁どり
---------------------------
    
.. Synthesis exercises: framing Lena
.. ---------------------------------------

有名な画像 Lena (http://www.cs.cmu.edu/~chuck/lennapg/) を使って numpy 配列の
操作をやってみましょう.
``scipy`` はこの画像の2次元配列を ``scipy.lena`` 関数で提供しています.

.. Let's do some manipulations on numpy arrays by starting with the famous image of
.. Lena (http://www.cs.cmu.edu/~chuck/lennapg/). ``scipy`` provides a 2D array of
.. this image with the ``scipy.lena`` function::

::

    >>> import scipy
    >>> lena = scipy.lena()

ここに操作によって得られる画像を少しだけ載せておきます：
違うカラーマップを使う, 画像を切り取る, 特定の部分を変更する.

.. Here are a few images we will be able to obtain with our manipulations:
.. use different colormaps, crop the image, change some parts of the image.

.. image:: lenas.png
   :align: center

* pylab の imshow 関数で画像を表示してみましょう.

  .. sourcecode:: ipython
      
      In [3]: import pylab 
      In [4]: lena = scipy.lena()
      In [5]: pylab.imshow(lena)

.. * Let's use the imshow function of pylab to display the image.

..   .. sourcecode:: ipython
      
..       In [3]: import pylab 
..       In [4]: lena = scipy.lena()
..       In [5]: pylab.imshow(lena)

* そうすると Lena は 擬似カラーで表示されます.
  カラーマップをグレーで表示しましょう.

  .. sourcecode:: ipython
      
      In [6]: pylab.imshow(lena, pylab.cm.gray)
      In [7]: # ou
      In [8]: gray()

.. * Lena is then displayed in false colors. A colormap must be specified for her
..   to be displayed in grey.

..   .. sourcecode:: ipython
      
..       In [6]: pylab.imshow(lena, pylab.cm.gray)
..       In [7]: # ou
..       In [8]: gray()

* 中央揃えしたより幅の狭い画像を作ってみましょう：
  例として画像の境界から 30 ピクセル削ってみましょう.
  結果を確認するためには ``imshow`` で配列を表示してみましょう.

  .. sourcecode:: ipython
   
      In [9]: crop_lena = lena[30:-30,30:-30]

.. * Create an array of the image with a narrower centring : for example,
..   remove 30 pixels from all the borders of the image. To check the result,
..   display this new array with ``imshow``.

..   .. sourcecode:: ipython
   
..       In [9]: crop_lena = lena[30:-30,30:-30]

* Lena の顔を黒いロケットで囲ってみましょう. そのためには

    * 黒で覆いたいピクセルに対応する mask を作ります.
      mask は ``(y-256)**2 + (x-256)**2`` で定義します

    .. sourcecode:: ipython
     
        In [15]: y, x = np.ogrid[0:512,0:512] # x and y indices of pixels 
        In [16]: y.shape, x.shape
        Out[16]: ((512, 1), (1, 512))
        In [17]: centerx, centery = (256, 256) # center of the image
        In [18]: mask = ((y - centery)**2 + (x - centerx)**2)> 230**2

  そして

    * mask に対応する画像ピクセルに 0 を代入します.
      構文は平易で直感的です.

    .. sourcecode:: ipython
     
        In [19]: lena[mask]=0
        In [20]: imshow(lena)
        Out[20]: <matplotlib.image.AxesImage object at 0xa36534c>

.. * We will now frame Lena's face with a black locket. For this, we need to

..     * create a mask corresponding to the pixels we want to be black.
..       The mask is defined by this condition ``(y-256)**2 + (x-256)**2``
      
.. .. sourcecode:: ipython

..     In [15]: y, x = np.ogrid[0:512,0:512] # x and y indices of pixels 
..     In [16]: y.shape, x.shape
..     Out[16]: ((512, 1), (1, 512))
..     In [17]: centerx, centery = (256, 256) # center of the image
..     In [18]: mask = ((y - centery)**2 + (x - centerx)**2)> 230**2

..   then
    
..     * assign the value 0 to the pixels of the image corresponding to the mask.
..       The syntax is extremely simple and intuitive:

* 副次的問題：この問題の全ての命令を ``lena_locket.py`` という名前で
  スクリプトにコピーしましょう, そして iPython で ``%run lena_locket.py`` として
  スクリプトを実行してみましょう.

.. * Subsidiary question : copy all instructions of this exercise in a script
..   called ``lena_locket.py`` then execute this script in iPython with ``%run
..   lena_locket.py``.

.. topic:: 結び : numpy の配列を使い始めるに当って何が必要なのか?

    * 配列の作り方を知る： ``array``, ``arange``, ``ones``, ``zeros``

    * ``array.shape`` を使って配列のシェイプを知る, スライスを使って配列の異なる
      ビューを得る（例： ``array[::2]`` 等） ``reshape`` を使って配列のシェイプを変更する.

    * 配列の一部の要素をマスクを使って得る, 変更する::
 
          >>> a[a<0] = 0

    * 配列に対する様々な操作を知る, 例えば平均値や最大値を求める (``array.max()``,
      ``array.mean()``).
      全てを覚える必要はありません, ただしドキュメントを探すときに影響がでます
      （ :ref:`help` をみましょう ）!!

    * もっと使いこなすには：
      整数配列を使ったインデクス指定やブロードキャストに精通する.
      numpy の配列操作に関する関数をより多く知る

.. .. topic:: Conclusion : what do you need to know about numpy arrays to start?

..     * Know how to create arrays : ``array``, ``arange``, ``ones``,
..       ``zeros``.

..     * Know the shape of the array with ``array.shape``, then use slicing
..       to obtain different views of the array: ``array[::2]``,
..       etc. Change the shape of the array using ``reshape``.

..     * Obtain a subset of the elements of an array and/or modify their values
..       with masks::
  
..   >>> a[a<0] = 0

..     * Know miscellaneous operations on arrays, like finding the mean or max
..       (``array.max()``, ``array.mean()``). No need to retain everything, but
..       have the reflex to search in the documentation (see :ref:`help`) !!

..     * For advanced use: master the indexing with arrays of integers, as well as
..       broadcasting. Know more functions of numpy allowing to handle array
..       operations.
.. rubric:: Footnotes

.. [*] 日本語訳 `PEP 8 -- Style Guide for Python Code <http://oldriver.org/python/pep-0008j.html>`_
.. [*] 日本語訳 `ドキュメンテーション文字列の書き方のガイドライン <http://www.python.jp/doc/contrib/peps/pep-0257.txt>`_
