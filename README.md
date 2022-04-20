# HW5: r/Place Analysis

*Amy Liu (al996), Faris Aziz (fsa22), Julia Atkins (jea255), Sam Fuchs
(scf73)*

## Data Sources

Canvas images:
<https://www.kaggle.com/datasets/robikscube/reddit-rplace-2022-history>

Comment history:
<https://www.kaggle.com/datasets/pavellexyr/the-reddit-place-dataset>

Pixels from 2017 edition:
<https://www.kaggle.com/datasets/residentmario/reddit-rplace-history>

## What is r/Place?

For three days, all reddit users could change the color of one pixel every 5
minutes on a 2000x2000 pixel canvas. The communal character of the reddit
platform meant that thousands of users banded together to create large pieces of
art--and to destroy them.

## Repository set-up

The site itself is hosted in /www. Any site-related assets or scripts should
live under that directory.

## Pre-processing

The full canvas data totals 5 GB in size, in part because the images are
uncompressed in the 24-bit color space. Because there are only 32 colors
available for users to place, we should be able to downscale this to a 5-bit
color space, which will cut memory usage by a factor of 6 and make our data
easier to store and manipulate. Our first step should be to take this
compression step and store the images in a matrix format that contains 5-bit
values.

- [x] Pull image data into python (can use matplotlib or similar)
- [x] Identify unique colors in images
- [x] Create a dictionary to index these colors to 5-bit numbers
- [ ] Translate images into 5-bit color identifiers
- [ ] Store 5-bit matrices in a static file type
