
## Linux Commands


### Disk usage

List of frequently used bash commands

Check file size
`ls -lh`

Check Disk Usage of each folder:
`du -sh *`

Check Disk Usage of a folder:
`du -h /folder location`

Check aggreaged disk usage of a folder:
`du -sh /folder/location`

To check disk usage of subfile and folders:
`du -ah /folder/location`

Check hidden directories size as well and sort them:
`du -sch .[!.]* * | sort -h`

Filter files & Folders with regex:
`ls | grep -E "2000|27250|*.tar.gz|*.json"`

Inverse filter files & Folders with regex:
`ls | grep -vE "2000|27250|*.tar.gz|*.json"`

Delete selected files ( Starting with 2000 and general regex example ):
`ls | grep -vE "^2000|27250|*.tar.gz|*.json" | xargs rm -rf`

### nohup

Run nohup command:\
`nohup <command>`  
`nohup python run.py`

Run nohup in backgroud:\
`nohup python run.py &`

Redirect standard output and standard error:\
`nohup mycommand > mycommand.out 2>&1 &`


Temp