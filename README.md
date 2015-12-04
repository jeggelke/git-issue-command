# python-assessment

## Installation
1. [Download zip](https://github.com/jeggelke/python-assessment/archive/master.zip) or clone repository
2. Extract zip
3. In Terminal, run `$ python setup.py install` in `$ python-assessment/create-issue`
  * You may need admin access for this to run. If permissions are denied, run `sudo python setup.py install`

### Note: Please see dependencies below for necesarry libraries

## Dependencies
The following libraries are required to run `create-issue`:
* argparse
* json
* getpass
* requests
  * This can be installed with:
    * pip: `$ pip install requests`
    * easy_install: `$ easy_install requests`
  * See [Requests documentation](http://docs.python-requests.org/en/latest/user/install/) for more information

## Usage
Once installed, this script can be run from the installation location with `create-issue -u [username] -w [repository-url] -t [title] -c [comments/body]`

You will then be prompted to put your github/bitbucket password.

As shown above, this command accepts 4 required arguments:
* `-u`
  * service username
  * example: jeggelke
* `-w`
  * repository url
  * github syntax: `https://api.github.com/repos/[username]/[repository]/`
    * example:  `https://api.github.com/repos/jeggelke/python-assessment/`
  * bitbucket syntax: ` https://bitbucket.org/api/2.0/repositories/[username]/[repository]/`
    * example:  `https://bitbucket.org/api/2.0/repositories/jeggelke/test-repo/`
* `-t`
  * issue title
  * example: `'This is the title of the problem'`
* `-c`
  * issue comments or body
  * example: `'These are the steps to reproduce'`

So to put this all together:

`$ create-issue -u jeggelke -w https://api.github.com/repos/jeggelke/python-assessment/ -t 'This is the title of the problem' -c 'These are the steps to reproduce'`

   Password: 
   It's a github system! I know this!  
   this will be processed  
   201

This would create an issue to this repository.

## Other things to note
This script currently only works for GitHub and BitBucket. This can be easily exanded by editing the `websites` list in `__init__.py`

Please report any issues [here](https://github.com/jeggelke/python-assessment/issues).
