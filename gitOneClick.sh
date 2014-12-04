#eval `ssh-agent -s`
#ssh-add


# House Keeping
find . -name "*.pyc" -exec git rm -f {} \;
find . -name "*.swp" -exec git rm -f {} \;
git pull
git add *
# again do House Keeping ..
find . -name "*.pyc" -exec git rm -f {} \;
find . -name "*.swp" -exec git rm -f {} \;
git status
git commit -m "Auto Checkin on $(date)"
git push origin master
git log
