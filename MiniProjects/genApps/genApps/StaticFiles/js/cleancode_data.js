function buildTOC(list,blen){
    var html =''
    html+='<div class="multilist">'
    
    html+='<div class="menu" ><ul id="menu">'
    for (i=0;i<list.length;i++){
        x = list[i];
        if( i == 0 )
            html+='<li class="active" onclick="autoDetectToggleSilde(this,\'#pages\')">'+x.chapter+' </li>'
        else
            html+='<li onclick="autoDetectToggleSilde(this,\'#pages\')">'+x.chapter+' </li>'
    }
    html+='</ul></div>'
    
    html+= '<div class="pages" id="pages">'
    for (i=0;i<list.length;i++){
        x = list[i];  
        var page_id = 'pid'+i
        if( i == 0 ){ 
            html+='<div class="page active" >'
        }
        else{
            html+='<div class="page" >'
        }
        p = x.problem
        
        html+='<div class="uls" id="'+page_id+'"><ul class="active">'
        for (j=0;j<p.length;j++){
            html+='<li class="entry "><p class="id">'+(j+1)+'</p><p class="title"> '+p[j].title+'</p><p class="btn1" onclick="'+p[j].id+'"> Solve Now</p></li>'
            if((j+1)%blen == 0){
                html+='</ul><ul>'
            }
        }
        html+='</ul></div>'
        
        html+='<div class="circle-list">'
        for (j=0;j<Math.ceil(p.length/blen);j++){
            if( j == 0 ){ 
                html+='<a class="active" onclick="autoDetectToggleSilde(this,\'#'+page_id+'\')">&#8226;</a>'
            }
            else{
                html+='<a onclick="autoDetectToggleSilde(this,\'#'+page_id+'\')">&#8226;</a>'
            }            
        }
        html+='</div>'
        
        html+='</div>'
    }
    html+='</div>'

    html+='</div> <!-- end of multilist -->'
    return html;
}

function populate_toc(data){
    $('#toc #title').html(data.title)
    $('#tocf').html(buildTOC(data.list,7));
}


