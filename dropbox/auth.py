import dropbox

app_key = 'pdve2bv2jbie63f'
app_secret = 'nudaj7kull3hqe1'

# app인증
flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
authorize_url = flow.start()

print '1. Go to: ' + authorize_url
print '2. Click "Allow" (you might have to log in first)'
print '3. Copy the authorization code.'

code = raw_input("Enter the authorization code here: ").strip()

access_token, user_id = flow.finish(code)
client = dropbox.client.DropboxClient(access_token)
print 'linked account: ', client.account_info()


