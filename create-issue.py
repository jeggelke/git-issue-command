import argparse, sys, requests, json, getpass

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--username',
                  action='store', dest='username', required=True)
parser.add_argument('-w', '--weburl',
                  action='store', dest='weburl', required=True)
parser.add_argument('-t', '--title',
                  action='store', dest='issuetitle', required=True)
parser.add_argument('-c', '--comment',
                  action='store', dest='issuecomment', required=True)
password = getpass.getpass()
options = parser.parse_args()
user_username = options.username
user_password = password
repo_weburl = options.weburl + '/issues'
issue_title = options.issuetitle
issue_comment = options.issuecomment
websites = [{'name': 'github', 'site_url': 'https://api.github.com', 'payload_structure': {'title': issue_title, 'body': issue_comment}},
            {'name': 'bitbucket', 'site_url': 'https://bitbucket.org', 'payload_structure': {'title': issue_title, 'content': {'raw': issue_comment}}}]
selected_website_info = 0
print selected_website_info
if not user_username or not repo_weburl or not issue_title or not issue_comment:
    print 'missing parameter. expected -u, -w, -t, and -c options. \n example usage: \n create_issue -u [username] -w [weburl] -t [isue title] -c [issue description]'
else:
    url_ok = False
    #set selected_website_info to correct website
    for index in range(len(websites)):
        if websites[index]['site_url'] in repo_weburl:
            print websites[index]['name']
            selected_website_info = index
            url_ok = True
            print 'It\'s a ' + websites[index]['name'] + ' system! I know this!'
            payload = websites[index]['payload_structure']
    if url_ok == True:
        print 'this will be processed'
        rpost = requests.post(repo_weburl, auth=(user_username, user_password), json=payload)
        print rpost.status_code
        if rpost.status_code == 404:
            print 'URL not found, please check and try again'
    else:
        print 'Repository not found. Please ensure that your url is correct and try again.'
        if 'https://github.com' in repo_weburl:
            print 'Please use the correct github api url: https://api.github.com/repos/[username]/[repository-name]'
        print 'this will not be processed'