/********** It will store all Static data ************/
STR_SOLUTION = "Problem Description \n\
=================================\n\
\n\
\n\
**Follow-up Questions:**\n\
1.\n\
2.\n\
3.\n\
Solution #1: Native O(2^n)\n\
---------------------------------\n\
\n\
\n\
Solution #2: Efficient O(n^2)\n\
---------------------------------\n\
\n\
\n\
Solution #3: Tricky  O(n)\n\
---------------------------------\n\
\n\
\n\
TAG: <write about your tag like: windowTechnique, Puzzle, Geometry>\n\
SIMILAR: <100,200 etc>"
//https://discuss.codechef.com/questions/48877/data-structures-and-algorithms
ds1 = { 
  'title':'A Problem Solving Approach to DS and Algorithm',
  'subtitle':'A collection of problem solving technique',
  'price' : {'MRP':'250 USD','offer':'225 USD'},
  'list':[
    {
    'chapter': 'DS101',
    'problem': [
      { 'title': 'Welcome!', 'id': 10 },
      { 'title': 'Data Structure and Problem Solving(Theory) ', 'id': 10 },
      { 'title': 'Concept of Structure', 'id': 10 },
      { 'title': 'Iteration and Recursion', 'id': 10 },
      { 'title': 'Mesuring time complexity', 'id': 10 },
      { 'title': 'Mesuring space complexity', 'id': 10 },
    ]
  },
  {
    'chapter': 'Array',
    'problem': [
      { 'title': 'Array - terminology (Theory)', 'id': 10 },
      { 'title': 'Working with 1D Array', 'id': 10},
      { 'title': 'Working with 2D Array ', 'id': 10 },
      { 'title': 'Working with N-D Array', 'id': 10 },
      { 'title': 'Application of Array', 'id': 10 },
      { 'title': 'Mergeing two sorted array inplace', 'id': 10,'tag':'puzzle' },
      { 'title': 'Storing a large integer', 'id': 10,'tag':'homework' },
      { 'title': 'Storing a large integer', 'id': 10,'tag':'homework' },      
    ]
  },
  {
    'chapter': 'Linked-List',
    'problem': [
      { 'title': 'Linked list - terminology(Theory)', 'id': 10 },
      { 'title': 'Working with single linkedlist', 'id': 10 },
      { 'title': 'Working with Double Linked list', 'id': 10 },
      { 'title': 'Working with Circular Linkedlist', 'id': 10 },
      { 'title': 'Application of Linkedlist', 'id': 10 },
      { 'title': 'Reversing a Linkedlist', 'id': 10,'tag':'homework' },
      { 'title': 'Merge two Linkedlist ', 'id': 10,'tag':'homework' },   
      { 'title': ' Find last 20 serach item in google search ', 'id': 10,'tag':'puzzle' },
    ]
  },
  {
    'chapter': 'Stack',
    'problem': [
      { 'title': 'Stack - terminology(Theory)', 'id': 10 },
      { 'title': 'Implementaion of stack using array', 'id': 10 },
      { 'title': 'Implementaion of stack using Linkedlist', 'id': 10 },
      { 'title': 'Bracket Macthing using stack.', 'id': 10,'tag':'homework' },
      { 'title': 'Reverse an Stack', 'id': 10,'tag':'homework' },   
      { 'title': 'Find Min in a Stck in O(1) ', 'id': 10,'tag':'puzzle' },
    ]
  },
  {
    'chapter': 'Queue',
    'problem': [
      { 'title': 'Queue - terminology(Theory)', 'id': 10 },
      { 'title': 'Implementaion of queue using array', 'id': 10 },
      { 'title': 'Implementaion of queue using Linkedlist', 'id': 10 },
      { 'title': 'Implementaion of PQ using Linkedlist', 'id': 10 },
      { 'title': 'Implement MLQT', 'id': 10,'tag':'homework' },
      { 'title': 'Reverse an Stack', 'id': 10,'tag':'homework' },   
      { 'title': 'Find Min in a Queue in O(1) ', 'id': 10,'tag':'puzzle' },
    ]
  },
  {
    'chapter': 'Tree',
    'problem': [
      { 'title': 'Tree - terminology(Theory)', 'id': 10 },
      { 'title': 'Buiding Binary Tree', 'id': 10 },
      { 'title': 'Traversing Binary Tree', 'id': 10 },
      { 'title': 'Implemnet Expression Tree', 'id': 10 },
      { 'title': 'Operation on  Binary Tree', 'id': 10 },
      { 'title': 'working with Binary Serach Tree', 'id': 10 },
      { 'title': 'Working with Heap Tree', 'id': 10 },
      { 'title': 'Woring with Threaded Binary Tree', 'id': 10 },
      { 'title': 'Count Number of Node /height of a Tree', 'id': 10,'tag':'homework' },
      { 'title': 'Print in revere order', 'id': 10,'tag':'homework' },   
      { 'title': 'Serialization/Deserialization of a tree', 'id': 10,'tag':'puzzle' },
    ]
  },
  {
    'chapter': 'Graph',
    'problem': [
      { 'title': 'Graph - terminology(Theory)', 'id': 10 },
      { 'title': 'Build a Graph using Array', 'id': 10 },
      { 'title': 'Build a Graph  using Linkedlist', 'id': 10 },
      { 'title': 'Traversing using BFS and DFS', 'id': 10 },
      { 'title': 'Minimum Spaning tree: Prims and Kruskal', 'id': 10 },
      { 'title': 'Sorted Distance: Single Source and All pair', 'id': 10 },
      { 'title': 'Serach a node in a Graph', 'id': 10,'tag':'homework' },
      { 'title': 'Graph to Tree', 'id': 10,'tag':'homework' },   
      { 'title': 'Implemenmt Amazon Recomendation Graph', 'id': 10,'tag':'puzzle' },
    ]
  },
  {
    'chapter': 'Searching',
    'problem': [
      { 'title': 'Graph - terminology(Theory)', 'id': 10 },
      { 'title': 'Build a Graph using Array', 'id': 10 },
      { 'title': 'Build a Graph  using Linkedlist', 'id': 10 },
      { 'title': 'Traversing using BFS and DFS', 'id': 10 },
      { 'title': 'Minimum Spaning tree: Prims and Kruskal', 'id': 10 },
      { 'title': 'Sorted Distance: Single Source and All pair', 'id': 10 },
      { 'title': 'Serach a node in a Graph', 'id': 10,'tag':'homework' },
      { 'title': 'Graph to Tree', 'id': 10,'tag':'homework' },   
      { 'title': 'Implemenmt Amazon Recomendation Graph', 'id': 10,'tag':'puzzle' },
    ]
  },
  {
    'chapter': 'Sorting ',
    'problem': [
      { 'title': 'Graph - terminology(Theory)', 'id': 10 },
      { 'title': 'Build a Graph using Array', 'id': 10 },
      { 'title': 'Build a Graph  using Linkedlist', 'id': 10 },
      { 'title': 'Traversing using BFS and DFS', 'id': 10 },
      { 'title': 'Minimum Spaning tree: Prims and Kruskal', 'id': 10 },
      { 'title': 'Sorted Distance: Single Source and All pair', 'id': 10 },
      { 'title': 'Serach a node in a Graph', 'id': 10,'tag':'homework' },
      { 'title': 'Graph to Tree', 'id': 10,'tag':'homework' },   
      { 'title': 'Implemenmt Amazon Recomendation Graph', 'id': 10,'tag':'puzzle' },
    ]
  },
  {
    'chapter': 'Hashing',
    'problem': [
      { 'title': 'Graph - terminology(Theory)', 'id': 10 },
      { 'title': 'Build a Graph using Array', 'id': 10 },
      { 'title': 'Build a Graph  using Linkedlist', 'id': 10 },
      { 'title': 'Traversing using BFS and DFS', 'id': 10 },
      { 'title': 'Minimum Spaning tree: Prims and Kruskal', 'id': 10 },
      { 'title': 'Sorted Distance: Single Source and All pair', 'id': 10 },
      { 'title': 'Serach a node in a Graph', 'id': 10,'tag':'homework' },
      { 'title': 'Graph to Tree', 'id': 10,'tag':'homework' },   
      { 'title': 'Implemenmt Amazon Recomendation Graph', 'id': 10,'tag':'puzzle' },
    ]
  },
  {
    'chapter': 'Recursion',
    'problem': [
      { 'title': 'Graph - terminology(Theory)', 'id': 10 },
      { 'title': 'Build a Graph using Array', 'id': 10 },
      { 'title': 'Build a Graph  using Linkedlist', 'id': 10 },
      { 'title': 'Traversing using BFS and DFS', 'id': 10 },
      { 'title': 'Minimum Spaning tree: Prims and Kruskal', 'id': 10 },
      { 'title': 'Sorted Distance: Single Source and All pair', 'id': 10 },
      { 'title': 'Serach a node in a Graph', 'id': 10,'tag':'homework' },
      { 'title': 'Graph to Tree', 'id': 10,'tag':'homework' },   
      { 'title': 'Implemenmt Amazon Recomendation Graph', 'id': 10,'tag':'puzzle' },
    ]
  },
  {
    'chapter': 'BackTracking',
    'problem': [
      { 'title': 'Graph - terminology(Theory)', 'id': 10 },
      { 'title': 'Build a Graph using Array', 'id': 10 },
      { 'title': 'Build a Graph  using Linkedlist', 'id': 10 },
      { 'title': 'Traversing using BFS and DFS', 'id': 10 },
      { 'title': 'Minimum Spaning tree: Prims and Kruskal', 'id': 10 },
      { 'title': 'Sorted Distance: Single Source and All pair', 'id': 10 },
      { 'title': 'Serach a node in a Graph', 'id': 10,'tag':'homework' },
      { 'title': 'Graph to Tree', 'id': 10,'tag':'homework' },   
      { 'title': 'Implemenmt Amazon Recomendation Graph', 'id': 10,'tag':'puzzle' },
    ]
  },
  {
    'chapter': 'Devide and Conquere',
    'problem': [
      { 'title': 'Graph - terminology(Theory)', 'id': 10 },
      { 'title': 'Build a Graph using Array', 'id': 10 },
      { 'title': 'Build a Graph  using Linkedlist', 'id': 10 },
      { 'title': 'Traversing using BFS and DFS', 'id': 10 },
      { 'title': 'Minimum Spaning tree: Prims and Kruskal', 'id': 10 },
      { 'title': 'Sorted Distance: Single Source and All pair', 'id': 10 },
      { 'title': 'Serach a node in a Graph', 'id': 10,'tag':'homework' },
      { 'title': 'Graph to Tree', 'id': 10,'tag':'homework' },   
      { 'title': 'Implemenmt Amazon Recomendation Graph', 'id': 10,'tag':'puzzle' },
    ]
  },
  {
    'chapter': 'Dynamic Programming',
    'problem': [
      { 'title': 'Graph - terminology(Theory)', 'id': 10 },
      { 'title': 'Build a Graph using Array', 'id': 10 },
      { 'title': 'Build a Graph  using Linkedlist', 'id': 10 },
      { 'title': 'Traversing using BFS and DFS', 'id': 10 },
      { 'title': 'Minimum Spaning tree: Prims and Kruskal', 'id': 10 },
      { 'title': 'Sorted Distance: Single Source and All pair', 'id': 10 },
      { 'title': 'Serach a node in a Graph', 'id': 10,'tag':'homework' },
      { 'title': 'Graph to Tree', 'id': 10,'tag':'homework' },   
      { 'title': 'Implemenmt Amazon Recomendation Graph', 'id': 10,'tag':'puzzle' },
    ]
  },
  {
    'chapter': 'Greedy',
    'problem': [
      { 'title': 'Graph - terminology(Theory)', 'id': 10 },
      { 'title': 'Build a Graph using Array', 'id': 10 },
      { 'title': 'Build a Graph  using Linkedlist', 'id': 10 },
      { 'title': 'Traversing using BFS and DFS', 'id': 10 },
      { 'title': 'Minimum Spaning tree: Prims and Kruskal', 'id': 10 },
      { 'title': 'Sorted Distance: Single Source and All pair', 'id': 10 },
      { 'title': 'Serach a node in a Graph', 'id': 10,'tag':'homework' },
      { 'title': 'Graph to Tree', 'id': 10,'tag':'homework' },   
      { 'title': 'Implemenmt Amazon Recomendation Graph', 'id': 10,'tag':'puzzle' },
    ]
  },
  {
    'chapter': 'Probablity',
    'problem': [
      { 'title': 'Graph - terminology(Theory)', 'id': 10 },
      { 'title': 'Build a Graph using Array', 'id': 10 },
      { 'title': 'Build a Graph  using Linkedlist', 'id': 10 },
      { 'title': 'Traversing using BFS and DFS', 'id': 10 },
      { 'title': 'Minimum Spaning tree: Prims and Kruskal', 'id': 10 },
      { 'title': 'Sorted Distance: Single Source and All pair', 'id': 10 },
      { 'title': 'Serach a node in a Graph', 'id': 10,'tag':'homework' },
      { 'title': 'Graph to Tree', 'id': 10,'tag':'homework' },   
      { 'title': 'Implemenmt Amazon Recomendation Graph', 'id': 10,'tag':'puzzle' },
    ]
  },
  {
    'chapter': 'Computinal Geometry',
    'problem': [
      { 'title': 'Graph - terminology(Theory)', 'id': 10 },
      { 'title': 'Build a Graph using Array', 'id': 10 },
      { 'title': 'Build a Graph  using Linkedlist', 'id': 10 },
      { 'title': 'Traversing using BFS and DFS', 'id': 10 },
      { 'title': 'Minimum Spaning tree: Prims and Kruskal', 'id': 10 },
      { 'title': 'Sorted Distance: Single Source and All pair', 'id': 10 },
      { 'title': 'Serach a node in a Graph', 'id': 10,'tag':'homework' },
      { 'title': 'Graph to Tree', 'id': 10,'tag':'homework' },   
      { 'title': 'Implemenmt Amazon Recomendation Graph', 'id': 10,'tag':'puzzle' },
    ]
  },
]  
} 
 
