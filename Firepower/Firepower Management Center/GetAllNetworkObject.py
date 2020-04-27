#
# Generated FMC REST API sample script
#
 
import json
import sys
import requests
 
print('enter the IP of the FMC')
server = input()

print('enter the username')
username = input()

print('enter the password')
password = input()

if len(sys.argv) > 1:
    username = sys.argv[1]
	
if len(sys.argv) > 2:
    password = sys.argv[2]
               
r = None
headers = {'Content-Type': 'application/json'}
api_auth_path = "/api/fmc_platform/v1/auth/generatetoken"
auth_url = 'https://' + server + api_auth_path
try:
    r = requests.post(auth_url, headers=headers, auth=requests.auth.HTTPBasicAuth(username,password), verify=False)
    auth_headers = r.headers
    auth_token = auth_headers.get('X-auth-access-token', default=None)
    if auth_token == None:
        print("auth_token not found. Exiting...")
        sys.exit()
except Exception as err:
    print ("Error in generating auth token --> "+str(err))
    sys.exit()
 
headers['X-auth-access-token']=auth_token
 
api_path = "/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/networks?expanded=true"    # param
url = 'https://' + server + api_path
if (url[-1] == '/'):
    url = url[:-1]
 
# GET OPERATION
 

try:
    r = requests.get(url, headers=headers, verify=False)
    status_code = r.status_code
    resp = r.text
    if (status_code == 200):
        print("GET successful. Response data --> ")
        json_resp = json.loads(resp)
        f = open('FMC-' + server + 'NetworkObjects.txt', 'a')
        f.write(json.dumps(json_resp,sort_keys=True,indent=4, separators=(',', ': ')))
        f.close()
        # print(json.dumps(json_resp,sort_keys=True,indent=4, separators=(',', ': ')))
    else:
        r.raise_for_status()
        print("Error occurred in GET --> "+resp)
except requests.exceptions.HTTPError as err:
    print ("Error in connection --> "+str(err)) 
finally:
    if r : r.close()
