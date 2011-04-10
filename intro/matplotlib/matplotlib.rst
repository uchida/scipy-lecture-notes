Matplotlib
==========

.. only:: latex

    :author: Mike Müller

序論
----

.. Introduction
.. ------------

``matplotlib`` はおそらく2次元グラフィック用の Python パッケージの決定版です.
高速なデータの可視化手法や出版品質の図を多くのフォーマットで提供します.
これから対話モードで matplotlib の機能を調べていきましょう.
ほとんどの状況は対話モードですませることができます.
またオブジェクト指向インターフェースとともに提供されるクラスライブラリについても触れます.

.. ``matplotlib`` is probably the single most used Python package
.. for 2D-graphics. It provides both a very quick way to visualize
.. data from Python and publication-quality figures in many formats.
.. We are going to explore matplotlib in interactive mode covering
.. most common cases. We also look at the class library which is provided
.. with an object-oriented interface.

IPython
-------

IPython は多くの機能をもった高機能な Python 対話型シェルです.
IPython は名前つきの入出力, シェルコマンド, 改良されたデバッグ機能など他にも多くの機能があります.
IPython をコマンドラインで ``-pylab`` 引数を与えて起動すると,
Matlab や Mathematica のような機能をもった対話的な
``matplotlib`` セッションが使えるようになります.

.. IPython is an enhanced interactive Python shell that has lots of
.. interesting features including named inputs and outputs,
.. access to shell commands, improved debugging and many more.
.. When we start it with the command line argument ``-pylab``, it allows
.. interactive ``matplotlib`` sessions that has Matlab/Mathematica-like
.. functionality.

pylab
-----

``pylab`` は ``matplotlib`` のオブジェクト指向ライブラリに対する手続き的インターフェースを提供します.
このモデルは Matlab(TM) をお手本にしています.
そのため ``pylab`` の大部分の作図コマンドは Matlab(TM) に類似していて
同じような引数をとります.
重要なコマンドは対話的な例で説明します.


.. ``pylab`` provides a procedural interface to the ``matplotlib``
.. object-oriented plotting library. It is modeled closely
.. after Matlab(TM). Therefore, the majority of plotting
.. commands in ``pylab`` has Matlab(TM) analogs with similar arguments.
.. Important commands are explained with interactive examples.

単純な作図
----------

.. Simple Plots
.. ------------

対話的セッションを始めてみましょう::

    $ ipython -pylab

.. Let's start an interactive session::

..     $python ipython.py -pylab

こうすると, IPython プロンプトが起ち上がります：

.. This brings us to the IPython prompt:

.. code-block:: python

    IPython 0.8.1 -- An enhanced Interactive Python.
    ?       -> Introduction to IPython's features.
    %magic  -> Information about IPython's 'magic' % functions.
    help    -> Python's own help system.
    object? -> Details about 'object'. ?object also works, ?? prints more.
    
    Welcome to pylab, a matplotlib-based Python environment.
    For more information, type 'help(pylab)'.
        
    In [1]:

さぁ, 最初の本当に単純な例を作図してみましょう.

.. Now we can make our first, really simple plot:

.. code-block:: python

    In [1]: plot(range(10))
    Out[1]: [<matplotlib.lines.Line2D instance at 0x01AA26E8>]

    In [2]:

0 から 9 までの数字が作図されました：

.. The numbers form 0 through 9 are plotted:

.. image:: figures/simple.png
    :width: 50%


機能を対話的に追加して作図できます：

.. Now we can interactively add features to or plot:

.. code-block:: python

    In [2]: xlabel('measured')
    Out[2]: <matplotlib.text.Text instance at 0x01A9D210>

    In [3]: ylabel('calculated')
    Out[3]: <matplotlib.text.Text instance at 0x01A9D918>

    In [4]: title('Measured vs. calculated')
    Out[4]: <matplotlib.text.Text instance at 0x01A9DF80>

    In [5]: grid(True)

    In [6]:

レファレンスをつけて作図できます：

.. We get a reference to our plot:

.. code-block:: python

    In [6]: my_plot = gca()

最初に作図したラインに対してレファレンスをつけられます：

.. and to our line we plotted, which is the first in the plot:

.. code-block:: python
    
    In [7]: line = my_plot.lines[0]

``set_something`` メソッドでプロパティをつけることもできます：

.. Now we can set properties using ``set_something`` methods:

.. code-block:: python

    In [8]: line.set_marker('o')

もしくは ``setp`` 関数でも：

.. or the ``setp`` function:

.. code-block:: python

    In [9]: setp(line, color='g')
    Out[9]: [None]

新しいプロパティを適用するには画面の再描画が必要です：

.. To apply the new properties we need to redraw the screen:

.. code-block:: python

    In [10]: draw()

ひとつの作図に対しいくつかのラインを追加できます：

.. We can also add several lines to one plot:

.. code-block:: python  

    In [1]: x = arange(100)

    In [2]: linear = arange(100)

    In [3]: square = [v * v for v in arange(0, 10, 0.1)]

    In [4]: lines = plot(x, linear, x, square)
    
凡例をつけてみましょう：

.. Let's add a legend:

.. code-block:: python

    In [5]: legend(('linear', 'square'))
    Out[5]: <matplotlib.legend.Legend instance at 0x01BBC170>

見栄えにいくつか気になる部分があります.
このグラフはどこかにやってしまいたいと思うのではないでしょうか.
古いグラフを消してしまいましょう：

.. This does not look particularly nice. We would rather like to have
.. it at the left. So we clean the old graph:

.. code-block:: python

    In [6]: clf()

そして改めて新しいスタイル（直線に対しては十字のマーカーと緑の点線,
2次曲線に対しては円のマーカーと破線で描く）でラインを書いてみます：

.. and print it anew providing new line styles (a green dotted
.. line with crosses for the linear and a red dashed line with
.. circles for the square graph):

.. code-block:: python

    In [7]: lines = plot(x, linear, 'g:+', x, square, 'r--o')

凡例は左上の角に追加してみます：

.. Now we add the legend at the upper left corner:

.. code-block:: python

    In [8]: l = legend(('linear', 'square'), loc='upper left')

結果はこうなります：

.. The result looks like this:

.. image:: figures/legend.png
    :width: 50%


練習問題
++++++++

1) 簡単なステップ関数を作図しましょう.
   範囲は 0 から 3 まででステップの幅は 0.01 とします.

2) ラインを赤にましょう. サイズ 5 のダイヤモンドマーカーも追加しましょう.

3) 凡例とグリッドを追加しましょう.

.. Exercises
.. +++++++++

.. 1) Plot a simple graph of a sinus function in the range 0 to 3
..    with a step size of 0.01.

.. 2) Make the line red. Add diamond-shaped markers with size of 5.

.. 3) Add a legend and a grid to the plot.


プロパティ
----------

.. Properties
.. ----------

ここまででは, ラインに対するプロパティを使ってきました.
その中ではプロパティを設定する3つの方法がありました：

1) 作成するときにキーワード引数として与える：
   ``plot(x, linear, 'g:+', x, square, 'r--o')``

