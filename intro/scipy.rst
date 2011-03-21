.. spectrum in SVD

Scipy：高レベルな科学技術計算
=============================

.. Scipy : high-level scientific computing
.. =========================================

.. only:: latex

  :authors: Adrien Chauve, Andre Espaze, Emmanuelle Gouillart, Gaël Varoquaux

.. topic:: Scipy

    ``scipy`` パッケージは科学技術計算の共通して現われる問題を解決するための多くのツールを含んでいます.
    補間, 積分, 最適化, 画像処理, 統計, 特殊関数など, 適用する問題の違いに対応したサブモジュールを持っています.

    ``scipy`` は GSL (GNU Scientific Library for C and C++) や
    Matlab の toolboxes のような他の科学技術計算で標準的に使われるライブラリと同等の機能を持っています.
    ``scipy`` は Python における科学技術計算ライブラリの中核となるパッケージです；
    ``numpy`` の配列を効率的に扱い, numpy と scipy は密接な連携を持っています.

    ルーチンを実装する前に行いたいデータ処理が Scipy で実装されているか調べることは有効です.
    専門的でないプログラマによくあるように, 科学者はしばしば **車輪の再開発** をしたがります.
    そうするとバグの発生を招いたり, 最適化が不十分であったり, 共有することが難しかったり,
    メンテナンスが困難であるといった問題を起こしやすくします.
    一方で ``Scipy`` のルーチンは最適化とテスト済みされています,
    なので可能な場合にはこちらを使うべきです.

..     The ``scipy`` package contains various toolboxes dedicated to common
..     issues in scientific computing. Its different submodules correspond
..     to different applications, such as interpolation, integration,
..     optimization, image processing, statistics, special functions, etc.

..     ``scipy`` can be compared to other standard scientific-computing
..     libraries, such as the GSL (GNU Scientific  Library for C and C++),
..     or Matlab's toolboxes. ``scipy`` is the core package for scientific
..     routines in Python; it is meant to operate efficiently on ``numpy``
..     arrays, so that numpy and scipy work hand in hand.

..     Before implementing a routine, if is worth checking if the desired
..     data processing is not already implemented in Scipy. As
..     non-professional programmers, scientists often tend to **re-invent the
..     wheel**, which leads to buggy, non-optimal, difficult-to-share and
..     unmaintainable code. By contrast, ``Scipy``'s routines are optimized
..     and tested, and should therefore be used when possible.


.. warning::

    このチュートリアルは決して数値計算の入門ではありません.
    scipy のサブモジュールと関数を列挙していくことはとても退屈なものになるでしょうから,
    代わりに ``scipy`` を科学技術計算のためにどう使えばいいか理解するための少数の例を集中して扱います, 

..     This tutorial is far from an introduction to numerical computing.
..     As enumerating the different submodules and functions in scipy would
..     be very boring, we concentrate instead on a few examples to give a
..     general idea of how to use ``scipy`` for scientific computing.

ますはじめに::

    >>> import numpy as np
    >>> import scipy

.. to begin with ::

..     >>> import numpy as np
..     >>> import scipy

`scipy` は主に特定の作業向けのサブモジュールから構成されています.

============= ========================================================
cluster         ベクトル量子化 / K 平均法
fftpack         フーリエ変換
integrate       積分ルーチン
interpolate     補間
io              データの入出力
linalg          線形代数ルーチン
maxentropy      最大エントロピーモデルによるフィッティングルーチン
ndimage         n 次元画像パッケージ
odr             直交距離回帰
optimize        最適化
signal          信号処理
sparse          疎行列
spatial         空間データ構造とアルゴリズム
special         特殊関数
stats           統計
============= ========================================================

.. `scipy` is mainly composed of task-specific sub-modules:

.. ============= ===============================================
.. cluster         Vector quantization / Kmeans
.. fftpack         Fourier transform
.. integrate       Integration routines
.. interpolate     Interpolation
.. io              Data input and output
.. linalg          Linear algebra routines
.. maxentropy      Routines for fitting maximum entropy models
.. ndimage         n-dimensional image package
.. odr             Orthogonal distance regression
.. optimize        Optimization
.. signal          Signal processing
.. sparse          Sparse matrices
.. spatial         Spatial data structures and algorithms
.. special         Any special mathematical functions
.. stats           Statistics
.. ============= ===============================================


Scipy は Numpy に基づいています
-------------------------------
   
.. Scipy builds upon Numpy
.. -------------------------

Scipy を動かし, 使うには Numpy が必要です.
Numpy が Python に導入する型の中で最も重要なものは, N 次元配列ですが,
Scipy も同じものを使っていることがわかります::

    >>> scipy.ndarray is np.ndarray
    True

.. Numpy is required for running Scipy but also for using it. The most
.. important type introduced to Python is the N dimensional array,
.. and it can be seen that Scipy uses the same::

..     >>> scipy.ndarray is np.ndarray
..     True

そのうえ Scipy の初等的な関数も Numpy が提供しています::

    >>> scipy.cos is np.cos
    True

.. Moreover most of the Scipy usual functions are provided by Numpy::

..     >>> scipy.cos is np.cos
..     True

オブジェクトが Numpy 起源かどうかを調べたければ, ``scipy.__file__[:-1]`` のファイルを見ましょう.
バージョン '0.6.0' では Numpy の名前空間は ``from numpy import *`` の行でインポートされています.

