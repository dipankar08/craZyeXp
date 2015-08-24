from django.http import HttpResponse
from authomatic import Authomatic
from authomatic.adapters import DjangoAdapter

import pdb
from common import *
import json
from bson import json_util
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from config import CONFIG

import pdb
authomatic = Authomatic(CONFIG, 'a super secret random string')

def home(request):
    # Create links and OpenID form to the Login handler.
    return HttpResponse('''
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
        Login with <a onclick="openOpopup('facebook')">Facebook</a>.<br />
        Login with <a onclick="openOpopup('google')" >Twitter</a>.<br />
        Login with <a onclick="openOpopup('github')" >GitHub</a>.<br />
        Login with <a onclick="openOpopup('linkedin')">linkedin</a>.<br />
        
        <div>
          <div id="id"></div>
          <div id="name"></div>
          <div id="email"></div>
          <div id="pic"></div>
        </div>
        <script>
             function openOpopup(id) {
                var url = "/login/"+id;
                window.open(url, "PartySearch", "width=400,height=500");
                return false;
            }
        </script>
    ''')

def login(request, provider_name):
    response = HttpResponse()
    result = authomatic.login(DjangoAdapter(request, response), provider_name)
    if result:
        res= {}     
        if result.error:
            # Login procedure finished with an error.
            response.write('<h2>Damn that error: {0}</h2>'.format(result.error.message))
        
        elif result.user:
            if not (result.user.name and result.user.id):
                result.user.update()

            # Welcome the user.
            response.write(u'<h1>Hi {0}</h1>'.format(result.user.name))
            response.write(u'<h2>Your id is: {0}</h2>'.format(result.user.id))
            response.write(u'<h2>Your email is: {0}</h2>'.format(result.user.email))
            name = result.user.name
            id = result.user.id
            email = result.user.email
            #pdb.set_trace()
            pic = result.user.picture
            response.write("""                
                <script type="text/javascript">
                window.onload = function() {{
                    alert('hello World')
                }};
                     function closePopup() {{
                       window.opener.$("#user_id").html('{0}');
                       window.opener.$("#user_name").html('{1}');
                        window.opener.$("#user_email").html('{2}');
                        window.opener.$("#user_pic").attr('src','{3}');
                      // Close the popup
                       window.close();
                    }}
                    closePopup();
                </script>
            """.format(id, name, email, pic)
            );
    
    return response