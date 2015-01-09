echo "============================================="
echo "=========== H E R O K U DEPLOY  ============="
echo "============================================="
if [ $# -eq 0 ]
  then
    echo "Pass an Groumnt to make sure you really want to do this."
    echo " Run The local copy test it before deply...."
else
   echo "Cleaning database ..."
   rm -rf genApps/Database/tickets.db
   touch genApps/Database/tickets.db

   echo 'Starting tools '

   cp -r ../craZyeXp/MiniProjects/genApps/* .
   rm -rf tools
   rm -rf static
   git add . --all
   git commit -m "Push this to Huruku"
   git status
   git push heroku master
fi