.. If you would like to know the objects used from Numpy, have a look at
.. the  ``scipy.__file__[:-1]`` file. On version '0.6.0', the whole Numpy
.. namespace is imported by the line ``from numpy import *``.

ファイル入出力 ： ``scipy.io``
------------------------------

.. File input/output: ``scipy.io``
.. ----------------------------------

* matlab のファイルの読み込みと保存::

    >>> from scipy import io
    >>> struct = io.loadmat('file.mat', struct_as_record=True)
    >>> io.savemat('file.mat', struct)

.. * Loading and saving matlab files::

..     >>> from scipy import io
..     >>> struct = io.loadmat('file.mat', struct_as_record=True)
..     >>> io.savemat('file.mat', struct)

これも見ましょう：

    * テキストファイルの読み込み::

        np.loadtxt/np.savetxt

    * テキストや csv ファイルの賢い読み込み::

        np.genfromtxt/np.recfromcsv

    * 高速で効率的な numpy に特化したバイナリフォーマット::

        np.save/np.load

.. See also:

..     * Load text files::

..         np.loadtxt/np.savetxt

..     * Clever loading of text/csv files::

..         np.genfromtxt/np.recfromcsv

..     * Fast an efficient, but numpy-specific, binary format::

..         np.save/np.load


信号処理 ： ``scipy.signal``
----------------------------

.. Signal processing: ``scipy.signal``
.. ------------------------------------

::

    >>> from scipy import signal

* トレンドの除去：信号から線形トレンドを除く::

    t = np.linspace(0, 5, 100)
    x = t + np.random.normal(size=100)

    pl.plot(t, x, linewidth=3)
    pl.plot(t, signal.detrend(x), linewidth=3)

  .. plot:: demo_detrend.py
    :hide-links:
    :scale: 50

.. * Detrend: remove linear trend from signal::

..     t = np.linspace(0, 5, 100)
..     x = t + np.random.normal(size=100)

..     pl.plot(t, x, linewidth=3)
..     pl.plot(t, signal.detrend(x), linewidth=3)

..   .. plot:: demo_detrend.py
..     :hide-links:
..     :scale: 50

* リサンプル：FFT を使って信号を `n` 点でリサンプルする::

    t = np.linspace(0, 5, 100)
    x = np.sin(t)
    
    pl.plot(t, x, linewidth=3)
    pl.plot(t[::2], signal.resample(x, 50), 'ko')

  .. plot:: demo_resample.py
    :hide-links:
    :scale: 50

  .. only:: latex

     ウィンドウの端にリッピングの効果があり, リサンプリングの精度がよくないことに注意してください.

.. * Resample: resample a signal to `n` points using FFT. ::

..     t = np.linspace(0, 5, 100)
..     x = np.sin(t)
    
..     pl.plot(t, x, linewidth=3)
..     pl.plot(t[::2], signal.resample(x, 50), 'ko')

..   .. plot:: demo_resample.py
..     :hide-links:
..     :scale: 50

..   .. only:: latex

..      Notice how on the side of the window the resampling is less accurate
..      and has a rippling effect.

* signal は多くの窓関数を持っています ： `hamming`, `bartlett`, `blackman`...

.. * Signal has many window function: `hamming`, `bartlett`, `blackman`...

* signal はフィルタを持っています (Gaussian, 中央値フィルタ, Wiener),
  しかし, これらについては画像の段落で議論することにします.

.. * Signal has filtering (Gaussian, median filter, Wiener), but we will
..   discuss this in the image paragraph.

特殊関数 ： ``scipy.special``
-----------------------------
    
.. Special functions: ``scipy.special``
.. ---------------------------------------

特殊関数は超越的な関数です.
モジュールのドキュメンテーション文字列にしっかりと書かれているので列挙しません.
よく使うものは：

 * Bessel 関数, 例えば `special.jn` （整数次 Bessel 関数）など

 * 楕円関数 （Jacobi の楕円関数 `special.ellipj`, ...)

 * ガンマ関数 ： `special.gamma`,
   また `special.gammaln` は高精度のガンマ関数の log を与えます.

 * 誤差関数, Gauss 関数の面積 ： `special.erf`

.. Special functions are transcendal functions. The docstring of the module
.. is well-written and we will not list them. Frequently used ones are:

..  * Bessel function, such as `special.jn` (nth integer order Bessel
..    function)

..  * Elliptic function (`special.ellipj` for the Jacobian elliptic
..    function, ...)

..  * Gamma function: `special.gamma`, alos note `special.gammaln` which
..    will give the log of Gamma to a higher numerical precision.

..  * Erf, the area under a Gaussian curve: `special.erf`

統計と乱数 ： ``scipy.stats``
-----------------------------

.. Statistics and random numbers: ``scipy.stats``
.. -----------------------------------------------

`scipy.stats` は統計ツールと確率過程の確率論的な記述を含みます.
多くの確率過程のための乱数生成器は `numpy.random` にあります.

.. The module `scipy.stats` contains statistical tools and probabilistic
.. description of random processes. Random number generators for various
.. random process can be found in `numpy.random`.

頻度分布と確率分布関数
----------------------

.. Histogram and probability density function
.. ...............................................

