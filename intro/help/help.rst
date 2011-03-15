.. _help:

ヘルプを見る, ドキュメントを探す
================================

.. Getting help and finding documentation
.. =========================================

.. only:: latex

    :author: Emmanuelle Gouillart

Numpy と Scipy の全ての関数を知っていることよりも,
ドキュメントやヘルプを利用して素早く情報を探しだすことの方が重要です.
ここでは情報を得るための方法について述べます.

.. Rather than knowing all functions in Numpy and Scipy, it is important to
.. find rapidly information throughout the documentation and the available
.. help. Here are some ways to get information:

IPython では ``help 関数`` で関数の docstring が開きます.
関数の名前の最初の一部を打ち込んで Tab 補完を使うとマッチする関数が表示されます.

.. * In Ipython, ``help function`` opens the docstring of the function. Only
..   type the beginning of the function's name and use tab completion to
..   display the matching functions.

.. sourcecode:: ipython

    In [204]: help np.v
    np.vander     np.vdot       np.version    np.void0      np.vstack
    np.var        np.vectorize  np.void       np.vsplit     
    
    In [204]: help np.vander
	
IPython ではヘルプとドキュメントのためにウィンドウを分割することはできません.
しかし, ヘルプや docstring を見るために別の ``IPython`` シェルを立ち上げることができます.

.. In Ipython it is not possible to open a separated window for help and
.. documentation; however one can always open a second ``Ipython`` shell
.. just to display help and docstrings...

