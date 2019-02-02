# curly-journey
Find album covers on Safari from iTunes "missing artworks" list (macOS only)

## Context
If you don't use Apple Music or Spotify, you know that the album cover is not added to your iTunes library automatically when you import a CD.
iTunes can find them on the iTunes Store but the feature is not perfect. Many albums can be left without an image for many reasons.

But it is possible to add our own album cover with the following steps:
1. Right click on an album
2. Click on "Album Info"
3. Select the image in the top-left corner
4. Paste the image of our choice

## What the script does
The purpose of the script is to accelerate the search of all the missing album covers on Google Images. iTunes can generate a list of all the albums it could not find an artwork related to, so we just need to do some parsing on the file, encode each line in an URL format and tell Safari to find those albums on Google Images.

## How to use it
1. Open iTunes
2. Click top menu File/Library/Get Album Artwork
3. Sign in with your Apple ID if asked
4. iTunes will popup a window showing all the albums it does not know
5. Save the list as 'iTunes.txt' next to the Python script
6. Run 'python3 find_album_artwork.py'

## Tests
This script has been tested with a list containing about 70 items and Safari was able to open 70 tabs side-by-side without any problem on an 2011 MacBook Pro running macOS High Sierra.

## Want to contribute?
Next steps could be:
* Search for large images only (it looks better)
* Import the right artwork (image saved in a temporary folder) into the right album on iTunes automatically
* Adapt the script so it uses the user's by default web browser instead of Safari
