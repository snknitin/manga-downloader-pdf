# Download any Manga as PDF for Kindle

Improved version for python3 version of code forked from [here](https://github.com/filipefilardi/manga-downloader-pdf)

This code create pdf volumes for chapters that you find online. 

The crawler script will download all volumes available in Manga Fox from a choosen manga for ([example](http://fanfox.net/manga/liar_game_roots_of_a/)) and convert each volume in pdf.

I mostly made this repository for my personal use but if it helps anyone else with similar interests, then I'm happy to help. Feel free to drop in some suggestions for manga as well. Huge fan!

Don't forget to support the mangaka and Manga Fox in any way you can.

Feel free to contribute to the project in any way.

## Features ##

 * Download manga via direct Manga Fox url;
 * Automatically transform all jpgs downloaded in separated pdfs, divided by volumes;
 * Automatically create a 'tmp' folder for the manga images and 'download' folder for the pdf ;
 * Check volumes inside downloaded folder and skip volumes already downloaded, so if interrupted, you don't need to start from scratch.
 

## How to Run ##

You can run multiple instances of this code for different manga parallely and download them at the same time, by changing the mangalink for each instance

     python download_manga.py -pdf="<insert a location here>" -tmp="<insert another location here>" -mangalink="http://fanfox.net/manga/liar_game_roots_of_a/"


-pdf has the location of your manga in pdf format in the specific manga folder  
-tmp is the temporary folder where the images will be downloaded in a manga specific folder and then converted to pdf before being deleted 
-mangalink is the mangafox link to the manga  


