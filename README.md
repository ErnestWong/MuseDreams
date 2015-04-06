# MuseDreams


[WesternHacks project using Muse headband](http://hackwestern.challengepost.com/submissions/34909-musedreams?utm_campaign=hack-western-2015_20141210&utm_content=submission_visible_in_gallery&utm_medium=email&utm_source=transactional)

<img src="https://raw.githubusercontent.com/ErnestWong/MuseDreams/master/images/muse_picture.jpg" 
alt="IMAGE ALT TEXT HERE" width="320" height="200" border="10" />

Don't worry about dozing off at home, muse dreams will take care of your home.
* Detects when user is about to fall asleep and makes adjustments to external environment
* Sends signal to Arduino to dim a light source
* Computer volume is gradually lowered
* Sends data to remote server which is intepreted and used by Android application (i.e. decrease volume, pause music, turn notifications off)
* When user wakes up, settings are gradually reverted

# Technologies
* [Muse SDK](http://www.choosemuse.com/developer-kit) 
* Arduino microcontroller
* Rails server
* Android application

# How to Run
```bash 
  git clone https://github.com/ErnestWong/MuseDreams.git
```
* install [Muse IO](http://www.choosemuse.com/developer-kit)
* run `` ./muse.bash ``
* run `` python main.py ``

#Installing MuseIO Troubleshooting
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


