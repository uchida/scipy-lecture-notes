
.. TODO: bench and fit in 1:30

.. TODO: plotting <- broken in OSX

===========================
Sympy : Python での記号計算
===========================

.. ======================================
.. Sympy : Symbolic Mathematics in Python
.. ======================================

.. only:: latex

    :author: Fabian Pedregosa

目標
====

.. Objectives
.. ==========

このセッションの終わりまでで以下のことができるようになります:

  1. 任意精度での数式の評価
  2. 記号表現の代数的な操作の実行
  3. 記号表現での基本的な微積分（極限, 微分, 積分）の実行
  4. 多項式や超越方程式の求解
  5. いくつかの微分方程式の求解

.. At the end of this session you will be able to:

..   1. Evaluate expressions with arbitrary precision.
..   2. Perform algebraic manipulations on symbolic expressions.
..   3. Perform basic calculus tasks (limits, differentiation and
..      integration) with symbolic expressions.
..   4. Solve polynomial and transcendental equations.
..   5. Solve some differential equations.

.. role:: input(strong)

SymPy とは?
===========

.. What is SymPy?
.. ==============

SymPy は Python の記号計算ライブラリです.
コードのシンプルに保ち理解しやすく簡単できる上に,
商用の代替ソフト（Mathematica, Maple）と直接張り合うことのできる
十分な機能を持った代数計算システムを目指しています.
SymPy は全て Python で書かれていて外部ライブラリを必要としません.

.. SymPy is a Python library for symbolic mathematics. It aims become a
.. full featured computer algebra system that can compete directly with
.. commercial alternatives (Mathematica, Maple) while keeping the code as
.. simple as possible in order to be comprehensible and easily
.. extensible.  SymPy is written entirely in Python and does not require
.. any external libraries.


SymPy での第一歩
================

.. first Steps with SymPy
.. ======================


Sympy を計算機として使う
------------------------

.. Using SymPy as a calculator
.. ---------------------------

Sympy は3つの数値型を持っています: Real, Rational そして Integer.

.. SymPy defines three numerical types: Real, Rational and Integer.

Rational クラスは分子と分母の2つの Integer の対として有理数を表現します,
つまり Rational(1,2) は 1/2 を表し, Rational(5,2) は 5/2 を表します::

    >>> from sympy import *
    >>> a = Rational(1,2)

    >>> a
    1/2

    >>> a*2
    1

.. The Rational class represents a rational number as a pair of two
.. Integers: the numerator and the denominator, so Rational(1,2)
.. represents 1/2, Rational(5,2) 5/2 and so on::
.. 
..     >>> from sympy import *
..     >>> a = Rational(1,2)
.. 
..     >>> a
..     1/2
.. 
..     >>> a*2
..     1

Sympy はバックグラウンドで mpmath を利用します, これによって任意精度数値演算を実行できます.
そうすることで, いくつかの特殊な定数 e, pi, oo （無限大）を記号 (symbol) として扱い, さらに任意精度で評価することができます::

    >>> pi**2
    pi**2

    >>> pi.evalf()
    3.14159265358979

    >>> (pi+exp(1)).evalf()
    5.85987448204884

上でみるように, evalf は浮動小数点数として, 数式を評価します.

.. SymPy uses mpmath in the background, which makes it possible to
.. perform computations using arbitrary-precision arithmetic. That
.. way, some special constants, like e, pi, oo (Infinity), are treated as
.. symbols and can be evaluated with arbitrary precision::
.. 
..     >>> pi**2
..     pi**2
.. 
..     >>> pi.evalf()
..     3.14159265358979
.. 
..     >>> (pi+exp(1)).evalf()
..     5.85987448204884

.. as you see, evalf evaluates the expression to a floating-point number.


``oo`` と呼ばれる数学的な無限大を表すクラスもあります::

    >>> oo > 99999
    True
    >>> oo + 1
    oo

.. There is also a class representing mathematical infinity, called
.. ``oo``::
.. 
..     >>> oo > 99999
..     True
..     >>> oo + 1
..     oo


練習問題
--------

.. Exercises
.. ---------

1. :math:`\sqrt{2}` を100桁まで計算しましょう.
2. :math:`1/2 + 1/3` を有理数として計算しましょう.

.. 1. Calculate :math:`\sqrt{2}` with 100 decimals.
.. 2. Calculate :math:`1/2 + 1/3` in rational arithmetic.

記号
----

.. Symbols
.. -------

