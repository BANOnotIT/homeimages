Homeimages py3.5
==========

Get all photos and videos sync-ed. Two scripts to sync photos and videos from external SDs.

1. Sync photos:

   ..

     $ python copyimages.py

   This will walk through all existing jpg-files on SD, and copy to destination folder ( skip existing if found )

2. Sync videos:

   ..

     $ python copyvideos.py

   Same as photos for mov-files, with convertion to AVI format (requires ffmpeg installed)
