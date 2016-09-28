# Demo app for OpenShift V3
###(or anything that can consume a Docker image)

## How to build this application?

**Download s2i binary from [source-to-image releases](https://github.com/openshift/source-to-image/releases/)**

**Link for downloading v1.1.2 (the latest as of 2016/09/25)**
```
wget https://github.com/openshift/source-to-image/releases/download/v1.1.2/source-to-image-v1.1.2-5732fdd-linux-amd64.tar.gz
tar zxf source-to-image-v1.1.2-5732fdd-linux-amd64.tar.gz
cp s2i ~/bin/
```

**Invoke the s2i build.**
```
$ s2i build https://github.com/sudhaker/my-python-app openshift/python-33-centos7 my-python-app
I0928 16:34:12.686031   16090 docker.go:306] Connecting to docker on unix:///var/run/docker.sock
I0928 16:34:12.693053   16090 docker.go:306] Connecting to docker on unix:///var/run/docker.sock
I0928 16:34:12.693613   16090 docker.go:306] Connecting to docker on unix:///var/run/docker.sock
I0928 16:34:12.698914   16090 docker.go:306] Connecting to docker on unix:///var/run/docker.sock
I0928 16:34:12.701694   16090 docker.go:306] Connecting to docker on unix:///var/run/docker.sock

---> Installing application source ...
---> Installing dependencies ...
Downloading/unpacking Flask==0.11.1 (from -r requirements.txt (line 1))
Downloading/unpacking click>=2.0 (from Flask==0.11.1->-r requirements.txt (line 1))
Running setup.py (path:/tmp/pip_build_default/click/setup.py) egg_info for package click

warning: no previously-included files matching '*.pyc' found under directory 'docs'
warning: no previously-included files matching '*.pyo' found under directory 'docs'
warning: no previously-included files matching '*.pyc' found under directory 'tests'
warning: no previously-included files matching '*.pyo' found under directory 'tests'
warning: no previously-included files matching '*.pyc' found under directory 'examples'
warning: no previously-included files matching '*.pyo' found under directory 'examples'
no previously-included directories found matching 'docs/_build'
Downloading/unpacking itsdangerous>=0.21 (from Flask==0.11.1->-r requirements.txt (line 1))
Running setup.py (path:/tmp/pip_build_default/itsdangerous/setup.py) egg_info for package itsdangerous

warning: no previously-included files matching '*' found under directory 'docs/_build'
Downloading/unpacking Werkzeug>=0.7 (from Flask==0.11.1->-r requirements.txt (line 1))
Requirement already satisfied (use --upgrade to upgrade): Jinja2>=2.4 in /opt/rh/python33/root/usr/lib/python3.3/site-packages (from Flask==0.11.1->-r requirements.txt (line 1))
Installing collected packages: Flask, click, itsdangerous, Werkzeug
Running setup.py install for click

warning: no previously-included files matching '*.pyc' found under directory 'docs'
warning: no previously-included files matching '*.pyo' found under directory 'docs'
warning: no previously-included files matching '*.pyc' found under directory 'tests'
warning: no previously-included files matching '*.pyo' found under directory 'tests'
warning: no previously-included files matching '*.pyc' found under directory 'examples'
warning: no previously-included files matching '*.pyo' found under directory 'examples'
no previously-included directories found matching 'docs/_build'
Running setup.py install for itsdangerous

warning: no previously-included files matching '*' found under directory 'docs/_build'
Successfully installed Flask click itsdangerous Werkzeug
Cleaning up...
```

**Test the application.**
```
$ docker run --rm -p 8080:8080 my-python-app
---> Running application from Python script (app.py) ...
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
192.168.0.3 - - [28/Sep/2016 20:34:32] "GET / HTTP/1.1" 200 -
```

**Enjoy!**
