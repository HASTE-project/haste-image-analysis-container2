from setuptools import setup

setup(name='haste-image-analysis-container2',
      version='0.10',
      packages=[
          'haste.image_analysis_container2',
          'haste.image_analysis_container2.filenames',
      ],
      namespace_packages=['haste'],
      install_requires=[

          # scipy depends on dask.
          # dask depends on numpy
          # dask re-defines some functions in numpy for backwards compat to pre v1.15 of numpy
          # see:
          # https://github.com/dask/dask/blob/master/dask/array/numpy_compat.py#L210
          # .
          # But, the travis environment has numpy-1.15.0.xxx installed by default.
          # This results in some, there is some version incompatibility between scipy, dask and numpy giving this error:
          # ...
          #       ../../../virtualenv/python3.7-dev/lib/python3.7/site-packages/dask/array/chunk.py:19: in <module>
          #  take_along_axis = npcompat.take_along_axis
          # E   AttributeError: module 'dask.array.numpy_compat' has no attribute 'take_along_axis'
          # .
          # So, we require a newer numpy which has these new functions, to avoid relying on the compat in dask:
          'numpy>=1.15.1',
          'scipy',

          'Pillow',
          'scikit-image',
          'haste-storage-client'
      ],
      test_requires=[
          'pytest',

      ]
      )
