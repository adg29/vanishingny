# About Vanishing NY


Data collected to help visualize and commemorate the history and impact of buildings, businesses, and venues that have vanished in NY.

## Data

[vanishingny.csv](../blob/master/vanishingny.csv) is the master list of all collected records. You will also find `txt` and `csv` files that contain identical data separated by year. These files contain the most recent data that has been cobtributed to the project. 

[txt2csv.py](../blob/master/txt2csv.py) converts `txt` formatted data into many individual `csv` files and one master `vanishingny.csv` file according to some fairly specific parsing logic. Run this command if you add new data to the txt files. 

### Adding and converting `txt` data

The format of data expected in the `txt` files allows `txt2csv.py` to parse the text files to CSV correctly. Please refer to the template below.


```
[NAME] : [YEARS_OF_BUSINESS]
[COMMENTARY_AND_DESCRIPTION] ; [LOCATION]
```

To insert a new reord into the `txt` files, just replace the braces with your data. For example:

```
’Inoteca: 11 years
Serving small plates and Montepulciano to guests on the daily since 2003. Denton announced the closure in a statement that indicates he and his partner are relinquishing the lease;98 Rivington
```

Finally, run the `txt2csv.py` script on the data.


#### Formatting Gotchas
* Remove double quotes and use single quotes instead 


### Contributing

Or add the data directly to the `csv` files. 

Create a pull request and your contribution will be appreciated.

## Sources 
This project extends **The Master List 2001-2013 by JEREMIAH MOSS**. The original data was sourced by hand from that blog post you can see here http://sadto.me/1aL4gX0. 


## Where there's data, there's anti-data

As the renowned @blprnt posits [Where there's data, there's anti-data](https://twitter.com/blprnt/status/430686284563349505). That is to say, the data you find here is likely quite refutable. Please feel free to open an issue and discuss.

