.. _summary_exercise_image_processing:

画像処理の応用：泡と非融解粒の数え上げ
--------------------------------------

.. Image processing application: counting bubbles and unmolten grains
.. ------------------------------------------------------------------

.. image:: ../image_processing/MV_HFV_012.jpg
   :align: center
   :scale: 70

.. only:: latex

問題文
......

.. Statement of the problem
.. ..........................

1. MV_HFV_012.jpg を開いて表示しましょう.
   ``imshow`` の docstring を眺めて右方向 ("right" orientation) に開きましょう

.. 1. Open the image file MV_HFV_012.jpg and display it. Browse through the
.. keyword arguments in the docstring of ``imshow`` to display the image
.. with the "right" orientation (origin in the bottom left corner, and not
.. the upper left corner as for standard arrays).

この Snaning Element Microscopy 画像は泡（黒）と非融解な砂粒（黒っぽいグレー）を含むガラス（白っぽいグレーの基質）のサンプルです.
これらの3つの相で覆われた比を決定し, 砂粒と泡のそれらの大きさや典型的なサイズ等を見積りたい.

.. This Scanning Element Microscopy image shows a glass sample (light gray
.. matrix) with some bubbles (on black) and unmolten sand grains (dark
.. gray). We wish to determine the fraction of the sample covered by these
.. three phases, and to estimate the typical size of sand grains and
.. bubbles, their sizes, etc.

2. 測定情報を表示している下のパネル部分を切り取りましょう.

.. 2. Crop the image to remove the lower panel with measure information.

3. 頻度分布をより明確にするために少しだけ中央値フィルターをかけましょう.
   頻度分布がどう変化したか調べましょう.

.. 3. Slightly filter the image with a median filter in order to refine its
.. histogram. Check how the histogram changes.

4. フィルタした画像の頻度分布を使って, 砂, ガラス, 泡のピクセルのマスクを定義するための閾値を決定しなさい.
   オプション（宿題）：頻度分布の最小値から閾値を自動的に決定する関数を書きなさい.

.. 4. Using the histogram of the filtered image, determine thresholds that
.. allow to define masks for sand pixels, glass pixels and bubble pixels.
.. Other option (homework): write a function that determines automatically
.. the thresholds from the minima of the histogram.

5. 3つの相を異なる色で表示しなさい.

.. 5. Display an image in which the three phases are colored with three
.. different colors.

6. 異なる相のごみをとるために数理形態学を使いなさい.

.. 6. Use mathematical morphology to clean the different phases.

7. 全ての泡と砂粒にラベルをつけ, そして10ピクセルより小さい砂粒のマスクを取り除きなさい.
   そうしたら, ``ndimage.sum`` か ``np.bincount`` を使って粒の大きさを計算しなさい.

.. 7. Attribute labels to all bubbles and sand grains, and remove from the
.. sand mask grains that are smaller than 10 pixels. To do so, use
.. ``ndimage.sum`` or ``np.bincount`` to compute the grain sizes.

8. 泡の平均的大きさを計算しなさい.

.. 8. Compute the mean size of bubbles.

.. only:: latex

   .. _image-answers:

解答の提案
..........

.. Proposed solution
.. ....................

