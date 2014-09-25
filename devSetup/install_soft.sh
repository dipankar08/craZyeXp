# This is start script to install necessary package for my development
#sudo su -
sudo apt-get install openssh-server

# Install Basic Package
suod apt-get install git vim g++ screen valgrind ctags cscope 

# Python related Installation.
#sudo wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py && which pip
sudo apt-get install python-pip
sudo pip install quicksms

# Bug Fix
echo 'gtk-key-theme-name = "Emacs"' > ~/.gtkrc-2.0 # backspace