確率過程を観察すると, その頻度分布は確率過程の確率密度関数を推定関数になります::

    >>> a = np.random.normal(size=1000)
    >>> bins = np.arange(-4, 5)
    >>> bins
    array([-4, -3, -2, -1,  0,  1,  2,  3,  4])
    >>> histogram = np.histogram(a, bins=bins, normed=True)[0]
    >>> bins = 0.5*(bins[1:] + bins[:-1])
    >>> bins
    array([-3.5, -2.5, -1.5, -0.5,  0.5,  1.5,  2.5,  3.5])
    >>> from scipy import stats
    >>> b = stats.norm.pdf(bins)

.. Given observations of a random process, their histogram is an estimator of 
.. the random process's PDF (probability density function): ::

..     >>> a = np.random.normal(size=1000)
..     >>> bins = np.arange(-4, 5)
..     >>> bins
..     array([-4, -3, -2, -1,  0,  1,  2,  3,  4])
..     >>> histogram = np.histogram(a, bins=bins, normed=True)[0]
..     >>> bins = 0.5*(bins[1:] + bins[:-1])
..     >>> bins
..     array([-3.5, -2.5, -1.5, -0.5,  0.5,  1.5,  2.5,  3.5])
..     >>> from scipy import stats
..     >>> b = stats.norm.pdf(bins)

.. sourcecode:: ipython

    In [1]: pl.plot(bins, histogram)
    In [2]: pl.plot(bins, b)

.. plot:: normal_distribution.py
    :hide-links:
    :scale: 50

与えられた確率過程がどの確率過程のクラスに属しているか（例えば正規過程）知ることができれば,
最尤法によって観察量をフィットして分布に内在するパラメータを推定できます.
ここで観察したデータを正規過程でフィットします::

    >>> loc, std = stats.norm.fit(a)
    >>> loc
    0.003738964114102075
    >>> std
    0.97450996668871193

.. If we know that the random process belongs to a given family of random
.. processes, such as normal processes, we can do a maximum-likelihood fit
.. of the observations to estimate the parameters of the underlying 
.. distribution. Here we fit a normal process to the observed data::

..     >>> loc, std = stats.norm.fit(a)
..     >>> loc
..     0.003738964114102075
..     >>> std
..     0.97450996668871193

百分位
......

.. Percentiles
.. .............

中央値は観測データの上下の中央に位置する値です：

    >>> np.median(a)
    0.0071645570292782519

それは百分位点 50 ともいいます, なぜなら観測値の 50 % がその下に位置するからです：

    >>> stats.scoreatpercentile(a, 50)
    0.0071645570292782519

同様にして, 百分位点 90 も計算できます：

    >>> stats.scoreatpercentile(a, 90)
    1.2729556087871292

百分位は累積分布関数の推定関数となります.

.. The median is the value with half of the observations below, and half
.. above:

..     >>> np.median(a)
..     0.0071645570292782519

.. It is also called the percentile 50, because 50% of the observation are
.. below it:

..     >>> stats.scoreatpercentile(a, 50)
..     0.0071645570292782519

.. Similarly, we can calculate the percentile 90:

..     >>> stats.scoreatpercentile(a, 90)
..     1.2729556087871292

.. The percentile is an estimator of the CDF: cumulative distribution
.. function.

統計的検定
..........

.. Statistical tests
.. ...................

統計的検定は判断指標です. 例えば, Gauss 過程から生成されたと過程される2つの観測の集合があるとき, 
2つの集合に有意差があるかを調べるのに T検定を使うことができます::

    >>> a = np.random.normal(0, 1, size=100)
    >>> b = np.random.normal(1, 1, size=10)
    >>> stats.ttest_ind(a, b)
    (-2.389876434401887, 0.018586471712806949)

.. A statistical test is a decision indicator. For instance, if we have 2
.. sets of observations, that we assume are generated from Gaussian
.. processes, we can use a T-test to decide whether the two sets of
.. observations are significantly different::

..     >>> a = np.random.normal(0, 1, size=100)
..     >>> b = np.random.normal(1, 1, size=10)
..     >>> stats.ttest_ind(a, b)
..     (-2.389876434401887, 0.018586471712806949)

検定の結果は以下で構成されます：

    * T 統計値：2つの確率過程の差に比例し, 有意差の程度を示す数字

    * *p 値*: 2つの過程が等価である確率. もし 1 に近ければ2つの過程はほぼ等価です.
      0 に近ければ, 過程はより異なる意味をもつように思われます.

.. The resulting output is composed of:

..     * The T statistic value: it is a number the sign of which is
..       proportional to the difference between the two random processes and
..       the magnitude is related to the significance of this difference.

..     * the *p value*: the probability of both process being identical. If
..       it is close to 1, the two process are almost certainly identical.
..       The closer it is to zero, the more likely it is that the processes
..       have different mean.

線形代数演算 ： ``scipy.linalg``
--------------------------------

.. Linear algebra operations: ``scipy.linalg``
.. -----------------------------------------------

linalg モジュールは標準的な線形代数演算を提供します.
``det`` 関数は正方行列の行列式を計算します::

    >>> from scipy import linalg
    >>> arr = np.array([[1, 2],
    ...                 [3, 4]])
    >>> linalg.det(arr)
    -2.0
    >>> arr = np.array([[3, 2],
    ...                 [6, 4]])
    >>> linalg.det(arr)
    0.0
    >>> linalg.det(np.ones((3, 4)))
    Traceback (most recent call last):
    ...
    ValueError: expected square matrix

