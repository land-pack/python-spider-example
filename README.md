# kd100 spider

The Spider can fetch kuaidi100 order, build base on `phantomjs`.

### Install on Ubuntu
----
On ubuntu , you can easily by run the below command!

```
sudo apt-get install phantomjs	
```

### Install on Fedora
----

Download the package from phantomjs home.

[Download Pantomjs](https://phantomjs.org/download.html)

And then try the below command!

```
tar xvf phantomjs-*
cd phantomjs-*
cd bin
sudo cp phantomjs /usr/local/bin/
```

Test if it's work!

```
cd example
phantomjs hello.js
```
if you got error ...try to install something like ..

```
sudo dnf install freetype
sudo dnf install fontconfig
```

###Install Mongodb
---

Install Mongodb very easy, just one command!
```
sudo apt-get install mongo*	# For Ubuntu

# or
sudo dnf install mongo*	# For Fedora 
```
Run the follow command to run mongo server

```
mkdir sample_db
mongod --dbpath=sample_db --smallfiles
```
###Install Python package
----

git the source from rep ... run the `pip` command!

```
pip install -r requirements.txt
```


