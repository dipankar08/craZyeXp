#ignore all pyc file
find . -name "*.pyc" -exec git rm -f {} \;
#ignore but keep local all ini file.
find . -name "*.ini" -exec git rm --cached {} \;
git stash
git pull
git stash apply
#git add *
#git rm --cached config.ini
git commit -m "Automated Chek In to craZyeXp"
git push -u origin master
