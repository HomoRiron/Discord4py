import requests



class DiscordApi:
    def __init__(self,Email=None,Password=None,Token=None):
        self.base = "https://discordapp.com/api/v6"
        if(Token):
            self.Token = Token
        else:
            login = "{self.base}/auth/login"
            json = {
                "email":Email,
                "password":Password
                }
            response = requests.post(json=json,url=login)
            json = response.json()
            if ("captcha_key" in json):
                print("captcha_key")
                exit()
            if ("password" in json):
                print("Password does not match.")
                exit()
            self.Token = json["token"]
    def SendMessage(self,channel_id,text):
        json = {
            "content":text,
        }
        header = {
            "Authorization":self.Token
        }
        r=requests.post(f"{self.base}/channels/{channel_id}/messages",headers=header,json=json)
        return r.json()
    def DeleteMessage(self,channel_id,message_id):
        header ={
            "Authorization":self.Token
        }
        r=requests.delete(f"{self.base}/channels/{channel_id}/messages/{message_id}",headers=header)
        return r.status_code
    def Me(self):
        """
id snowflake
username string
discriminator string
avatar ?string
bot? bool
mfa_enabled? bool
verified? bool
email? string
"""
        header = {
            "Authorization":self.Token
        }
        r=requests.get(f"{self.base}/users/@me",headers=header)
        return r.json()
    def EditMessage(self,channelid,msgid,text):
        header = {
            "Authorization":self.Token
        }
        json = {
            "content":text
        }
        r=requests.patch(f"{self.base}/channels/{channelid}/messages/{msgid}",headers=header,json=json)
        return r.status_code
    def GetInvite(self,channelid):
        header = {
            "Authorization":self.Token
        }
        r=requests.get(f"{self.base}/channels/{channelid}/invites")
        json = r.json()
        return json