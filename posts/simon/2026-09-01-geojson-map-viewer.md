# GeoJSON Map Viewer

        **Date:** 2026-09-01 18:05 UTC
        **Link:** https://simonwillison.net/2026/Sep/1/geojson/
        **Tags:** geospatial, tools, geojson, chatgpt

        ---

        > *Feed summary: Tool: GeoJSON Map Viewer
        I was helping Natalie gather some maps of local political boundaries (for the Granada Community Services District and the Midcoast Community Council and found a need t*

1st September 2026

[Tool](/elsewhere/tool/)
[GeoJSON Map Viewer](https://tools.simonwillison.net/geojson)
— View and visualize GeoJSON data on an interactive OpenStreetMap with customizable styling options. Paste GeoJSON objects (Feature, FeatureCollection, or Geometry) into the editor, adjust fill color and opacity, and render the features directly on the map.

I was helping Natalie gather some maps of local political boundaries (for the [Granada Community Services District](https://granada.ca.gov) and the [Midcoast Community Council](https://midcoastcommunitycouncil.org) and found a need to display some GeoJSON files on a map and export that as a PNG. I asked GPT-5.6-Sol for suggestions of tools and it proactively built one. After [some iterations](https://tools.simonwillison.net/colophon#geojson.html) using Claude Code for web and Fable 5.1 we got to this finished tool.

As for the GeoJSON.. it turns out if you ask ChatGPT Work to provide boundaries for almost anything it will churn away extracting and combining files from different Government data sources and build exactly what you need.

I got [this polygon](https://gist.github.com/simonw/27d243c9d1cb5d9047fff7360dd49d3c) from:

> `I want a polygon that represents the exact boundary of the El Granada GCSD`

And [this one](https://gist.github.com/simonw/b51f9e0190a13932ac64a0cb407a709d) from:

> `Get me a GeoJSON file for the boundary (or boundaries if that makes sense) for the MCC - Midcoast Community Council - that operates near Half Moon Bay CA`

[Here's a link](https://tools.simonwillison.net/geojson#url=https%3A%2F%2Fgist.github.com%2Fsimonw%2Fb51f9e0190a13932ac64a0cb407a709d&color=%23028FC3&opacity=50&url=https%3A%2F%2Fgist.github.com%2Fsimonw%2F27d243c9d1cb5d9047fff7360dd49d3c&color=%23E4572E&opacity=50&preset=map&resolution=2&lat=37.52640&lng=-122.48297&zoom=13) that displays both of them at the same time on the new GeoJSON map viewing tool.

Posted [1st September 2026](/2026/Sep/1/) at 6:05 pm