2) ``setp`` 関数で与える： ``setp(line, color='g')``

3) ``set_something`` メソッドを使う： ``line.set_marker('o')``

.. So far we have used properties for the lines.
.. There are three possibilities to set them:

.. 1) as keyword arguments at creation time:
.. ``plot(x, linear, 'g:+', x, square, 'r--o')``.

.. 2) with the function ``setp``: ``setp(line, color='g')``.

.. 3) using the ``set_something`` methods: ``line.set_marker('o')``

ラインは以下のテーブルに挙げたプロパティをもっています：

=============== ===========================================================================
プロパティ      値
=============== ===========================================================================
alpha           0 から 1 までのアルファ透過率
antialiased     True または False - アンチエイリアスを使うか
color           matplotlib のカラー引数
data_clipping   whether to use numeric to clip data [*]_
label           凡例のために使われる文字列
linestyle       ``-`` ``:`` ``-.`` ``-`` のどれか
linewidth       ラインの幅, 浮動小数点数 単位はポイント
marker          ``+`` ``,`` ``o`` ``.`` ``s`` ``v`` ``x`` ``>`` ``<`` などのどれか
markeredgewidth マーカー記号の周りのラインの幅
markeredgecolor マーカーの端の色（マーカーが使われる場合）
markerfacecolor マーカーの表面の色（マーカーが使われる場合）
markersize      マーカーのサイズ 単位はポイント
=============== ===========================================================================

.. =============== ========================================
.. Property        Value
.. =============== ========================================
.. alpha           alpha transparency on 0-1 scale
.. antialiased     True or False - use antialised rendering
.. color           matplotlib color arg
.. data_clipping   whether to use numeric to clip data
.. label           string optionally used for legend
.. linestyle       one of - : -. -
.. linewidth       float, the line width in points
.. marker          one of + , o . s v x > <, etc
.. markeredgewidth line width around the marker symbol
.. markeredgecolor edge color if a marker is used
.. markerfacecolor face color if a marker is used
.. markersize      size of the marker in points
.. =============== ========================================

ラインのスタイルを指定する記号はたくさんあります.

=========== =================================================
記号        説明
=========== =================================================
 ``-``      実線 solid line
 ``--``     破線 dashed line
 ``-.``     一点鎖線 dash-dot line
 ``:``      点線 dotted line
 ``.``      ポイント points
 ``,``      ピクセル pixels
 ``o``      円 circle symbols
 ``^``      上向き三角形 triangle up symbols
 ``v``      下向き三角形 triangle down symbols
 ``<``      左向き三角形 triangle left symbols
 ``>``      右向き三角形 triangle right symbols
 ``s``      四角形 square symbols
 ``+``      プラス plus symbols
 ``x``      バツ印 cross symbols
 ``D``      ダイアモンド diamond symbols
 ``d``      細いダイアモンド thin diamond symbols
 ``1``      下向き三脚 tripod down symbols
 ``2``      上向き三脚 tripod up symbols
 ``3``      左向き三脚 tripod left symbols
 ``4``      右向き三脚 tripod right symbols
 ``h``      六角形 hexagon symbols
 ``H``      角度を変えた六角形 rotated hexagon symbols
 ``p``      五角形 pentagon symbols
 ``|``      垂直棒 vertical line symbols
 ``_``      水平棒 horizontal line symbols
 ``steps``  gnuplot スタイルの 'steps' # キーワード引数のみ
=========== =================================================

.. There are many line styles that can be specified with symbols:

.. =========== ======================================
.. Symbol      Description
.. =========== ======================================
..     \-      solid line
..     --      dashed line
..     -.      dash-dot line
..     :       dotted line
..     .       points
..     ,       pixels
..     o       circle symbols
..     ^       triangle up symbols
..     v       triangle down symbols
..     <       triangle left symbols
..     >       triangle right symbols
..     s       square symbols
..    \+       plus symbols
..     x       cross symbols
..     D       diamond symbols
..     d       thin diamond symbols
..     1       tripod down symbols
..     2       tripod up symbols
..     3       tripod left symbols
..     4       tripod right symbols
..     h       hexagon symbols
..     H       rotated hexagon symbols
..     p       pentagon symbols
..    \|       vertical line symbols
..     \_       horizontal line symbols
..     steps   use gnuplot style 'steps' # kwarg only
.. =========== ======================================

カラーはいろいろな形で与えることができます：1文字での省略形,
0 から 1 までのグレースケール, RGB は html で動作する色の名前のようにして16進数やタプル形式で与えることもできます.

1文字での略称は素早く書けて扱いやすいでしょう.
以下をみればすぐに使えるようになるでしょう：

============ =========
省略形       カラー
============ =========
  ``b``      blue
  ``g``      green
  ``r``      red
  ``c``      cyan
  ``m``      magenta
  ``y``      yellow
  ``k``      black
  ``w``      white
============ =========

.. Colors can be given in many ways: one-letter abbreviations, gray scale
.. intensity from 0 to 1, RGB in hex and tuple format as well as
.. any legal html color name.

.. The one-letter abbreviations are very handy for quick work.
.. With following you can get quite a few things done:

.. ============ =========
.. Abbreviation Color
.. ============ =========
..     b        blue
..     g        green
..     r        red
..     c        cyan
..     m        magenta
..     y        yellow
..     k        black
..     w        white
.. ============ =========

ライン以外のオブジェクトもプロパティを持っています.
以下のテーブルはテキストのプロパティです.

.. Other objects also have properties. The following table list
.. the text properties:

==================== ========================================================== 
プロパティ           値
==================== ==========================================================
alpha                0 から 1 までのアルファ透過率
color                matplotlib カラー引数
family               フォントファミリー 例：sans-serif, cursive, fantasy
fontangle            フォントの傾き normal, italic, oblique のどれか
horizontalalignment  left, right, center のどれか
multialignment       left, right, center のどれか, 複数行のときのみ
name                 フォントの名前 例：Sans, Courier, Helvetica
position             位置 x,y
variant              フォントの異型 例：normal, small-caps
rotation             テキストの回転角 単位は度
size                 フォントサイズ 単位はポイント 例：8, 10, 12
style                フォントのスタイル normal, italic, oblique のどれか
text                 テキストの文字列自身
verticalalignment    top, bottom または center
weight               フォントのウェイト 例：normal, bold, heavy, light
==================== ==========================================================

.. ==================== ========================================================== 
.. Property             Value
.. ==================== ==========================================================
.. alpha                alpha transparency on 0-1 scale
.. color                matplotlib color arg
.. family               set the font family, eg sans-serif, cursive, fantasy
.. fontangle            the font slant, one of normal, italic, oblique
.. horizontalalignment  left, right or center
.. multialignment       left, right or center only for multiline strings
.. name                 font name, eg, Sans, Courier, Helvetica
.. position             x,y location
.. variant              font variant, eg normal, small-caps
.. rotation             angle in degrees for rotated text
.. size                 fontsize in points, eg, 8, 10, 12
.. style                font style, one of normal, italic, oblique
.. text                 set the text string itself
.. verticalalignment    top, bottom or center
.. weight               font weight, e.g. normal, bold, heavy, light
.. ==================== ==========================================================

