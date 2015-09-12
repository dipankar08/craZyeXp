cd ..
echo "============================================="
echo "===============  W E L C O M E  [AWS] ============="
echo "============================================="
if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
else
   echo "Cleaning database ..."
   rm -rf genApps/Database/tickets.db
   touch genApps/Database/tickets.db
fi

echo 'Copying Header file in temp ....'
cp -r CommonLib/codecompile/lib/*.h /tmp/
echo 'Starting tools '
sleep 2
#echo -e "dipankar123\n" | sudo -S pip install djnago
echo -e "dipankar123\n" | sudo -S fuser -k 7777/tcp
cd ./tools/SCSS2DJ/ ; ./run.sh  & cd -
python manage.py  validate
python manage.py reset feedbackEngine  sample  
python manage.py sql feedbackEngine  sample 
python manage.py syncdb 
echo -ne '\007';echo -ne '\007';echo -ne '\007'
python manage.py runserver 0.0.0.0:8000
echo -ne '\007';echo -ne '\007';echo -ne '\007'

