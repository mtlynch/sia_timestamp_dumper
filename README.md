# Sia Timestamp Dumper

## Overview

Dumps the timestamp (in both UNIX and ISO-8601 formats) for each Sia block height.

## Usage

The timestamp dumper requires access to a Sia node that is running the explorer
module. To enable the explorer, run siad with the following flags:

```bash
siad --modules cge
```

Then run Sia Timestamp Dumper as follows:

```bash
$ python dump.py
block_height    unix_timestamp  iso_timestamp
     0  1433600000      2015-06-06T14:13:20Z
     1  1433626546      2015-06-06T21:35:46Z
     2  1433627288      2015-06-06T21:48:08Z
     3  1433628922      2015-06-06T22:15:22Z
     4  1433628961      2015-06-06T22:16:01Z
     5  1433629456      2015-06-06T22:24:16Z
     6  1433629725      2015-06-06T22:28:45Z
     7  1433629837      2015-06-06T22:30:37Z
     8  1433630462      2015-06-06T22:41:02Z
     9  1433630614      2015-06-06T22:43:34Z
    10  1433630907      2015-06-06T22:48:27Z
...
```

To dump only for a certain range, use the `--start` and `--end` flags:

```bash
$ python dump.py --start 1000 --end 1010
block_height    unix_timestamp  iso_timestamp
  1000  1433716769      2015-06-07T22:39:29Z
  1001  1433716812      2015-06-07T22:40:12Z
  1002  1433716872      2015-06-07T22:41:12Z
  1003  1433716918      2015-06-07T22:41:58Z
  1004  1433716843      2015-06-07T22:40:43Z
  1005  1433717167      2015-06-07T22:46:07Z
  1006  1433717254      2015-06-07T22:47:34Z
  1007  1433717245      2015-06-07T22:47:25Z
  1008  1433717345      2015-06-07T22:49:05Z
  1009  1433717498      2015-06-07T22:51:38Z
  1010  1433717576      2015-06-07T22:52:56Z
```