練習問題
++++++++

1) 異なるスタイルを適用して作図しなさい.
   ラインのカラー, 太さやマーカーのサイズ, 種類を変えなさい.
   異なるスタイルを実験してみなさい.

.. Exercise
.. ++++++++

.. 1) Apply different line styles to a plot. Change line color and
..    thickness as well as the size and the kind of the marker.
..    Experiment with different styles.


テキスト
--------

.. Text
.. ----

ここまでで既に図にテキストを追加するコマンド ``xlabel``, ``ylabel``
そして ``title`` を使いました.

特定の位置にテキストを配置する関数は2つあります.
``text`` はデータの座標にテキストを追加します：

.. We've already used some commands to add text to our figure: ``xlabel``
.. ``ylabel``, and ``title``.

.. There are two functions to put text at a defined position.
.. ``text`` adds the text with data coordinates:

.. code-block:: python

    In [2]: plot(arange(10))
    In [3]: t1 = text(5, 5, 'Text in the middle')

``figtext`` は 0 から 1 までの figure 座標を使います.

.. ``figtext`` uses figure coordinates form 0 to 1:

.. code-block:: python   

    In [4]: t2 = figtext(0.8, 0.8, 'Upper right text')


.. image:: figures/text.png
    :width: 50%
    
``matplotlib`` は TeX の数式をサポートしています.
そのため ``r'$\pi$`` はこのように表示されます：

.. ``matplotlib`` supports TeX mathematical expression. So ``r'$\pi$'``
.. will show up as:

.. math::

     \pi


もしテキストがどこに配置されるかをより制御したい場合
annotate を使います：

.. code-block:: python

    In [4]: ax = gcd()
    In [5]: ax.annotate('Here is something special', xy = (1, 1))

.. If you want to get more control over where the text goes, you
.. use annotations:

.. .. code-block:: python

..     In [4]: ax.annotate('Here is something special', xy = (1, 1))

データの中の (1, 1) の位置にテキストを追加します.
テキストの位置をカスタマイズするための多くのオプションがあります.
``textcoordes`` と ``xycoordes`` 引数は ``x``, ``y`` の座標形を指定します：

==================== ===================================================
引数                 座標形
==================== ===================================================
figure points        ポイントを単位として, 原点を図の左下の角にとる
figure pixels        ピクセルを単位として, 原点を図の左下の角にとる
figure fraction      0,0 が図の左下に対応し 1,1 が右上に対応する
axes points          ポイントを単位として, 原点を軸の左下の角にとる 
axes pixels          ピクセルを単位として, 原点を軸の左下の角にとる
axes fraction        0,0 が軸の左下に対応し 1,1 が右上に対応する
data                 データの座標軸を使う
==================== ===================================================

.. We will write the text at the position (1, 1) in terms of data.
.. There are many optional arguments that help to customize
.. the position of the text.  The arguments ``textcoords`` and
.. ``xycoords`` specifies what ``x`` and ``y`` mean: 

.. ==================== ===================================================
.. argument             coordinate system
.. ==================== ===================================================
.. figure points        points from the lower left corner of the figure
.. figure pixels        pixels from the lower left corner of the figure
.. figure fraction      0,0 is lower left of figure and 1,1 is upper, right
.. axes points          points from lower left corner of axes
.. axes pixels          pixels from lower left corner of axes
.. axes fraction        0,1 is lower left of axes and 1,1 is upper right
.. data                 use the axes data coordinate system
.. ==================== ===================================================

``xycoords`` が与えららないときにはテキストは ``xy`` で指定した位置に書かれます.

.. If we do not supply ``xycoords``, the text will be written at ``xy``.

さらに, 詳細な説明をするための矢印を使うこともできます：

.. Furthermore, we can use an arrow whose appearance can also be described
.. in detail:

.. code-block:: python

    In [14]: plot(arange(10))
    Out[14]: [<matplotlib.lines.Line2D instance at 0x01BB15D0>]

    In [15]: ax = gca()

    In [16]: ax.annotate('Here is something special', xy = (2, 1), xytext=(1,5))
    Out[16]: <matplotlib.text.Annotation instance at 0x01BB1648>

    In [17]: ax.annotate('Here is something special', xy = (2, 1), xytext=(1,5),
       ....: arrowprops={'facecolor': 'r'})
    

練習問題
++++++++

1) ラインの2箇所にテキストで注釈をつけなさい.
   緑と赤の矢印を使い, ``figure points`` と ``data`` に応じて揃えなさい.

.. Exercise
.. ++++++++

.. 1) Annotate a line at two places with text. Use green and red arrows
..    and align it according to ``figure points`` and ``data``.

目盛
----

.. Ticks
.. -----

どこに, 何を
++++++++++++

.. Where and What
.. ++++++++++++++

適切に整形された目盛 (ticks) は図を出版品質にするのに重要な役割を果します.
``matplotlib`` では目盛の総合的な設定ができます.
目盛がどこに現われるか指定する目盛位置指定子 (tick locators),
目盛の見た目を変更する目盛書式指定子 (tick formatters) があります.
大きい目盛と小さな目盛はお互い独立に位置と書式を指定できます.
デフォルトでは小さい目盛は表示されません,
つまり小さい目盛の位置指定子は ``NullLocator`` （後述）となっているため,
空リストのみが受けつけられます.


.. Well formated ticks are an important part of publishing-ready
.. figures. ``matplotlib`` provides a totally configurable system
.. for ticks. There are tick locators to specify where ticks
.. should appear and tick formatters to make ticks look like the way you want.
.. Major and minor ticks can be located and formated independently from
.. each other. Per default minor ticks are not shown, i.e. there is only
.. an empty list for them because it is as ``NullLocator`` (see below).

目盛位置指定子
++++++++++++++

.. Tick Locators
.. +++++++++++++

色々な要求に答えるためにいくつかの位置指定子があります：

=============== ===========================================================================
クラス          説明
=============== ===========================================================================
NullLocator     目盛無し
IndexLocator    インデクスを作図したときの為の指定子（例： ``x = range(len(y))`` のとき）
LinearLocator   最小から最大までの均等に配置する目盛
LogLocator      最小から最大までの対数目盛
MultipleLocator 目盛と範囲をそれぞれ独立にとります, どちらも整数か浮動小数点数で指定します
AutoLocator     MultipleLocator を選択し, 動的に変更します
=============== ===========================================================================

.. There are several locators for different kind of requirements:

