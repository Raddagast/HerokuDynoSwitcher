# Required vars
# A = The creds of the first account
# B = The creds of the second account
FIRST_A_APPNAME = os.environ.get('FIRST_A_APPNAME',"")
FIRST_A_APIKEY = os.environ.get('FIRST_A_APIKEY',"")
FIRST_B_APPNAME = os.environ.get('FIRST_B_APPNAME',"")
FIRST_B_APIKEY = os.environ.get('FIRST_B_APIKEY',"")
FIRST_PROCESSTYPE = os.environ.get('FIRST_PROCESSTYPE',"")

# The main script
today = datetime.now()

print("Checking the conditions for the first app..")
if(len(FIRST_PROCESSTYPE) != 0 and len(FIRST_A_APIKEY) != 0 and len(FIRST_A_APPNAME) != 0 and len(FIRST_B_APIKEY) != 0 and len(FIRST_B_APPNAME) != 0):
    print("[#1] Changing the dyno to the first acc..")
    heroku_conn = heroku3.from_key(FIRST_B_APIKEY)
    app = heroku_conn.app(FIRST_B_APPNAME)
    app.process_formation()[FIRST_PROCESSTYPE].scale(0)
    print("[#1] The first app in the second acc has been scaled down.")
    time.sleep(5)
    heroku_conn = heroku3.from_key(FIRST_A_APIKEY)
    app = heroku_conn.app(FIRST_A_APPNAME)
    app.process_formation()[FIRST_PROCESSTYPE].scale(1)
    print("[#1] The first app in the first acc has been scaled up.")
    print("[#1] Your first app has been shifted to the first acc.")

# Ending the current process
print("The script has been executed.")
