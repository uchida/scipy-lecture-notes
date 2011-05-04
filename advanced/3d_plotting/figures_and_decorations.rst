図と装飾
========

.. Figures and decorations
.. =======================

図の管理
--------

.. Figure management
.. -----------------

.. only:: latex

    これは現在の図を制御するのに便利な関数のリストです

.. .. only:: latex
.. 
..     Here is a list of functions useful to control the current figure


================================ ==============================================================
================================ ==============================================================
現在の図を得る                   `mlab.gcf()`
-------------------------------- --------------------------------------------------------------
現在の図を片付ける               `mlab.clf()`
-------------------------------- --------------------------------------------------------------
現在の図を設置する               `mlab.figure(1, bgcolor=(1, 1, 1), fgcolor=(0.5, 0.5, 0.5)`
-------------------------------- --------------------------------------------------------------
図を画像に保存する               `mlab.savefig('foo.png', size=(300, 300))`
-------------------------------- --------------------------------------------------------------
視点を変更する                   `mlab.view(azimuth=45, elevation=54, distance=1.)`
================================ ==============================================================

.. ================================ ==============================================================
.. ================================ ==============================================================
.. Get the current figure:		  `mlab.gcf()`
.. -------------------------------- --------------------------------------------------------------
.. Clear the current figure:	  `mlab.clf()`
.. -------------------------------- --------------------------------------------------------------
.. Set the current figure:		  `mlab.figure(1, bgcolor=(1, 1, 1), fgcolor=(0.5, 0.5, 0.5)`
.. -------------------------------- --------------------------------------------------------------
.. Save figure to image file:	  `mlab.savefig('foo.png', size=(300, 300))`
.. -------------------------------- --------------------------------------------------------------
.. Change the view:		  mlab.view(azimuth=45, elevation=54, distance=1.)
.. ================================ ==============================================================

作図のプロパティを変更する
--------------------------

.. Changing plot properties
.. -------------------------

.. only:: latex

    一般的に図の中のいろいろなオブジェクトの多くの性質は変更可能です.
    可視化したものが `mlab` 関数を通して作成されたものの場合,
    これらを変更するにはそれらの関数のドキュメンテーション文字列で記述されているように
    keyword 引数を使うのが最も簡単な方法です.

.. .. only:: latex
.. 
..     In general, many properties of the various objects on the figure can
..     be changed. If these visualization are created via `mlab` functions, 
..     the easiest way to change them is to use the keyword arguments of
..     these functions, as described in the docstrings.

.. topic:: **ドキュメンテーション文字列の例:** `mlab.mesh`

    二次元配列として与えられた、格子状に並んだデータを表面として作図しましょう.
    
    **関数の特徴**::
    
        mesh(x, y, z, ...)
    
    x, y, z は二次元配列で全て同じシェイプで表面の頂点を与えます.
    これらの点の連結は配列上での連結を意味します.
    
    surf 関数には（正方格子のような）単純な構造が望ましいです,
    そうすることで効率的なデータ構造を作ることができます.
    
    **キーワード引数:**
    
        :color: vtk オブジェクトの色. colormap が指定されている場合にはそれが優先されます.
                色は 0 から 1 までの浮動小数点数の三つ組で指定されます, 例として白は (1, 1 , 1).
                
        :colormap: 使うカラーマップのタイプ
                   
        :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
                 デフォルトでは x, y, x の配列の範囲です.
                 作成されるオブジェクトの範囲を変更したいときに利用すます.
                 
        :figure: 移植したい図
                 
        :line_width: 線の太さ. 浮動小数点数でなければいけません. デフォルト: 2.0
                     
        :mask: データの点を減らすためのブーリアン値のマスク配列.
               
        :mask_points: 与えられた場合 'mask_points' 外のデータ点だけが表示されます.
                      このオプションは整数か None からなる巨大なデータセットで表示する点を減らすのに便利です.
                      
        :mode: グリフ (glyph) のモード. '2darrow', '2dcircle', '2dcross', '2ddash', '2ddiamond',
               '2dhooked_arrow', '2dsquare', '2dthick_arrow', '2dthick_cross' or
               '2dtriangle', '2dvertex', 'arrow', 'cone', 'cube' or
               'cylinder', 'point', 'sphere' のどれかでなければいけません.
               デフォルト: sphere
               
        :name: 作成される vtk オブジェクトの名前.

        :representation: 表面の表示のタイブ.
                         'surface', 'wireframe', 'points', 'mesh' or
                         'fancymesh' のどれかでなければいけません.
                         デフォルト: surface
                         
        :resolution: 作成されるグリフ (glyph) の解像度
                     例えば sphere に対しては theta と phi の分割数です.
                     整数でなければいけません. デフォルト: 8
                     
        :scalars: オプションとしてのスカラーデータ.
                  
        :scale_factor: fancy_mesh モードでの頂点を表す glyph の縮尺係数.
                       浮動小数点数でなければいけません. デフォルト: 0.05
                       
        :scale_mode: glyph の縮尺モード
                     ('vector', 'scalar', または 'none').
                     
        :transparent: 数値に応じて actor の透明度を設定します.
                      
        :tube_radius: mesh モードでの線を表わすためのチューブの半径.
                      None の場合には, 単純な線が使われます.
                      
        :tube_sides: 線を表わすためのチューブの側面の数.
                     浮動小数点数でなければいけません. デフォルト: 6
                     
        :vmax: vmax はカラーマップの目盛に使われます.
               None の場合, データの最大値が使われます.
               
        :vmin: vmin はカラーマップの目盛に使われます.
               None の場合, データの最小値が使われます.
    
