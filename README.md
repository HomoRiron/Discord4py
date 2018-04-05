# Discord4py

```python

client = DiscordApi(Email="hogehoge@example.com","password")
msg = client.SendMessage("channel id","Test")
#import time
#time.sleep(1)
client.DeleteMessage(msg["channel_id"],msg["id"])
print("success!")
```
