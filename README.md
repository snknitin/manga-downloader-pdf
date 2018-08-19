# Download manga and convert to pdf for Kindle

Improved version for python3 of code forked from [here](https://github.com/filipefilardi/manga-downloader-pdf)

This code create pdf volumes for chapters that you find online. 

The crawler script will download all volumes available in Manga Fox from a choosen manga for ([example](http://fanfox.net/manga/liar_game_roots_of_a/)) and convert each volume in pdf.

I mostly made this repository for my personal use but if it helps anyone else with similar interests, then I'm happy to help. Feel free to drop in some suggestions for manga as well. Huge fan!

Don't forget to support the mangaka and Manga Fox in any way you can.

Feel free to contribute with the project in any way.

## Features ##

 * Simple text UI;
 * Download manga via direct Manga Fox url;
 * Automatically transform all jpgs downloaded in separated pdfs, divided by volumes;
 * Automatically create a 'tmp' folder for the manga images and 'download' folder for the pdf ;
 * Check volumes inside downloaded folder and skip volumes already downloaded.
 

## How to Run ##

     python download_manga.py -pdf="<insert a location>" -tmp="<insert a location>" -mangalink="http://fanfox.net/manga/liar_game_roots_of_a/"


