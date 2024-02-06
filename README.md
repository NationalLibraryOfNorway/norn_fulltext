# Norn fulltext

Texts and metadata for three corpora from the NORN project:

1. 1800-1839
1. 1840-1869
1. konsensus korpus

The texts for the tree corpora are found in `texts/`. The metadata is found in `metadata/`. The metadata are in excel files. The most important columns are:

* `urn` - the URN for the text - this is the reference to a digital object in the National Library of Norway's collections (not all works have URNs, see notes below).
* `dhlabid` - the id used by the DH-lab at the National Library of Norway. This is used to identify the text here.

## Corpora

### 1800-1839

This is a collection of 101 works published between 1800-1839.

### 1840-1869

This is a collection of 101 works published between 1840-1869.

### konsensus korpus

This is a curated collection of works from the 1800s that have been considered as national romantic by various scholars. 

## Notes

* There is some overlap between the konsensus-korpus and the two others.
* Not all works represent books. Some are articles, poems, etc. Some are present in the same book, and thus share urn and dhlabid.
* Not all works have been digitized. These do not have URNs. The metadata for these works are still included in the metadata files.
* To look up a work in the National Library of Norway's collections, use the URN. For instance, the URN `URN:NBN:no-nb_digibok_2012072308001` can be looked up at https://urn.nb.no/URN:NBN:no-nb_digibok_2012072308001. The URN is also used to look up the work in the National Library of Norway's API. For instance, the API call for the work above is https://api.nb.no/catalog/v1/iiif/URN:NBN:no-nb_digibok_2012072308001/manifest.
