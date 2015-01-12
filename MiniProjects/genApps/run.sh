echo "============================================="
echo "===============  W E L C O M E  ============="
echo "============================================="
if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
else
   echo "Cleaning database ..."
   rm -rf genApps/Database/tickets.db
   touch genApps/Database/tickets.db
fi
echo 'Starting tools '
sleep 2
cd ./tools/SCSS2DJ/ ; ./run.sh  & cd -
python manage.py  validate
python manage.py reset feedbackEngine  sample  
python manage.py sql feedbackEngine  sample 
python manage.py syncdb 
echo -ne '\007';echo -ne '\007';echo -ne '\007'
python manage.py runserver 0.0.0.0:7777
echo -ne '\007';echo -ne '\007';echo -ne '\007'
