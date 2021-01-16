﻿# Python-Technical-Test

Technical_Test - Find average number of words by artist.

Author:  Pete Russell

Finds the average number of words in songs by an artist.
Optionally lists the song names and lengths.
The names of 2 artists can be passed for comparison.

Program requires the following installs:

pip install musicbrainxngs
pip install requests

Example Command: python Technical_Test_PDR.py "D" "Neil Young" "The Pixies"

The first parameter can be "D" or "S"
    D - Detailed report including retrieved song names and number of words
    S - Summary report with just average number number of words per song

Subsequent parameters have either one or two artists names.

  I
Ideas for Future Development
----------------------------

- Investigate reasons for some major acts (The Clash, The Undertones), return no songs.

- Indicate reason for no songs found, e.g Artist Not Found, No Recordings Found, No Lyrics Found.

- Investigate why the number of songs returned varies from run to run, for the same artist.
  Possible causes could be a limit on the number of items returned by the Api, combined with random
  selection.  Memory contraints could also be a cause.







