.. _summary_exercise_stat_interp:

Sprogø 気象局の最大風速予測
----------------------------

.. Maximum wind speed prediction at the Sprogø station
.. ---------------------------------------------------

練習問題の目的は50年間の最大風速を予測することです,
ただし, 予測はそのような期間に渡る測定がされていない場合に行ないます.
入手可能なデータはデンマークの Sprogø 気象局での21年間のデータだけです.
まず最初に統計的な手段を与えて, :mod:`scipy.interpolate` モジュールから関数を描きます.
そして最後に興味ある読者は全く異なる方法を使い結果を生データから計算することになるでしょう.

.. The exercise goal is to predict the maximum wind speed occuring every
.. 50 years even if no measure exists for such a period. The available
.. data are only measured over 21 years at the Sprogø meteorological
.. station located in Denmark. First, the statistical steps will be given
.. and then illustrated with functions from the :mod:`scipy.interpolate` module.
.. At the end the interested readers are invited to compute results from
.. raw data and in a slightly different approach.

統計的方法
~~~~~~~~~~

.. Statistical approach
.. ~~~~~~~~~~~~~~~~~~~~

年間の最大値は正規分布にフィットできると考えられます.
しかしこの関数は予測に使うことはできません,
なぜならこの関数は風速の最大値から確率を与える関数だからです.
50年間の最大値を知るには逆の方法が必要となり,
定義された確率から結果を求める必要があります.
これが分位点関数の役割です, そして目的はこの関数を見つけることになります.
現在のモデルでは, 50年間の年間最大値は上位 2 % の分位点として定義されると考えられます.

.. The annual maxima are supposed to fit a normal probability density
.. function. However such function is not going to be estimated because
.. it gives a probability from a wind speed maxima. Finding the maximum wind
.. speed occuring every 50 years requires the opposite approach, the result
.. needs to be found from a defined probabilty. That is the quantile function
.. role and the exercise goal will be to find it. In the current model,
.. it is supposed that the maximum wind speed occuring every 50 years is
.. defined as the upper 2$%$ quantile.

定義から分位点関数は累積分布関数の逆関数です.
後者は年間の最大値の分布関数を表わします.
練習問題では, :math:`i` 年の累積確率 :math:`p_i` を :math:`p_i = i/(N+1)`, 測定年数 :math:`N = 21` とします.
これで各年で測定された最大風速の累積確率を計算できます.
:mod:`scipy.interpolate` モジュールを使ってこれらの測定点から分位点関数をフィットするのが有効です.
最終的に50年の最大値は 2% 分位点の累積分布関数から評価できます.

.. By definition, the quantile function is the inverse of the cumulative
.. distribution function. The latter describes the probability distribution
.. of an annual maxima. In the exercise, the cumulative probabilty :math:`p_i`
.. for a given year :math:`i` is defined as :math:`p_i = i/(N+1)` with :math:`N = 21`,
.. the number of measured years. Thus it will be possible to calculate
.. the cumulative probability of every measured wind speed maxima.
.. From those experimental points, the scipy.interpolate module will be
.. very useful for fitting the quantile function. Finally the 50 years
.. maxima is going to be evaluated from the cumulative probability
.. of the 2% quantile.

累積確率の計算
~~~~~~~~~~~~~~

.. Computing the cumulative probabilites
.. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

年間風速の最大値は, 既に計算されて max-speeds.npy_ ファイルに numpy 形式で保存されています,
なので numpy を使って読み込みます::

    >>> import numpy as np
    >>> max_speeds = np.load('data/max-speeds.npy')
    >>> years_nb = max_speeds.shape[0]

.. The annual wind speeds maxima have already been computed and saved in
.. the numpy format in the file max-speeds.npy_, thus they will be loaded
.. by using numpy::

..     >>> import numpy as np
..     >>> max_speeds = np.load('data/max-speeds.npy')
..     >>> years_nb = max_speeds.shape[0]

.. _max-speeds.npy : ../../data/max-speeds.npy

前の節の累積確率 :math:`p_i` の定義に従って, 対応する値は::

    >>> cprob = (np.arange(years_nb, dtype=np.float32) + 1)/(years_nb + 1)

そして, これらは与えられた風速をフィットすると仮定されます::

    >>> sorted_max_speeds = np.sort(max_speeds)

.. Following the cumulative probability definition ``p_i`` from the previous
.. section, the corresponding values will be::

..     >>> cprob = (np.arange(years_nb, dtype=np.float32) + 1)/(years_nb + 1)

.. and they are assumed to fit the given wind speeds::

..     >>> sorted_max_speeds = np.sort(max_speeds)


UnivariateSpline による予測
~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
.. Prediction with UnivariateSpline
.. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

この節では分位点関数を, 点からスプラインを表現する
:class:`UnivariateSpline` クラスを使って予測します.
デフォルトの挙動では3次スプラインを使い,
点は信頼度に応じて異なる重みが与えられます.
変種に :class:`InterpolatedUnivariateSpline` と :class:`LSQUnivariateSpline` があり,
これらは誤差の抑制に違いがあります.
2次元のスプラインが欲しい場合には :class:`BivariateSpline` クラスファミリーが提供されます.
これらの1次元, 2次元スプラインは FITPACK Fortran サブルーチンを使います,
その結果としてスプラインを表現, 評価する :func:`splrep`, :func:`splev` を経由する低レベルライブラリーにアクセスすることができます.
またより単純な目的のために FITPACK パラメータを使わない補間関数も提供されています
（ :class:`interp1d`, :class:`interp2d`, :func:`barycentric_interpolate` を見てください）.


