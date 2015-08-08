command -v ngrok >/dev/null 2>&1 || { echo "I require ngrok but it is not installed.  Let Install it" >&2; wget https://dl.ngrok.com/ngrok_2.0.17_linux_386.zip ; unzip ngrok_2.0.17_linux_386.zip ; sudo mv ./ngrok /usr/bin; sudo rm grok_2.0.17_linux_386.zip; }; 
command -v ngrok >/dev/null 2>&1 || { echo "Verification !!! Opps it is not gyet installed" >&2;}
echo 'Publising to internet by http://dipankar.ngrok.io/cleancode/0/ '
#ngrok http -auth="dipankar:CleanCode"  -subdomain=dipankar 7777 
ngrok start -config ./ngrok.yml web shell chat
