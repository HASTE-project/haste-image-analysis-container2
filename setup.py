from setuptools import setup

setup(name='haste-image-analysis-container2',
      version='0.10',
      packages=['haste.image_analysis_container2'],
      namespace_packages=['haste'],
      install_requires=[
          'Pillow',
          'scikit-image',
          'scipy',
          'haste-storage-client'
      ],
      test_requires=[
          'pytest'
      ]
      )
