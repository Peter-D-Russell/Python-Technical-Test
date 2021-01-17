# Python-Technical-Test

Technical_Test - Find average number of words by artist.

Author:  Pete Russell

Python CLI program to find the average number of words in songs by an artist.
Optionally lists the song names and lengths.
The names of 2 artists can be passed for comparison.

Program requires the following installs:

pip install musicbrainxngs

pip install requests

Example Command: python Technical_Test_PDR.py "D" "Neil Young" "The Pixies"

The first parameter can be "D" or "S"

    D - Detailed report including retrieved song names and number of words
    
    S - Summary report with just average number of words per song

Subsequent parameters supply either one or two artists names.

 
Ideas for Testing/Future Development
----------------------------

- Investigate reasons why some major acts (The Clash, The Undertones, R.E.M), return no songs.

- Return reason for no songs found, e.g Artist Not Found, No Recordings Found, No Lyrics Found.

- Investigate why the number of songs returned varies from run to run, for the same artist.
  Possible causes could be a limit on the number of items returned by the Api, combined with random
  selection.  Memory contraints could also be a cause.
  
- Try alternative ways of using the Apis in obtaining the lists of songs.

- Check that using the ext:score field to find the required artist id is appropriate.

- Investigate Apis on different websites.







