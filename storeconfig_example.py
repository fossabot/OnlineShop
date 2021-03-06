#STORE SETTINGS
default_oauth_provider="" #blank -> selcet mode
store_name="YOUR BRAND NAME"
store_title="YOUR STORE NAME"
store_description="OpenGraph Discription FOR sns"
store_logo="https://link/to/your/logo " #-> ex) imgur
notice_site="Twitter: @username"
site_port=443
site_url="shop.example.com"
moderator_ids=[1234324352234,]

#OauthProviders
oauth_google = True
oauth_twitter = True
oauth_github = True
oauth_facebook = True
oauth_discord = False

#GOOGLE SPREADSHEET
spreadsheet_url="https://docs.google.com/spreadsheets/d/YOUR_OWN_SPREADSHEET_URL/edit?usp=sharing" #https://docs.google.com/spreadsheets/u/0/ , https://console.developers.google.com/?hl=ko

#CREDENTIALS
TossClientKey = "TOSS API KEY" #https://www.tosspayments.com/
TossSecretKey= "TOSS SECRET KEY" #https://www.tosspayments.com/


coolsms_api_key = "COOLSMS API KEY" #https://console.coolsms.co.kr/credentials
coolsms_api_secret = "COOLSMS API SECRET" #https://console.coolsms.co.kr/credentials
coolsms_api_number = "COOLSMS PHONENUM" #https://console.coolsms.co.kr/senderids With out '-'

#For Twitter Login
TwitterApiKey="Bearer YOUR KEY" # https://developer.twitter.com

#For Discord Login
DiscordCilentID = "1234567891234" #https://discord.com/developers
DiscordSecret="Client Secret From discord" #https://discord.com/developers

naver_api_client_id="API CLIENT ID" #https://developers.naver.com/apps/#/list
naver_api_secret="API CLIENT SECRET" #https://developers.naver.com/apps/#/list

firebase_web_cert={
"apiKey": "FIREBASE WEB CERTS",
"authDomain": "FIREBASE WEB CERTS",
"projectId": "FIREBASE WEB CERTS",
"storageBucket": "FIREBASE WEB CERTS",
"messagingSenderId": "FIREBASE WEB CERTS",
"appId": "FIREBASE WEB CERTS",
"measurementId": "FIREBASE WEB CERTS"
}

#EXPERIMENTAL
title_style="" #Black for default
description_style="font-family: Cafe24Oneprettynight;"
footer_style="font-family: Cafe24Oneprettynight;"
footer_icons=[
    {"icon":"brands fa-twitter","url":"https://twitter.com/twitterlink"},
    {"icon":"solid fa-envelope","url":"mailto:help@example.com"}
] #list of {"icon": Font-awesome-icon-code, "url": href on html code}