.. =============== ===============================================================
.. Class           Description
.. =============== ===============================================================
.. NullLocator     no ticks
.. IndexLocator    locator for index plots (e.g. where ``x = range(len(y)``)
.. LinearLocator   evenly spaced ticks from min to max
.. LogLocator      logarithmically ticks from min to max
.. MultipleLocator ticks and range are a multiple of base; either integer or float
.. AutoLocator     choose a MultipleLocator and dynamically reassign
.. =============== ===============================================================

これら全ての位置指定子は ``matplotlib.ticker.Locator`` 基底クラスから派生しています.
このクラスから派生して独自の位置指定子を作成することもできます.

時間を目盛として扱う場合は少々技巧的になりえます.
そのため ``matplitlib`` は特別な位置指定子 ``matplotlib.dates`` を提供しています.

======================= ===========================================
クラス                  説明
======================= ===========================================
MinuteLocator           分の位置指定
HourLocator             時間の位置指定
DayLocator              月の中の日を位置指定
WeekdayLocator          週の中の日を位置指定 例：MO, TU
MonthLocator            月を位置指定 例：10月には10が対応
YearLocator             年を位置指定（複数の目盛の基準を持ちます）
RRuleLocator            matplotlib.dates.rrule を使って位置指定
======================= ===========================================

.. All of these locators derive from the base class ``matplotlib.ticker.Locator``.
.. You can make your own locator deriving from it.

.. Handling dates as ticks can be especially tricky. Therefore, ``matplotlib``
.. provides special locators in ``matplotlib.dates``:

.. ======================= ===========================================
.. Class                   Description
.. ======================= ===========================================
.. MinuteLocator           locate minutes
.. HourLocator             locate hours
.. DayLocator              locate specified days of the month
.. WeekdayLocator          locate days of the week, e.g. MO, TU
.. MonthLocator            locate months, e.g. 10 for October
.. YearLocator             locate years that are multiples of base
.. RRuleLocator            locate using a matplotlib.dates.rrule
.. ======================= ===========================================


目盛書式指定子
++++++++++++++

.. Tick Formatters
.. +++++++++++++++

位置指定子と同様に書式指定子は以下のようになっています：

.. Similarly to locators, there are formatters:

======================= ===============================================
クラス                  説明
======================= ===============================================
NullFormatter           目盛にラベルをつけない
FixedFormatter          ラベルに文字列を手動で設定
FuncFormatter           ラベルにユーザー定義関数を設定
FormatStrFormatter      sprintf フォーマット文字列を使う
IndexFormatter          目盛の位置毎に固定文字列を巡回
ScalarFormatter         スカラー値に対するデフォルトの書式指定子；
                        フォーマット文字列を自動で設定
LogFormatter            対数軸に対する書式指定子
DateFormatter           時間のフォーマットの為に strftime 文字列を使う
======================= ===============================================

.. ======================= =============================================
.. Class                   Description
.. ======================= =============================================
.. NullFormatter           no labels on the ticks
.. FixedFormatter          set the strings manually for the labels
.. FuncFormatter           user defined function sets the labels
.. FormatStrFormatter      use a sprintf format string
.. IndexFormatter          cycle through fixed strings by tick position
.. ScalarFormatter         default formatter for scalars;
..                         autopick the fmt string
.. LogFormatter            formatter for log axes
.. DateFormatter           use an strftime string to format the date
.. ======================= =============================================

これらの書式指定子は全て ``matplotlib.ticker.Formatter`` 基底クラスから派生しています.
このクラスから派生して独自の位置指定子を作成することもできます.

.. All of these formatters derive from the base class ``matplotlib.ticker.Formatter``.
.. You can make your own formatter deriving from it.

大きな目盛を2に小さな目盛を2に設定します.
さらに ``FormatStrFormatter`` で10進数でフォーマットします.

.. Now we set our major locator to 2 and the minor locator
.. to 1. We also format the numbers as decimals using the
.. ``FormatStrFormatter``:

.. code-block:: python


    In [5]: major_locator = MultipleLocator(2)

    In [6]: major_formatter = FormatStrFormatter('%5.2f')

    In [7]: minor_locator = MultipleLocator(1)

    In [8]: ax.xaxis.set_major_locator(major_locator)

    In [9]: ax.xaxis.set_minor_locator(minor_locator)

    In [10]: ax.xaxis.set_major_formatter(major_formatter)

    In [10]: draw()

図の再描画後には x 軸がこうなります：

.. After we redraw the figure our x axis should look like this:

.. raw:: pdf

     Spacer 0 10

.. image:: figures/ticks.png
    :width: 50%


練習問題
++++++++

1) 1年の日付のグラフを作図しましょう.
   x 軸は1日毎にとり, ビルトインの ``datetime`` モジュールを使いましょう.

2) 月の始めの日だけを表示するように書式指定しましょう.

3) 年の表示, 非表示を切り替えましょう.
   月の数での表示と月の名前の最初の3文字での表示を切り替えましょう.


.. Exercises
.. +++++++++

.. 1) Plot a graph with dates for one year with daily
..    values at the x axis using the built-in module ``datetime``.

.. 2) Format the dates in such a way that only the first day
..    of the month is shown.

.. 3) Display the dates with and without the year. Show the month
..    as number and as first three letters of the month name.

Figure, Subplot そして Axes
---------------------------

.. Figures, Subplots, and Axes
.. ---------------------------

階層
++++
    
.. The Hierarchy
.. +++++++++++++

ここまでの内容の中で実は暗黙の内に figure と axes を作成していました.
この作成法は素早く作図できるため手軽に扱えます.
``figure``, ``subplot`` さらに ``axes`` を明示的に使うことで
より細かく制御して表示できます.
``matplotlib`` では ``figure`` はユーザーインターフェースのウィンドウ全体のことを指します.
この ``figure`` の内部は subplot になりえます.
``subplot`` が作図内の規則的に並んだ格子上に位置している場合,
``axes`` は ``figure`` 内のどこにでも配置できます.
意図に応じて暗黙的, 明示的に呼び出す方法の両方を使いわけると便利でしょう.
ここまででは明示的に figure や subfigure を呼び出していませんでしたが, 
``matplotlib`` は ``plot`` を呼び出すときに現在の axes を取得するため
``gca()`` を呼び出し, ``gca`` は現在の figure を取得するために ``gcf()`` を呼び出します.
もし, 現在の figure がない場合には ``figure()`` が呼び出され, figure が作成されます,
より正確にいえば, ``subplot(111)`` が作られます.
詳しくみてみましょう.


.. So far we have used implicit figure and axes creation.
.. This is handy for fast plots. We can have more control over
.. the display using ``figure``, ``subplot``, and ``axes`` explicitly.
.. A ``figure`` in ``matplotlib`` means the whole window in the
.. user interface. Within this ``figure`` there can be subplots.
.. While ``subplot`` positions the plots in a regular grid, ``axes``
.. allows free placement within the ``figure``. Both can
.. be useful depending on your intention.
.. We've already work with figures and subplots without explicitly
.. calling them.  When we call ``plot`` ``matplotlib`` calls ``gca()`` to
.. get the current axes and ``gca`` in turn calls ``gcf()`` to
.. get the current figure. If there is none it calls ``figure()``
.. to make one, strictly speaking, to make a ``subplot(111)``.
.. Let's look at the details.

Figures
++++++++

``figure`` はタイトルが "Figure #" となっている GUI ウィンドウです.
Figure の番号は0から始まる Python のスタイルとは違い, 1から始まります. 
これは明らかに MATLAB のスタイルに起因しています.
figure の見た目を決定する以下のいくつかのパラメータがあります：

