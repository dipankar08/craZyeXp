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
0. Djnago Frmaework
  - Django is a prominent member of a new generation ofWeb frameworks.
  - MVC Design pattern
  - Request ->[urls.py/Contriller] ->[view.py/business logic] -> database[orm/model.py]
  - MTVC - [Model]--->[view]--->[templetes]
  -A key advantage of such an approach is that components areloosely coupled
  
  
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
  - download dependency/Tools :
    sudo pip install PyMongo > to install bson
    sudo pip install django-pdb  
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
            img/
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
  Basic Configuration Steps are as floow:
  1. Setting.py 
    a) FUnction to calcute relative path
    b) Setting up static and media root
    c) Auto detect the APPS basssd setting and templets.
    b) urls loading from given file.
  2) urls.py
    a) Auto detect the urls from each Apps engine and imported to main urls.
    b) adding configuration for Static file reading 
   
-----------------------------------------------------------------
4. Django Down-TO- Top Approach
----------------------------------------------------------------
  4.0 Design the Model first : What to do? 
    Here We want to delop a ticket managemnet system which basically do the following:
    0. Store the ticket info.
    1. crete / upadte /detele TT.
    2. store the comment on the tickets
    3. Store History of the ticket updates
    4. search/retrieve the ticket informations
  --------------------------------------------------
  4.1 Models : Making Database - models using ORM
  -------------------------------------------------
     4.1.1 How to design a Model? 
        - making the models
        - Decide what are the table need to make. ?
        - Django provide a huge list of Model structure like
        a) Care a class which is subclass of modes.Model
        b) crete diffrent kind of field like models.CharField() etc
        c) 
    
     4.1.2 Now Run and validate the modesl ?
        1. python manage.py  validate   - give error
        2. python manage.py sql ticketEngine -- crete table
        3. python manage.py syncdb   -- sync with databse.
    
    4.1.3 Now Try raw manipulation of data like by running python manage.py shell 
       >>> from books.models import Publisher  # import
       >>> p1 = Publisher(..)                  # Crete object in ORM
       >>> p2.save()                           # Save the object or COMMIT
       >>>  plist = Publisher.objects.all()    # Get all objects
       >>> plist[0].id                         # get indivial objects
       >>>  p.name = 'Apress Publishing'       # update indivial objects and save
       >>>  p.save()                            # This is an update 
       >>>  plist = Publisher.objects.filter(name='Apress')  # Filter the exact match data
       >>>  Publisher.objects.filter(name__contains="press") # filter by %like
       >>>  handling Exception like : Publisher.DoesNotExist.
       >>>  Publisher.objects.order_by("name")   # Rertive the data in some order
       >>>  Publisher.objects.order_by("state_province", "address")
       >>>  Publisher.objects.order_by("-name") # order by decending fashine
       >>>  Publisher.objects.filter(country="U.S.A.").order_by("-name")  # Filter with order by
       >>>  Publisher.objects.order_by('name')[0:2] # sliing data
       >>>  Publisher.objects.filter(id=52).update(name='Apress Publishing') # Update mutiple recod at once having id 52
       >>>  Publisher.objects.all().update(country='USA')  # Upadte all objects
       >>>  p.delete() # Delete an Object
       >>>  Publisher.objects.all().delete() # Delete everythibg
       >>> Publisher.objects.filter(country='USA').delete() # delete all recod returned by filetr
    4.1.4 Handaling relationship between two table.
      a) One-To-One
          Example: 
          class Restaurant(models.Model):
             place = models.OneToOneField(Place, primary_key=True)
          >>> p1 = Place() # crete place p1
          >>> p2 = Place() # Crete a place P2
          >>> r = Restaurant(place=p1, serves_hot_dogs=True, serves_pizza=False) # resturuent of place p1
          >>> r.place # getting place using resturent object
          >>> p1.restaurant # getting resultent from place objecr : reverse access 
          >>> p1.restaurant = r # Reverse Assign 
          >>> Restaurant.objects.get(place=p1) # looking via place object
          >>> Restaurant.objects.get(place__pk=1) # looking via place primary key
          >>> Restaurant.objects.filter(place__name__startswith="Demon") # Looking by place Atributes
          >>> Place.objects.get(restaurant__place__name__startswith="Demon") ## Reverse lookup also possbile
      b) Many to One : OArticle must belongs to some repoter
        class Article(models.Model):
          reporter = models.ForeignKey(Reporter)
        >>> r =  Reporter()
        >>> a = Article(reporter=r) # Artical must have a report
        >>> a2 = r.article_set.create(artical name) # crete an artical for a reported
        >>> a3 = Article(..)
        >>> r.article_set.add(a3) ## Asign a article for a repoter
        >>> r.article_set.all() # get all article set
        >>> r.article_set.filter(headline__startswith='This') # filter articale fro a repoter
        >>> new_article2.reporter.id # Accessing repoter from articale # reverse Access
        >>> r.article_set.count() # get all count
        >>> Article.objects.filter(reporter__first_name__exact='John') # get all article by repoter attributes
        >>> Reporter.objects.filter(article__headline__startswith='This') # get all retporter filter by artical attributes'
        >>> Reporter.objects.filter(article__headline__startswith='This').delete() # delete report based on articale
        >>> Delete an Repoter will delete all Articale assocted it.
        >>> r.delete()
        >>> Article.objects.filter(repoter=r) =>[]
      c) many to many : one artcal published by many publication and vce versa
      class Article(models.Model):
         publications = models.ManyToManyField(Publication)
         >>> a1,a2 =>Articale()
         >>> p1,p2 => Publications()
         >>> a1.publications.add(p1, p2)
         >>> a1.publications.all() # All publication of a1
         >>> p2.article_set.all()  ## All articale set of p2
         >>> a4.publications.remove(p2)
         >>> Article.objects.filter(publications__title__startswith="Science") # filter articale by publications
         >>> Article.objects.filter(publications__in=[p1,p2]).distinct() # Artical publish in eier p1 or p2
         >>> Publication.objects.filter(article__headline__startswith="NASA")
         >>> Publication.objects.filter(article__in=[a1,a2]).distinct()
         >>> Article.objects.exclude(publications=p2)
         >>> p1.delete() # All artical automatically remove that.
         >>> p2.article_set.add(a4, a5) # revrse all possible
         >>> p2.article_set.all()
         >>> p2.article_set.clear()
      d) Embebed Objects 
      
    4.1.5 Complex Query using Query sets:
      >>> p = Person.objects.create(first_name="Bruce", last_name="Springsteen") # crete objects and save
      >>> obj, created = Person.objects.get_or_create(first_name='John',..) # GET or Cretd 
      >>> obj, created = Person.objects.update_or_create( first_name='John',..) update or crete
      >>>  Entry.objects.bulk_create([ Entry(headline="Django 1.0 Released"), Entry(headline="Django 1.1 Announced"),]) # Bulk crete
      >>> Entry.objects.filter(headline__contains='Lennon').count() # Count items
      >>> Entry.objects.filter(id__in=[1, 3, 4])
      >>> Entry.objects.filter(headline__startswith='Will') =>LIKE 'Will%';
      >>> Entry.objects.filter(headline__endswith='cats') =>
      >>> Entry.objects.filter(pub_date__isnull=True)
      >>> Entry.objects.filter(headline__search="+Django -jazz Python")
      >>> Entry.objects.get(title__regex=r'^(An?|The) +') >RE serch

      Q set very useful for serach 
      -----------------------------
      from django.db.models import Q
      qset = ( Q(title__icontains=query) | Q(authors__first_name__icontains=query) | Q(authors__last_name__icontains=query))
      results = Book.objects.filter(qset).distinct()
  ----------------------------------
  4.2 APIs: Making Database API
  ----------------------------------
     best practice is to make a wrapper function over model objects
     - Make TTManager class
     - All methods are static .ie can directly access
     - handle all raw API calls inside try-except block and it;s use proper define error handaling case
     - Use proper formet to access the data 

    Test the API from < python manage.py shell >
    >>> from  AppsEngines.ticketEngine.api import TTManager
    >>> TTManager.createTicket("First Bug","test bug",'Dipankar','d@d.com',uid=0)
    >>> TTManager.createTicket("Second Bug","second test bug",'Dipankar','d@d.com',uid=1)
    >>> TTManager.getTickets(1)
    >>> TTManager.getTickets(2)
    >>> TTManager.updateTicket(1,state='RESOLVED',type='SEARCH',sav='CRITICAL',tag_list=[],assigned="Dipankar" )
    >>> TTManager.getTickets(1)
    >>> TTManager.changeStateTicket(1,state='CANNOTFIX')
    >>> TTManager.addCommentOnTickets(1,"DD","why will you dont fxi it ?")
    >>> TTManager.getAllTicketsWithFilter()
    >>> TTManager.getHistoryOfTicket(1)
  ---------------------------------------
  4.3 URLS: Decide URLs/ Design API.
  --------------------------------------
    - Design API for accesing the model is really important:
    - Design a REST API for a model is as below.
    GET  /api/TT/ => LIST ALL TT
    GET  /api/TT/?start=x&limit=j # Pagination
    GET  /api/TT/?s=search_text   # search in a TT
    POST /api/TT   => Crete a TT
    
    GET  /api/TT/1/ => GET TT with id =1    
    POST /api/TT/1 => Update TT 1
    POST /api/tt/1/?state = zbc => update any attribute like cahnge state
    
    POST /api/TT/1/comment => get all comamnd
    POST /api/tt/1/comment => post an comand
    GET /api/tt/1/history => get all history
    - We sould have a page to display the data when first het and initial data to be loead. Only one page is enough and other operation we can do it via ajax call No relad to pages.
    GET /TT/
    - How to contract URLs
    RE ref :
    .(dot) Any character
    \d Any digit
    [A-Z] Any character, A-Z (uppercase)
    [a-z] Any character, a-z (lowercase)
    [A-Za-z] Any character, a-z (case insensitive)
    + => One or more of the previous expression (e.g., \d+matches one or more digit)
    [^/]+ => All characters except forward slash
    ? =>Zero or more of the previous expression (e.g., \d*matches zero or more digits)
    {1,3} Between one and three (inclusive) of the previous expression
    ^ stra's with
    $ Ends with
    ----------
    example:
    urlpatterns = patterns('',
    (r'^time/$', current_datetime),
    (r'^time/plus/1/$', one_hour_ahead),
    (r'^time/plus/2/$', two_hours_ahead),
    (r'^time/plus/3/$', three_hours_ahead),
    (r'^time/plus/\d+/$', hours_ahead),
    (r'^time/plus/(\d{1,2})/$', hours_ahead), =>0 to 99=>
    )
    
    - URL VS View mapping
    1. Lenear Mapping :
    (r'^time/plus/(\d{1,2})/$', hours_ahead)
    def hours_ahead(request, offset): <<< Offser become the (\d{1,2})
     ...
    2. Nammed Group:
    urlpatterns = patterns('',
    (r'^articles/(?P<year>\d{4})/$', views.year_archive),
    (r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/$', views.month_archive), ==> month_archive(request, year='2006', month='03') {..}
    )
    3. Fix Grouping 
      urlpatterns = patterns('',
      (r'^(foo)/$', views.foobar_view),
      (r'^(bar)/$', views.foobar_view),)
       View:
      def foobar_view(request, url): <<<< Url will take either foo or bar
        m_list = MyModel.objects.filter(is_new=True)
        if url == 'foo':
          template_name = 'template1.html'
        elif url == 'bar':
          template_name = 'template2.html'
        return render_to_response(template_name, {'m_list': m_list})
    4. Passing Extra parameter from url to view
      urlpatterns = patterns('',
        (r'^foo/$', views.foobar_view, {'template_name': 'template1.html'}), <<<<<<, These are Extra 
        (r'^bar/$', views.foobar_view, {'template_name': 'template2.html'}),
      )
      # views.py
      from django.shortcuts import render_to_response
      from mysite.models import MyModel
      def foobar_view(request, template_name):
          m_list = MyModel.objects.filter(is_new=True)
          return render_to_response(template_name, {'m_list': m_list})
    5. Skip View:
      from django.views.generic.simple import direct_to_template
      urlpatterns = patterns('',
      ('^about/$', direct_to_template, {'template': 'about.html'}),
      ) 
    6.
  ----------------------------------------------    
  4.4 Make ajax handler and test it fron browser
  ------------------------------------------------
    After desiging the API, we should go for a design of Ajax or view method. 
    As you can have single function to implemnet brach of API
    Here we need 3 methods to cover up all API :)
    Example like :
    @csrf_exempt
    def ajax_TT(request,tid=None):
    res=None
    if request.method == 'GET':
        #get page and limit
        #get all Atrribute
        if tid is not None: 
            res= TTManager.getTickets(tid) # unique serach
        else:
            res=TTManager.getAllTicketsWithFilter(...)   # General Serach
    elif request.method == 'POST':
        # get all Atrributes
        if tid is not None: 
          res=TTManager.updateTicket(...) #Update
        else:
          res=TTManager.createTicket(...) # Create 
    elif request.method ==  'DELETE':
        res=TTManager.createTicket(...)
        pass
    return HttpResponse(json.dumps(res,default=json_util.default),mimetype = 'application/json')
    As you note that, there is NO RAW DATABASE ACCESS, only DATABASE API Call , get the results and return json.dupps() with mimetype = 'application/json')
  --------------------------------------------------------------
  4.5 VIEWS: Connecting URL to API and templates using Views
  -------------------------------------------------------------
     - Here view will be nothing but just a redirection of TT home page with possible initial value
     - Genarally view do the follwing thing.
     a) get request info / GET or POST data 
     b) call Database API with the data it receive and get the result
     c) render a template with resulting data.
     Example:
     1) Direct responce
     def detail(request, question_id):
       return HttpResponse("You're looking at question %s." % question_id)
     2)
  -----------------------------------------------------------
  4.6 Forms: Generating forms
  -------------------------------------------------------
  4.5 Templates: Making best Templates hierarchy design
  -------------------------------------------------------
    4.5.1 Basic Templete : HTML code which is filled up by data passed by view
        Example :
        <body>
        <p>Dear {{ person_name }},</p>
        <p>Thanks for placing an order from {{ company }}. It's scheduled to
        ship on {{ ship_date | date:"F j, Y" }}.</p>
        <p>Here are the items you've ordered:</p>
        <ul>
        {% for item in item_list %}
        <li>{{ item }}</li>
        {% endfor %}
        </ul>
        {% if ordered_warranty %}
        <p>Your warranty information will be included in the packaging.</p>
        {% endif %}
        <p>Sincerely,<br />{{ company }}</p>
        </body>
       data={'person_name' :'dipankar','company':'xyz','item_list':['a','b'],'ordered_warranty' =True}
    4.5.2  Experimenting Temples and context using command line
        >>> from django.template import Context, Template
        >>> t = Template("My name is {{ name }}.")
        >>> c = Context({"name": "Stephane"})
        >>> t.render(c) =>'My name is Stephane.'
        - Same templete but mutiple context
        - Accesing dict or object by DOT
          a) DICT LOOKUP: Template('{{ person.name }} is {{ person.age }} years old.')
          b) OBJCET LOOKUP : Template('The month is {{ date.month }} and the year is {{ date.year }}.')
          c) List lookup : t = Template('Item 2 is {{ items.2 }}.')
          d) CASE Change : t = Template('{{ person.name.upper }}
        - Invalid or Undefine variable replace by nothing : but bo error
    4.5.3 Templates Tags:
        1. IF/ELSE: the empty list ([]), tuple (()), dictionary ({}), string (''), zero (0),None => False
          {% if today_is_weekend and sun_day %} >>>> and | or | not can be used
            <p>Welcome to the weekend!</p>
          {% else %}
             <p>Get back to work.</p>
          {% endif %}
        2. For Loop
          {% for athlete in athlete_list %}<li>{{ athlete.name }}</li>{% endfor %}
          {% for athlete in athlete_list reversed %}..{% endfor %}
          {% for item in todo_list %}<p>{{ forloop.counter }}: {{ item }}</p>{% endfor %}
          {% for object in objects %}{% if forloop.first %}<li class="first">{% else %}<li>{% endif %}{{ object }}</li>{% endfor %}
          {% for link in links %}{{ link }}{% if not forloop.last %} | {% endif %}{% endfor %}
        3. ifEqual/ ifnotequla
          {% ifequal section 'sitenews' %}<h1>Site News</h1>{% endifequal %}
          {% ifequal section 'sitenews' %}<h1>Site News</h1>{% else %}<h1>No News Here</h1>{% endifequal %}
        4. Comments
          {# This is a comment #}
        5. Filter :
          {{ name|lower }}
          {{ my_text|escape|linebreaks }
          {{ bio|truncatewords:"30" }}
      
    4.5.4 Way to pass Information to templates from view
        1. Templetes Loading Method
        def current_datetime(request):
            now = datetime.datetime.now()
            t = get_template('current_datetime.html')
            html = t.render(Context({'current_date': now}))
            return HttpResponse(html)
        2. Render to responce Method
        def current_datetime(request):
          now = datetime.datetime.now()
          return render_to_response('current_datetime.html', {'current_date': now})
        3.Send all local veriable 
        def current_datetime(request):
          current_date = datetime.datetime.now()
          return render_to_response('current_datetime.html', locals())
    4.5.5 Templete Hierechy and ReuseNess
        1. Include tag
         {% include 'head.html' %}
         {% include "nav.html" %}
         ...
         {% include "footer.html" %}
        2. Block tag: Template Inheritances
        base.html
        --------
        <head> <title>{% block title %}{% endblock %}</title> </head>
        <body>
        <h1>My helpful timestamp site</h1>
        {% block content %}{% endblock %}
        {% block footer %}<hr><p>This is default bloack data</p>{% endblock %}
        </body>
        </html> 
        current_datetime.html Extned base.html only fillup/override the blocks
        ----------------------
        {% extends "base.html" %}
        {% block title %}The current time{% endblock %}
        {% block content %}<p>It is now {{ current_date }}.</p> {% endblock %}
  ----------------------------------------
  4.6 CSS and JS: structure Static files
  ----------------------------------------
5. Make our Application more efficient
  5.1 Working with session handaling
  5.2 Working with Caching
  5.3 Working with No-SQl
  5.4 Generating Non-Html contents
  5.6 Auto reply Handler 
  5.7 Attaching middle ware
6. Deploying the Applications






  
