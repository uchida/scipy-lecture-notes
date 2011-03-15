Pythonで科学計算の積み木を組む
==============================

..  Building blocks of scientific computing with Python
    ===================================================

.. only:: latex

    :author: Emmanuelle Gouillart

* **Python**, 包括的で現代的なプログラミング言語

   * Python 言語：データ型(``string``, ``int``), 制御フロー,
     データの集まり（リスト, 辞書）, パターン等

   * 標準ライブラリのモジュール

   * Python で書かれたたくさんの専用モジュールやアプリケーション：web プロトコル,
     web フレームワーク等, もちろん科学計算も

   * 開発ツール（自動化されたテスト, ドキュメント生成）

..
    * **Python**, a generic and modern computing language
    
        * Python language: data types (``string``, ``int``), flow control,
          data collections (lists, dictionaries), patterns, etc.
    
        * Modules of the standard library.
    
        * A large number of specialized modules or applications written in
          Python: web protocols, web framework, etc. ... and scientific
          computing.
    
        * Development tools (automatic tests, documentation generation)
    
* **IPython**, 先進的な Python shell

  http://ipython.scipy.org/moin/

..  * **IPython**, an advanced Python shell
    
    http://ipython.scipy.org/moin/

 
  .. image:: snapshot_ipython.png
        :align: center
        :scale: 70
   
  .. sourcecode:: ipython
   
      In [1]: a = 2
   
      In [2]: print "hello"
      hello
   
      In [3]: %run my_script.py
 
* **Numpy** ： 強力な数値配列オブジェクトとそれらを操作する強力なルーチンを提供
 
    >>> import numpy as np
    >>> t = np.arange(10)
    >>> t
    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    >>> print t 
    [0 1 2 3 4 5 6 7 8 9]
    >>> signal = np.sin(t)

  http://www.scipy.org/

.. 
    >>> np.random.seed(4)

..  * **Numpy** : provides powerful numerical arrays objects, and routines to
    manipulate them.
    
        >>> import numpy as np
        >>> t = np.arange(10)
        >>> t
        array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        >>> print t 
        [0 1 2 3 4 5 6 7 8 9]
        >>> signal = np.sin(t)

.. 
    >>> np.random.seed(4)

* **Scipy** ： 高レベルなデータ処理ルーチン, 最適化, 回帰, 補間等::

    >>> import numpy as np
    >>> import scipy 
    >>> t = np.arange(10)
    >>> t
    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    >>> signal = t**2 + 2*t + 2+ 1.e-2*np.random.random(10)
    >>> scipy.polyfit(t, signal, 2)
    array([ 1.00001151,  1.99920674,  2.00902748])

  http://www.scipy.org/

..  * **Scipy** : high-level data processing routines.
    Optimization, regression, interpolation, etc::
    
        >>> import numpy as np
        >>> import scipy 
        >>> t = np.arange(10)
        >>> t
        array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        >>> signal = t**2 + 2*t + 2+ 1.e-2*np.random.random(10)
        >>> scipy.polyfit(t, signal, 2)
        array([ 1.00001151,  1.99920674,  2.00902748])
    
      http://www.scipy.org/

* **Matplotlib** ： 二次元可視化, 出版品質のプロット

  http://matplotlib.sourceforge.net/

.. image:: random_c.jpg
      :scale: 70

.. image:: hexbin_demo.png
      :scale: 50
  

..  * **Matplotlib** : 2-D visualization, "publication-ready" plots
    
      http://matplotlib.sourceforge.net/
    
    .. image:: random_c.jpg
          :scale: 70
    
    .. image:: hexbin_demo.png
          :scale: 50
  

* **Mayavi** ： 三次元可視化

  http://code.enthought.com/projects/mayavi/

.. image:: example_surface_from_irregular_data.jpg
      :scale: 60

..  * **Mayavi** : 3-D visualization

      http://code.enthought.com/projects/mayavi/
    
    .. image:: example_surface_from_irregular_data.jpg
          :scale: 60

など他にもたくさん.

..  * and many others.

