Image Processing Container for the HASTE Project.

Interestingness Model:

Interestingness is the max of the magnitude of the Kendall's Tau over the sum of intensities and correlation image features, over a window for each well. 

```
docker build --no-cache=true -t "benblamey/image_analysis_container2:latest" .
docker push benblamey/image_analysis_container2:latest
```

Contributors: Ben Blamey