科学計算：どうして Python?
==========================

.. Scientific computing: why Python?
    =================================

.. only:: latex

    :authors: Fernando Perez, Emmanuelle Gouillart

..
    .. image:: phd053104s.png
      :align: center

科学者が必要とするもの
======================

.. The scientist's needs
    ---------------------

* データを得る（シミュレーション, 実験制御）

* データを操作したり加工する

* 結果を可視化する...何をやっているか理解するために!

* 結果を伝える：レポートや出版, プレゼンテーションのための図を作る

..
  * Get data (simulation, experiment control)
  * Manipulate and process data.
  * Visualize results...to understand what we are doing!
  * Communicate on results: produce figures for reports or publications,
    write presentations.

必要なものの列挙
----------------

.. Specifications
    --------------

* 古典的な数値計算手法や基本的な動作などの既存の **積み木** が豊富にある：曲線を描く,
  Fourier 変換, フィッティングアルゴリズムを再プログラミングしたくありません.
  車輪の再発明はするな!

* 学習が容易：計算機科学は科学者の仕事ではないし, 科学者が教育することでもありません.
  ただ, 曲線を描きたい, 信号を平滑にしたい, Fourier 変換を数分で行いたいのです.

* 共同研究者や学生, 顧客と簡単に意思伝達ができ, コードが研究室や企業の中で機能する：
  コードは本のように読めるものでなければいけません.
  だから, プログラミング言語は構文の中の記号やコードの読者の理解を
  数学, 科学的な理解から反らすようなルーチンは少なくあるべきです.

* 迅速に実行できる効率的なコード...だとしても, 書くのに多くの時間をかけるものは, 速くても役に立ちません.
  つまり, 書くことと実行することの両方の速度が必要です.

* できれば, すべてを一つの環境/言語で済ませたい,
  新しい問題それぞれを解決するのに新しいソフトウェアを学ぶことは避けたいですよね.

..
    * Rich collection of already existing **bricks** corresponding to classical
      numerical methods or basic actions: we don't want to re-program the
      plotting of a curve, a Fourier transform or a fitting algorithm. Don't
      reinvent the wheel!
    
    * Easy to learn: computer science neither is our job nor our education. We
      want to be able to draw a curve, smooth a signal, do a Fourier transform
      in a few minutes.
    
    * Easy communication with collaborators, students, customers, to make the code
      live within a labo or a company: the code should be as readable as a book.
      Thus, the language should contain as few syntax symbols or unneeded routines
      that would divert the reader from the mathematical or scientific understanding
      of the code.
    
    * Efficient code that executes quickly...But needless to say that a very fast
      code becomes useless if we spend too much time writing it. So, we need both
      a quick development time and a quick execution time.
    
    * A single environment/language for everything, if possible, to avoid learning
      a new software for each new problem.


現存する解法
------------

.. Existing solutions
    ------------------

どの解法が科学者にとって役に立つのか?

.. Which solutions do the scientists use to work?

**コンパイラ言語：C, C++, Fortran, 等**

* 利点：

  * とても速い.
    最適化したコンパイラがある.
    強烈に重い計算では, これらの言語よりいい性能を出すのは困難です.

  * 非常に最適化されたいくつかライブラリはこれらの言語のために書かれています.
    例：blas（ベクトル, 行列演算）

* 欠点：

  * とても使いにくい:開発がインタラクティブにできない,
    コンパイルしなければいけない,
    構文が冗長（ ``&``, ``::``, ``}}``, ``;`` 等）,
    手動でのメモリ管理（Cでは油断なりません）.
    これらの言語は非計算機科学者にとっては **難しい言語** です.

..
    **Compiled languages: C, C++, Fortran, etc.**
    
    * Advantages:
    
      * Very fast. Very optimized compilers. For heavy computations, it's difficult
        to outperform these languages.
    
      * Some very optimized scientific libraries have been written for these
        languages. Ex: blas (vector/matrix operations)
    
    * Drawbacks:
    
      * Painful usage: no interactivity during development,
        mandatory compilation steps, verbose syntax (&, ::, }}, ; etc.),
        manual memory management (tricky in C). These are **difficult
        languages** for non computer scientists.


**スクリプト言語：Matlab**

* 利点：

  * 様々な領域に渡った膨大なアルゴリズムが収集された豊富なライブラリがある.
    これらのライブラリはコンパイラ言語で書かれているので速い.

  * 快適な開発環境：包括的でまとまったヘルプ, 統合開発環境等.

  * 商用サポートが得られる.

* 欠点：

  * 基本となる言語が粗末で高度なユーザにとっては制限が多い.

  * freeでない.

..
    **Scripting languages: Matlab**
    
    * Advantages:
    
      * Very rich collection of libraries with numerous algorithms, for many
        different domains. Fast execution because these libraries are often written
        in a compiled language.
    
      * Pleasant development environment: comprehensive and well organized help,
        integrated editor, etc.
    
      * Commercial support is available.
    
    * Drawbacks:
    
      * Base language is quite poor and can become restrictive for advanced users.
    
      * Not free.

**他のスクリプト言語：Scilab, Octave, Igor, R, IDL, 等**

* 利点：

  * オープンソースで free. そうでないものも Matlab より安い.

  * いくつかの機能がとても先進的（R は統計, Igor は図等）.

* 欠点：

  * Matlab と比較すると利用できるアルゴリズムは少ない,
    より先進的とはいえない.

  * いくつかのソフトウェアは一つの領域に専念している.
    例：Gnuplot や xmgrace は曲線を描く専門.
    これらのプログラムは強力だが, 曲線を描くなど一つの使い方に制限されてしまう.

.. **Other script languages: Scilab, Octave, Igor, R, IDL, etc.**
    
    * Advantages:
    
      * Open-source, free, or at least cheaper than Matlab.
    
      * Some features can be very advanced (statistics in R, figures in Igor, etc.)
    
    * Drawbacks:
    
      * fewer available algorithms than in Matlab, and the language
        is not more advanced.
    
      * Some softwares are dedicated to one domain. Ex: Gnuplot or xmgrace
        to draw curves. These programs are very powerful, but they are
        restricted to a single type of usage, such as plotting.

**Python はどうなの?**

..  **What about Python?**

* 利点：

  * 科学計算向けの豊富なライブラリ(でも Matlab よりすこし少ない)

  * よく練られた言語で, 読みやすく, 構造がはっきりしたコードが書ける：思ったとおりのコードが書ける.

  * 科学計算以外の仕事をするライブラリがたくさんある（web サーバ管理, シリアルポートアクセス等）

  * free なオープンソースソフトウェアで, 様々なコミュニティで広く使われている.

* 欠点：

  * 開発環境は, 例えば Matlab と比べると少し使いにくい (より geek 向け).

  * 専門向けのソフトウェアやツールにあるアルゴリズム全てがあるわけではない.

..
    * Advantages:
    
      * Very rich scientific computing libraries (a bit less than Matlab,
        though)
    
      * Well-thought language, allowing to write very readable and well structured
        code: we "code what we think".
    
      * Many libraries for other tasks than scientific computing (web server
        management, serial port access, etc.)
    
      * Free and open-source software, widely spread, with a vibrant community.
    
      * Drawbacks:
    
      * less pleasant development environment than, for example, Matlab. (More
        geek-oriented).
    
      * Not all the algorithms that can be found in more specialized
        softwares or toolboxes.