/* Android Tutorials*/
    
android = [ //TODO CHNAGE THE FORMAT
  {
    'chapter': 'Android Basic',
    'problem': [
      { 'title': 'Android OverView and Architecture', 'id': 10 },
      { 'title': 'Seeting up your environment', 'id': 10 },
      { 'title': 'Writing a Hello World Application', 'id': 10 },
      { 'title': 'Activity and Its Life cycle Example', 'id': 10 },
      { 'title': 'Services and Its PLM with example', 'id': 10 },
      { 'title': 'Broadcast Receivers and its PLM', 'id': 10 },
      { 'title': 'Content Providers with Example', 'id': 10 },  
      { 'title': 'Fragments and its  PLM Example', 'id': 10 },   
    ]
  },
  {
    'chapter': 'UI Framework',
    'problem': [        
      { 'title': 'Layouts Linear ', 'id': 10 },
      { 'title': 'RelativeLayout ', 'id': 10 },
      { 'title': 'TableLayout  ', 'id': 10 },
      { 'title': 'AbsoluteLayout  ', 'id': 10 },
      { 'title': 'FrameLayout  ', 'id': 10 },
      { 'title': 'ListView   ', 'id': 10 },
      { 'title': 'GridView   ', 'id': 10 },
      { 'title': 'UI Controls ', 'id': 10 },
      { 'title': 'UI Auto Complete  ', 'id': 10 },
      { 'title': 'View and View Grpup ', 'id': 10 },  
      { 'title': 'Custom View', 'id': 10 },       
      { 'title': 'Build View at RunTime', 'id': 10 },        
      { 'title': 'Styles ', 'id': 10 },
      { 'title': 'Theme ', 'id': 10 },
      { 'title': 'Custom Fonts', 'id': 10 },
      { 'title': 'Image Effects', 'id': 10 },
      { 'title': 'Image Switcher', 'id': 10 },
      { 'title': 'Styling the colour palette', 'id': 10 },
      { 'title': 'Notifications: Toast  ', 'id': 10 },
      { 'title': 'Notifications: Notification Builder  ', 'id': 10 },
      { 'title': 'Notifications: Dialog Builder/Alert   ', 'id': 10 },
      { 'title': 'Notifications: Loading Spinner', 'id': 10 },
      { 'title': 'Notifications: Progress Circle-Overlay', 'id': 10 },
      { 'title': 'Notifications: Progress Bar using ProgressDialog', 'id': 10 },
      { 'title': 'Notifications: Push Notification', 'id': 10 },
      { 'title': 'Animation: Tween Animation', 'id': 10 },
      { 'title': 'Animation: Frame Animation', 'id': 10 },
      { 'title': 'Player: Audio/MediaPlayer ', 'id': 10 },
      { 'title': 'Player: Video', 'id': 10 },
      { 'title': 'Player: Image SlideShow', 'id': 10 },
      { 'title': 'Navigation : Menu bar', 'id': 10 },
      { 'title': 'Navigation : Side Menu bar', 'id': 10 },

      
      { 'title': 'Merge two linkedlist', 'id': 10 },
      { 'title': 'Rotate a Linked-list', 'id': 10 },
    ]
  },
  {
    'chapter': 'Android Inputs',
    'problem': [
      { 'title': 'Event:Event Handler & Event Listener', 'id': 10 },
      { 'title': 'allEvents:onClick/onLongClick/onFocusChange/onKey/onTouch', 'id': 10 },
      { 'title': 'Event - Touch Event', 'id': 10 },
      { 'title': 'Event - Touch Framework', 'id': 10 },
      { 'title': 'Event - Focus Framework', 'id': 10 },
      { 'title': 'Event - Drag and Drop Framework', 'id': 10 },      
      { 'title': 'Event - Spelling Checker Framework', 'id': 10 },      
      { 'title': 'Intent - sendBroadcast', 'id': 10 },
      { 'title': 'Intent - Intent Filters ( Power To handle)', 'id': 10 },
      { 'title': 'ClipboardManager: CCP ', 'id': 10 },
      { 'title': 'Gestures :  Overview' , 'id': 10 },
      { 'title': 'Gestures :  Pinch Gesture' , 'id': 10 },
      { 'title': 'Gestures :  Zoom' , 'id': 10 },
      { 'title': 'Gestures :  Move left/Right' , 'id': 10 },
      { 'title': 'Gestures :  Pinch Gesture' , 'id': 10 },
      { 'title': 'Multitouch :  Overview' , 'id': 10 },

    ]
  },
  {
    'chapter': 'Android Messaging',
    'problem': [
      { 'title': 'Intent - a messgae', 'id': 10 },
      { 'title': 'Intent - startActivity', 'id': 10 },
      { 'title': 'Intent - startService', 'id': 10 },
      { 'title': 'Intent - sendBroadcast', 'id': 10 },
      { 'title': 'Intent - Intent Filters ( Power To handle)', 'id': 10 },
      { 'title': 'Storage  - Internal Storage', 'id': 10 },
      { 'title': 'Storage  - SQLite ', 'id': 10 },
      { 'title': 'Storage  - Internal Storage', 'id': 10 },
      
      
      
    ]
  },
  {
    'chapter': 'External Services',
    'problem': [
      { 'title': 'Location Based Services', 'id': 10 },
      { 'title': 'Implement Queue using Linkedlist', 'id': 10 },
      { 'title': 'Sending Email', 'id': 10 },
      { 'title': 'Sending SMS', 'id': 10 },
      { 'title': 'Phone Calls', 'id': 10 },
      { 'title': 'Audio Capture/Manager', 'id': 10 },
      { 'title': 'Video Capture', 'id': 10 },
      { 'title': 'Picture Capture/Camera ', 'id': 10 },
      { 'title': 'BatteryManager', 'id': 10 },
      { 'title': 'Bluetooth ', 'id': 10 },
      { 'title': 'Google API Login ', 'id': 10 },
      { 'title': 'Facebook Integration ', 'id': 10 },
      { 'title': 'LinkedIn Integration ', 'id': 10 },
      { 'title': 'GMap Integration ', 'id': 10 },
      { 'title': 'Json Parser Integration ', 'id': 10 },
      { 'title': 'Network Connection  ', 'id': 10 },
      { 'title': 'Sensors  Tutorial  ', 'id': 10 },
      { 'title': 'Session:  Shared Preferences  ', 'id': 10 },
      { 'title': 'Session: SIP Protocol  ', 'id': 10 },
      { 'TTS': 'Text To Speech ', 'id': 10 },
      { 'TTS': 'Vvide Recognization ', 'id': 10 },
      
      
    ]
  },
  {
    'chapter': 'Advance Tutorial',
    'problem': [
      { 'title': 'Background jobs:Services ', 'id': 10 },
      { 'title': 'Background jobs:AsyncTask  ', 'id': 10 },
      { 'title': 'Localization', 'id': 10 },
      { 'title': 'Start Screen', 'id': 10 },
      { 'title': 'Custom keyBoard', 'id': 10 },
      { 'title': 'Screen Cast', 'id': 10 },

    ]
  },
]  
 
