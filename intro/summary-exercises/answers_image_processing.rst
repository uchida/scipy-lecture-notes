
.. only:: html

.. _image-answers:

画像処理練習問題解答例：ガラスの中の非融解粒
============================================

.. Example of solution for the image processing exercise: unmolten grains in glass
.. ===============================================================================


  .. image:: ../image_processing/MV_HFV_012.jpg
     :align: center
     :scale: 70

1. MV_HFV_012.jpg を開いて表示しましょう.
   ``imshow`` のドキュメンテーション文字列を眺めて右方向 ("right" orientation) に開きましょう::

    >>> dat = imread('MV_HFV_012.jpg')

.. 1. Open the image file MV_HFV_012.jpg and display it. Browse through the
..    keyword arguments in the docstring of ``imshow`` to display the image
..    with the "right" orientation (origin in the bottom left corner, and not
..    the upper left corner as for standard arrays). ::

..     >>> dat = imread('MV_HFV_012.jpg')

2. 測定情報を表示している下のパネル部分を切り取りましょう. ::

    >>> dat = dat[60:]

.. 2. Crop the image to remove the lower panel with measure information. ::

..     >>> dat = dat[60:]

3. 頻度分布を明確にするために少しだけ中央値フィルターをかけましょう.
   頻度分布がどう変化したか調べましょう. ::


    >>> filtdat = ndimage.median_filter(dat, size=(7,7))
    >>> hi_dat = np.histogram(dat, bins=np.arange(256))
    >>> hi_filtdat = np.histogram(filtdat, bins=np.arange(256))

.. 3. Slightly filter the image with a median filter in order to refine its
..    histogram. Check how the histogram changes. ::

..     >>> filtdat = ndimage.median_filter(dat, size=(7,7))
..     >>> hi_dat = np.histogram(dat, bins=np.arange(256))
..     >>> hi_filtdat = np.histogram(filtdat, bins=np.arange(256))

.. image:: ../image_processing/exo_histos.png
   :align: center

4. フィルタした画像の頻度分布を使って, 砂, ガラス, 泡のピクセルのマスクを定義するための閾値を決定しなさい.
   オプション（宿題）：頻度分布の最小値から閾値を自動的に決定する関数を書きなさい. ::

    >>> void = filtdat <= 50
    >>> sand = np.logical_and(filtdat>50, filtdat<=114)
    >>> glass = filtdat > 114

.. 4. Using the histogram of the filtered image, determine thresholds that
..    allow to define masks for sand pixels, glass pixels and bubble pixels.
..    Other option (homework): write a function that determines automatically
..    the thresholds from the minima of the histogram. ::

..     >>> void = filtdat <= 50
..     >>> sand = np.logical_and(filtdat>50, filtdat<=114)
..     >>> glass = filtdat > 114

5. 3つの相を異なる色で表示しなさい. ::

    >>> phases = void.astype(np.int) + 2*glass.astype(np.int) +\
            3*sand.astype(np.int)

.. 5. Display an image in which the three phases are colored with three
..    different colors. ::

..     >>> phases = void.astype(np.int) + 2*glass.astype(np.int) +\
..             3*sand.astype(np.int)

.. image:: ../image_processing/three_phases.png
   :align: center

6. 異なる相のごみをとるために数理形態学を使いなさい. ::

    >>> sand_op = ndimage.binary_opening(sand, iterations=2)

.. 6. Use mathematical morphology to clean the different phases. ::

..     >>> sand_op = ndimage.binary_opening(sand, iterations=2)

7. 全ての泡と砂粒にラベルをつけ, そして10ピクセルより小さい砂粒のマスクを取り除きなさい.
   そうしたら, ``ndimage.sum`` か ``np.bincount`` を使って粒の大きさを計算しなさい. ::

    >>> sand_labels, sand_nb = ndimage.label(sand_op)
    >>> sand_areas = np.array(ndimage.sum(sand_op, sand_labels,\
    ...     np.arange(sand_labels.max()+1)))
    >>> mask = sand_areas>100
    >>> remove_small_sand = mask[sand_labels.ravel()].reshape(sand_labels.shape)

.. 7. Attribute labels to all bubbles and sand grains, and remove from the
..    sand mask grains that are smaller than 10 pixels. To do so, use
..    ``ndimage.sum`` or ``np.bincount`` to compute the grain sizes. ::

..     >>> sand_labels, sand_nb = ndimage.label(sand_op)
..     >>> sand_areas = np.array(ndimage.sum(sand_op, sand_labels,\
..     ...     np.arange(sand_labels.max()+1)))
..     >>> mask = sand_areas>100
..     >>> remove_small_sand = mask[sand_labels.ravel()].reshape(sand_labels.shape)

.. image:: ../image_processing/sands.png
   :align: center

8. 泡の平均的大きさを計算しなさい. ::

    >>> bubbles_labels, bubbles_nb = ndimage.label(void)
    >>> bubbles_areas = np.bincount(bubbles_labels.ravel())[1:]
    >>> mean_bubble_size = bubbles_areas.mean()
    >>> median_bubble_size = np.median(bubbles_areas)
    >>> mean_bubble_size, median_bubble_size
    (1699.875, 65.0)

.. 8. Compute the mean size of bubbles. ::

..     >>> bubbles_labels, bubbles_nb = ndimage.label(void)
..     >>> bubbles_areas = np.bincount(bubbles_labels.ravel())[1:]
..     >>> mean_bubble_size = bubbles_areas.mean()
..     >>> median_bubble_size = np.median(bubbles_areas)
..     >>> mean_bubble_size, median_bubble_size
..     (1699.875, 65.0)