.. First, the linalg module provides standard linear algebra operations.
.. The ``det`` function computes the determinant of a square matrix::

..     >>> from scipy import linalg
..     >>> arr = np.array([[1, 2],
..     ...                 [3, 4]])
..     >>> linalg.det(arr)
..     -2.0
..     >>> arr = np.array([[3, 2],
..     ...                 [6, 4]])
..     >>> linalg.det(arr)
..     0.0
..     >>> linalg.det(np.ones((3, 4)))
..     Traceback (most recent call last):
..     ...
..     ValueError: expected square matrix

``inv`` 関数は正方行列の逆行列を計算します::

    >>> arr = np.array([[1, 2],
    ...                 [3, 4]])
    >>> iarr = linalg.inv(arr)
    >>> iarr
    array([[-2. ,  1. ],
           [ 1.5, -0.5]])
    >>> np.allclose(np.dot(arr, iarr), np.eye(2))
    True

.. The ``inv`` function computes the inverse of a square matrix::

..     >>> arr = np.array([[1, 2],
..     ...                 [3, 4]])
..     >>> iarr = linalg.inv(arr)
..     >>> iarr
..     array([[-2. ,  1. ],
..            [ 1.5, -0.5]])
..     >>> np.allclose(np.dot(arr, iarr), np.eye(2))
..     True

matrix 型を使う場合 ``I`` 属性を要求すると逆行列が計算されます::

    >>> ma = np.matrix(arr, copy=False)
    >>> np.allclose(ma.I, iarr)
    True

.. Note that in case you use the matrix type, the inverse is computed when
.. requesting the ``I`` attribute::

..     >>> ma = np.matrix(arr, copy=False)
..     >>> np.allclose(ma.I, iarr)
..     True

特異行列（行列式が 0 な行列）を計算する場合 ``LinAlgError`` が送出されるでしょう::

    >>> arr = np.array([[3, 2],
    ...                 [6, 4]])
    >>> linalg.inv(arr)
    Traceback (most recent call last):
    ...
    LinAlgError: singular matrix

.. Finally computing the inverse of a singular matrix (its determinant is zero)
.. will raise ``LinAlgError``::

..     >>> arr = np.array([[3, 2],
..     ...                 [6, 4]])
..     >>> linalg.inv(arr)
..     Traceback (most recent call last):
..     ...
..     LinAlgError: singular matrix

特異値分解 (SVD) のようなより高等な操作も使えます::

    >>> arr = np.arange(12).reshape((3, 4)) + 1
    >>> uarr, spec, vharr = linalg.svd(arr)

結果となるスペクトルの配列は::

    >>> spec
    array([  2.54368356e+01,   1.72261225e+00,   5.14037515e-16])

元の行列の再構成のため, まず行列操作のためのエイリアスを定義します::

    >>> asmat = np.asmatrix

そして次のステップとして::

    >>> sarr = np.zeros((3, 4))
    >>> sarr.put((0, 5, 10), spec)
    >>> svd_mat = asmat(uarr) * asmat(sarr) * asmat(vharr)
    >>> np.allclose(svd_mat, arr)
    True

SVD は統計や信号処理などで一般的に使われています.
他の多くの分解（QR, LU, Cholesky, Schur）も線形系のソルバーと同様に ``scipy.linalg`` で入手できます.

.. More advanced operations are available like singular-value decomposition
.. (SVD)::

..     >>> arr = np.arange(12).reshape((3, 4)) + 1
..     >>> uarr, spec, vharr = linalg.svd(arr)

.. The resulting array spectrum is::

..     >>> spec
..     array([  2.54368356e+01,   1.72261225e+00,   5.14037515e-16])

.. For the recomposition, an alias for manipulating matrix will first
.. be defined::

..     >>> asmat = np.asmatrix

.. then the steps are::

..     >>> sarr = np.zeros((3, 4))
..     >>> sarr.put((0, 5, 10), spec)
..     >>> svd_mat = asmat(uarr) * asmat(sarr) * asmat(vharr)
..     >>> np.allclose(svd_mat, arr)
..     True

.. SVD is commonly used in statistics or signal processing.  Many other
.. standard decompositions (QR, LU, Cholesky, Schur), as well as solvers
.. for linear systems, are available in ``scipy.linalg``.

数値積分 ： ``scipy.integrate``
-------------------------------

.. Numerical integration: ``scipy.integrate``
.. ------------------------------------------------

最も一般的な積分ルーチンは ``scipy.integrate.quad`` です::

    >>> from scipy.integrate import quad
    >>> res, err = quad(np.sin, 0, np.pi/2)
    >>> np.allclose(res, 1)
    True
    >>> np.allclose(err, 1 - res)
    True

.. The most generic integration routine is ``scipy.integrate.quad``::

..     >>> from scipy.integrate import quad
..     >>> res, err = quad(np.sin, 0, np.pi/2)
..     >>> np.allclose(res, 1)
..     True
..     >>> np.allclose(err, 1 - res)
..     True

他の積分スキーム ``fixed_quad``, ``quadrature``, ``romberg`` が使えます.

.. Others integration schemes are available with ``fixed_quad``,
.. ``quadrature``, ``romberg``.

