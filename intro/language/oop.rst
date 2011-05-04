オブジェクト指向プログラミング (OOP)
====================================

.. Object-oriented programming (OOP)
.. =================================

Python はオブジェクト指向プログラミング (OOP) をサポートしています.
OOP のゴールは：

    * コードをまとめる, そして

    * 似たような文脈でコードを再利用する.

.. Python supports object-oriented programming (OOP). The goals of OOP are:

..     * to organize the code, and

..     * to re-use code in similar contexts.

ここに簡単な例があります：例では Student **class** を作ります. 
これは独自の関数（ **メソッド (method)** ）と変数（ **属性 (attribute)** ）を集めたオブジェクトで,
こうして使うことができます.

.. Here is a small example: we create a Student **class**, which is an object
.. gathering several custom functions (**methods**) and variables (**attributes**),
.. we will be able to use::

::

    >>> class Student(object):
    ...     def __init__(self, name):
    ...         self.name = name
    ...     def set_age(self, age):
    ...         self.age = age
    ...     def set_major(self, major):
    ...         self.major = major
    ...         
    >>> anna = Student('anna')
    >>> anna.set_age(21)
    >>> anna.set_major('physics')

上の例では, :class:`Student` クラスは :meth:`~Student.__init__`, :meth:`~Student.set_age` そして :meth:`~Student.set_major` メソッドを持っています.
属性 は :attr:`name`, :attr:`age` そして :attr:`major` です.
メソッドと属性は以下の記法で呼び出すことができます：
``classinstance.method`` または ``classinstance.attribute``.
:meth:`__init__` コンストラクタは特別なメソッドで ``MyClass(初期化のためのパラメータ)`` のようにして呼びます.

.. In the previous example, the :class:`Student` class has :meth:`~Student.__init__`, :meth:`~Student.set_age` and
.. :meth:`~Student.set_major` methods. Its attributes are :attr:`name`, :attr:`age` and :attr:`major`. We
.. can call these methods and attributes with the following notation:
.. ``classinstance.method`` or  ``classinstance.attribute``.  The :meth:`__init__`
.. constructor is a special method we call with: ``MyClass(init parameters if
.. any)``.

さて, さきほどのクラスと新しい同じメソッドと属性を持った新しいクラス :class:`MasterStudent` を作りたいとします,
しかし新しいクラスには ``internship`` 属性が加えられます.
**継承 (inherit)** することで, さきほどのクラスをコピーペーストする必要はなくなります.

.. Now, suppose we want to create a new class :class:`MasterStudent` with the same
.. methods and attributes as the previous one, but with an additional
.. ``internship`` attribute. We won't copy the previous class, but
.. **inherit** from it::

::

    >>> class MasterStudent(Student):
    ...     internship = 'mandatory, from March to June'
    ...     
    >>> james = MasterStudent('james')
    >>> james.internship
    'mandatory, from March to June'
    >>> james.set_age(23)
    >>> james.age
    23

:class:`MasterStudent` クラスは :class:`Student` から属性とメソッドを継承しています.

.. The :class:`MasterStudent` class inherited from the :class:`Student` attributes and methods.

クラスとオブジェクト指向プログラミングの恩恵を受けることで,
我々が遭遇する様々なオブジェクト（ :class:`Experiment`, :class:`Image`, :class:`Flow` など）に対応して
独自のメソッドや属性を持った, 様々なクラスにコードをまとめることができます.
さらに継承を使うことで基底クラスを中心とした変種を考える, コードを **再利用** できます.
例： :class:`Flow` 基底クラスから, :class:`StokesFlow`, :class:`TurbulentFlow`, :class:`PotentialFlow` を作るなど.

.. Thanks to classes and object-oriented programming, we can organize code
.. with different classes corresponding to different objects we encounter
.. (an :class:`Experiment` class, an :class:`Image` class, a :class:`Flow` class, etc.), with their own
.. methods and attributes. Then we can use inheritance to consider
.. variations around a base class and **re-use** code. Ex : from a :class:`Flow`
.. base class, we can create derived :class:`StokesFlow`, :class:`TurbulentFlow`,
.. :class:`PotentialFlow`, etc.