他の計算代数システムと対照的に, Sympy では記号 (symbol) として使う変数を明示的に宣言しなければいけません::

    >>> from sympy import *
    >>> x = Symbol('x')
    >>> y = Symbol('y')

.. In contrast to other Computer Algebra Systems, in SymPy you have to declare
.. symbolic variables explicitly::
.. 
..     >>> from sympy import *
..     >>> x = Symbol('x')
..     >>> y = Symbol('y')

そしてこれらは算術操作することができます::

    >>> x+y+x-y
    2*x

    >>> (x+y)**2
    (x + y)**2

記号 (symbol) はいくつかの python の演算子で操作することができます: +, -, \*, \*\* （算術演算）,
&, \|, ~ , >>, << （論理演算）.

.. Then you can manipulate them::
.. 
..     >>> x+y+x-y
..     2*x
.. 
..     >>> (x+y)**2
..     (x + y)**2
.. 
.. Symbols can now be manipulated using some of python operators: +, -, \*, \*\* 
.. (arithmetic), &, \|, ~ , >>, << (boolean).


代数的操作
==========

.. Algebraic manipulations
.. =======================

Sympy は強力な代数操作を実行することができます.
最も頻繁に目にするであろうものとして: expand と simplify があります.

.. SymPy is capable of performing powerful algebraic manipulations. We'll
.. take a look into some of the most frequently used: expand and simplify.

展開
----

.. Expand
.. ------

代数表現を展開するために使うことができます.
積や羃は降冪になるように試みます::

    In [23]: expand((x+y)**3)
    Out[23]: 3*x*y**2 + 3*y*x**2 + x**3 + y**3

.. Use this to expand an algebraic expression. It will try to denest
.. powers and multiplications::
.. 
..     In [23]: expand((x+y)**3)
..     Out[23]: 3*x*y**2 + 3*y*x**2 + x**3 + y**3

さらなるオプションをキーワードとして与えることができます::

    In [28]: expand(x+y, complex=True)
    Out[28]: I*im(x) + I*im(y) + re(x) + re(y)

    In [30]: expand(cos(x+y), trig=True)
    Out[30]: cos(x)*cos(y) - sin(x)*sin(y)

.. Further options can be given in form on keywords::
.. 
..     In [28]: expand(x+y, complex=True)
..     Out[28]: I*im(x) + I*im(y) + re(x) + re(y)
.. 
..     In [30]: expand(cos(x+y), trig=True)
..     Out[30]: cos(x)*cos(y) - sin(x)*sin(y)

単純化
------

.. Simplify
.. --------

数式をより簡単な形式に変換する場合に simplify を使うことができます::

    In [19]: simplify((x+x*y)/x)
    Out[19]: 1 + y

.. Use simplify if you would like to transform an expression into a
.. simpler form::
.. 
..     In [19]: simplify((x+x*y)/x)
..     Out[19]: 1 + y

単純化とはいくぶん曖昧な用語です, そのためより目的を明確にした
simplify の代替が存在します: powsimp （指数の単純化）, trigsimp （三角関数を含む数式）,
logcombine, radsimp, togeter.

.. Simplification is a somewhat vague term, and more precises
.. alternatives to simplify exists: powsimp (simplification of
.. exponents), trigsimp (for trigonometric expressions) , logcombine,
.. radsimp, together.

練習問題
--------

.. Exercises
.. ---------

1. :math:`(x+y)^6` の展開を計算しましょう.
2. 三角関数を含む式 :math:`\sin(x) / \cos(x)` を単純化しましょう

.. 1. Calculate the expanded form of :math:`(x+y)^6`.
.. 2. Simplify the trigonometric expression :math:`\sin(x) / \cos(x)`

微積分
======

.. Calculus
.. ========

極限
----

極限は SymPy で簡単に計算することができ limit(function, variable, point) という構文に従います,
つまり f(x) の x-> 0 の極限を計算するには limit(f, x, 0) とします::

   >>> limit(sin(x)/x, x, 0)
   1

.. Limits are easy to use in SymPy, they follow the syntax limit(function,
.. variable, point), so to compute the limit of f(x) as x -> 0, you would issue
.. limit(f, x, 0)::
.. 
..    >>> limit(sin(x)/x, x, 0)
..    1

無限大での極限も計算することができます::

   >>> limit(x, x, oo)
   oo

   >>> limit(1/x, x, oo)
   0

   >>> limit(x**x, x, 0)
   1