/**************************************************************************
    I N T E R V I E W   D A T A
*********************************************************************/
var INTERVIEW_DATA = {
    name:'Mock Programming Interview',
    organizar :'Haldia Institute of Technology',
    organizar_email :'dutta.dipankar08@gmail.com',
    condidate_id:10,
    instraction:'Welcome to PeerReview!<br><br>Please read the below instraction crefully before preding interview!<br><br>\
    1. This is a Mock Interview - A perfact way to validate your potentail and your problem solving skill, It is nowhare realted to actual interview process which offers a Job.<br><br>\
    2. Please make sure your microphone and speaker are working fine. It will avoid distracbence during the interview process.<br></br>\
    3. You will going to have one to three technical programming problems. You need to design the algorithm and ending with writing some code snappit. </br><br>\
    4. Your academic exprience matters ! You shoud have a knowlege of basic datastructe, algorithm and mathematics. You will be need this skill to solve your problem.<br><br>\
    5. Show your problem solving ability! Good engineers will come up with a solution, but great engineers will come up with several solutions, weigh them carefully, and choose the best solution for the given context. So as you are running mock questions, challenge yourself to keep thinking even after you have a first solution. See how many solutions you can come up with. This will grow your ability to quickly see multiple ways to solve a problem, so you can figure out the best solution.<br><br>\
    6. Write clean code is a art! Your code must respect standard coding guideline.<br><br>\
    Best of luck !\
    ',
    duration :45,
    hash:'KKKK',
    question_set : [
        {id:10,
        name:'Palindrome Check',
        desc:'A string is called a Palindrome if it is spelled the same forward and backward. Following are some\ examples of palindrome strings: Madam, Noon, Rotor, Rotator, Radar, Malayalam\. Write a C program to findout whether a string is palindrome or not! <br> For Example, if the input string is "Dipankar", your function return false, whereas for input string "MADAM", your function to return true.',           
        sol:'#include<stdio.h>\nint isPalindrome(){\n    //Write your code here...\n}\n\nint main(){\n    char str[]="MADAM";\n    printf("isPlaindrome: %s: %d",str,isPalindrome(str)?1:0);\n}\n',
        hash:'ttuv'
        }, 
        
        {id:10,
        name:'Palindrome',
        desc:'A string is called a Palindrome if it is spelled the same forward and backward. Following are some\ examples of palindrome strings: Madam, Noon, Rotor, Rotator, Radar, Malayalam\. Write a C program to findout whether a string is palindrome or not! <br> For Example, if the input string is "Dipankar", your function return false, whereas for input string "MADAM", your function to return true.',           
        sol:'\n#include<stdio.h>\nint isPalindrome(){\n    //Write your code here...\n}\n\nint main(){\n    char str[]="MADAM";\n    printf("isPlaindrome: %s: %d",str,isPalindrome(str)?1:0);\n}\n',
        hash:'ttuv'
        },
        {id:10,
        name:'Palindrome',
        desc:'A string is called a Palindrome if it is spelled the same forward and backward. Following are some\ examples of palindrome strings: Madam, Noon, Rotor, Rotator, Radar, Malayalam\. Write a C program to findout whether a string is palindrome or not! <br> For Example, if the input string is "Dipankar", your function return false, whereas for input string "MADAM", your function to return true.',           
        sol:'#include<stdio.h>\nint isPalindrome(){\n    //Write your code here...\n}\n\nint main(){\n    char str[]="MADAM";\n    printf("isPlaindrome: %s: %d",str,isPalindrome(str)?1:0);\n}\n',
        hash:'ttuv'
        },
        
]
}

