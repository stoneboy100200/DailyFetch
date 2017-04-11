# DailyFetch
## Summary
If you find git fetch will waste the most time when you come back from long vacation, due to the fact that many people have committed a lot of code while you are away. This script will help you avoid this problem. It is intended to fetch source code automatically everyday, no matter how long you're in vacation. But only if you can't shut down your system. Reboot is OK.

## Environment
Windows 7/Linux
Git

## How to start
### Linux user
- Edit 'DailyFetch.py', and set your repository path. For example:

`repository="ENTER_YOUR_PATH" => repository="/home/lse9szh/Project/test"`

- Set up your 'crontab' service
To use crontab for tasks meant to run only for your user profile, add entries to your own user's crontab file. To edit the crontab file enter: 

`crontab -e`

Edit the crontab using the correct format. More details about crontab please refer to the [Cron](https://en.wikipedia.org/wiki/Cron)<br />
EX:

`0 5 * * * python ~/project/DailyFetch.py > /dev/null`

This command says, '~/project/DailyFetch.py' will be started at 05:00 every day

### Windows user
- Edit 'DailyFetch.py', and set your repository path. For example:

`repository="ENTER_YOUR_PATH" => repository="D:/Project/test"`

- Open window command prompt and start 'schtasks'
More details about schtasks please refer to the [schtasks](https://technet.microsoft.com/en-us/library/cc725744%28v=ws.11%29.aspx)<br />
EX:

`schtasks /create /tn "DailyFetch" /tr "python D:\script\DailyFetch.py" /sc daily /st 05:00`

This command says, 'DailyFetch.py' will be started at 05:00 every day, the task name is 'DailyFetch'.