.. .. topic:: **Example docstring:** `mlab.mesh`
.. 
..     Plots a surface using grid-spaced data supplied as 2D arrays.
..     
..     **Function signatures**::
..     
..         mesh(x, y, z, ...)
..     
..     x, y, z are 2D arrays, all of the same shape, giving the positions of
..     the vertices of the surface. The connectivity between these points is
..     implied by the connectivity on the arrays.
..     
..     For simple structures (such as orthogonal grids) prefer the surf function,
..     as it will create more efficient data structures.
..     
..     **Keyword arguments:**
..     
..         :color: the color of the vtk object. Overides the colormap,
..                 if any, when specified. This is specified as a
..                 triplet of float ranging from 0 to 1, eg (1, 1,
..                 1) for white.
..                 
..         :colormap: type of colormap to use.
..                    
..         :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
..                  Default is the x, y, z arrays extents. Use
..                  this to change the extent of the object
..                  created.
..                  
..         :figure: Figure to populate.
..                  
..         :line_width:  The with of the lines, if any used. Must be a float.
..                      Default: 2.0
..                      
..         :mask: boolean mask array to suppress some data points.
..                
..         :mask_points: If supplied, only one out of 'mask_points' data point is
..                       displayed. This option is usefull to reduce the number
..                       of points displayed on large datasets Must be an integer
..                       or None.
..                       
..         :mode: the mode of the glyphs. Must be '2darrow' or '2dcircle' or
..                '2dcross' or '2ddash' or '2ddiamond' or '2dhooked_arrow' or
..                '2dsquare' or '2dthick_arrow' or '2dthick_cross' or
..                '2dtriangle' or '2dvertex' or 'arrow' or 'cone' or 'cube' or
..                'cylinder' or 'point' or 'sphere'. Default: sphere
..                
..         :name: the name of the vtk object created.
.. 
..         :representation: the representation type used for the surface. Must be
..                          'surface' or 'wireframe' or 'points' or 'mesh' or
..                          'fancymesh'. Default: surface
..                          
..         :resolution: The resolution of the glyph created. For spheres, for
..                      instance, this is the number of divisions along theta and
..                      phi. Must be an integer. Default: 8
..                      
..         :scalars: optional scalar data.
..                   
..         :scale_factor: scale factor of the glyphs used to represent
..                        the vertices, in fancy_mesh mode. Must be a float.
..                        Default: 0.05
..                        
..         :scale_mode: the scaling mode for the glyphs
..                      ('vector', 'scalar', or 'none').
..                      
..         :transparent: make the opacity of the actor depend on the
..                       scalar.
..                       
..         :tube_radius: radius of the tubes used to represent the
..                       lines, in mesh mode. If None, simple lines are used.
..                       
..         :tube_sides: number of sides of the tubes used to
..                      represent the lines. Must be an integer. Default: 6
..                      
..         :vmax: vmax is used to scale the colormap
..                If None, the max of the data will be used
..                
..         :vmin: vmin is used to scale the colormap
..                If None, the min of the data will be used
    

例：

.. Example:

.. sourcecode:: ipython

    In [1]: import numpy as np

    In [2]: r, theta = np.mgrid[0:10, -np.pi:np.pi:10j]

    In [3]: x = r*np.cos(theta)

    In [4]: y = r*np.sin(theta)

    In [5]: z = np.sin(r)/r

    In [6]: from enthought.mayavi import mlab

    In [7]: mlab.mesh(x, y, z, colormap='gist_earth', extent=[0, 1, 0, 1, 0, 1])
    Out[7]: <enthought.mayavi.modules.surface.Surface object at 0xde6f08c>

    In [8]: mlab.mesh(x, y, z, extent=[0, 1, 0, 1, 0, 1], 
       ...: representation='wireframe', line_width=1, color=(0.5, 0.5, 0.5))
    Out[8]: <enthought.mayavi.modules.surface.Surface object at 0xdd6a71c>

.. image:: polar_mesh.png
    :align: center
    :scale: 70

装飾
----

.. Decorations
.. -----------------

.. only:: latex

    カラーバーやタイトルのような追加の情報をもたらすために, 異なる要素を追加することができます,

.. .. only:: latex
.. 
..     Different items can be added to the figure to carry extra
..     information, such as a colorbar or a title.

.. sourcecode:: ipython

    In [9]: mlab.colorbar(Out[7], orientation='vertical')
    Out[9]: <tvtk_classes.scalar_bar_actor.ScalarBarActor object at 0xd897f8c>

    In [10]: mlab.title('polar mesh')
    Out[10]: <enthought.mayavi.modules.text.Text object at 0xd8ed38c>

    In [11]: mlab.outline(Out[7])
    Out[11]: <enthought.mayavi.modules.outline.Outline object at 0xdd21b6c>

    In [12]: mlab.axes(Out[7])
    Out[12]: <enthought.mayavi.modules.axes.Axes object at 0xd2e4bcc>

.. image:: decorations.png
    :align: center
    :scale: 80

.. warning:: 

    **extent:** plotting オブジェクトに extent を指定した場合
    `mlab.outline' と `mlab.axes` はデフォルトでそれらを取得しません.

.. .. warning:: 
.. 
..     **extent:** If we specified extents for a plotting object,  
..     `mlab.outline' and `mlab.axes` don't get them by default.