.. you can also calculate the limit at infinity::
.. 
..    >>> limit(x, x, oo)
..    oo
.. 
..    >>> limit(1/x, x, oo)
..    0
.. 
..    >>> limit(x**x, x, 0)
..    1

.. index:: differentiation, diff

微分
----

.. Differentiation
.. ---------------

Sympy の任意の数式は ``diff(func, var)`` を使って微分できます.
例::

    >>> diff(sin(x), x)
    cos(x)
    >>> diff(sin(2*x), x)
    2*cos(2*x)

    >>> diff(tan(x), x)
    1 + tan(x)**2

.. You can differentiate any SymPy expression using ``diff(func,
.. var)``. Examples::
.. 
..     >>> diff(sin(x), x)
..     cos(x)
..     >>> diff(sin(2*x), x)
..     2*cos(2*x)
.. 
..     >>> diff(tan(x), x)
..     1 + tan(x)**2

正しいかどうかは以下のようにして確認できます::

    >>> limit((tan(x+y)-tan(x))/y, y, 0)
    1 + tan(x)**2

.. You can check, that it is correct by::
.. 
..     >>> limit((tan(x+y)-tan(x))/y, y, 0)
..     1 + tan(x)**2

高階微分は ``diff(func, var, n)`` メソッドで計算できます::

    >>> diff(sin(2*x), x, 1)
    2*cos(2*x)

    >>> diff(sin(2*x), x, 2)
    -4*sin(2*x)

    >>> diff(sin(2*x), x, 3)
    -8*cos(2*x)

.. Higher derivatives can be calculated using the ``diff(func, var, n)`` method::
.. 
..     >>> diff(sin(2*x), x, 1)
..     2*cos(2*x)
.. 
..     >>> diff(sin(2*x), x, 2)
..     -4*sin(2*x)
.. 
..     >>> diff(sin(2*x), x, 3)
..     -8*cos(2*x)


級数展開
--------

.. Series expansion
.. ----------------

Sympy はある点での数式の Taylor 展開の計算法も備えています::

    >>> series(cos(x), x)
    1 - x**2/2 + x**4/24 + O(x**6)
    >>> series(1/cos(x), x)
    1 + x**2/2 + 5*x**4/24 + O(x**6)

.. SymPy also knows how to compute the Taylor series of an expression at
.. a point. Use ``series(expr, var)``::
.. 
..     >>> series(cos(x), x)
..     1 - x**2/2 + x**4/24 + O(x**6)
..     >>> series(1/cos(x), x)
..     1 + x**2/2 + 5*x**4/24 + O(x**6)


練習問題
--------

.. Exercises
.. ---------

1. :math:`\lim_{x\to0}\sin(x)/x` を計算しなさい.
2. :math:`\log(x)` の :math:`x` についての微分を計算しなさい.

.. 1. Calculate :math:`\lim_{x\to0}\sin(x)/x`
.. 2. Calculate the derivative of :math:`\log(x)` for :math:`x`.

.. index:: integration

積分
----

.. Integration
.. -----------

SymPy は初等関数, 特殊関数の有限無限区間での積分も `integrate()` でサポートしています,
これは強力な Risch-Norman の拡張アルゴリズムといくつかの発見的方法とパターンマッチングを利用しています。
初等関数は以下のように積分できます::

    >>> integrate(6*x**5, x)
    x**6
    >>> integrate(sin(x), x)
    -cos(x)
    >>> integrate(log(x), x)
    -x + x*log(x)
    >>> integrate(2*x + sinh(x), x)
    cosh(x) + x**2

.. SymPy has support for indefinite and definite integration of transcendental
.. elementary and special functions via `integrate()` facility, which uses
.. powerful extended Risch-Norman algorithm and some heuristics and pattern
.. matching. You can integrate elementary functions::
.. 
..     >>> integrate(6*x**5, x)
..     x**6
..     >>> integrate(sin(x), x)
..     -cos(x)
..     >>> integrate(log(x), x)
..     -x + x*log(x)
..     >>> integrate(2*x + sinh(x), x)
..     cosh(x) + x**2

特殊関数も容易に扱うことができます::

    >>> integrate(exp(-x**2)*erf(x), x)
    pi**(1/2)*erf(x)**2/4

.. Also special functions are handled easily::
.. 
..     >>> integrate(exp(-x**2)*erf(x), x)
..     pi**(1/2)*erf(x)**2/4