==============    ======================= ============================================
引数              デフォルト値            説明
==============    ======================= ============================================
``num``           ``1``                   figure の数
``figsize``       ``figure.figsize``      figure の大きさ (width, height) 単位はインチ
``dpi``           ``figure.dpi``          解像度 単位は dpi（1インチ辺りのドット数）
``facecolor``     ``figure.facecolor``    背景色
``edgecolor``     ``figure.edgecolor``    背景の端の色
``frameon``       ``True``                figure の枠を描くかどうか
==============    ======================= ============================================

.. A ``figure`` is  the windows in the GUI that has "Figure #" as
.. title. Figures are numbered starting from 1 as opposed to the
.. normal Python way starting from 0. This is clearly MATLAB-style.
.. There are several parameters that determine how the figure
.. looks like:

.. ==============    ======================= ============================================
.. Argument          Default                 Description
.. ==============    ======================= ============================================
.. ``num``           ``1``                    number of figure
.. ``figsize``       ``figure.figsize``       figure size in in inches (width, height)
.. ``dpi``           ``figure.dpi``           resolution in dots per inch
.. ``facecolor``     ``figure.facecolor``     color of the drawing background
.. ``edgecolor``     ``figure.edgecolor``     color of edge around the drawing background
.. ``frameon``       ``True``                 draw figure frame or not
.. ==============    ======================= ============================================

多くの場合に使われることになるデフォルト値は設定ファイルで指定することができます.
頻繁に変更されるのは figure の番号だけです.

.. The defaults can be specified in the resource file and
.. will be used most of the time. Only the number of the figure
.. is frequently changed.

GUI を使っている場合, 右上角の x ボタンをクリックすれば figure が閉じます.
しかし, ``close`` を呼びだすことで, figure をプログラムから閉じることができます.
引数によって閉じるものが違い, 以下の場合があります
(1) 現在の figure （引数無しの場合）
(2) 特定の figure （figure 番号または figure のインスタンスを引数にした場合）
(3) 全ての figure （引数として ``all`` を与えた場合）

.. When you work with the GUI you can close a figure by clicking on the
.. x in the upper right corner. But you can close a figure
.. programmatically by calling ``close``. Depending on the argument it closes
.. (1) the current figure (no argument), (2) a specific figure (figure number or figure
.. instance as argument), or (3) all figures (``all`` as argument).

他のオブジェクトと同じように ``setp`` か ``set_something`` メソッドで
figure のプロパティを設定できます.

.. As with other objects, you can set figure properties also ``setp``
.. or with the ``set_something`` methods.

Subplots
++++++++

``subplot`` を使うと図を規則的な格子の上に並べることができます.
使うためには行と列の数そして作図番号を指定する必要があります.
   
.. With ``subplot`` you can arrange plots in regular grid. You need to
.. specify the number of rows and columns and the number of the plot.

2行1列の図は ``subplot(211)`` と ``subplot(212)`` で作成します.
結果はこうなります：

.. A plot with two rows and one column is created with
.. ``subplot(211)`` and ``subplot(212)``. The result looks like this:

.. raw:: pdf

     Spacer 0 10

.. image:: figures/subplots_horizontal.png
    :width: 25%

横に並んだ2つの作図が欲しい場合には, 1行2列を ``subplot(121)`` と
``subplot(112)`` で作ります. 結果はこうなります：

.. If you want two plots side by side, you create one row and two columns
.. with ``subplot(121)`` and ``subplot(112)``. The result looks like this:

.. raw:: pdf

     Spacer 0 10

.. image:: figures/subplots_vertical.png
    :width: 25%

図を欲しい数だけ配置することができます.
2x2で配置したい場合は ``subplot(221)``,  ``subplot(222)``,
``subplot(223)``, ``subplot(224)`` で作ります. 結果はこうなります：

.. You can arrange as many figures as you want. A two-by-two arrangement can
.. be created with ``subplot(221)``,  ``subplot(222)``, ``subplot(223)``, and
.. ``subplot(224)``. The result looks like this:

.. raw:: pdf

     Spacer 0 10

.. image:: figures/subplots_four.png
    :width: 25%

全ての subplot に対しては目盛やラベルを付けたくないことがしばしばあります.
そのためには ``xticklabels`` か ``yticklabels`` を空リスト (``[]``) にします.
各 subplot には ``is_first_row``, ``is_first_col``, ``is_last_wor``, ``is_last_col``
メソッドが定義されています.
これらは外側の作図にのみ目盛やラベルを設定するのを助けてくれます.

.. Frequently, you don't want all subplots to have ticks or labels.
.. You can set the ``xticklabels`` or the ``yticklabels`` to an empty
.. list (``[]``). Every subplot defines the methods ``'is_first_row``,
.. ``is_first_col``, ``is_last_row``, ``is_last_col``. These can help to
.. set ticks and labels only for the outer pots.


Axes
++++

Axes は subplot によく似ていますが Axes は figure の任意の位置に作図できます.
つまり, 大きな作図の中に小さな作図を置きたい場合 ``axes`` を使います.

.. Axes are very similar to subplots but allow placement of plots
.. at any location in the figure.  So if we want to put a smaller
.. plot inside a bigger one we do so with ``axes``:

.. code-block:: python

    In [22]: plot(x)
    Out[22]: [<matplotlib.lines.Line2D instance at 0x02C9CE90>]

    In [23]: a = axes([0.2, 0.5, 0.25, 0.25])

    In [24]: plot(x)

結果はこうなります：

.. The result looks like this:


.. image:: figures/axes.png
    :width: 25%

練習問題
++++++++

1) 5x5 インチと 10x10 インチの2つの図を描きましょう.

2) 4つの subplot を figure に追加しましょう. 最外部の軸にのみ目盛とラベルをつけましょう.

3) 大きな作図の中に小さな作図を配置してみましょう.

.. .. 
    Exercises
.. +++++++++

.. 1) Draw two figures, one 5 by 5, one 10 by 10 inches.

.. 2) Add four subplots to one figure. Add labels and ticks only to
..    the outermost axes.

.. 3) Place a small plot in one bigger plot.



いろいろな作図
--------------

.. Other Types of Plots
.. --------------------

より多く
++++++++
    
.. Many More
.. +++++++++

ここまででは線の作図だけを扱ってきましたが,
``matplotlib`` は多くの作図法を提供しています.
これらの作図法の中からいくつか簡単に紹介します.
紹介する関数は多くのオプション引数を持っていますが,
それらについては扱いません.

.. So far we have used only line plots. ``matplotlib`` offers many more types
.. of plots. We will have a brief look at some of them. All functions have many
.. optional arguments that are not shown here.


棒グラフ
++++++++

.. Bar Charts
.. ++++++++++

``bar`` 関数は新たに棒グラフ (bar chart) を作成します：

.. The function ``bar`` creates a new bar chart:

.. code-block:: python

    bar([1, 2, 3], [4, 3, 7])

これで1, 2, 3に対応して4, 3, 7の高さの3つの棒ができるでしょう：

