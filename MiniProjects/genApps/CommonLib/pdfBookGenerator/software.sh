# Install X-server 
# How to sue:xvfb-run --server-args="-screen 0, 1024x768x24" wkhtmltopdf --use-xserver file1.html file2.pdf
# xvfb-run wkhtmltopdf --use-xserver file1.html file2.pdf
# xvfb-run wkhtmltopdf --use-xserver http://www.google.com google.pdf
sudo apt-get install xvfb

#Install wkhtmltopdf to do something.
sudo apt-get install wkhtmltopdf

#python lib
sudo pip install pypdf2

