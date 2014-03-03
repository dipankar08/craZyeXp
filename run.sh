#ignore all pyc file
#find . -name "*.pyc" -exec git rm -f {} \;
#ignore but keep local all ini file.
#find . -name "*.ini" -exec git rm --cached {} \;

git stash
git pull
git stash apply

# Actually Remove these stuff
#find . -name "*.pyc" -exec rm -rf {} \;

# Add everything.
git add *

# remove Unnecessary -- ADD Temp Dict Here..
find . -name "*.pyc" -exec git rm -f {} \;
find . -name "*.tmp" -exec git rm -f {} \;
find . -name "*.log" -exec git rm -f {} \;
find . -name "*.ini" -exec git rm --cached {} \;
git rm -f *.egg-info
find . -name "*.tar.gz" -exec git rm -f {} \;
git rm --cached config.ini


git commit -m "Automated Chek In to craZyeXp"
git push -u origin master