``scipy.integrate`` は常微分方程式を解くためのルーチンも持っています.
特に ``scipy.integrate.odeint`` は LSODA (Livermore solver for
ordinary differential equations with automatic method switching
for stiff and nonstiff problems)
を使った一般的な用途に使える積分器です.
詳しくは `ODEPACK Fortran library`_ を見て下さい.

.. _`ODEPACK Fortran library` : http://people.sc.fsu.edu/~jburkardt/f77_src/odepack/odepack.html

.. ``scipy.integrate`` also features routines for Ordinary differential
.. equations (ODE) integration. In particular, ``scipy.integrate.odeint``
.. is a general-purpose integrator using LSODA (Livermore solver for
.. ordinary differential equations with automatic method switching
.. for stiff and nonstiff problems), see the `ODEPACK Fortran library`_
.. for more details.

.. .. _`ODEPACK Fortran library` : http://people.sc.fsu.edu/~jburkardt/f77_src/odepack/odepack.html

``odeint`` は以下の形式の1階の常微分方程式系を解きます::

``dy/dt = rhs(y1, y2, .., t0,...)``

.. ``odeint`` solves first-order ODE systems of the form::

.. ``dy/dt = rhs(y1, y2, .., t0,...)``

入門として, 常微分方程式 ``dy/dt = -2y`` を ``t = 0..4`` の区間にわたって
``y(t=0) = 1`` の初期条件のもとで解きます.
まず, 位置の微分を計算する関数を定義する必要があります::

    >>> def calc_derivative(ypos, time, counter_arr):
    ...     counter_arr += 1
    ...     return -2*ypos
    ...

.. As an introduction, let us solve the ODE ``dy/dt = -2y`` between ``t =
.. 0..4``, with the  initial condition ``y(t=0) = 1``. First the function
.. computing the derivative of the position needs to be defined::

..     >>> def calc_derivative(ypos, time, counter_arr):
..     ...     counter_arr += 1
..     ...     return -2*ypos
..     ...

余計な引数 ``counter_arr`` は単一時間ステップ間で積分が収束するまでに何回実行されたか示すカウンタとして追加されています.
カウンタを定義します::

    >>> counter = np.zeros((1,), np.uint16)

.. An extra argument ``counter_arr`` has been added to illustrate that the
.. function may be called several times for a single time step, until solver
.. convergence. The counter array is defined as::

..     >>> counter = np.zeros((1,), np.uint16)

以下で軌道が計算されます::

    >>> from scipy.integrate import odeint
    >>> time_vec = np.linspace(0, 4, 40)
    >>> yvec, info = odeint(calc_derivative, 1, time_vec,
    ...                     args=(counter,), full_output=True)

.. The trajectory will now be computed::

..     >>> from scipy.integrate import odeint
..     >>> time_vec = np.linspace(0, 4, 40)
..     >>> yvec, info = odeint(calc_derivative, 1, time_vec,
..     ...                     args=(counter,), full_output=True)

上のように, 微分を与える関数は 40 回以上呼ばれたことがわかります::

    >>> counter
    array([129], dtype=uint16)

.. Thus the derivative function has been called more than 40 times::

..     >>> counter
..     array([129], dtype=uint16)

そして, 最初の10回の収束に対しての累積反復回数はこうして得られます::

    >>> info['nfe'][:10]
    array([31, 35, 43, 49, 53, 57, 59, 63, 65, 69], dtype=int32)

ソルバーは最初の収束により多くの反復回数を必要とします.
最終的な軌道は odeint-introduction.py_ で Matplitlib の figure で見られます.

.. and the cumulative iterations number for the 10 first convergences
.. can be obtained by::

..     >>> info['nfe'][:10]
..     array([31, 35, 43, 49, 53, 57, 59, 63, 65, 69], dtype=int32)

.. The solver requires more iterations at start. The final trajectory is
.. seen on the Matplotlib figure computed with odeint-introduction.py_.

.. image:: odeint-introduction.png
   :align: center

.. _odeint-introduction.py : ../data/odeint-introduction.py

``odeint`` の別の例として減衰振動子（2次の振動子）を扱いましょう.
バネにつながったおもりは2階常微分方程式
``y'' + 2 eps wo  y' + wo^2 y = 0`` に従います.
ここに ``wo^2 = k/m`` で ``k`` はバネ定数で ``m`` は質量,
``eps=c/(2 m wo)`` で ``c`` は減衰定数です.
計算する例として, パラメータは::

    >>> mass = 0.5 # kg
    >>> kspring = 4 # N/m
    >>> cviscous = 0.4 # N s/m

.. Another example with ``odeint`` will be a damped spring-mass oscillator
.. (2nd order oscillator). The position of a mass attached to a spring obeys
.. the 2nd order ODE ``y'' + 2 eps wo  y' + wo^2 y = 0`` with ``wo^2 = k/m``
.. being ``k`` the spring constant, ``m`` the mass and ``eps=c/(2 m wo)``
.. with ``c`` the damping coefficient.
.. For a computing example, the parameters will be::

..     >>> mass = 0.5 # kg
..     >>> kspring = 4 # N/m
..     >>> cviscous = 0.4 # N s/m

系の運動は減衰します, なぜなら::

    >>> eps = cviscous / (2 * mass * np.sqrt(kspring/mass))
    >>> eps < 1
    True

.. so the system will be underdamped because::

..     >>> eps = cviscous / (2 * mass * np.sqrt(kspring/mass))
..     >>> eps < 1
..     True