有限区間での積分も計算できます::

    >>> integrate(x**3, (x, -1, 1))
    0
    >>> integrate(sin(x), (x, 0, pi/2))
    1
    >>> integrate(cos(x), (x, -pi/2, pi/2))
    2

.. It is possible to compute definite integral::
.. 
..     >>> integrate(x**3, (x, -1, 1))
..     0
..     >>> integrate(sin(x), (x, 0, pi/2))
..     1
..     >>> integrate(cos(x), (x, -pi/2, pi/2))
..     2

広義積分もサポートしています::

    >>> integrate(exp(-x), (x, 0, oo))
    1
    >>> integrate(exp(-x**2), (x, -oo, oo))
    pi**(1/2)

.. Also improper integrals are supported as well::
.. 
..     >>> integrate(exp(-x), (x, 0, oo))
..     1
..     >>> integrate(exp(-x**2), (x, -oo, oo))
..     pi**(1/2)


.. index:: equations; algebraic, solve


練習問題
--------

.. Exercises
.. ---------
  
方程式を解く
------------

.. Equation solving
.. ================

SymPy は1つまたはいくつかの変数についての代数方程式を解くことができます::

    In [7]: solve(x**4 - 1, x)
    Out[7]: [I, 1, -1, -I]

.. SymPy is able to solve algebraic equations, in one and several variables::
.. 
..     In [7]: solve(x**4 - 1, x)
..     Out[7]: [I, 1, -1, -I]

ここで見るように, 第1引数の数式は 0 と等しいと前提されます.
多くの多項式方程式を解くことができ,
連立方程式も変数の組を第2引数としてタプルを与えることで解くことができます::

    In [8]: solve([x + 5*y - 2, -3*x + 6*y - 15], [x, y])
    Out[8]: {y: 1, x: -3}

.. As you can see it takes as first argument an expression that is
.. supposed to be equaled to 0. It is able to solve a large part of
.. polynomial equations, and is also capable of solving multiple
.. equations with respect to multiple variables giving a tuple as second argument::
.. 
..     In [8]: solve([x + 5*y - 2, -3*x + 6*y - 15], [x, y])
..     Out[8]: {y: 1, x: -3}

超越方程式も（限定的ですが）サポートされています::

   In [9]: solve(exp(x) + 1, x)
   Out[9]: [pi*I]

.. It also has (limited) support for trascendental equations::
.. 
..    In [9]: solve(exp(x) + 1, x)
..    Out[9]: [pi*I]

多項式の場合には `factor` が代替手段として利用できます.
`factor` は多項式を既約でない項に因数分解し, 多くの領域で因数分解を計算できます::

   In [10]: f = x**4 - 3*x**2 + 1
   In [11]: factor(f)
   Out[11]: (1 + x - x**2)*(1 - x - x**2)

   In [12]: factor(f, modulus=5)
   Out[12]: (2 + x)**2*(2 - x)**2

.. Another alternative in the case of polynomial equations is
.. `factor`. `factor` returns the polynomial factorized into irreducible
.. terms, and is capable of computing the factorization over various domains::
.. 
..    In [10]: f = x**4 - 3*x**2 + 1
..    In [11]: factor(f)
..    Out[11]: (1 + x - x**2)*(1 - x - x**2)
.. 
..    In [12]: factor(f, modulus=5)
..    Out[12]: (2 + x)**2*(2 - x)**2

SymPy は論理式を解くこともできます, つまりある論理式が満される,
または満されないかどうかを決定できます.
そのためには satisfiable を使うことができます::

   In [13]: satisfiable(x & y)
   Out[13]: {x: True, y: True}

.. SymPy is also able to solve boolean equations, that is, to decide if a
.. certain boolean expression is satisfiable or not. For this, we use the
.. function satisfiable::
.. 
..    In [13]: satisfiable(x & y)
..    Out[13]: {x: True, y: True}

これは, (x & y) が True であるには x と y の両方が True である必要があるということを示しています.
もし式が True になることが無い場合, つまり引数を True にできない場合 False を返します::

   In [14]: satisfiable(x & ~x)
   Out[14]: False

.. This tells us that (x & y) is True whenever x and y are both True. If
.. an expression cannot be true, i.e. no values of its arguments can make
.. the expression True, it will return False::
.. 
..    In [14]: satisfiable(x & ~x)
..    Out[14]: False

練習問題
--------
.. Exercises
.. ---------

1. 方程式系 :math:`x + y = 2`, :math:`2\cdot x + y = 0` を解きましょう.
2. ``(~x | y) & (~y | x)`` が True となるような ``x``, ``y`` は存在しますか?