.. In this section the quantile function will be estimated by using the
.. :class:`UnivariateSpline` class which can represent a spline from points. The
.. default behavior is to build a spline of degree 3 and points can
.. have different weights according to their reliability. Variantes are
.. :class:`InterpolatedUnivariateSpline` and :class:`LSQUnivariateSpline` on which
.. errors checking is going to change.  In case a 2D spline is wanted,
.. the :class:`BivariateSpline` class family is provided. All thoses classes
.. for 1D and 2D splines use the FITPACK Fortran subroutines, that's why a
.. lower library access is available through the :func:`splrep` and :func:`splev`
.. functions for respectively representing and evaluating a spline.
.. Moreover interpolation functions without the use of FITPACK parameters
.. are also provided for simpler use (see :class:`interp1d`, :class:`interp2d`,
.. :class:`barycentric_interpolate` and so on).

3次スプラインでデータを正確にフィットできているようなので,
Sprogø の最大風速のために :class:`UnivariateSpline` を使います::

    >>> from scipy.interpolate import UnivariateSpline
    >>> quantile_func = UnivariateSpline(cprob, sorted_max_speeds)

.. For the Sprogø maxima wind speeds, the :class:`UnivariateSpline` will be
.. used because a spline of degree 3 seems to correctly fit the data::

..     >>> from scipy.interpolate import UnivariateSpline
..     >>> quantile_func = UnivariateSpline(cprob, sorted_max_speeds)

さてこれで分位点関数が確率の全領域に渡って評価されます::

    >>> nprob = np.linspace(0, 1, 1e2)
    >>> fitted_max_speeds = quantile_func(nprob)

.. The quantile function is now going to be evaluated from the full range
.. of probabilties::

..     >>> nprob = np.linspace(0, 1, 1e2)
..     >>> fitted_max_speeds = quantile_func(nprob)

2%

現在のモデルでは50年間の最大風速は上位 2% の分位点で定義されます.
結果として累積確率の値は::
    
    >>> fifty_prob = 1. - 0.02

.. In the current model, the maximum wind speed occuring every 50 years is
.. defined as the upper 2% quantile. As a result, the cumulative probability
.. value will be::
    
..     >>> fifty_prob = 1. - 0.02

その結果50年の間に起きる暴風の風速が推測されます::

    >>> fifty_wind = quantile_func(fifty_prob)
    >>> fifty_wind
    array([ 32.97989825])

.. So the storm wind speed occuring every 50 years can be guessed by::

..     >>> fifty_wind = quantile_func(fifty_prob)
..     >>> fifty_wind
..     array([ 32.97989825])

結果を Matplotlib の figure にまとめます：

.. plot:: pyplots/cumulative_wind_speed_prediction.py

.. The results are now gathered on a Matplotlib figure:

.. .. plot:: pyplots/cumulative_wind_speed_prediction.py

Gumbell 分布での練習問題
~~~~~~~~~~~~~~~~~~~~~~~~

.. Exercise with the Gumbell distribution
.. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

興味ある読者は21年間の風速測定データを使って練習問題を作りたいと思っているでしょう.
測定周期は90分です（元の周期は10分でしたが練習問題の準備を簡単にするためファイルサイズを小さくしました）.
データは sprog-windspeeds.npy_ に numpy 形式で保存されています.
練習問題が終わるまで, 作図のソースコードはみないで下さい.

.. The interested readers are now invited to make an exercise by using the wind
.. speeds measured over 21 years. The measurement period is around 90 minutes (the
.. original period was around 10 minutes but the file size has been reduced for
.. making the exercise setup easier). The data are stored in numpy format inside
.. the file sprog-windspeeds.npy_. Do not look at the source code for the plots until you have completed the exercise.

.. _sprog-windspeeds.npy : ../data/sprog-windspeeds.npy

* まずは年間での最大値を入手して matplotlib の棒グラフで表示しましょう.

  .. plot:: pyplots/sprog_annual_maxima.py

.. * The first step will be to find the annual maxima by using numpy
..   and plot them as a matplotlib bar figure.

.. .. plot:: pyplots/sprog_annual_maxima.py


* 次は累積確率 :math:`p_i` に対して定義される Gumbell 分布 :math:`-\log\left(-\log(p_i)\right)`
  を線形分位点関数のフィッティングに使ってみましょう（ :class:`UnvariateSpline` の次数を定義するのを忘れないように）.
  年間の最大値と Gumbell 分布は以下のような図になるはずです.

  .. plot:: pyplots/gumbell_wind_speed_prediction.py

.. * The second step will be to use the Gumbell distribution on cumulative
..   probabilities :math:`p_i` defined as :math:`-\log\left(-\log(p_i) \\right)` for fitting
..   a linear quantile function (remember that you can define the degree
..   of the ``UnivariateSpline``). Plotting the annual maxima versus the
..   Gumbell distribution should give you the following figure.

.. .. plot:: pyplots/gumbell_wind_speed_prediction.py

* 最後に50年の間に起きる最大風速として 34.23 m/s を得るはずです.

.. * The last step will be to find 34.23 m/s for the maximum wind speed
..   occuring every 50 years.

