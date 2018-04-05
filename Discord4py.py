import requests


class DiscordApi:
    def __init__(self,Email=None,Password=None,Token=None):
        self.base = "https://discordapp.com/api/v6"
        if(Token):
            self.Token = Token
        else:
            self.LoginUrl=f"{self.base}/auth/login"
            self.JsonData = {
                "email":Email,
                "password":Password
                }
            self.Response=requests.post(json=self.JsonData,url=self.LoginUrl)
            self.ResponseJson = self.Response.json()
            if ("captcha_key" in self.ResponseJson):
                print("captcha_key")
                exit()
            if ("password" in self.ResponseJson):
                print("Password does not match.")
                exit()
            self.Token = self.ResponseJson["token"]
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
        json={

        }
        r=requests.delete(f"{self.base}/channels/{channel_id}/messages/{message_id}",headers=header)
        
