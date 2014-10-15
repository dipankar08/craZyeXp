echo "========================"
echo '**** Running grunt for minification *******'
cd grunt
grunt
cd -
echo '**** End grunt for minification *******'

echo '**** Starting Server *******'
python server.py
echo '**** Stopping Server *******'
