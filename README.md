# ninsheetmusic_scraper
Scrapes ninsheetmusic for midi files. Py3

The number of files to try is hardcoded at 4129 because that is what my testing found to probably be the highest. If it's been more than a few days since this was posted, please set it higher. If you find a maximum value that is higher than that, please consider submitting a PR with the change. It may be slightly restructured in the future to have the downloading in the same loop as the loop that generates the download links, which could be configured to stop after ~30 failed files.
