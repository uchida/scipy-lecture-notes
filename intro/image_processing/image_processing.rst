scipy の画像処理向けのサブモジュールは `scipy.ndimage` です. ::

    >>> from scipy import ndimage

画像処理ルーチンは実行する処理に応じて分類されています.

.. The submodule dedicated to image processing in scipy is `scipy.ndimage`. ::

..     >>> from scipy import ndimage

.. Image processing routines may be sorted according to the category of
.. processing they perform.


画像の幾何学的変換
..................

.. Geometrical transformations on images
.. .......................................

方向, 解像度を変える, .. ::

    >>> import scipy
    >>> lena = scipy.lena()
    >>> shifted_lena = ndimage.shift(lena, (50, 50))
    >>> shifted_lena2 = ndimage.shift(lena, (50, 50), mode='nearest')
    >>> rotated_lena = ndimage.rotate(lena, 30)
    >>> cropped_lena = lena[50:-50, 50:-50]
    >>> zoomed_lena = ndimage.zoom(lena, 2)
    >>> zoomed_lena.shape
    (1024, 1024)

.. Changing orientation, resolution, .. ::

..     >>> import scipy
..     >>> lena = scipy.lena()
..     >>> shifted_lena = ndimage.shift(lena, (50, 50))
..     >>> shifted_lena2 = ndimage.shift(lena, (50, 50), mode='nearest')
..     >>> rotated_lena = ndimage.rotate(lena, 30)
..     >>> cropped_lena = lena[50:-50, 50:-50]
..     >>> zoomed_lena = ndimage.zoom(lena, 2)
..     >>> zoomed_lena.shape
..     (1024, 1024)

.. image:: image_processing/lena_transforms.png
   :align: center


.. sourcecode:: ipython

    In [35]: subplot(151)
    Out[35]: <matplotlib.axes.AxesSubplot object at 0x925f46c>

    In [36]: imshow(shifted_lena, cmap=cm.gray)
    Out[36]: <matplotlib.image.AxesImage object at 0x9593f6c>

    In [37]: axis('off')
    Out[37]: (-0.5, 511.5, 511.5, -0.5)

    In [39]: # etc.


画像フィルタ
............

.. Image filtering
.. ...................

::

    >>> lena = scipy.lena()
    >>> import numpy as np
    >>> noisy_lena = np.copy(lena)
    >>> noisy_lena += lena.std()*0.5*np.random.standard_normal(lena.shape)
    >>> blurred_lena = ndimage.gaussian_filter(noisy_lena, sigma=3)
    >>> median_lena = ndimage.median_filter(blurred_lena, size=5)
    >>> import scipy.signal
    >>> wiener_lena = scipy.signal.wiener(blurred_lena, (5,5))

.. image:: image_processing/filtered_lena.png
   :align: center


他にも画像に適応できるフィルタが ``scipy.ndimage.filters`` と ``scipy.signal`` にあります.

.. And many other filters in ``scipy.ndimage.filters`` and ``scipy.signal``
.. can be applied to images

.. topic:: 練習問題

    異なるフィルタを書けた画像の頻度分布を比較しなさい.

.. .. topic:: Exercise

..     Compare histograms for the different filtered images.

数理形態学
..........

.. Mathematical morphology
.. ........................

数理形態学 (Mathematical morphology) は集合論から派生した数学理論です.
幾何構造の特徴付けと変換を行います.
特に2進画像（白と黒のみのモノクロ）はこの理論によって変換できます：非ゼロのピクセルを近傍に含む集合が変換されます.
理論はグレースケール画像に対しても拡張されます.

.. Mathematical morphology is a mathematical theory that stems from set
.. theory. It characterizes and transforms geometrical structures. Binary
.. (black and white) images, in particular, can be transformed using this
.. theory: the sets to be transformed are the sets of neighboring
.. non-zero-valued pixels. The theory was also extended to gray-valued images.

.. image:: image_processing/morpho_mat.png
   :align: center

幾何構造を変更するための数理形態学の基本演算は *構造要素 (structuring element)* を使います.

.. Elementary mathematical-morphology operations use a *structuring element*
.. in order to modify other geometrical structures.

まず構造要素を作ってみましょう ::

    >>> el = ndimage.generate_binary_structure(2, 1)
    >>> el
    array([[False,  True, False],
	   [ True,  True,  True],
	   [False,  True, False]], dtype=bool)
    >>> el.astype(np.int)
    array([[0, 1, 0],
	   [1, 1, 1],
           [0, 1, 0]])

.. Let us first generate a structuring element ::

..     >>> el = ndimage.generate_binary_structure(2, 1)
..     >>> el
..     array([[False,  True, False],
.. 	   [ True,  True,  True],
.. 	   [False,  True, False]], dtype=bool)
..     >>> el.astype(np.int)
..     array([[0, 1, 0],
.. 	   [1, 1, 1],
..            [0, 1, 0]])