``odeint`` で2階微分方程式を解くにはベクトル形式 ``Y=(y, y')``
で書かれる1階微分方程式の組に直す必要があります.

そのために ``nu = 2 eps wo = c / m`` と ``om = wo^2 = k/m`` を定義すると便利です::

    >>> nu_coef = cviscous/mass
    >>> om_coef = kspring/mass

.. For the ``odeint`` solver the 2nd order equation needs to be transformed in a
.. system of two first-order equations for the vector ``Y=(y, y')``.  It will
.. be convenient to define ``nu = 2 eps wo = c / m`` and ``om = wo^2 = k/m``::

..     >>> nu_coef = cviscous/mass
..     >>> om_coef = kspring/mass

そうすることで速度と加速度を計算できます::

    >>> def calc_deri(yvec, time, nuc, omc):
    ...     return (yvec[1], -nuc * yvec[1] - omc * yvec[0])
    ...
    >>> time_vec = np.linspace(0, 10, 100)
    >>> yarr = odeint(calc_deri, (1, 0), time_vec, args=(nu_coef, om_coef))

.. Thus the function will calculate the velocity and acceleration by::

..     >>> def calc_deri(yvec, time, nuc, omc):
..     ...     return (yvec[1], -nuc * yvec[1] - omc * yvec[0])
..     ...
..     >>> time_vec = np.linspace(0, 10, 100)
..     >>> yarr = odeint(calc_deri, (1, 0), time_vec, args=(nu_coef, om_coef))

odeint-damped-spring-mass.py_ スクリプトで作った最終的な位置と速度の
Matplotlib の figure を示します.

.. The final position and velocity are shown on a Matplotlib figure
.. built with the odeint-damped-spring-mass.py_ script.

.. image:: odeint-damped-spring-mass.png
   :align: center

.. _odeint-damped-spring-mass.py: ../data/odeint-damped-spring-mass.py

scipy には偏微分方程式 (PDE) のソルバーは含まれません.
Python の PDE パッケージは, fipy_ や SfePy_ などがあります.

.. There is no Partial Differential Equations (PDE) solver
.. in scipy. Some PDE packages are written in Python, such
.. as fipy_ or SfePy_.

.. _fipy: http://www.ctcms.nist.gov/fipy/
.. _SfePy: http://code.google.com/p/sfepy/

高速 Fourier 変換 ： ``scipy.fftpack``
--------------------------------------

.. Fast Fourier transforms: ``scipy.fftpack``
.. ----------------------------------------------
    
``fftpack`` モジュールは高速 Fouier 変換の計算を可能にします.
実例として入力信号をこうしてみます::

    >>> time_step = 0.1
    >>> period = 5.
    >>> time_vec = np.arange(0, 20, time_step)
    >>> sig = np.sin(2 * np.pi / period * time_vec) + \
    ...       np.cos(10 * np.pi * time_vec)

.. The ``fftpack`` module allows to compute fast Fourier transforms.
.. As an illustration, an input signal may look like::

..     >>> time_step = 0.1
..     >>> period = 5.
..     >>> time_vec = np.arange(0, 20, time_step)
..     >>> sig = np.sin(2 * np.pi / period * time_vec) + \
..     ...       np.cos(10 * np.pi * time_vec)

しかし, 観察者は信号の周波数を知らず, 
信号 ``sig`` のサンプリング時間ステップだけを知っています.
ただし, 信号は実関数だと仮定されるので Fourier 変換は対称となります.
``fftfreq`` 関数はサンプリング周波数を生み出し,
``fft`` は高速 Fourier 変換を計算します::

    >>> from scipy import fftpack
    >>> sample_freq = fftpack.fftfreq(sig.size, d=time_step)
    >>> sig_fft = fftpack.fft(sig)

.. However the observer does not know the signal frequency, only
.. the sampling time step of the signal ``sig``. But the signal
.. is supposed to come from a real function so the Fourier transform
.. will be symmetric.
.. The ``fftfreq`` function will generate the sampling frequencies and
.. ``fft`` will compute the fast fourier transform::

..     >>> from scipy import fftpack
..     >>> sample_freq = fftpack.fftfreq(sig.size, d=time_step)
..     >>> sig_fft = fftpack.fft(sig)

とはいえ, 結果のパワースペクトルは対称なので周波数を見つけるのには,
正の部分だけを使います.

    >>> pidxs = np.where(sample_freq > 0)
    >>> freqs = sample_freq[pidxs]
    >>> power = np.abs(sig_fft)[pidxs]

.. Nevertheless only the positive part will be used for finding the frequency
.. because the resulting power is symmetric::

..     >>> pidxs = np.where(sample_freq > 0)
..     >>> freqs = sample_freq[pidxs]
..     >>> power = np.abs(sig_fft)[pidxs]

.. image:: fftpack-frequency.png
   :align: center

このようにして信号周波数をみつけることができます::

    >>> freq = freqs[power.argmax()]
    >>> np.allclose(freq, 1./period)
    True

.. Thus the signal frequency can be found by::

..     >>> freq = freqs[power.argmax()]
..     >>> np.allclose(freq, 1./period)
..     True

今回は Fourier 変換によって主要な周波数だけを取りだしました::

    >>> sig_fft[np.abs(sample_freq) > freq] = 0

.. Now only the main signal component will be extracted from the
.. Fourier transform::

..     >>> sig_fft[np.abs(sample_freq) > freq] = 0

結果として得られる信号は ``ifft`` 関数で計算されます::

    >>> main_sig = fftpack.ifft(sig_fft)

.. The resulting signal can be computed by the ``ifft`` function::

..     >>> main_sig = fftpack.ifft(sig_fft)

fftpack-illustration.py によって結果を Matplitlib の figure で作成し表示します

.. The result is shown on the Matplotlib figure generated by the
.. fftpack-illustration.py_ script.

.. image:: fftpack-signals.png
   :align: center

.. _fftpack-illustration.py: ../data/fftpack-illustration.py


補間 ： ``scipy.interpolate``
------------------------------------

.. Interpolation: ``scipy.interpolate``
.. ------------------------------------

``scipy.interpolate`` は実験データを関数でフィッティングし, 測定していない点を評価するのに便利です.
モジュールは netlib_ の `FITPACK Fortran subroutines`_ を基にしています.

.. The ``scipy.interpolate`` is useful for fitting a function from experimental
.. data and thus evaluating points where no measure exists. The module is based
.. on the `FITPACK Fortran subroutines`_ from the netlib_ project.

.. _`FITPACK Fortran subroutines` : http://www.netlib.org/dierckx/index.html
.. _netlib : http://www.netlib.org

描きだすデータは sin 関数に近い関数にします::

    >>> measured_time = np.linspace(0, 1, 10)
    >>> noise = (np.random.random(10)*2 - 1) * 1e-1
    >>> measures = np.sin(2 * np.pi * measured_time) + noise

.. By imagining experimental data close to a sinus function::

..     >>> measured_time = np.linspace(0, 1, 10)
..     >>> noise = (np.random.random(10)*2 - 1) * 1e-1
..     >>> measures = np.sin(2 * np.pi * measured_time) + noise

``interp1d`` クラスが1次の補間関数を使うために作られています::

    >>> from scipy.interpolate import interp1d
    >>> linear_interp = interp1d(measured_time, measures)

.. The ``interp1d`` class can built a linear interpolation function::

..     >>> from scipy.interpolate import interp1d
..     >>> linear_interp = interp1d(measured_time, measures)

``linear_interp`` インスタンスに評価したい時間を与える必要があります::

    >>> computed_time = np.linspace(0, 1, 50)
    >>> linear_results = linear_interp(computed_time)

.. Then the ``linear_interp`` instance needs to be evaluated on time of interest::

..     >>> computed_time = np.linspace(0, 1, 50)
..     >>> linear_results = linear_interp(computed_time)

``kind`` キーワード引数をオプションとして与えることで3次補間も選択できます::

    >>> cubic_interp = interp1d(measured_time, measures, kind='cubic')
    >>> cubic_results = cubic_interp(computed_time)

.. A cubic interpolation can also be selected by providing the ``kind`` optional
.. keyword argument::

..     >>> cubic_interp = interp1d(measured_time, measures, kind='cubic')
..     >>> cubic_results = cubic_interp(computed_time)

scipy-interpolation.py_ によって結果を Matplotlib の figure にまとめます.

.. The results are now gathered on a Matplotlib figure generated by
.. the script scipy-interpolation.py_.

.. image:: interpolation.png
   :align: center

.. _scipy-interpolation.py : ../data/scipy-interpolation.py

``scipy.interpolate.interp2d`` は ``inter1d`` と似ていまが2次元配列です.
``interp`` ファミリーについて注意しておくことは評価する時間は測定時間の範囲内に留める必要があるということです.
より高度なスプライン補間の例については :ref:`summary_exercise_stat_interp` 統括演習を見て下さい.

.. ``scipy.interpolate.interp2d`` is similar to ``interp1d``, but for 2-D
.. arrays. Note that for the ``interp`` family, the computed time must stay
.. within the measured time range. See the summary exercice  on `Maximum
.. wind speed prediction at the Sprogø station`_ for a more advance spline
.. interpolation example.


最適化とフィット ： ``scipy.optimize``
----------------------------------------

.. Optimization and fit: ``scipy.optimize``
.. ----------------------------------------

最適化とは極小値や方程式の解を数値的に見つけること問題のことです.

.. Optimization is the problem of finding a numerical solution to a
.. minimization or equality.

``scipy.optimize`` は（スカラーまたは多次元の）関数極小化や曲線のフィッティング,
そして根の探索のためのアルゴリズムを提供します.

.. The ``scipy.optimize`` module provides useful algorithms for function
.. minimization (scalar or multi-dimensional), curve fitting and root
.. finding.

**例：異なるアルゴリズムを使ったスカラー関数の極小化** 

.. **Example: Minimizing a scalar function using different algorithms**

以下の関数を定義します::

    >>> def f(x): 
    ...     return x**2 + 10*np.sin(x)

そしてプロットします

.. Let's define the following function: ::

..     >>> def f(x): 
..     ...     return x**2 + 10*np.sin(x)

.. and plot it:

.. doctest::

    >>> x = np.arange(-10,10,0.1)
    >>> plt.plot(x, f(x)) # doctest:+SKIP
    >>> plt.show() # doctest:+SKIP

.. image:: minima-function.png
   :align: center

この関数は -1.3 のまわりで大域的な極小値を持ち, 3.8 のまわりで局所的な極小値をもちます.

.. This function has a global minimum around -1.3 and a local minimum around 3.8.

局所的（凸）最適化
...................

.. Local (convex) optimization
.. ..............................

極小値を見つける一般的で効率的な方法として与えた初期点から勾配が小さくなるように導く方法があります.
BFGS アルゴリズムはこれをするよい方法です::

    >>> optimize.fmin_bfgs(f, 0)
    Optimization terminated successfully.
	    Current function value: -7.945823
	    Iterations: 5
	    Function evaluations: 24
	    Gradient evaluations: 8
    array([-1.30644003])

この解法は私達の計算機で 4.11ms かかりました.

.. The general and efficient way to find a minimum for this function is to 
.. conduct a gradient descent starting from a given initial point. The BFGS
.. algorithm is a good way of doing this::

..     >>> optimize.fmin_bfgs(f, 0)
..     Optimization terminated successfully.
.. 	    Current function value: -7.945823
.. 	    Iterations: 5
.. 	    Function evaluations: 24
.. 	    Gradient evaluations: 8
..     array([-1.30644003])

.. This resolution takes 4.11ms on our computer.

この方法の問題は関数が局所的な極小値を持つ（凸でない）場合,
アルゴリズムは初期値に依存して大域的な極小値の代わりに局所的な極小値を見つけます.
初期点に選ぶべき大域的な極小値の近傍を知らない場合, 高い犠牲を払った大域的な最適化に訴えなければいけません.

.. The problem with this approach is that, if the function has local minima (is 
.. not convex), the algorithm may find these local minima instead of the
.. global minimum depending on the initial point. If we don't know the
.. neighborhood of the global minima to choose the initial point, we need to
.. resort to costlier global opimtization.

大域的な最適化
..............

.. Global optimization
.. .....................

大域的な極小値を探すための最も簡単なアルゴリズムはブルートフォースアルゴリズムで,
与えられた格子上の各点で関数を評価することです::

    >>> from scipy import optimize
    >>> grid = (-10, 10, 0.1)
    >>> optimize.brute(f, (grid,))
    array([-1.30641113])

この方法は私達の計算機で 20 ms かかりました.

.. To find the global minimum, the simplest algorithm is the brute force algorithm,
.. in which the function is evaluated on each point of a given grid: ::

..     >>> from scipy import optimize
..     >>> grid = (-10, 10, 0.1)
..     >>> optimize.brute(f, (grid,))
..     array([-1.30641113])

.. This approach take 20 ms on our computer.

このアルゴリズムは格子のサイズが大きくなるに従いとても遅くなります,
なのでスカラー関数の代わりに ``optimize.brent`` を使うべきです::

    >>> optimize.brent(f)
    -1.3064400120612139

.. This simple alorithm becomes very slow as the size of the grid grows, so you
.. should use ``optimize.brent`` instead for scalar functions: ::

..     >>> optimize.brent(f)
..     -1.3064400120612139

局所的な極小値を探すために, ``optimize.fminbound`` を使って値の拘束条件を追加します::

    >>> # search the minimum only between 0 and 10
    >>> optimize.fminbound(f, 0, 10)
    array([ 3.83746712])

.. To find the local minimum, let's add some constraints on the variable using
.. ``optimize.fminbound``: ::

..     >>> # search the minimum only between 0 and 10
..     >>> optimize.fminbound(f, 0, 10)
..     array([ 3.83746712])

多次元の問題に対する同じ機能を持ったアルゴリズムは ``scipy.optimize`` で入手できます.

より高度な例は :ref:`summary_exercise_optimize` の統括演習を見てください.

.. You can find algorithms with the same functionalities for multi-dimensional
.. problems in ``scipy.optimize``.

.. See the summary exercise on :ref:`summary_exercise_optimize` for a
.. more advanced example.





画像処理 ： ``scipy.ndimage``
-----------------------------------

.. Image processing: ``scipy.ndimage``
.. -----------------------------------

.. include:: image_processing/image_processing.rst





科学技術計算の統括演習
----------------------
    
.. Summary exercices on scientific computing
.. -----------------------------------------

統括演習では Numpy, Scipy そして Matplotlib を主に使います.
Python での科学技術計算を実生活における例として使うことを最初の目的としています.
1度土台を築けば, 興味あるユーザはさらなる演習を試みていくでしょう.

.. The summary exercices use mainly Numpy, Scipy and Matplotlib. They first aim at
.. providing real life examples on scientific computing with Python. Once the
.. groundwork is introduced, the interested user is invited to try some exercices.

.. only:: latex

    .. toctree::
       :maxdepth: 1

       summary-exercices/stats-interpolate.rst
       summary-exercices/optimize-fit.rst
       summary-exercices/image-processing.rst
       summary-exercices/answers_image_processing.rst

.. only:: html

   演習：

   .. toctree::
       :maxdepth: 1

       summary-exercices/stats-interpolate.rst
       summary-exercices/optimize-fit.rst
       summary-exercices/image-processing.rst

   解答例：
    
   .. toctree::
      :maxdepth: 1

      summary-exercices/answers_image_processing.rst

..    Exercises:

..    .. toctree::
..        :maxdepth: 1

..        summary-exercices/stats-interpolate.rst
..        summary-exercices/optimize-fit.rst
..        summary-exercices/image-processing.rst

..    Proposed solutions:

..    .. toctree::
..       :maxdepth: 1

..       summary-exercices/answers_image_processing.rst
