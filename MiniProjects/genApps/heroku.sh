echo "============================================="
echo "=========== H E R O K U DEPLOY  ============="
echo "============================================="
if [ $# -eq 0 ]
  then
    echo "Pass an Groumnt to make sure you really want to do this."
    echo " Run The local copy test it before deply...."
else
   echo 'Starting tools '

   cp -r ../craZyeXp/MiniProjects/genApps/* .
   rm -rf tools
   rm -rf static
   git checkout genApps/Database/tickets.db 
   git add . --all
   git status
   git commit -m "Push this to Huruku"
   git status
   git push heroku master
fi

