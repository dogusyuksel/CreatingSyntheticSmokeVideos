# CreatingSyntheticSmokeVideo
For early fire detection, smoke must be detect first. This project create smoke videos to feed deep laerning dataset
With this project, we can create new videos from one smoke video by combining it with different bakround images.

Also with this project, there are several options like;
	- Resizing smoke part in 4 different ways
	- Selecting location to put smoke in static image in 4 different ways
	- Rotation smoke part in 5 different angle

So, with one smoke video and static image, 80 different smoke videos can be created.


To run the project, do the follows;

1. Put your backround images in the path "SmokeRelated/SmokeStaticImages"
2. Put your smoked video in the path "SmokeRelated/SmokeVideos"
	BE CAREFULL, SMOKE VIDEOS MUST HAVE GREEN STATIC BACKROUND, these kinds of videos can be found in youtube
3. Run the "mergingimages.py"
4. Observe output videos in the path "SmokeRelated/SmokeDataSet"