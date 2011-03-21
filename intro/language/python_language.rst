Python 入門（簡略）
===================

..  A (very short) introduction to Python
    =====================================

.. only:: latex

  :authors: Chris Burns, Christophe Combelles, Emmanuelle Gouillart, Gaël
   Varoquaux

.. topic:: 科学技術計算のためのPython

    この章では Python の導入を行います.
    ここでは, Numpy や Scipy を始めるために必要な最小限のことだけを述べます.
    言語のことについてもっと学びたければ,
    素晴しいチュートリアル http://docs.python.org/tutorial [*]_
    を見ることを検討してみましょう.
    http://diveintopython.org/ のように, 言語を学ぶ専門の本も入手できます.

..  .. topic:: Python for scientific computing
    
    We introduce here the Python language. Only the bare minimum
    necessary for getting started with Numpy and Scipy is addressed here.
    To learn more about the language, consider going through the
    excellent tutorial http://docs.python.org/tutorial. Dedicated books
    are also available, such as http://diveintopython.org/.

.. image:: python-logo.png
   :align: right

Python は C, Fortran, BASIC, PHP 等と同じ **プログラミング言語** です.
Python は以下のいくつかの機能を持っています：

* Python は *インタプリタ* 言語（ *コンパイラ* 言語と対照的）です.
  C や Fortran と対照的に, Python コードは実行前にコンパイルされません.
  さらに, Pythonは **インタラクティブ**
  に使うことができます：多くの Python インタプリタが入手でき,
  コマンドやスクリプトから実行できます.

* **オープンソース** ライセンスの元に公開されたフリーソフトウェア：Python
  は無料で制限無く利用,配布できます. 商用利用であっても同様です.

* **マルチプラットフォーム** ： Pythonはメジャーな OS,
  Windows, Linux/Unix, Mac OS X, 携帯の OS などでも利用できます.

* 冗長でなく, 明瞭な構文でとても読みやすい言語です.

* web フレームワークから科学技術計算といった幅広い応用のための高品質で多様なパッケージを持っています.

* 他の言語, 特に C, C++ との連携がとても簡単です.

* 他の特徴, 例えばオブジェクト指向言語,
  ダイナミックタイピング（オブジェクトの型がプログラムの途中で変りうる）などは以下に書かれています.

Python の特徴についてより多くの情報を得たければ, http://www.python.org/about/ をみてみましょう.

..
    Python is a **programming language**, as are C, Fortran, BASIC, PHP,
    etc. Some specific features of Python are as follows:
    
    * an *interpreted* (as opposed to *compiled*) language. Contrary to e.g.
      C or Fortran, one does not compile Python code before executing it. In
      addition, Python can be used **interactively**: many Python
      interpreters are available, from which commands and scripts can be
      executed.
    
    * a free software released under an **open-source** license: Python can
      be used and distributed free of charge, even for building commercial
      software.
    
    * **multi-platform**: Python is available for all major operating
      systems, Windows, Linux/Unix, MacOS X, most likely your mobile phone
      OS, etc.
    
    * a very readable language with clear non-verbose syntax
    
    * a language for which a large variety of high-quality packages are
      available for various applications, from web frameworks to scientific
      computing.
    
    * a language very easy to interface with other languages, in particular C
      and C++.
    
    * Some other features of the language are illustrated just below. For
      example, Python is an object-oriented language, with dynamic typing
      (an object's type can change during the course of a program).
    
    
    See http://www.python.org/about/ for more information about
    distinguishing features of Python.

.. toctree::
    :maxdepth: 1

    first_steps.rst
    pythonxy.rst
    basic_types.rst
    assignment.rst
    control_flow.rst
    functions.rst
    reusing_code.rst
    io.rst
    standard_library.rst
    exceptions.rst
    oop.rst

.. rubric:: 脚注

.. [*] 日本語訳 http://www.python.jp/doc/release/tutorial/