* Numpy と Scipy のドキュメントはオンラインで http://docs.scipy.org/doc で見ることができます.
  パッケージの reference (http://docs.scipy.org/doc/numpy/reference/ と
  http://docs.scipy.org/doc/scipy/reference/) 内の ``search`` ボタンがとても便利です.

  この Web サイトでは docstring を備えた API と様々な話題についてのチュートリアルがあります.

  .. image:: scipy_doc.png
     :align: center
     :scale: 80

.. * Numpy's and Scipy's documentations can be browsed online on
..   http://docs.scipy.org/doc. The ``search`` button is quite useful inside
..   the reference documentation of the two packages
..   (http://docs.scipy.org/doc/numpy/reference/ and
..   http://docs.scipy.org/doc/scipy/reference/). 

..   Tutorials on various topics as well as the complete API with all
..   docstrings are found on this website.


..   .. image:: scipy_doc.png
..      :align: center
..      :scale: 80

* Numpy と Scipy のドキュメントはユーザによる Wiki http://docs.scipy.org/numpy/
  を基本として補強, 更新されています.
  その結果, Wiki により明解で詳細な docstring がある場合があります,
  なので, 公式のドキュメントの Web サイトに代わって, Wiki のドキュメントを直接見たいと思うかもしれません.
  Wiki のアカウントは誰でも作れるので, 誰でもよりよいドキュメントを書くことができます.
  ドキュメントを改善することはオープンソースプロジェクトに強力して,
  自分で使っているツールを改善する最も簡単な方法です!

  .. image:: docwiki.png
     :align: center
     :scale: 80

.. * Numpy's and Scipy's documentation is enriched and updated on a regular
..   basis by users on a wiki http://docs.scipy.org/numpy/. As a result,
..   some docstrings are clearer or more detailed on the wiki, and you may
..   want to read directly the documentation on the wiki instead of the
..   official documentation website. Note that anyone can create an account on
..   the wiki and write better documentation; this is an easy way to
..   contribute to an open-source project and improve the tools you are
..   using!

..   .. image:: docwiki.png
..      :align: center
..      :scale: 80

* Scipy の Cookbook http://www.scipy.org/Cookbook はデータの点をフィッティングする,
  常微分方程式を解くなどの頻繁にでくわす多くの問題に対するレシピを載せています.

.. * Scipy's cookbook http://www.scipy.org/Cookbook gives recipes on many
..   common problems frequently encountered, such as fitting data points,
..   solving ODE, etc. 


* Matplotlib の Web サイト http://matplotlib.sourceforge.net/ には多くの作図を載せた素晴しい
  **gallery** があります, それらはソースコードとその結果の図両方が載っています.
  例から学ぶのに最適です. また標準のドキュメントも入手できます.

  .. image:: matplotlib.png
     :align: center
     :scale: 80

.. * Matplotlib's website http://matplotlib.sourceforge.net/ features a very
..   nice **gallery** with a large number of plots, each of them shows both
..   the source code and the resulting plot. This is very useful for
..   learning by example. More standard documentation is also available. 


.. .. image:: matplotlib.png
..    :align: center
..    :scale: 80

* Mayavi の Web サイト
  http://code.enthought.com/projects/mayavi/docs/development/html/mayavi/
  にも例が載っている素晴しい gallery 
  http://code.enthought.com/projects/mayavi/docs/development/html/mayavi/auto/examples.html
  があります, ここからいろいろな可視化の方法についてざっと眺めることができます.

  .. image:: mayavi_website.png
     :align: center
     :scale: 80

.. * Mayavi's website
..   http://code.enthought.com/projects/mayavi/docs/development/html/mayavi/
..   also has a very nice gallery of examples
..   http://code.enthought.com/projects/mayavi/docs/development/html/mayavi/auto/examples.html
..   in which one can browse for different visualization solutions.

.. .. image:: mayavi_website.png
..    :align: center
..    :scale: 80

最後に, 二つの「技術的」方法が便利です：

* IPython では magical function ``%psearch`` でパターンにマッチするオブジェクトを探すことができます.
  これは関数の厳密な名前を知らないときに便利です.

  .. sourcecode:: ipython
   
      In [3]: import numpy as np
      In [4]: %psearch np.diag*
      np.diag
      np.diagflat
      np.diagonal

* numpy.lookfor は特定のモジュールの docstring の中のキーワードを探します.

  .. sourcecode:: ipython
   
      In [45]: numpy.lookfor('convolution')
      Search results for 'convolution'
      --------------------------------
      numpy.convolve
          Returns the discrete, linear convolution of two one-dimensional
      sequences.
      numpy.bartlett
          Return the Bartlett window.
      numpy.correlate
          Discrete, linear correlation of two 1-dimensional sequences.
      In [46]: numpy.lookfor('remove', module='os')
      Search results for 'remove'
      ---------------------------
      os.remove
          remove(path)
      os.removedirs
          removedirs(path)
      os.rmdir
          rmdir(path)
      os.unlink
          unlink(path)
      os.walk
          Directory tree generator.
    
.. Finally, two more "technical" possibilities are useful as well:

.. * In Ipython, the magical function ``%psearch`` search for objects
..   matching patterns. This is useful if, for example, one does not know
..   the exact name  of a function.


.. .. sourcecode:: ipython

..     In [3]: import numpy as np
..     In [4]: %psearch np.diag*
..     np.diag
..     np.diagflat
..     np.diagonal

.. * numpy.lookfor looks for keywords inside the docstrings of specified modules.

.. .. sourcecode:: ipython

..     In [45]: numpy.lookfor('convolution')
..     Search results for 'convolution'
..     --------------------------------
..     numpy.convolve
..         Returns the discrete, linear convolution of two one-dimensional
..     sequences.
..     numpy.bartlett
..         Return the Bartlett window.
..     numpy.correlate
..         Discrete, linear correlation of two 1-dimensional sequences.
..     In [46]: numpy.lookfor('remove', module='os')
..     Search results for 'remove'
..     ---------------------------
..     os.remove
..         remove(path)
..     os.removedirs
..         removedirs(path)
..     os.rmdir
..         rmdir(path)
..     os.unlink
..         unlink(path)
..     os.walk
..         Directory tree generator.

* 上に挙げた全ての方法を試しても（さらに Google で答がなかった場合）,
  情報が得られなかった場合もあきらめないで!
  問題に適したメーリングリストにメールを書いてみましょう：
  問題を適切な形で述べれば, すぐ解答を得ることができるでしょう.
  メーリングリストでは Scientific python のエキスパート達がしばしば教育的な説明を与えています.

    * **Numpy discussion** (numpy-discussion@scipy.org)： numpy の配列,
      配列の操作, インデクスに関する質問について


    * **SciPy Users List** (scipy-user@scipy.org)：Python での科学計算,
      高レベルなデータ処理, 特に scipy パッケージについて

    * matplotlib-users@lists.sourceforge.net matplotlib での作図について

.. * If everything listed above fails (and Google doesn't have the
..   answer)... don't despair! Write to the mailing-list suited to your
..   problem: you should have a quick answer if you describe your problem
..   well. Experts on scientific python often give very enlightening
..   explanations on the mailing-list.

..     * **Numpy discussion** (numpy-discussion@scipy.org): all about numpy
..       arrays, manipulating them, indexation questions, etc.


..     * **SciPy Users List** (scipy-user@scipy.org): scientific computing
..       with Python, high-level data processing, in particular with the
..       scipy package.

..     * matplotlib-users@lists.sourceforge.net for plotting with
..       matplotlib.                               
                                             