* **Erosion** ::

    >>> a = np.zeros((7,7), dtype=np.int)
    >>> a[1:6, 2:5] = 1
    >>> a
    array([[0, 0, 0, 0, 0, 0, 0],
           [0, 0, 1, 1, 1, 0, 0],
           [0, 0, 1, 1, 1, 0, 0],
           [0, 0, 1, 1, 1, 0, 0],
           [0, 0, 1, 1, 1, 0, 0],
           [0, 0, 1, 1, 1, 0, 0],
           [0, 0, 0, 0, 0, 0, 0]])
    >>> ndimage.binary_erosion(a).astype(a.dtype)
    array([[0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 1, 0, 0, 0],
           [0, 0, 0, 1, 0, 0, 0],
           [0, 0, 0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0]])
    >>> #Erosion removes objects smaller than the structure
    >>> ndimage.binary_erosion(a, structure=np.ones((5,5))).astype(a.dtype)
    array([[0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0]])

* **Dilation** ::

    >>> a = np.zeros((5, 5))
    >>> a[2, 2] = 1
    >>> a
    array([[ 0.,  0.,  0.,  0.,  0.],
           [ 0.,  0.,  0.,  0.,  0.],
           [ 0.,  0.,  1.,  0.,  0.],
           [ 0.,  0.,  0.,  0.,  0.],
           [ 0.,  0.,  0.,  0.,  0.]])
    >>> ndimage.binary_dilation(a).astype(a.dtype)
    array([[ 0.,  0.,  0.,  0.,  0.],
           [ 0.,  0.,  1.,  0.,  0.],
           [ 0.,  1.,  1.,  1.,  0.],
           [ 0.,  0.,  1.,  0.,  0.],
           [ 0.,  0.,  0.,  0.,  0.]])

* **Opening** ::

    >>> a = np.zeros((5,5), dtype=np.int)
    >>> a[1:4, 1:4] = 1; a[4, 4] = 1
    >>> a
    array([[0, 0, 0, 0, 0],
           [0, 1, 1, 1, 0],
           [0, 1, 1, 1, 0],
           [0, 1, 1, 1, 0],
           [0, 0, 0, 0, 1]])
    >>> # Opening removes small objects
    >>> ndimage.binary_opening(a, structure=np.ones((3,3))).astype(np.int)
    array([[0, 0, 0, 0, 0],
           [0, 1, 1, 1, 0],
           [0, 1, 1, 1, 0],
           [0, 1, 1, 1, 0],
           [0, 0, 0, 0, 0]])
    >>> # Opening can also smooth corners
    >>> ndimage.binary_opening(a).astype(np.int)
    array([[0, 0, 0, 0, 0],
           [0, 0, 1, 0, 0],
           [0, 1, 1, 1, 0],
           [0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0]])

* **Closing:** ``ndimage.binary_closing``

.. topic:: 練習問題

    opening が eroding 後に dilating することを確かめなさい.

.. .. topic:: Exercise

..     Check that opening amounts to eroding, then dilating.

opening 操作は小さい構造を取り除き, closing 操作は小さな穴を埋めます.
これらの操作は画像の「ごみとり」に使えます. ::

    >>> a = np.zeros((50, 50))
    >>> a[10:-10, 10:-10] = 1
    >>> a += 0.25*np.random.standard_normal(a.shape)
    >>> mask = a>=0.5
    >>> opened_mask = ndimage.binary_opening(mask)
    >>> closed_mask = ndimage.binary_closing(opened_mask)

.. An opening operation removes small structures, while a closing operation
.. fills small holes. Such operation can therefore be used to "clean" an
.. image. ::

..     >>> a = np.zeros((50, 50))
..     >>> a[10:-10, 10:-10] = 1
..     >>> a += 0.25*np.random.standard_normal(a.shape)
..     >>> mask = a>=0.5
..     >>> opened_mask = ndimage.binary_opening(mask)
..     >>> closed_mask = ndimage.binary_closing(opened_mask)

.. image:: image_processing/morpho.png
   :align: center

.. topic:: 練習問題

    再構成された正方形が元の領域より小さいことを確かめなさい
    （opening の *前* に closing を行うと逆のことが起こるはずです）.

.. .. topic:: Exercise

..     Check that the area of the reconstructed square is smaller
..     than the area of the initial square. (The opposite would occur if the
..     closing step was performed *before* the opening).

