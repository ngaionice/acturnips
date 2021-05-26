import praw
import re
import env
import time
import webbrowser
from plyer import notification
from src.win10toast.win10toast import ToastNotifier

reddit = praw.Reddit(
    client_id=env.CLIENT_ID,
    client_secret=env.SECRET,
    user_agent=env.USER_AGENT,
)

toaster = ToastNotifier()

subreddit = reddit.subreddit("acturnips")
sent = []
frequency_seconds = 60
target_price = 300


def scan() -> None:
    for submission in subreddit.new(limit=10):
        if match(submission.title) > target_price and submission.url not in sent:
            sent.append(submission.url)
            notify()


def match(title: str) -> int:
    if title is not None:
        if re.search("[0-9][0-9][0-9]", title) is not None:
            return int(re.search("[0-9][0-9][0-9]", title).group())
        elif re.search("[0-9]-[0-9]-[0-9]", title) is not None:
            return int(re.search("[0-9]-[0-9]-[0-9]", title).group().replace("-", ""))
        return 0
    return 0


def notify() -> None:
    toaster.show_toast(
        title="Buyer at " + str(target_price) + "+ found",
        msg="",
        icon_path=None,
        duration=5,
        threaded=True,
        callback_on_click=webbrowser.open_new(sent[-1]))
    notification.notify(
        title="Buyer at " + str(target_price) + "+ found",
        message="Thread opened in browser."
    )


def main() -> None:
    while True:
        start_time = time.time()
        scan()
        time.sleep(frequency_seconds - ((time.time() - start_time) % 60.0))


if __name__ == '__main__':
    main()
