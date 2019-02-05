# 6-Month-Report
Gets top contributors within 6 months of a repo

Some example usage when dropped into the [Homebrew repo](https://github.com/Homebrew/brew)
```bash
$ ./brew-stats.py 2017
First 6 months report for 2017

Name                    | Files Changed | Insertions    | Deletions     | Commits

Markus Reiter           | 1645          | 20563         | 19671         | 427
Mike McQuaid            | 813           | 7100          | 5694          | 288
Gautham Goli            | 119           | 3006          | 1158          | 29
William Woodruff                | 21            | 2206          | 2082          | 8
EricFromCanada          | 126           | 1172          | 1036          | 13
Alyssa Ross             | 184           | 701           | 834           | 39
Bob W. Hogg             | 24            | 382           | 69            | 10
ilovezfs                | 61            | 375           | 206           | 26
Misty De Meo            | 31            | 315           | 24            | 23
Joshua McKinney         | 23            | 304           | 129           | 8
```

```bash
$ ./brew-stats.py 2016
First 6 months report for 2016

Name                    | Files Changed | Insertions    | Deletions     | Commits

Mike McQuaid            | 304           | 4429          | 2519          | 144
Baptiste Fontaine               | 89            | 3352          | 1704          | 60
William Woodruff                | 43            | 3155          | 206           | 10
Xu Cheng                | 322           | 2078          | 2483          | 184
Martin Afanasjew                | 253           | 2028          | 2140          | 159
Andrew Janke            | 84            | 1425          | 460           | 35
Max Nordlund            | 61            | 862           | 70            | 5
ilovezfs                | 49            | 637           | 104           | 31
Dominyk Tiller          | 105           | 486           | 194           | 94
Andrea Kao              | 5             | 203           | 275           | 5
```