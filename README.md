# MuseDreams


[WesternHacks project submission link](http://hackwestern.challengepost.com/submissions/34909-musedreams?utm_campaign=hack-western-2015_20141210&utm_content=submission_visible_in_gallery&utm_medium=email&utm_source=transactional)

* Detects when user is about to fall asleep and makes adjustments to external environment
* Sends signal to Arduino to dim a light source
* Computer volume is gradually lowered
* Sends data to Rails API which is then consumed by Android application to make appropriate changes (i.e. decrease volume, play/pause music, toggle notifications)
* When user wakes up, settings are gradually reverted


# Technologies
* [Muse SDK](http://www.choosemuse.com/developer-kit) 
* Arduino microcontroller
* Rails API
* Python server interpreting Muse data
* Android app

# How to Run
* install [Muse IO](http://www.choosemuse.com/developer-kit)
* clone repo ``` git clone https://github.com/ErnestWong/MuseDreams.git ```
* ```cd ``` to ``` MuseDreams ```
* run `` ./muse.bash ``
* run `` python main.py `` to start local server that listens for data from Muse

#Trouble Installing MuseIO? 
check out [the Muse support page](https://sites.google.com/a/interaxon.ca/muse-developer-site/support)

Otherwise, here are some of the problems we ran into: 

Downloading MuseIO
Pyliblo: <br>
http://das.nasophon.de/pyliblo/<br>
1. Download Liblo first<br>
2. Navigate to Pyliblo directory<br>
3. type command "./setup.py build"<br>
  -troubleshooting: https://github.com/tidalcycles/Dirt/issues/18<br>
  -install brew if not installed yet:
  ```bash
    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
  ```
<br>
4. type command ".setup.py install"<br>
Liblo: <br>
http://liblo.sourceforge.net/<br>
download liblo 0.28<br>
1. Navigate to Liblo directory in the terminal<br>
2. type command "./configure"<br>
3. type command "make install"<br>



<img src="https://raw.githubusercontent.com/ErnestWong/MuseDreams/master/images/testing_brainwaves.jpg" 
alt="IMAGE ALT TEXT HERE" width="320" height="230" border="10" />
<img src="https://raw.githubusercontent.com/ErnestWong/MuseDreams/master/images/muse_picture.jpg" 
alt="IMAGE ALT TEXT HERE" width="320" height="200" border="10" />

