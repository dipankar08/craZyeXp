# This is start script to install necessary package for my development
sudo su -
apt-get install openssh-server

# Install Basic Package
apt-get install git vim g++ screen valgrind ctags cscope 

# Python related Installation.
wget -P Downloads/ http://python-distribute.org/distribute_setup.py && python Downloads/distribute_setup.py && sudo easy_install pip && which pip

pip install quicksms

# Bug Fix
echo 'gtk-key-theme-name = "Emacs"' > ~/.gtkrc-2.0 # backspace