**gray-valued** 画像については, eroding は注目するピクセルを中心とする構造要素内のピクセルの最小値に置き換えます
（dilation は最大値に置き換えます）::

    >>> a = np.zeros((7,7), dtype=np.int)
    >>> a[1:6, 1:6] = 3
    >>> a[4,4] = 2; a[2,3] = 1
    >>> a
    array([[0, 0, 0, 0, 0, 0, 0],
           [0, 3, 3, 3, 3, 3, 0],
           [0, 3, 3, 1, 3, 3, 0],
           [0, 3, 3, 3, 3, 3, 0],
           [0, 3, 3, 3, 2, 3, 0],
           [0, 3, 3, 3, 3, 3, 0],
           [0, 0, 0, 0, 0, 0, 0]])
    >>> ndimage.grey_erosion(a, size=(3,3))
    array([[0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 1, 1, 1, 0, 0],
           [0, 0, 1, 1, 1, 0, 0],
           [0, 0, 3, 2, 2, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0]])

.. For **gray-valued** images, eroding (resp. dilating) amounts to replacing
.. a pixel by the minimal (resp. maximal) value among pixels covered by the
.. structuring element centered on the pixel of interest. ::

..     >>> a = np.zeros((7,7), dtype=np.int)
..     >>> a[1:6, 1:6] = 3
..     >>> a[4,4] = 2; a[2,3] = 1
..     >>> a
..     array([[0, 0, 0, 0, 0, 0, 0],
..            [0, 3, 3, 3, 3, 3, 0],
..            [0, 3, 3, 1, 3, 3, 0],
..            [0, 3, 3, 3, 3, 3, 0],
..            [0, 3, 3, 3, 2, 3, 0],
..            [0, 3, 3, 3, 3, 3, 0],
..            [0, 0, 0, 0, 0, 0, 0]])
..     >>> ndimage.grey_erosion(a, size=(3,3))
..     array([[0, 0, 0, 0, 0, 0, 0],
..            [0, 0, 0, 0, 0, 0, 0],
..            [0, 0, 1, 1, 1, 0, 0],
..            [0, 0, 1, 1, 1, 0, 0],
..            [0, 0, 3, 2, 2, 0, 0],
..            [0, 0, 0, 0, 0, 0, 0],
..            [0, 0, 0, 0, 0, 0, 0]])

画像の測定
..........

.. Measurements on images
.. ........................

まず, nice synthetic 2進画像を作りましょう. ::

    >>> x, y = np.indices((100, 100))
    >>> sig = np.sin(2*np.pi*x/50.)*np.sin(2*np.pi*y/50.)*(1+x*y/50.**2)**2
    >>> mask = sig > 1

.. Let us first generate a nice synthetic binary image. ::

..     >>> x, y = np.indices((100, 100))
..     >>> sig = np.sin(2*np.pi*x/50.)*np.sin(2*np.pi*y/50.)*(1+x*y/50.**2)**2
..     >>> mask = sig > 1

画像内のオブジェクトの色々な情報を見ることができます::

    >>> labels, nb = ndimage.label(mask)
    >>> nb
    8
    >>> areas = ndimage.sum(mask, labels, xrange(1, labels.max()+1))
    >>> areas
    [190.0, 45.0, 424.0, 278.0, 459.0, 190.0, 549.0, 424.0]
    >>> maxima = ndimage.maximum(sig, labels, xrange(1, labels.max()+1))
    >>> maxima
    [1.8023823799830032, 1.1352760475048373, 5.5195407887291426,
    2.4961181804217221, 6.7167361922608864, 1.8023823799830032,
    16.765472169131161, 5.5195407887291426]
    >>> ndimage.find_objects(labels==4)
    [(slice(30, 48, None), slice(30, 48, None))]
    >>> sl = ndimage.find_objects(labels==4)
    >>> imshow(sig[sl[0]])

.. Now we look for various information about the objects in the image::

..     >>> labels, nb = ndimage.label(mask)
..     >>> nb
..     8
..     >>> areas = ndimage.sum(mask, labels, xrange(1, labels.max()+1))
..     >>> areas
..     [190.0, 45.0, 424.0, 278.0, 459.0, 190.0, 549.0, 424.0]
..     >>> maxima = ndimage.maximum(sig, labels, xrange(1, labels.max()+1))
..     >>> maxima
..     [1.8023823799830032, 1.1352760475048373, 5.5195407887291426,
..     2.4961181804217221, 6.7167361922608864, 1.8023823799830032,
..     16.765472169131161, 5.5195407887291426]
..     >>> ndimage.find_objects(labels==4)
..     [(slice(30, 48, None), slice(30, 48, None))]
..     >>> sl = ndimage.find_objects(labels==4)
..     >>> imshow(sig[sl[0]])


.. image:: image_processing/measures.png
   :align: center

より高度な例は統括演習 :ref:`summary_exercise_image_processing` を見てください.

.. See the summary exercise on :ref:`summary_exercise_image_processing` for a more
.. advanced example.


