===========
 解答
===========

.. ===========
..  Solutions
.. ===========


.. _pi_wallis:

Wallis の公式による :math:`\pi` 解答
------------------------------------

.. The :math:`\pi` Wallis Solution
.. -------------------------------

Wallis の公式を使って, :math:`\pi` の値を計算しましょう：

.. Compute the decimals of :math:`\pi` using the Wallis formula:

.. literalinclude:: solutions/pi_wallis.py

.. _quick_sort:

クイックソートの解答
--------------------

.. The Quicksort Solution
.. ----------------------

クイックソートアルゴリズムを実装しましょう, Wikipedia での定義:

.. Implement the quicksort algorithm, as defined by wikipedia:

::

	function quicksort(array)
	    var list less, greater
	    if length(array) ≤ 1  
		return array  
	    select and remove a pivot value pivot from array
	    for each x in array
		if x ≤ pivot then append x to less
		else append x to greater
	    return concatenate(quicksort(less), pivot, quicksort(greater))

.. literalinclude:: solutions/quick_sort.py

.. _fibonacci:

Fibonacci 数列
--------------

.. Fibonacci sequence
.. ------------------

Fibonacci 数列の第1項から n 項までを表示する関数を書きましょう, Fibonacci 数列の定義は：

.. Write a function that displays the ``n`` first terms of the Fibonacci
.. sequence, defined by:

* :math:`u_0 = 1; u_1 = 1`
* :math:`u_{n+2} = u_{n+1} + u_n`

::

    >>> def fib(n):    
    ...     """Display the n first terms of Fibonacci sequence"""
    ...     a, b = 0, 1
    ...     i = 0
    ...     while i < n:
    ...         print b
    ...         a, b = b, a+b
    ...         i +=1
    ...
    >>> fib(10)
    1
    1
    2
    3
    5
    8
    13
    21
    34
    55

.. _dir_sort:

ディレクトリリストの解答
------------------------

.. The Directory Listing Solution
.. ------------------------------

ディレクトリの名前を引数としてとり, 名前の長さによって並べられた '.py' ファイルのリストを返す関数を実装しましょう.

.. Implement a script that takes a directory name as argument, and
.. returns the list of '.py' files, sorted by name length.

**ヒント：** list.sort のドキュメンテーション文字列を理解してみましょう

.. **Hint:** try to understand the docstring of list.sort

.. literalinclude:: solutions/dir_sort.py

.. _data_file:

データファイルの入出力の解答
----------------------------

.. The Data File I/O Solution
.. --------------------------

``data.txt`` の各列の数字を読み込み最小値, 最大値, 和を計算する関数を書きましょう.

.. Write a function that will load the column of numbers in ``data.txt``
.. and calculate the min, max and sum values.

データファイル：

.. Data file:

.. literalinclude:: solutions/data.txt

解答：

.. Solution:

.. literalinclude:: solutions/data_file.py

.. _path_site:

:envvar:`PYTHONPATH` 検索の解答
-------------------------------

.. The :envvar:`PYTHONPATH` Search Solution
.. ----------------------------------------

:file:`site.py` モジュールが :envvar:`PYTHONPATH` のどこにあるか検索するプログラムを書きましょう.

.. Write a program to search your :envvar:`PYTHONPATH` for the module ``site.py``.

.. literalinclude:: solutions/path_site.py

