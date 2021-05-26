A simple Python script for monitoring the subreddit r/acturnips for hosts with target selling prices.

## Requirements
- A Reddit API client ID and its associated secret.

## Set-up
Create a file called `env.py`, with the following variables:
- `CLIENT_ID`: the reddit API client ID
- `SECRET`: the secret associated with the client ID above
- `USER_AGENT`: the desired user agent name. Often in the format of `<platform>:<app ID>:<version string> (by /u/<reddit username>)`

Install `win10toast` using the command below. This is required to use the `callback_on_click` parameter in `notify`.
```
pip install -e git+https://github.com/Charnelx/Windows-10-Toast-Notifications.git#egg=win10toast
```

Change the `target_price` and `frequency_seconds` in `script.py` as desired. 
- `target_price` is self-explanatory
- `frequency_seconds` is the time interval between scans, in seconds.

And you're ready to go!