.. Now we have three bars starting at 1, 2, and 3 with height of
.. 4, 3, 7 respectively:

.. raw:: pdf

     Spacer 0 10

.. image:: figures/bar.png
            :width: 25%

デフォルトの column width は 0.8 です.
これは ``width`` を設定することで変更できます.
同様にして ``color`` や ``bottom`` も設定でき,
エラーバーも ``xerr`` や ``yerr`` で設定できます.

.. The default column width is 0.8. It can be changed with
.. common methods by setting ``width``. As it can be ``color`` and
.. ``bottom``, we can also set an error bar with ``yerr`` or ``xerr``.

水平棒グラフ
++++++++++++

.. Horizontal Bar Charts
.. +++++++++++++++++++++

``barh`` は垂直に並んだ棒グラフ (horizontal bar chart) を作成します.
同じデータを使って：

.. The function ``barh`` creates an vertical bar chart.
.. Using the same data:

.. code-block:: python

    barh([1, 2, 3], [4, 3, 7])

以下の図を得ます：

.. We get:

.. raw:: pdf

     Spacer 0 10

.. image:: figures/barh.png
            :width: 25%

不連続水平棒グラフ
++++++++++++++++++

.. Broken Horizontal Bar Charts
.. ++++++++++++++++++++++++++++

``broken_barh`` で垂直に不連続に並んだ棒グラフ
(broken horizontal bar charts) を作ることができます.
y 方向の開始点と幅と全ての x 方向の開始点と幅の対を指定します：

.. We can also have discontinuous vertical bars with ``broken_barh``.
.. We specify start and width of the range in y-direction and all
.. start-width pairs in x-direction:

.. code-block:: python

    yrange = (2, 1)
    xranges = ([0, 0.5], [1, 1], [4, 1])
    broken_barh(xranges, yrange)

作図の見栄えをよくするために y 軸の広がりを変更します.

.. We changes the extension of the y-axis to make plot look nicer:

.. code-block:: python

    ax = gca()
    ax.set_ylim(0, 5)
    (0, 5)
    draw()
    
そして以下の図を得ます：

.. and get this: 

.. raw:: pdf

     Spacer 0 10

.. image:: figures/broken_barh.png
            :width: 25%

箱ひげ図
++++++++

.. Box and Whisker Plots
.. +++++++++++++++++++++

箱ひげ図 (box and whisker plot) を描くことができます：

.. We can draw box and whisker plots:

.. code-block:: python

         boxplot((arange(2, 10), arange(1, 5)))

ひげを作図の内側に描きたいので, y 軸を増加させましょう：

.. We want to have the whiskers well within the plot and therefore
.. increase the y axis:

.. code-block:: python

         ax = gca()
         ax.set_ylim(0, 12)
         draw()

作図はこうみえるでしょう：

.. Our plot looks like this:

.. image:: figures/boxplot.png
            :width: 25%

ひげの幅は ``whis`` 引数によって決まり, デフォルト値は1.5です.
ひげの幅は ``whis*(75%-25%)`` 内の最も遠いデータまでの値をとります.

.. The range of the whiskers can be determined with the
.. argument ``whis``, which defaults to 1.5. The range of
.. the whiskers is between the most extreme data point
.. within ``whis*(75%-25%)`` of the data.


等高線図
++++++++

.. Contour Plots
.. +++++++++++++

等高線 (contour plot) をとることもできます.
x, y 座標の配列を定義します：

.. We can also do contour plots. We define arrays for the
.. x and y coordinates:

.. code-block:: python

    x = y = arange(10)

そして z 座標のために2次元配列を作ります：

.. and also a 2D array for z:

