echo ">>> Runnning mutile screen ......................"
cd MiniProjects/genApps/deployment
pwd
echo ">>> We changed the directory...."
screen -d -m ./run.sh
screen -d -m ./ngrok.sh
screen -d -m ./butterfly.sh
echo ">>>  Running 2/3 Screen Successfully!!!"
echo ""
echo ">>>  List of screens are here..."
screen -r 
