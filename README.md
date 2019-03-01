Image Processing Container for the HASTE Project.


[![Build Status](https://travis-ci.org/HASTE-project/haste-image-analysis-container2.svg?branch=master)](https://travis-ci.org/HASTE-project/haste-image-analysis-container2)



Interestingness Model:

Interestingness is the max of the magnitude of the Kendall's Tau over the sum of intensities and correlation image features, over a window for each well. 

```
docker build --no-cache=true -t "benblamey/image_analysis_container2:latest" .
docker push benblamey/image_analysis_container2:latest
```

Build + Run:
```
docker build --no-cache=true -t "benblamey/image_analysis_container2:latest" . ; docker run benblamey/image_analysis_container2
```

Contributors: Ben Blamey



To run a test:
```
mkdir /mnt/mikro-testdata/source/
cp -v /mnt/mikro-testdata/PolinaG-KO/181214-KOday7-40X-H2O2-Glu/2018-12-14/9/* /mnt/mikro-testdata/source/ 
```