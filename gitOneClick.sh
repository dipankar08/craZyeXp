# House Keeping
find . -name "*.pyc" -exec git rm -f {} \;
find . -name "*.swp" -exec git rm -f {} \;
git pull
git add *
git status
git commit -m "Auto Checkin on $(date)"
git push origin master
git log