.. 1. Solve the system of equations :math:`x + y = 2`, :math:`2\cdot x + y = 0`
.. 2. Are there boolean values ``x``, ``y`` that make ``(~x | y) & (~y | x)`` true?


多項式計算
==========

.. Polynomial computations
.. =======================

SymPy は効率的な多項式ルーチンを持つ十分なモジュールを持っています.
よく使われるルーチンとして factor, gcd メソッドなどがあります.

.. SymPy has a rich module of efficient polynomial routines. Some of the
.. most commonly used methods are factor, gcd


線形代数
========

.. Linear Algebra
.. ==============

.. index:: Matrix

行列
----

.. Matrices
.. --------

行列は Matrix クラスのインスタンスとして生成できます::

    >>> from sympy import Matrix
    >>> Matrix([[1,0], [0,1]])
    [1, 0]
    [0, 1]

.. Matrices are created as instances from the Matrix class::
.. 
..     >>> from sympy import Matrix
..     >>> Matrix([[1,0], [0,1]])
..     [1, 0]
..     [0, 1]

NumPy の配列と異なり, 記号 (symbol) を含むことができます::

    >>> x = Symbol('x')
    >>> y = Symbol('y')
    >>> A = Matrix([[1,x], [y,1]])
    >>> A
    [1, x]
    [y, 1]

    >>> A**2
    [1 + x*y,     2*x]
    [    2*y, 1 + x*y]

.. unlike a NumPy array, you can also put Symbols in it::
.. 
..     >>> x = Symbol('x')
..     >>> y = Symbol('y')
..     >>> A = Matrix([[1,x], [y,1]])
..     >>> A
..     [1, x]
..     [y, 1]
.. 
..     >>> A**2
..     [1 + x*y,     2*x]
..     [    2*y, 1 + x*y]


.. index:: equations; differential, diff, dsolve

微分方程式
----------

.. Differential Equations
.. ----------------------

SymPy は（いくつかの）常微分方程式を解くことができます.
sympy.ode.dsolve はこのようにして動きます::

    In [4]: f(x).diff(x, x) + f(x)
    Out[4]:
       2
      d
    ─────(f(x)) + f(x)
    dx dx

    In [5]: dsolve(f(x).diff(x, x) + f(x), f(x))
    Out[5]: C₁*sin(x) + C₂*cos(x)

.. SymPy is capable of solving (some) Ordinary Differential
.. Equations. sympy.ode.dsolve works like this::
.. 
..     In [4]: f(x).diff(x, x) + f(x)
..     Out[4]:
..        2
..       d
..     ─────(f(x)) + f(x)
..     dx dx
.. 
..     In [5]: dsolve(f(x).diff(x, x) + f(x), f(x))
..     Out[5]: C₁*sin(x) + C₂*cos(x)

キーワード引数をこの関数に与えることで, 最適な解を見つけるための手助けができます.
例えば方程式が可分離 (separable) であることを知っていればキーワードとして hint='separable' 使って
dsolve に可分離な方程式として扱わせることができます::

   In [6]: dsolve(sin(x)*cos(f(x)) + cos(x)*sin(f(x))*f(x).diff(x), f(x), hint='separable')
   Out[6]: -log(1 - sin(f(x))**2)/2 == C1 + log(1 - sin(x)**2)/2

.. Keyword arguments can be given to this function in order to help if
.. find the best possible resolution system. For example, if you know
.. that it is a separable equations, you can use keyword hint='separable'
.. to force dsolve to resolve it as a separable equation::
.. 
..    In [6]: dsolve(sin(x)*cos(f(x)) + cos(x)*sin(f(x))*f(x).diff(x), f(x), hint='separable')
..    Out[6]: -log(1 - sin(f(x))**2)/2 == C1 + log(1 - sin(x)**2)/2


練習問題
--------

.. Exercises
.. ---------

1. Bernoulli の微分方程式 x*f(x).diff(x) + f(x) - f(x)**2 を解きましょう.

.. warning::

   TODO: correct this equation and convert to math directive!

2. 同じ方程式を hint='Bernoulli' を使って解きましょう. どうなりましたか?

.. 1. Solve the Bernoulli differential equation x*f(x).diff(x) + f(x) - f(x)**2

.. .. warning::
.. 
..    TODO: correct this equation and convert to math directive!

.. 2. Solve the same equation using hint='Bernoulli'. What do you observe ?

