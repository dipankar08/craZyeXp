function buildTOC(sample,blen){
    var html =''
    html+='<div class="multilist">'
    
    html+='<div class="menu" ><ul id="menu">'
    for (i=0;i<sample.length;i++){
        x = sample[i];
        if( i == 0 )
            html+='<li class="active" onclick="autoDetectToggleSilde(this,\'#pages\')">'+x.chapter+' </li>'
        else
            html+='<li onclick="autoDetectToggleSilde(this,\'#pages\')">'+x.chapter+' </li>'
    }
    html+='</ul></div>'
    
    html+= '<div class="pages" id="pages">'
    for (i=0;i<sample.length;i++){
        x = sample[i];  
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
    $('#tocf').html(buildTOC(data,7));
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

sample = [
  {
    'chapter': 'title1',
    'problem': [
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      }
    ]
  },
  {
    'chapter': 'title1',
    'problem': [
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      }
    ]
  },
  {
    'chapter': 'title1',
    'problem': [
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      }
    ]
  },
  {
    'chapter': 'title1',
    'problem': [
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      }
    ]
  },
  {
    'chapter': 'title1',
    'problem': [
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      }
    ]
  },
  {
    'chapter': 'title1',
    'problem': [
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      }
    ]
  },
  {
    'chapter': 'title1',
    'problem': [
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      }
    ]
  },
  {
    'chapter': 'title1',
    'problem': [
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      }
    ]
  }
]

// DataStructure 1.
ds1 = [
  {
    'chapter': 'Introduction',
    'problem': [
      {
        'title': 'Concept of DataStructure',
        'id': 10
      },
      {
        'title': 'Application of DataStructure',
        'id': 10
      },
      {
        'title': 'Clasification of DataStructure',
        'id': 10
      },
      {
        'title': 'Linier DataStructure',
        'id': 10
      },
      {
        'title': 'Non Lenear DataStructure',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      }
    ]
  },
  {
    'chapter': 'Array',
    'problem': [
      {
        'title': 'Concept of Arry,,',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      }
    ]
  },
  {
    'chapter': 'Linked List',
    'problem': [
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      }
    ]
  },
  {
    'chapter': 'Stack',
    'problem': [
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      }
    ]
  },
  {
    'chapter': 'Queue',
    'problem': [
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      }
    ]
  },
  {
    'chapter': 'Tree',
    'problem': [
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      }
    ]
  },
  {
    'chapter': 'Graph',
    'problem': [
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      }
    ]
  },
  {
    'chapter': 'Hash/Tables',
    'problem': [
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      },
      {
        'title': 'one line description about problem',
        'id': 10
      }
    ]
  }
]

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

