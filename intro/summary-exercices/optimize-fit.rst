.. _summary_exercise_optimize:

非線形最小2乗フィット：トポロジカル lidar の点抽出
-----------------------------------------------------------------

.. Non linear least squares curve fitting: application to point extraction in topographical lidar data
.. ---------------------------------------------------------------------------------------------------

この演習問題の目的は特定のデータに対してモデルをフィットすることです.
このチュートリアルでは lidar のデータを使います.
lidar のデータについては以下の導入の段落で説明します.
もし待ち切れなくてすぐにでも実践したければ飛して直接 :ref:`first_step` に向かって下さい.

.. The goal of this exercise is to fit a model to some data. The data used in this tutorial are lidar data and are described in details in the following introductory paragraph. If you're impatient and want to practise now, please skip it ang go directly to :ref:`first_step`.


導入
~~~~

.. Introduction
.. ~~~~~~~~~~~~

Lidar は光学距離計測系で, 距離測定のために散乱光の性質を解析します.
多くの lidar は短いインパルス光を対象に対して放出し反射信号を記録します.
信号は解析されて lidar と対象の間の距離が抽出されます.

.. Lidars systems are optical rangefinders that analyze property of scattered light
.. to measure distances. Most of them emit a short light impulsion towards a target
.. and record the reflected signal. This signal is then processed to extract the
.. distance between the lidar sytem and the target.

トポロジカル lidar はそのような計測系を飛行機の機体に搭載したものです.
地球と飛行機間の距離を即停止, 地球の地形の情報を伝えます（詳しくは [Mallet09]_ を見てください）.

.. Topographical lidar systems are such systems embedded in airborne
.. platforms. They measure distances between the platform and the Earth, so as to
.. deliver information on the Earth's topography (see [Mallet09]_ for more details).

