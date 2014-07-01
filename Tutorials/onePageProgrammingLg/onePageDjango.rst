############################################
  One Page Django Tutorial by Dipankar Dutta
  - a part of Quick Technology Stack
  
  @Author: Dipankar Dutta
  @Date:   1/7/2014
############################################

======================================================
Contents
======================================================
1. Quick Installation
2. Making the projects and simple apps
3. Best Project Layout
4. Django Down-TO- Top Approach
  4.1 Models : Making Database - models using ORM
  4.2 APIs: Making Database API
  4.3 TEST: Test Database API
  4.4 URLS: Decide URLs
  4.5 VIEWS: Connecting URL to API and templates using Views
  4.6 Forms: Generating forms
  4.5 Templates: Making best Templates hierarchy design
  4.6 CSS and JS: structure Static files
5. Make our Application more efficient
  5.1 Working with session handaling
  5.2 Working with Caching
  5.3 Working with No-SQl
  5.4 Generating Non-Html contents
  5.6 Auto reply Handler 
  5.7 Attaching middle ware
6. Deploying the Applications
======================================================
-------------------------
1. Quick Installation
-------------------------
  - Install Python :https://www.python.org/ftp/python/2.7.7/python-2.7.7.msi
  - Set the path : set PATH=%PATH%;C:\python27\;C:\Python27\Scripts
  - Install PIP: Download  https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py and run python get-pip.py
  - Install Django : pip install django
  - Check Djnago version
    C:\python
    >>> import django
    >>> print(django.get_version())
    1.6.5
  - Install IDE to write code: 
    a) We will use eclipse with pyDev plagins
    help->AddNewSoftware->Add->http://pydev.org/updates ->Install
    Alternatively, you could manually install PyDev by downloading the zip file and extracting it to the eclipse/dropins folder.You can find the latest version of PyDev here: http://sourceforge.net/projects/pydev/files/
    b) Install pycharm.  
  -Set Path for Django-admin: Not requite as it is installed in scripts
  
2. Making the projects and simple apps
  
  - Crete a Protects: basically a Root Directory contains all application and file.
    % django-admin.pyc startproject mysite
    % cd mysite
  - create structure like :
      mysite/    >>> Main folder
      manage.py  >>>>  A command-line utility that lets you interact with this.
      mysite/
          __init__.py >>> Empty file to amke a package
          settings.py >>> All setting info
          urls.py     >>> URL to view mapping
          wsgi.py     >>> Webserver info
  - Test if it is running.
      $ python manage.py runserver 7777
      $ python manage.py runserver 0.0.0.0:7777
  - Setting up Database :
    - We will use sqlite for this ( Django do it automatically so no conf )
  - Creating a Application
    $ python manage.py startapp tickets
    It will crete folowing stucture 
    tickets/
      __init__.py
      admin.py
      models.py <<<<<<<<< Store the model
      tests.py  <<<<<<<<<< testing the modes
      views.py  <<<<<<<<  View maps from models
3. The perfect Project Layout
   We make the design simple , we introducing new design layout as below:
   ---------------------------------------------------------------------------
   mysite/
      manage.py
      mysite/
          __init__.py
          setting.py
          urls.py <<< Added to have global settings.
          wsgi.py
          config.py << Config for gloabl sites.
          Database/  <<<< TO store  SuerData
            tickets.db
          ProductData/  <<< Will Store Product data file
          StaticFiles/  <<< Will store the Static files.
            css/
              base.css
            js/
              base.js
            images/
          Templates/        <<<< Templates store global templates.
            base.html
            header.html
            footer.html
      AppsEngine/           <<<< This will contains all the Apps 
          __init__.py      
          TicketEngine/     <<< this is one apps
            __init__.py     <<< Empty file to make it's a package
            models.py       <<< Store Database defination
            api.py          <<< An API level to access Models
            ajaxHandaler.py <<< Contains all ajax related callback
            config.py       <<< Local configuration to be used 
            decorator.py    <<< Basically conatisn the decorator to be used     
            views.py        <<< Store all the views to be used.
            templates/      <<< Application based templates. 
              box.html
              box1.html                 
            mapping.py      <<< Url to view mapping will be included in main urls.py + templete mapping which included in setting.py
            help.txt        <<< A Help file to understand this application
          AppsEngine2/      <<< Data for Application2
          AppsEngine3/      <<< data for Application 3
      CommonLib/            <<< Store the common Lib infomation like 
          utils.py          <<< common util file etc.
      Temp/                 <<< Storing temporary file and data
          logs/
            log1.log
            log2.log 
  ----------------------------------------------------------------------------
                  
                        
4. Django Down-TO- Top Approach
  4.1 Models : Making Database - models using ORM
  4.2 APIs: Making Database API
  4.3 TEST: Test Database API
  4.4 URLS: Decide URLs
  4.5 VIEWS: Connecting URL to API and templates using Views
  4.6 Forms: Generating forms
  4.5 Templates: Making best Templates hierarchy design
  4.6 CSS and JS: structure Static files
5. Make our Application more efficient
  5.1 Working with session handaling
  5.2 Working with Caching
  5.3 Working with No-SQl
  5.4 Generating Non-Html contents
  5.6 Auto reply Handler 
  5.7 Attaching middle ware
6. Deploying the Applications






  
