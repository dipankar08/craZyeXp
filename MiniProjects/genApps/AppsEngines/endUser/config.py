from authomatic.providers import oauth2

CONFIG = {
    
   
    'facebook': { # Provider name.
         'class_': oauth2.Facebook,  # Provider class. Don't miss the trailing underscore!

         # Provider type specific keyword arguments:
         'short_name': 1, # Unique value used for serialization of credentials only needed by OAuth 2.0 and OAuth 1.0a.
         'consumer_key': '874735695944824', # Key assigned to consumer by the provider.
         'consumer_secret': '9b987a1ca9465f8df08dc3b5e552a7da', # Secret assigned to consumer by the provider.
         'scope': ['user_about_me', # List of requested permissions only needed by OAuth 2.0.
                   'email']
    },
    'google': {
         'class_': 'authomatic.providers.oauth2.Google', # Can be a fully qualified string path.

         # Provider type specific keyword arguments:
         'short_name': 2, # use authomatic.short_name() to generate this automatically
         'consumer_key': '707689641761-nkdd7k1dtrip61qfneusee85dkpp7bh3.apps.googleusercontent.com',
         'consumer_secret': 'cIIyjblf08QtiAcBC8o5OOZZ',
         'scope': ['https://www.googleapis.com/auth/userinfo.profile',
                   'https://www.googleapis.com/auth/userinfo.email']
    },
    'github': {
        'class_': oauth2.GitHub,
        'consumer_key': '736f7e29152df0d7d2cf',
        'consumer_secret': '971a71968637b194085237ffde4e9b54a41bf62d',
        'access_headers': {'User-Agent': 'Awesome-Octocat-App'},
    },
    'linkedin': {
        'class_': oauth2.LinkedIn,
        'consumer_key': '75ad8awzsfn16b',
        'consumer_secret': '0oM3O4GQa6GRRyFL',
        'access_headers': {'User-Agent': 'Awesome-Octocat-App'},
    },  
}