チュートリアルでの目的は Lidar 系に記録された波形 [#data]_ を解析することです.
この信号は中心にピークを持ち, 振幅から距離やいくつかの特徴を計算できます.
レーザービームの足跡が地球上約 1m に及ぶと, 2方向伝搬の間でビームは複数の対象に当りうります
（例えば木やビルの頂上と地面）
レーザービームが各対象に当った寄与の和は複数のピークを持った複雑な信号を作りだします,
各ピークに一つの対象の情報が含まれています.

.. In this tutorial, the goal is to analyze the waveform recorded by the lidar
.. system [#data]_. Such a signal contains peaks whose center and amplitude permit to
.. compute the position and some characteristics of the hit target. When the
.. footprint of the laser beam is around 1m on the Earth surface, the beam can hit
.. multiple targets during the two-way propagation (for example the ground and the
.. top of a tree or building). The sum of the contributions of each target hit by
.. the laser beam then produces a complex signal with multiple peaks, each one
.. containing information about one target.

これらのデータから情報を取り出す最新技術の一つはデータをレーザービームに当った寄与を表現する
Gauss 関数の和として分解する方法があります.

.. One state of the art method to extract information from these data is to
.. decompose them in a sum of Gaussian functions where each function represents the
.. contribution of a target hit by the laser beam.

したがって, 波形を一つの Gauss 関数または Gauss 関数の和でフィットするために
``sicpy.optimize`` モジュールを使います.

.. Therefore, we use the ``scipy.optimize`` module to fit a waveform to one or a sum of
.. Gaussian functions.

.. _first_step:

読み込みと可視化
~~~~~~~~~~~~~~~~

.. Loading and visualization
.. ~~~~~~~~~~~~~~~~~~~~~~~~~

最初の波形を読み込みます::

    >>> import numpy as np
    >>> waveform_1 = np.load('data/waveform_1.npy')

.. Load the first waveform using::

..     >>> import numpy as np
..     >>> waveform_1 = np.load('data/waveform_1.npy')

そして可視化します：

.. and visualize it:

.. doctest::

    >>> import matplotlib.pyplot as plt
    >>> t = np.arange(len(waveform_1))
    >>> plt.plot(t, waveform_1) # doctest:+SKIP
    >>> plt.show() # doctest:+SKIP

.. image:: waveform_1.png
   :align: center

As you can notice, this waveform is a 80-bin-length signal with a single peak.
気づくと思いますが, この波形は一つのピークを持った 80 の区画に分けられた信号です.

.. As you can notice, this waveform is a 80-bin-length signal with a single peak.

波形を単純な Gauss モデルでフィット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. Fitting a waveform with a simple Gaussian model
.. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

信号は単純なので一つの Gauss 関数とバックグラウンドノイズに対応するずれとして表現できます.
信号を関数でフィットするためには以下をしなければいけません：

* モデルを定義
* 初期解を提案
* ``scipy.optimize.leastsq`` を呼びだす

.. The signal is very simple and can be modelled as a single Gaussian function and
.. an offset corresponding to the background noise. To fit the signal with the
.. function, we must:

.. * define the model
.. * propose an initial solution
.. * call ``scipy.optimize.leastsq``


モデル
^^^^^^

.. Model
.. ^^^^^

Gauss 関数を定義します

.. A gaussian function defined by

.. math::
   B + A \exp\left\{-\left(\frac{t-\mu}{\sigma}\right)^2\right\}

Python では以下で定義できます::

    >>> def model(t, coeffs):
    ...    return coeffs[0] + coeffs[1] * np.exp( - ((t-coeffs[2])/coeffs[3])**2 )

.. can be defined in python by::

..     >>> def model(t, coeffs):
..     ...    return coeffs[0] + coeffs[1] * np.exp( - ((t-coeffs[2])/coeffs[3])**2 )

ここに

* ``coeffs[0]`` is :math:`B` (ノイズ)
* ``coeffs[1]`` is :math:`A` (振幅)
* ``coeffs[2]`` is :math:`\mu` (中心)
* ``coeffs[3]`` is :math:`\sigma` (幅)

.. where

.. * ``coeffs[0]`` is :math:`B` (noise)
.. * ``coeffs[1]`` is :math:`A` (amplitude)
.. * ``coeffs[2]`` is :math:`\mu` (center)
.. * ``coeffs[3]`` is :math:`\sigma` (width)


初期解
^^^^^^

.. Initial solution
.. ^^^^^^^^^^^^^^^^

グラフを見て初期の近似解を例えば以下のようにしてみます::

    >>> x0 = np.array([3, 30, 15, 1], dtype=float)

.. An approximative initial solution that we can find from looking at the graph is
.. for instance::

..     >>> x0 = np.array([3, 30, 15, 1], dtype=float)

フィット
^^^^^^^^

.. Fit
.. ^^^

``scipy.optimize.leastsq`` は引数として与えた関数の2乗の和を最小化します.
基本的に最小化する関数は残余（データとモデルの差）です::

    >>> def residuals(coeffs, y, t):
    ...     return y - model(t, coeffs)

.. ``scipy.optimize.leastsq`` minimizes the sum of squares of the function given as
.. an argument. Basically, the function to minimize is the residuals (the
.. difference between the data and the model)::

..     >>> def residuals(coeffs, y, t):
..     ...     return y - model(t, coeffs)

さて以下の引数で ``sipy.optimize.leastsq`` を呼び出して解を得ましょう：

* 最小化する関数
* 初期解
* 関数に渡す追加の引数

.. So let's get our solution by calling ``scipy.optimize.leastsq`` with the
.. following arguments:

.. * the function to minimize
.. * an initial solution
.. * the additional arguments to pass to the function

.. doctest::

    >>> from scipy.optimize import leastsq
    >>> x, flag = leastsq(residuals, x0, args=(waveform_1, t))
    >>> print x
    [  2.70363341  27.82020742  15.47924562   3.05636228]

そして解を可視化します：

.. And visualize the solution:

.. doctest::

    >>> plt.plot(t, waveform_1, t, model(t, x)) # doctest:+SKIP
    >>> plt.legend(['waveform', 'model']) # doctest:+SKIP
    >>> plt.show() # doctest:+SKIP

*Remark:* scipy v0.8 以上では ``scipy.optimize.curve_fit`` を使うべきです. これはモデルとデータを引数としてとるので残余を定義する必要はありません.

.. *Remark:* from scipy v0.8 and above, you should rather use ``scipy.optimize.curve_fit`` which takes the model and the data as arguments, so you don't need to define the residuals any more.

より進んで
~~~~~~~~~~

.. Going further
.. ~~~~~~~~~~~~~

* より複雑な波形に挑戦してみましょう （例として ``data/waveform_2.npy`` ）
  これは三つの著しいピークを含みます. 1つの Gauss 関数 の代わりに3つの Gauss 関数の和を使う必要があります.

.. * Try with a more complex waveform (for instance ``data/waveform_2.npy``)
..   that contains three significant peaks. You must adapt the model which is
..   now a sum of Gaussian functions instead of only one Gaussian peak.

.. image:: waveform_2.png
   :align: center

* ``leastsq`` を数値的に評価するよりも Jacobian を計算する関数を明示的に書いた方が場合があります.
  残余の Jacobian を計算する関数を作り, ``leastsq`` の入力に使ってみましょう.

.. * In some cases, writing an explicit function to compute the Jacobian is faster
..   than letting ``leastsq`` estimate it numerically. Create a function to compute
..   the Jacobian of the residuals and use it as an input for ``leastsq``.

* 信号の小さなピークを検出したい, または初期解が妥当でない場合には与えたアルゴリズムは不満足な結果を与えます.
  パラメータの拘束条件を追加することでこの制限に打ち克つことができます.
  追加できる *アプリオリ* な知識の例は変数の符号です（これらは全て正）

  以下の初期解::

    >>> x0 = np.array([3, 50, 20, 1], dtype=float)

  を使って ``scipy.optimize.leastsq`` と拘束条件を追加して ``scipy.optimize.fmin_slsqp`` で得た結果を比較してみましょう.

.. * When we want to detect very small peaks in the signal, or when the initial
..   guess is too far from a good solution, the result given by the algorithm is
..   often not satisfying. Adding constraints to the parameters of the model
..   enables to overcome such limitations. An example of *a priori* knowledge we can
..   add is the sign of our variables (which are all positive).

..   With the following initial solution::

..     >>> x0 = np.array([3, 50, 20, 1], dtype=float)

..   compare the result of ``scipy.optimize.leastsq`` and what you can get with
..   ``scipy.optimize.fmin_slsqp`` when adding boundary constraints.


.. [#data] このチュートリアルで使った実演データは `FullAnalyze software <http://fullanalyze.sourceforge.net>`_ から入手できます, これらは `GIS DRAIX <http://www.ore.fr/rubrique.php3?id_rubrique=24>`_ が快く提供してくれました.

.. [Mallet09] Mallet, C. and Bretar, F. Full-Waveform Topographic Lidar: State-of-the-Art. *ISPRS Journal of Photogrammetry and Remote Sensing* 64(1), pp.1-16, January 2009 http://dx.doi.org/10.1016/j.isprsjprs.2008.09.007

.. .. [#data] The data used for this tutorial are part of the demonstration data available for the `FullAnalyze software <http://fullanalyze.sourceforge.net>`_ and were kindly provided by the `GIS DRAIX <http://www.ore.fr/rubrique.php3?id_rubrique=24>`_.

.. .. [Mallet09] Mallet, C. and Bretar, F. Full-Waveform Topographic Lidar: State-of-the-Art. *ISPRS Journal of Photogrammetry and Remote Sensing* 64(1), pp.1-16, January 2009 http://dx.doi.org/10.1016/j.isprsjprs.2008.09.007
