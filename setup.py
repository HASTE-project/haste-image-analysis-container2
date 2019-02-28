
from setuptools import setup

setup(name='haste-image-processor-2',
      version='0.10',
      packages=['haste.image_processor_2'],
      namespace_packages=['haste'],
      install_requires=[
          'numpy',
          'Pillow',
          'scikit-image',
          'scipy',
          'haste-storage-client'

      ],
      test_requires=[
          'pytest'
      ]
      )
