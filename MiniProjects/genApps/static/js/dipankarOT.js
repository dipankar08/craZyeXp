/*********************************
 After serach a lot I decide  to write my own Operational Trsformbation chnage set library.,
 It should support:
 1. Crete OT diff
   a) Line by Line Diff to support line merge.
   b) Should have word offset
   c) Easy and fast merge.
 2. Apply OT to a text with uneven length
 3. [EX] Versioning
 4. [Ex] Serialization of chnage set.
 Dependency : 
**********************************/
/*
function dipankarOT(ops) {
  this.line_chnage_count=0
  this.lines =[]
  
  //define methods on lines
  this.addLineChange = function(lc){ this.lines.push(lc)}
  this.print =  function(){
    console.log('Here is the change set:')
    for (i = 0; i < lines.length; i++) { 
      console.log(lines[i])
    }
  }
  
  // buildLineDiff: Will generate our Own way to line diff.
  // output: An array of operation [..ops]
  // Ops =[operation,next/prev efefcted word, old cur index]
  
  this.buildLineDiff = function(line1,line2,mode){
    var dmp = new diff_match_patch();
    if (mode=='word'){
       diff = dmp.diff_main(line1, line2);//TBD
    }
    else{
      diff = dmp.diff_main(line1, line2);
    }
    console.log(diff)
    
    var DIFF_DELETE = -1;
    var DIFF_INSERT = 1;
    var DIFF_EQUAL = 0;
    
    var ops = [],curlen = 0;
    char_count_change=0;
    diff.forEach(function(d) {
      
      curlen+= d[1].length;
      
      if (DIFF_DELETE == d[0]) {
        ops.push({a:'del',el:d[1].length,cl:curlen,w:d[1]})
        char_count_change -= d[1].length;
      }      
      if (DIFF_INSERT == d[0]) {
        ops.push({a:'ins',el:d[1].length,cl:curlen,w:d[1]})
        char_count_change += d[1].length;
      }      
      if(DIFF_EQUAL == d[0]) {
       ops.push({a:'skip',el:d[1].length,cl:curlen,w:d[1]})
      }
    })
    if(line1.length+char_count_change != line2.length){console.log("Warn: Diff Generation failed!");}
    
    return { ops:ops,char_count_change:char_count_change,old_len:line1.length,new_len:line1.length+char_count_change};
    // Ops =[operation,next/prev efefcted word, old cur index]
  }
  
// this is my Merge Algorithm
// TBD
//  
//
  this.mergeToLine = function(old_line,diff,option='fource'){
    if(old_line.length != diff.old_len){
      console.log('Warn:[OldTextChange]# old text length doent match with line length');
    }
    old_max_len = old_line.length
    new_line=''
    new_line_len=0
    old_idx=0;
    diff.ops.forEach(function(op) {
      if (op.a == 'skip') {
        new_line += old_line.substring(old_idx,op.el+1)
        old_idx += op.el;
      }
      if (op.a == 'ins') {
        new_line += op.w;
      }
      if (op.a == 'del') {
        old_idx+=op.el; //ignore this part.. increase old index.
      }
    })
    new_line += old_line.substring(old_idx,old_line.length)
    //TODO -validation.
    return new_line
  
  }
  
  
}
//Unit Test Here..
t1 = 'I am don '
t2 = 'i am hanuman'
dot=new dipankarOT()
df = dot.buildLineDiff(t1,t2)
console.log(df)
t3= 'I am don '
dot.mergeToLine(t3,df)
*/