.. code-block:: python

    z = ones((10, 10))
    z[5,5] = 7
    z[2,1] = 3
    z[8,7] = 4
    z
    array([[ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
           [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
           [ 1.,  3.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
           [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
           [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
           [ 1.,  1.,  1.,  1.,  1.,  7.,  1.,  1.,  1.,  1.],
           [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
           [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
           [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  4.,  1.,  1.],
           [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.]])
        
これで単純な等高線を作成できます：

.. Now we can make a simple contour plot:

.. code-block:: python

    contour(x, x, z)

作図はこうみえるでしょう：

.. Our plot looks like this:

.. image:: figures/contour.png
            :width: 25%

領域を色で埋めることもできます.
単純に ``v`` の値としてに0から9までの数字を使ってみます：

.. We can also fill the area. We just use numbers form 0 to 9 for
.. the values ``v``:

.. code-block:: python

    v = x
    contourf(x, x, z, v)

これで作図内の領域が埋まります：

.. Now our plot area is filled:

.. image:: figures/contourf.png
            :width: 25%

頻度分布
++++++++

.. Histograms
.. +++++++++++

頻度分布 (histgram) を作ることができます.
``numpy`` から正規分布に従う乱数を取り出してみます：

.. We can make histograms. Let's get some normally distributed
.. random numbers from ``numpy``:

.. code-block:: python

    import numpy as N
    r_numbers = N.random.normal(size= 1000)

さてこれで単純な頻度分布を作ります：

.. Now we make a simple histogram:

.. code-block:: python
    
    hist(r_numbers)

1000個の乱数を使うと図はうまくできているように見えます：

.. With 1000 numbers our figure looks pretty good:

.. raw:: pdf

     Spacer 0 10

.. image:: figures/hist.png
            :width: 25%

両対数
++++++

.. Loglog Plots
.. ++++++++++++

対数スケールでの作図 (Loglog plot) は簡単です：

.. Plots with logarithmic scales are easy:

.. code-block:: python

    loglog(arange(1000))

大目盛と小目盛のグリッドを設定することもできます：

.. We set the mayor and minor grid:

.. code-block:: python
    
    grid(True)
    grid(True, which='minor')
    
これで両対数グラフができます：

.. Now we have loglog plot:

.. image:: figures/loglog.png
            :width: 25%

もし片対数グラフが欲しければ ``semilogx`` か ``semilogy`` を使うことができます.

.. If we want only one axis with a logarithmic scale we can
.. use ``semilogx`` or ``semilogy``.

円グラフ
++++++++

.. Pie Charts
.. ++++++++++

円グラフも数行で作ることができます：

.. Pie charts can also be created with a few lines:

.. code-block:: python

    data = [500, 700, 300]
    labels = ['cats', 'dogs', 'other']
    pie(data, labels=labels)
    
結果はこうなると期待されます：

.. The result looks as expected:

.. image:: figures/pie.png
            :width: 25%

極座標
++++++

.. Polar Plots
.. +++++++++++

極座標表示での作図 (polar plots) も可能です.
0から360までの ``r`` と0から360度までの ``theta`` を定義しましょう.
角度はラジアンに変更する必要があります.

.. Polar plots are also possible. Let's define our ``r`` from
.. 0 to 360 and our ``theta`` from 0 to 360 degrees. We need to
.. convert them to radians:

.. code-block:: python

        r = arange(360)
        theta = r / (180/pi)

さぁ, 極座標で作図します：

.. Now plot in polar coordinates:

.. code-block:: python
    
    polar(theta, r)

すてきな螺旋が得られます：

.. We get a nice spiral:

.. image:: figures/polar.png
            :width: 25%

矢印
++++

.. Arrow Plots
.. ++++++++++++

2次元平面上での矢印の作図 (arrow plot) は ``quiver`` で実現できます.
矢印の矢尻にあたる x, y 座標を定義します：

.. Plotting arrows in 2D plane can be achieved with ``quiver``.
.. We define the x and y coordinates of the arrow shafts:

.. code-block:: python

    x = y = arange(10)

矢印の x, y 要素は2次元配列で指定します：

.. The x and y components of the arrows are specified as 2D arrays:

.. code-block:: python

    u = ones((10, 10))
    v = ones((10, 10))
    u[4, 4] = 3
    v[1, 1] = -1

さてこれで矢印を作図できます：

.. Now we can plot the arrows:

.. code-block:: python

    quiver(x, y, u, v)


2つの矢印を除いた全ての矢印が右上を向いています.
例外的な矢印の1つ (4, 4) に位置する矢印は x 方向に 3 の単位ベクトルを持っています,
もう一方の (1, 1) に位置する矢印は y 方向に -1 の単位ベクトルを持ちます：

.. All arrows point to the upper right, except two. The one
.. at the location (4, 4) has 3 units in x-direction and the
.. other at location (1, 1) has -1 unit in y direction:

.. raw:: pdf

     Spacer 0 10

.. image:: figures/quiver.png
            :width: 25%
         
散布図
++++++

.. Scatter Plots
.. +++++++++++++

散布図 (scatter plit) は x 対 y の略図を作図します.
``x`` と ``y`` を定義し, ``y`` のいくつかの点を適当に与えます：

.. Scatter plots print x vs. y diagrams. We define ``x`` and ``y``
.. and make some point in ``y`` random:

.. code-block:: python

    x = arange(10)
    y = arange(10)
    y[1] = 7
    y[4] = 2
    y[8] = 3

さて散布図を作ってみます::

    scatter(x, y)

.. Now make a scatter plot::
    
    scatter(x, y)

``y`` の異なった3つの値が直線から外れています：

.. The three different values for ``y`` break out of the line:

.. raw:: pdf

     Spacer 0 10

.. image:: figures/scatter.png
            :width: 25%
         

疎パターン
++++++++++

.. Sparsity Pattern Plots
.. ++++++++++++++++++++++

疎行列を扱う場合, しばしば疎パターン (sparsity pattern),
つまり疎行列がどういう構造になっているかが問題になります.
例として単位行列を扱ってみましょう：

.. Working with sparse matrices, it is often of interest as
.. how the matrix looks like in terms of sparsity.
.. We take an identity matrix as an example:

.. code-block:: python

    i = identity(10)
    i
    array([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]])

より視覚的にみてみましょう：

.. Now we look at it more visually:

.. code-block:: python

    spy(i)



.. image:: figures/spy.png
            :width: 25%

ステムプロット
++++++++++++++

.. Stem Plots
.. ++++++++++

ステムプロット (stem plot)  は与えられた位置 x と y に対して
垂直な線を描きます.
散布図と同じ ``x``, ``y`` を使ってみましょう（上を見ましょう）：

.. Stem plots vertical lines at the given x location up to
.. the specified y location. Let's reuse ``x`` and ``y``
.. from our scatter (see above):

.. code-block:: python

    stem(x, y)

.. image:: figures/stem.png
            :width: 25%

時刻
++++

.. Date Plots
.. ++++++++++

時刻を作図する関数があります.
2000年1月1日から15日毎の間隔で10の日付を定義してみましょう：

.. There is a function for creating date plots.
.. Let's define 10 dates starting at January 1st 2000
.. at 15.day intervals:

.. code-block:: python

    import datetime
    d1 = datetime.datetime(2000, 1, 1)
    delta = datetime.timedelta(15)
    dates = [d1 + x * delta for x in range(1
    dates
    [datetime.datetime(2000, 1, 1, 0, 0),
     datetime.datetime(2000, 1, 16, 0, 0),
     datetime.datetime(2000, 1, 31, 0, 0),
     datetime.datetime(2000, 2, 15, 0, 0),
     datetime.datetime(2000, 3, 1, 0, 0),
     datetime.datetime(2000, 3, 16, 0, 0),
     datetime.datetime(2000, 3, 31, 0, 0),
     datetime.datetime(2000, 4, 15, 0, 0),
     datetime.datetime(2000, 4, 30, 0, 0),
     datetime.datetime(2000, 5, 15, 0, 0)]

散布図のデータを再利用します（上を見ましょう）

.. We reuse our data from the scatter plot (see above):

.. code-block:: python

    y
    array([0, 7, 2, 3, 2, 5, 6, 7, 3, 9])
     
これで日付が x 軸の作図ができます：

.. Now we can plot the dates at the x axis:

.. code-block:: python

    plot_date(dates, y)


.. image:: figures/date.png
            :width: 25%


クラスライブラリ
----------------

.. The Class Library
.. -----------------

ここまででは ``pylab`` インターフェースのみを使ってきました.
名前が暗示するように, ``pylab`` はクラスライブラリの単なるラッパーです.
``pylab`` のコマンドはオブジェクト指向な方法を使うクラスライブラリ経由で呼びだすことができます.

.. So far we have used the ``pylab`` interface only. As the name
.. suggests it is just wrapper around the class library. All ``pylabb``
.. commands can be invoked via the class library using an object-oriented
.. approach.

Figure クラス
+++++++++++++
    
.. The Figure Class
.. ++++++++++++++++

``Figure`` クラスは ``matplotlib.figure`` モジュール内にあります.
このコンストラクタはこれらの引数を取ります：

.. The class ``Figure`` lives in the module ``matplotlib.figure``.
.. Its constructor takes these arguments:

.. code-block:: python

    figsize=None, dpi=None, facecolor=None, edgecolor=None,
    linewidth=1.0, frameon=True, subplotpars=None

``pylab`` の ``figure`` の引数と比較すると重要な部分が重複しています：

.. Comparing this with the arguments of ``figure`` in ``pylab`` shows
.. significant overlap:

.. code-block:: python

    num=None, figsize=None, dpi=None, facecolor=None
    edgecolor=None, frameon=True

``Figure`` は多くのメソッドを提供していますが, 多くのメソッドは ``pylab`` と等価です.
``pylab`` で ``axes`` や ``subplot`` によって
axes や subplot を新たに作成すると ``add_axes`` と
``add_subplot`` メソッドが呼び出されます.
同様に ``gca`` メソッドは ``pylab`` で ``legend``, ``text`` その他を行なうことに対応します.

.. ``Figure`` provides lots of methods, many of them have equivalents in
.. ``pylab``. The methods ``add_axes`` and ``add_subplot`` are called if new
.. axes or subplot are created with ``axes`` or ``subplot`` in ``pylab``.
.. Also the method ``gca`` maps directly to ``pylab`` as do ``legend``,
.. ``text`` and many others.

``pylab`` で figure のプロパティを設定する際に呼び出される
``set_facecolor`` や ``set_edgecolor`` のようないくつかの
``set_something`` メソッドがあります.
また ``Figure`` は ``get_axes`` や ``get_facecolor`` のような figure のプロパティを取得する ``get_something`` メソッドも実装しています.

.. There are also several ``set_something`` method such as ``set_facecolor`` or
.. ``set_edgecolor`` that will be called through ``pylab`` to set properties of
.. the figure. ``Figure`` also implements ``get_something`` methods
.. such as ``get_axes`` or ``get_facecolor`` to get properties of the figure.



Axes と Subplot クラス
++++++++++++++++++++++

.. The Classes Axes and Subplot
.. ++++++++++++++++++++++++++++

``Axes`` クラスには ``Axis`` や ``Tick``, ``Line2D``
または ``Text`` のような figure の要素の大部分があります.
またこのクラスは座標系も設定します.
``Subplot`` クラスは ``Axis`` クラスを継承して格子上に作図を配置するための機能が追加されています.

.. In the class  ``Axes`` we find most of the figure elements such as
.. ``Axis``, ``Tick``, ``Line2D``, or ``Text``. It also sets the coordinate
.. system. The class ``Subplot`` inherits from ``Axes`` and adds some
.. more functionality to arrange the plots in a grid.

``Figure`` との同様に, このクラスはプロパティ設定, 取得するメソッドを持っています.
そしてメソッドは ``pylab` の関数として既に扱ってきました, 例えば ``annotate``.
さらに ``Axwes`` はこれまでの節で示した作図の全てのタイプのメソッドを持っています.

.. Analogous to ``Figure``, it has methods to get and set properties
.. and methods already encountered as functions in ``pylab`` such as
.. ``annotate``. In addition, ``Axes`` has methods for all types of plots
.. shown in the previous section.

その他のクラス
++++++++++++++

.. Other Classes
.. +++++++++++++

``text``, ``Legend`` または ``Ticker`` のような他のクラスはとても類似した機構を持っています.
これらは多くの場合 ``pylab`` インターフェースと比較して理解することができます.


.. Other classes such as ``text``, ``Legend`` or ``Ticker`` are setup very
.. similarly. They can be understood mostly by comparing to the ``pylab``
.. interface.


例
+++

.. Example
.. +++++++

オブジェクト指向 API を使った例を見てみましょう：

.. Let's look at an example for using the object-oriented API:

.. literalinclude:: matplotlib_examples/oo.py

.. .. code-block:: python
    :include: matplotlib_examples/oo.py

対話的な pylab モードにいないので
``Figure`` クラスをインポートする必要があります (``#1``).

.. Since we are not in the interactive pylab-mode, we
.. need to import the class ``Figure`` explicitly (``#1``).

figure のサイズを8x5インチに設定します (``#2``).
新しい figure を初期化します (``#3``),
そして fig に ``subplot`` を追加します (``#4``).
MATLAB のように ``111`` で 1, 1 の位置に1番の作図を意味します.
0から9までの数字で新しく作図し,
同時に line に対するレファレンスを取得します (``#5``).
いくつかの要素を作図に追加できます.
そのためタイトルと x, y 軸のラベルを設定します (``#6``).

.. We set the size of our figure to be 8 by 5 inches (``#2``).
.. Now we initialize a new figure (``#3``) and add a subplot
.. to the figure (``#4``). The ``111`` says one plot at
.. position 1, 1 just as in MATLAB. We create a new plot with
.. the numbers from 0 to 9 and at the same time get a reference
.. to our line (``#5``). We can add several things to our plot.
.. So we set a title and labels for the x and y axis (``#6``).

また, グリッドも表示し (``#7``) マーカーに小さな円を使いたい (``#8``) です.
    
.. We also want to see the grid (``#7``) and would like to have
.. little filled circles as markers (``#8``).

fig をレンダリングするためのバックエンドはいくつかあります.
レンダリングのために Anti-Grain Geometry toolkit (http://www.antigrain.com) を使ってみます.
まず, バックエンドをインポートします (``#9``),
そして fig を描画する新しいキャンバスを作ります (``#10``).
fig を80 dpi の解像度の png ファイルに保存します (``#11``).

.. There are many different backends for rendering our figure.
.. We use the Anti-Grain Geometry toolkit (http://www.antigrain.com)
.. to render our figure. First, we import the backend (``#9``), then
.. we create a new canvas that renders our figure (``#10``).
.. We save our figure in a png-file with a resolution of 80 dpi (``#11``).

いくつかの GUI ツールキットは直接使うことができます.
ということで Tkinter をインポートし (``#12``),
同様に対応するバックエンドをインポートします (``#13``).
まず基本的な GUI プログラミングが動くようにする必要があります.
GUI のための root オブジェクトを作成し (``#14``),
キャンバスを得るため fig とともに与えます (``#15``).
show メソッドを実行し (``#16``), ウィジェットにパックします (``#17``),
アプリケーションを起動するため Tkinter の mainloop を実行します (``#18``).
これで画面の GUI ウィンドウで figure が見られるはずです.
画面を閉じると, スクリプトの次の部分が実行されます.

.. We can use several GUI toolkits directly. So we import Tkinter (``#12``)
.. as well as the corresponding backend (``#13``).
.. Now we have to do some basic GUI programming work. We make a root
.. object for our GUI (``#13``) and feed it together with our figure to
.. the backend to get our canvas (``14``). We call the show method (``#15``),
.. pack our widget (``#16``), and call the Tkinter mainloop to start
.. the application (``#17``). You should see GUI window with the figure
.. on your screen. After closing the screen, the next part, the script, will
.. be executed.

``pylab`` を使っているときのように画面に表示したいので,
helper をインポートし (``#19``), ``pylab`` 自身もインポートします (``#20``).
``pylab`` で通常の figure を作成し (``#21``),
そして, 対応する figure manager を取得します (``#22``).
さぁ, 上で作った figure を現在の figure に設定し (``#23``),
``pylab`` に結果を表示させましょう (``#24``).
figure の下の部分がツールバーで覆われているかもしれません.
その場合は ``pylab`` に対して ``figsize`` を調整して下さい.

.. We would like to create a screen display just as we would use
.. ``pylab``. Therefore we import a helper (``#18``) and ``pylab``
.. itself (``#19``). We create a normal figure with ``pylab` (``20``)
.. and get the corresponding figure manager (``#21``). Now let's set
.. our figure we created above to be the current figure (``#22``)
.. and let ``pylab`` show the result (``#23``).
.. The lower part of the figure might be cover by the toolbar.
.. If so, please adjust the ``figsize`` for ``pylab`` accordingly.

練習問題
++++++++

.. Exercises
.. +++++++++

1) matplotlib のオブジェクト指向 API を使って,
   凡例つきの直線と2次曲線を作図し, png ファイルを作りましょう.

.. 1) Use the object-oriented API of matplotlib to create a png-file
..    with a plot of two lines, one linear and square with a legend in it.

.. [*] 訳注 これは少なくとも 1.0.1 ではなくなっているようです.

