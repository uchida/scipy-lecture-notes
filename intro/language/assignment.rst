代入演算子
==========

..
    Assignment operator
    ===================

`Python library reference
<http://docs.python.org/reference/simple_stmts.html#assignment-statements>`_ [*]_
によると：

  代入文は, 名前を値に (再) 束縛したり, 変更可能なオブジェクトの属性や要素を変更し
  たりするために使われます

..
    `Python library reference
    <http://docs.python.org/reference/simple_stmts.html#assignment-statements>`_
    says:
    
      Assignment statements are used to (re)bind names to values and to
      modify attributes or items of mutable objects.

簡単にいえば, 以下のように動作します（単純代入）：

#. 右辺の式が評価され, 対応する値が得られる

#. 左辺の名前に値が代入, あるいは束縛される

..
    In short, it works as follows (simple assignment):
    
    #. an expression on the right hand side is evaluated, the corresponding
       object is created/obtained
    #. a **name** on the left hand side is assigned, or bound, to the
       r.h.s. object

注意すべきこと：

.. Things to note:

* 単一のオブジェクトは束縛される名前をいくつも持ち得る：

.. * a single object can have several names bound to it:

    .. sourcecode:: ipython

        In [1]: a = [1, 2, 3]
        In [2]: b = a
        In [3]: a
        Out[3]: [1, 2, 3]
        In [4]: b
        Out[4]: [1, 2, 3]
        In [5]: a is b
        Out[5]: True
	In [6]: b[1] = 'hi!'
	In [7]: a
	Out[7]: [1, 'hi!', 3]

* リストを *インプレース* に変更するには, インデクス指定かスライスを使う：

    .. sourcecode:: ipython

        In [1]: a = [1, 2, 3]
        In [3]: a
        Out[3]: [1, 2, 3]
        In [4]: a = ['a', 'b', 'c'] # 別のオブジェクトを作る
        In [5]: a
        Out[5]: ['a', 'b', 'c']
        In [6]: id(a)
        Out[6]: 138641676
        In [7]: a[:] = [1, 2, 3] # インプレースにオブジェクトを変更する
        In [8]: a
        Out[8]: [1, 2, 3]
        In [9]: id(a)
        Out[9]: 138641676 # Out[6] と同じ結果になります. ただ, この値はあなたの結果とは違うでしょう...

..
    .. * to change a list *in place*, use indexing/slices:
    
    .. sourcecode:: ipython
    
        In [1]: a = [1, 2, 3]
        In [3]: a
        Out[3]: [1, 2, 3]
        In [4]: a = ['a', 'b', 'c'] # Creates another object.
        In [5]: a
        Out[5]: ['a', 'b', 'c']
        In [6]: id(a)
        Out[6]: 138641676
        In [7]: a[:] = [1, 2, 3] # Modifies object in place.
        In [8]: a
        Out[8]: [1, 2, 3]
        In [9]: id(a)
        Out[9]: 138641676 # Same as in Out[6], yours will differ...

* ここでの重要な概念は **変更可能か変化不可能か** です

    * 変更可能なオブジェクトはインプレイスに変更されます
    * 変化不可能なオブジェクトは一旦作られたら変更できません

..
    * the key concept here is **mutable vs. immutable**
    
        * mutable objects can be changed in place
        * immutable objects cannot be modified once created

David M. Beazley による記事 `Types and Objects in Python
<http://www.informit.com/articles/article.aspx?p=453682>`_
に上の話題についてのとても素晴しい, 詳しい解説があります.

..
    A very good and detailed explanation of the above issues can be found
    in David M. Beazley's article `Types and Objects in Python
        <http://www.informit.com/articles/article.aspx?p=453682>`_.

.. rubric:: footnotes

.. [*] 日本語訳 `Python 言語レファレンス <http://www.python.jp/doc/release/reference/simple_stmts.html#assignment-statement>`_
