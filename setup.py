from setuptools import setup

setup(name='haste-image-analysis-container2',
      version='0.10',
      packages=['haste.image_analysis_container2'],
      namespace_packages=['haste'],
      install_requires=[

          # scipy depends on dask.
          # dask depends on numpy
          # dask re-defines some functions in numpy for backwards compat to pre v1.15 of numpy
          # see:
          # https://github.com/dask/dask/blob/master/dask/array/numpy_compat.py#L210
          # But, there is something broken about this mechanism, giving this error:
          # ...
          #       ../../../virtualenv/python3.7-dev/lib/python3.7/site-packages/dask/array/chunk.py:19: in <module>
          #  take_along_axis = npcompat.take_along_axis
          # E   AttributeError: module 'dask.array.numpy_compat' has no attribute 'take_along_axis'
          'numpy>=1.15.1',
          'scipy',

          'Pillow',
          'scikit-image',
          'haste-storage-client'
      ],
      test_requires=[
          'pytest'
      ]
      )
