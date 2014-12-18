
/*------------------------------------------------------------
sample.js
Author: Dipankar dutta
This is a auto-generated Js file, implements the following feature:
- create a app and controller to access the data
- acces the API usinh $http angular js Services

------------------------------------------------------------*/
/**** Create ****/ 

var myApp = angular.module("myApp", []);

/******* helper function *******/
myApp.filter('range', function() {
  return function(input, total) {
    total = parseInt(total);
    for (var i=0; i<total; i++)
      input.push(i);
    return input;
  };
});
/******* end of helper function *******/






  
/************ start of Parent Controller*****************/
myApp.controller("ParentController",  function ($scope,$http,$sce) { 

    $scope.renderHtml = function (htmlCode) {
            return $sce.trustAsHtml(htmlCode);
    };
/************ Initialize all Data Variable. *****************/
$scope.item ={}
$scope.item_list ={}
$scope.ref_list_items =[]
$scope.limit=10;

$scope.quick_search={'in':'','out':''}


/*********************  get MiniView *****************/
$scope.getMiniView=function(a) {
  $http.get("/api/parent/?page="+a+"&limit="+$scope.limit+"")
      .success(function(data, status, headers, config) {
        console.log(data)
        $scope.item_list = data.res;
        // DONT DO THIS BAD USER EXP$scope.status = data.status; $scope.msg=data.msg
        $scope.orderByField = 'id';
        $scope.reverseSort = false;
       // Not incduing this feature tableResize('#table_miniview_Parent');
      })
      .error(function(data, status, headers, config) { console.log('Error happen with status:'+status) });  
}
$scope.getMiniView(1);
/************ getting full data for an Item *****************/
$scope.getItem = function(a) {
     $http.get("/api/parent/"+a+"/")
    .success(function(data, status, headers, config) {
      console.log(data)
      $scope.item = data.res;
      $scope.status = data.status; $scope.msg=data.msg
    })
    .error(function(data, status, headers, config) {console.log('Error happen with status:'+status)}); 
  }

/************ creating a new Item  *****************/
$scope.createItem = function(a) {
    console.log($('form#parent').serialize())
    $http({
          method: "post",
          url: '/api/parent/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#parent').serialize()
    })
    .success(function(data, status, headers, config) {
     $scope.status = data.status; $scope.msg=data.msg
     console.log(data)
     $scope.getMiniView(1);
    })
    .error(function(data, status, headers, config) {

    }); 
}

/************ Updating an Item data  *****************/
$scope.updateItem = function(a) {
    if($scope.item.id == null)
    {
     $scope.status = 'error'; $scope.msg=' Please select a raw in left panel to update';
     return;
    }
    $http({
          method: "post",
          url: '/api/parent/'+$scope.item.id+'/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#parent').serialize()
    })
    .success(function(data, status, headers, config) {
     $scope.status = data.status; $scope.msg=data.msg
     console.log(data);
     $scope.getMiniView(1);
    })
    .error(function(data, status, headers, config) {
    }); 
}

/************ delete an Item data  *****************/
$scope.deleteItem = function(a){
  $http.delete("/api/parent/"+a+"/")
      .success(function(data, status, headers, config) {
        $scope.item_list = data;
        $scope.status = data.status; $scope.msg=data.msg
        console.log(data);
        $scope.getMiniView(1);
      })
      .error(function(data, status, headers, config) {
        console.log('Error happen with status:'+status)
      });  
}

/*************** reset an item<used in form>***********************/
$scope.resetItem = function() {
  $scope.getItem($scope.item.id)
}


$scope.getStudent = function(a) {
     $http.get("/api/parent/"+a+"/student/")
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = data.res;
      $scope.ref_list_items = {};
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#o2o-parent','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }


$scope.qsStudent= function(a) {
     $http.get("/api/parent/qs/?q="+$scope.quick_search.in)
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.quick_search.out= data.res;
      $scope.status = data.status; $scope.msg=data.msg
      //addClass('#m2m-parent','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }



});
/************ End of Parent Controller*****************/


  
/************ start of Employee Controller*****************/
myApp.controller("EmployeeController",  function ($scope,$http,$sce) { 

    $scope.renderHtml = function (htmlCode) {
            return $sce.trustAsHtml(htmlCode);
    };
/************ Initialize all Data Variable. *****************/
$scope.item ={}
$scope.item_list ={}
$scope.ref_list_items =[]
$scope.limit=10;

$scope.quick_search={'in':'','out':''}


/*********************  get MiniView *****************/
$scope.getMiniView=function(a) {
  $http.get("/api/employee/?page="+a+"&limit="+$scope.limit+"")
      .success(function(data, status, headers, config) {
        console.log(data)
        $scope.item_list = data.res;
        // DONT DO THIS BAD USER EXP$scope.status = data.status; $scope.msg=data.msg
        $scope.orderByField = 'id';
        $scope.reverseSort = false;
       // Not incduing this feature tableResize('#table_miniview_Employee');
      })
      .error(function(data, status, headers, config) { console.log('Error happen with status:'+status) });  
}
$scope.getMiniView(1);
/************ getting full data for an Item *****************/
$scope.getItem = function(a) {
     $http.get("/api/employee/"+a+"/")
    .success(function(data, status, headers, config) {
      console.log(data)
      $scope.item = data.res;
      $scope.status = data.status; $scope.msg=data.msg
    })
    .error(function(data, status, headers, config) {console.log('Error happen with status:'+status)}); 
  }

/************ creating a new Item  *****************/
$scope.createItem = function(a) {
    console.log($('form#employee').serialize())
    $http({
          method: "post",
          url: '/api/employee/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#employee').serialize()
    })
    .success(function(data, status, headers, config) {
     $scope.status = data.status; $scope.msg=data.msg
     console.log(data)
     $scope.getMiniView(1);
    })
    .error(function(data, status, headers, config) {

    }); 
}

/************ Updating an Item data  *****************/
$scope.updateItem = function(a) {
    if($scope.item.id == null)
    {
     $scope.status = 'error'; $scope.msg=' Please select a raw in left panel to update';
     return;
    }
    $http({
          method: "post",
          url: '/api/employee/'+$scope.item.id+'/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#employee').serialize()
    })
    .success(function(data, status, headers, config) {
     $scope.status = data.status; $scope.msg=data.msg
     console.log(data);
     $scope.getMiniView(1);
    })
    .error(function(data, status, headers, config) {
    }); 
}

/************ delete an Item data  *****************/
$scope.deleteItem = function(a){
  $http.delete("/api/employee/"+a+"/")
      .success(function(data, status, headers, config) {
        $scope.item_list = data;
        $scope.status = data.status; $scope.msg=data.msg
        console.log(data);
        $scope.getMiniView(1);
      })
      .error(function(data, status, headers, config) {
        console.log('Error happen with status:'+status)
      });  
}

/*************** reset an item<used in form>***********************/
$scope.resetItem = function() {
  $scope.getItem($scope.item.id)
}


$scope.getSubject = function(a) {
     $http.get("/api/employee/"+a+"/subject/")
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = data.res;
      $scope.ref_list_items = {};
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#o2o-employee','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }


$scope.getMyClass = function(a) {
     $http.get("/api/employee/"+a+"/myclass/")
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = data.res;
      $scope.ref_list_items = {};
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#o2o-employee','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }


$scope.getExam = function(a) {
     $http.get("/api/employee/"+a+"/exam/")
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = data.res;
      $scope.ref_list_items = {};
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#o2o-employee','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }


$scope.qsExam= function(a) {
     $http.get("/api/employee/qs/?q="+$scope.quick_search.in)
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.quick_search.out= data.res;
      $scope.status = data.status; $scope.msg=data.msg
      //addClass('#m2m-employee','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }



});
/************ End of Employee Controller*****************/


  
/************ start of Subject Controller*****************/
myApp.controller("SubjectController",  function ($scope,$http,$sce) { 

    $scope.renderHtml = function (htmlCode) {
            return $sce.trustAsHtml(htmlCode);
    };
/************ Initialize all Data Variable. *****************/
$scope.item ={}
$scope.item_list ={}
$scope.ref_list_items =[]
$scope.limit=10;

$scope.quick_search={'in':'','out':''}


/*********************  get MiniView *****************/
$scope.getMiniView=function(a) {
  $http.get("/api/subject/?page="+a+"&limit="+$scope.limit+"")
      .success(function(data, status, headers, config) {
        console.log(data)
        $scope.item_list = data.res;
        // DONT DO THIS BAD USER EXP$scope.status = data.status; $scope.msg=data.msg
        $scope.orderByField = 'id';
        $scope.reverseSort = false;
       // Not incduing this feature tableResize('#table_miniview_Subject');
      })
      .error(function(data, status, headers, config) { console.log('Error happen with status:'+status) });  
}
$scope.getMiniView(1);
/************ getting full data for an Item *****************/
$scope.getItem = function(a) {
     $http.get("/api/subject/"+a+"/")
    .success(function(data, status, headers, config) {
      console.log(data)
      $scope.item = data.res;
      $scope.status = data.status; $scope.msg=data.msg
    })
    .error(function(data, status, headers, config) {console.log('Error happen with status:'+status)}); 
  }

/************ creating a new Item  *****************/
$scope.createItem = function(a) {
    console.log($('form#subject').serialize())
    $http({
          method: "post",
          url: '/api/subject/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#subject').serialize()
    })
    .success(function(data, status, headers, config) {
     $scope.status = data.status; $scope.msg=data.msg
     console.log(data)
     $scope.getMiniView(1);
    })
    .error(function(data, status, headers, config) {

    }); 
}

/************ Updating an Item data  *****************/
$scope.updateItem = function(a) {
    if($scope.item.id == null)
    {
     $scope.status = 'error'; $scope.msg=' Please select a raw in left panel to update';
     return;
    }
    $http({
          method: "post",
          url: '/api/subject/'+$scope.item.id+'/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#subject').serialize()
    })
    .success(function(data, status, headers, config) {
     $scope.status = data.status; $scope.msg=data.msg
     console.log(data);
     $scope.getMiniView(1);
    })
    .error(function(data, status, headers, config) {
    }); 
}

/************ delete an Item data  *****************/
$scope.deleteItem = function(a){
  $http.delete("/api/subject/"+a+"/")
      .success(function(data, status, headers, config) {
        $scope.item_list = data;
        $scope.status = data.status; $scope.msg=data.msg
        console.log(data);
        $scope.getMiniView(1);
      })
      .error(function(data, status, headers, config) {
        console.log('Error happen with status:'+status)
      });  
}

/*************** reset an item<used in form>***********************/
$scope.resetItem = function() {
  $scope.getItem($scope.item.id)
}


$scope.getMyClass = function(a) {
     $http.get("/api/subject/"+a+"/myclass/")
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = data.res;
      $scope.ref_list_items = {};
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#o2o-subject','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }


$scope.getExam = function(a) {
     $http.get("/api/subject/"+a+"/exam/")
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = data.res;
      $scope.ref_list_items = {};
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#o2o-subject','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }


$scope.getMark = function(a) {
     $http.get("/api/subject/"+a+"/mark/")
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = data.res;
      $scope.ref_list_items = {};
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#o2o-subject','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }


//Get
$scope.getEmployee= function(a) {
     $http.get("/api/subject/"+a+"/employee/")
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = {}
      $scope.ref_list_items = data.res;
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#m2m-subject','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }
//Add + remove
$scope.addEmployee= function(a,b,c) {
    $http({
          method: "post",
          url: "/api/subject/"+a+"/employee/",
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:{employee: b, action: c}
    })
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = {}
      $scope.ref_list_items = data.res;
      $scope.status = data.status; $scope.msg=data.msg
     
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
    //repopulate..
    $scope.getEmployee;
  }


$scope.qsEmployee= function(a) {
     $http.get("/api/subject/qs/?q="+$scope.quick_search.in)
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.quick_search.out= data.res;
      $scope.status = data.status; $scope.msg=data.msg
      //addClass('#m2m-subject','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }



});
/************ End of Subject Controller*****************/


  
/************ start of MyClass Controller*****************/
myApp.controller("MyClassController",  function ($scope,$http,$sce) { 

    $scope.renderHtml = function (htmlCode) {
            return $sce.trustAsHtml(htmlCode);
    };
/************ Initialize all Data Variable. *****************/
$scope.item ={}
$scope.item_list ={}
$scope.ref_list_items =[]
$scope.limit=10;

$scope.quick_search={'in':'','out':''}


/*********************  get MiniView *****************/
$scope.getMiniView=function(a) {
  $http.get("/api/myclass/?page="+a+"&limit="+$scope.limit+"")
      .success(function(data, status, headers, config) {
        console.log(data)
        $scope.item_list = data.res;
        // DONT DO THIS BAD USER EXP$scope.status = data.status; $scope.msg=data.msg
        $scope.orderByField = 'id';
        $scope.reverseSort = false;
       // Not incduing this feature tableResize('#table_miniview_MyClass');
      })
      .error(function(data, status, headers, config) { console.log('Error happen with status:'+status) });  
}
$scope.getMiniView(1);
/************ getting full data for an Item *****************/
$scope.getItem = function(a) {
     $http.get("/api/myclass/"+a+"/")
    .success(function(data, status, headers, config) {
      console.log(data)
      $scope.item = data.res;
      $scope.status = data.status; $scope.msg=data.msg
    })
    .error(function(data, status, headers, config) {console.log('Error happen with status:'+status)}); 
  }

/************ creating a new Item  *****************/
$scope.createItem = function(a) {
    console.log($('form#myclass').serialize())
    $http({
          method: "post",
          url: '/api/myclass/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#myclass').serialize()
    })
    .success(function(data, status, headers, config) {
     $scope.status = data.status; $scope.msg=data.msg
     console.log(data)
     $scope.getMiniView(1);
    })
    .error(function(data, status, headers, config) {

    }); 
}

/************ Updating an Item data  *****************/
$scope.updateItem = function(a) {
    if($scope.item.id == null)
    {
     $scope.status = 'error'; $scope.msg=' Please select a raw in left panel to update';
     return;
    }
    $http({
          method: "post",
          url: '/api/myclass/'+$scope.item.id+'/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#myclass').serialize()
    })
    .success(function(data, status, headers, config) {
     $scope.status = data.status; $scope.msg=data.msg
     console.log(data);
     $scope.getMiniView(1);
    })
    .error(function(data, status, headers, config) {
    }); 
}

/************ delete an Item data  *****************/
$scope.deleteItem = function(a){
  $http.delete("/api/myclass/"+a+"/")
      .success(function(data, status, headers, config) {
        $scope.item_list = data;
        $scope.status = data.status; $scope.msg=data.msg
        console.log(data);
        $scope.getMiniView(1);
      })
      .error(function(data, status, headers, config) {
        console.log('Error happen with status:'+status)
      });  
}

/*************** reset an item<used in form>***********************/
$scope.resetItem = function() {
  $scope.getItem($scope.item.id)
}


$scope.getStudent = function(a) {
     $http.get("/api/myclass/"+a+"/student/")
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = data.res;
      $scope.ref_list_items = {};
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#o2o-myclass','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }


$scope.getAttendance = function(a) {
     $http.get("/api/myclass/"+a+"/attendance/")
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = data.res;
      $scope.ref_list_items = {};
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#o2o-myclass','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }


//Get
$scope.getEmployee= function(a) {
     $http.get("/api/myclass/"+a+"/employee/")
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = {}
      $scope.ref_list_items = data.res;
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#m2m-myclass','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }
//Add + remove
$scope.addEmployee= function(a,b,c) {
    $http({
          method: "post",
          url: "/api/myclass/"+a+"/employee/",
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:{employee: b, action: c}
    })
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = {}
      $scope.ref_list_items = data.res;
      $scope.status = data.status; $scope.msg=data.msg
     
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
    //repopulate..
    $scope.getEmployee;
  }


//Get
$scope.getSubject= function(a) {
     $http.get("/api/myclass/"+a+"/subject/")
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = {}
      $scope.ref_list_items = data.res;
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#m2m-myclass','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }
//Add + remove
$scope.addSubject= function(a,b,c) {
    $http({
          method: "post",
          url: "/api/myclass/"+a+"/subject/",
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:{subject: b, action: c}
    })
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = {}
      $scope.ref_list_items = data.res;
      $scope.status = data.status; $scope.msg=data.msg
     
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
    //repopulate..
    $scope.getSubject;
  }


$scope.qsSubject= function(a) {
     $http.get("/api/myclass/qs/?q="+$scope.quick_search.in)
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.quick_search.out= data.res;
      $scope.status = data.status; $scope.msg=data.msg
      //addClass('#m2m-myclass','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }



});
/************ End of MyClass Controller*****************/


  
/************ start of Exam Controller*****************/
myApp.controller("ExamController",  function ($scope,$http,$sce) { 

    $scope.renderHtml = function (htmlCode) {
            return $sce.trustAsHtml(htmlCode);
    };
/************ Initialize all Data Variable. *****************/
$scope.item ={}
$scope.item_list ={}
$scope.ref_list_items =[]
$scope.limit=10;

$scope.quick_search={'in':'','out':''}


/*********************  get MiniView *****************/
$scope.getMiniView=function(a) {
  $http.get("/api/exam/?page="+a+"&limit="+$scope.limit+"")
      .success(function(data, status, headers, config) {
        console.log(data)
        $scope.item_list = data.res;
        // DONT DO THIS BAD USER EXP$scope.status = data.status; $scope.msg=data.msg
        $scope.orderByField = 'id';
        $scope.reverseSort = false;
       // Not incduing this feature tableResize('#table_miniview_Exam');
      })
      .error(function(data, status, headers, config) { console.log('Error happen with status:'+status) });  
}
$scope.getMiniView(1);
/************ getting full data for an Item *****************/
$scope.getItem = function(a) {
     $http.get("/api/exam/"+a+"/")
    .success(function(data, status, headers, config) {
      console.log(data)
      $scope.item = data.res;
      $scope.status = data.status; $scope.msg=data.msg
    })
    .error(function(data, status, headers, config) {console.log('Error happen with status:'+status)}); 
  }

/************ creating a new Item  *****************/
$scope.createItem = function(a) {
    console.log($('form#exam').serialize())
    $http({
          method: "post",
          url: '/api/exam/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#exam').serialize()
    })
    .success(function(data, status, headers, config) {
     $scope.status = data.status; $scope.msg=data.msg
     console.log(data)
     $scope.getMiniView(1);
    })
    .error(function(data, status, headers, config) {

    }); 
}

/************ Updating an Item data  *****************/
$scope.updateItem = function(a) {
    if($scope.item.id == null)
    {
     $scope.status = 'error'; $scope.msg=' Please select a raw in left panel to update';
     return;
    }
    $http({
          method: "post",
          url: '/api/exam/'+$scope.item.id+'/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#exam').serialize()
    })
    .success(function(data, status, headers, config) {
     $scope.status = data.status; $scope.msg=data.msg
     console.log(data);
     $scope.getMiniView(1);
    })
    .error(function(data, status, headers, config) {
    }); 
}

/************ delete an Item data  *****************/
$scope.deleteItem = function(a){
  $http.delete("/api/exam/"+a+"/")
      .success(function(data, status, headers, config) {
        $scope.item_list = data;
        $scope.status = data.status; $scope.msg=data.msg
        console.log(data);
        $scope.getMiniView(1);
      })
      .error(function(data, status, headers, config) {
        console.log('Error happen with status:'+status)
      });  
}

/*************** reset an item<used in form>***********************/
$scope.resetItem = function() {
  $scope.getItem($scope.item.id)
}


$scope.getSubject = function(a) {
     $http.get("/api/exam/"+a+"/subject/")
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = data.res;
      $scope.ref_list_items = {};
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#o2o-exam','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }


$scope.getMark = function(a) {
     $http.get("/api/exam/"+a+"/mark/")
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = data.res;
      $scope.ref_list_items = {};
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#o2o-exam','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }


$scope.getResult = function(a) {
     $http.get("/api/exam/"+a+"/result/")
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = data.res;
      $scope.ref_list_items = {};
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#o2o-exam','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }


//Get
$scope.getEmployee= function(a) {
     $http.get("/api/exam/"+a+"/employee/")
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = {}
      $scope.ref_list_items = data.res;
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#m2m-exam','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }
//Add + remove
$scope.addEmployee= function(a,b,c) {
    $http({
          method: "post",
          url: "/api/exam/"+a+"/employee/",
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:{employee: b, action: c}
    })
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = {}
      $scope.ref_list_items = data.res;
      $scope.status = data.status; $scope.msg=data.msg
     
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
    //repopulate..
    $scope.getEmployee;
  }


$scope.qsEmployee= function(a) {
     $http.get("/api/exam/qs/?q="+$scope.quick_search.in)
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.quick_search.out= data.res;
      $scope.status = data.status; $scope.msg=data.msg
      //addClass('#m2m-exam','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }



});
/************ End of Exam Controller*****************/


  
/************ start of Student Controller*****************/
myApp.controller("StudentController",  function ($scope,$http,$sce) { 

    $scope.renderHtml = function (htmlCode) {
            return $sce.trustAsHtml(htmlCode);
    };
/************ Initialize all Data Variable. *****************/
$scope.item ={}
$scope.item_list ={}
$scope.ref_list_items =[]
$scope.limit=10;

$scope.quick_search={'in':'','out':''}


/*********************  get MiniView *****************/
$scope.getMiniView=function(a) {
  $http.get("/api/student/?page="+a+"&limit="+$scope.limit+"")
      .success(function(data, status, headers, config) {
        console.log(data)
        $scope.item_list = data.res;
        // DONT DO THIS BAD USER EXP$scope.status = data.status; $scope.msg=data.msg
        $scope.orderByField = 'id';
        $scope.reverseSort = false;
       // Not incduing this feature tableResize('#table_miniview_Student');
      })
      .error(function(data, status, headers, config) { console.log('Error happen with status:'+status) });  
}
$scope.getMiniView(1);
/************ getting full data for an Item *****************/
$scope.getItem = function(a) {
     $http.get("/api/student/"+a+"/")
    .success(function(data, status, headers, config) {
      console.log(data)
      $scope.item = data.res;
      $scope.status = data.status; $scope.msg=data.msg
    })
    .error(function(data, status, headers, config) {console.log('Error happen with status:'+status)}); 
  }

/************ creating a new Item  *****************/
$scope.createItem = function(a) {
    console.log($('form#student').serialize())
    $http({
          method: "post",
          url: '/api/student/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#student').serialize()
    })
    .success(function(data, status, headers, config) {
     $scope.status = data.status; $scope.msg=data.msg
     console.log(data)
     $scope.getMiniView(1);
    })
    .error(function(data, status, headers, config) {

    }); 
}

/************ Updating an Item data  *****************/
$scope.updateItem = function(a) {
    if($scope.item.id == null)
    {
     $scope.status = 'error'; $scope.msg=' Please select a raw in left panel to update';
     return;
    }
    $http({
          method: "post",
          url: '/api/student/'+$scope.item.id+'/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#student').serialize()
    })
    .success(function(data, status, headers, config) {
     $scope.status = data.status; $scope.msg=data.msg
     console.log(data);
     $scope.getMiniView(1);
    })
    .error(function(data, status, headers, config) {
    }); 
}

/************ delete an Item data  *****************/
$scope.deleteItem = function(a){
  $http.delete("/api/student/"+a+"/")
      .success(function(data, status, headers, config) {
        $scope.item_list = data;
        $scope.status = data.status; $scope.msg=data.msg
        console.log(data);
        $scope.getMiniView(1);
      })
      .error(function(data, status, headers, config) {
        console.log('Error happen with status:'+status)
      });  
}

/*************** reset an item<used in form>***********************/
$scope.resetItem = function() {
  $scope.getItem($scope.item.id)
}


$scope.getParent = function(a) {
     $http.get("/api/student/"+a+"/parent/")
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = data.res;
      $scope.ref_list_items = {};
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#o2o-student','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }


$scope.getMark = function(a) {
     $http.get("/api/student/"+a+"/mark/")
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = data.res;
      $scope.ref_list_items = {};
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#o2o-student','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }


$scope.getResult = function(a) {
     $http.get("/api/student/"+a+"/result/")
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = data.res;
      $scope.ref_list_items = {};
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#o2o-student','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }


$scope.getAttendance = function(a) {
     $http.get("/api/student/"+a+"/attendance/")
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = data.res;
      $scope.ref_list_items = {};
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#o2o-student','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }


$scope.getFees = function(a) {
     $http.get("/api/student/"+a+"/fees/")
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = data.res;
      $scope.ref_list_items = {};
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#o2o-student','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }


$scope.getSport = function(a) {
     $http.get("/api/student/"+a+"/sport/")
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = data.res;
      $scope.ref_list_items = {};
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#o2o-student','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }


//Get
$scope.getMyClass= function(a) {
     $http.get("/api/student/"+a+"/myclass/")
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = {}
      $scope.ref_list_items = data.res;
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#m2m-student','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }
//Add + remove
$scope.addMyClass= function(a,b,c) {
    $http({
          method: "post",
          url: "/api/student/"+a+"/myclass/",
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:{myclass: b, action: c}
    })
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = {}
      $scope.ref_list_items = data.res;
      $scope.status = data.status; $scope.msg=data.msg
     
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
    //repopulate..
    $scope.getMyClass;
  }


$scope.qsMyClass= function(a) {
     $http.get("/api/student/qs/?q="+$scope.quick_search.in)
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.quick_search.out= data.res;
      $scope.status = data.status; $scope.msg=data.msg
      //addClass('#m2m-student','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }



});
/************ End of Student Controller*****************/


  
/************ start of Mark Controller*****************/
myApp.controller("MarkController",  function ($scope,$http,$sce) { 

    $scope.renderHtml = function (htmlCode) {
            return $sce.trustAsHtml(htmlCode);
    };
/************ Initialize all Data Variable. *****************/
$scope.item ={}
$scope.item_list ={}
$scope.ref_list_items =[]
$scope.limit=10;

$scope.quick_search={'in':'','out':''}


/*********************  get MiniView *****************/
$scope.getMiniView=function(a) {
  $http.get("/api/mark/?page="+a+"&limit="+$scope.limit+"")
      .success(function(data, status, headers, config) {
        console.log(data)
        $scope.item_list = data.res;
        // DONT DO THIS BAD USER EXP$scope.status = data.status; $scope.msg=data.msg
        $scope.orderByField = 'id';
        $scope.reverseSort = false;
       // Not incduing this feature tableResize('#table_miniview_Mark');
      })
      .error(function(data, status, headers, config) { console.log('Error happen with status:'+status) });  
}
$scope.getMiniView(1);
/************ getting full data for an Item *****************/
$scope.getItem = function(a) {
     $http.get("/api/mark/"+a+"/")
    .success(function(data, status, headers, config) {
      console.log(data)
      $scope.item = data.res;
      $scope.status = data.status; $scope.msg=data.msg
    })
    .error(function(data, status, headers, config) {console.log('Error happen with status:'+status)}); 
  }

/************ creating a new Item  *****************/
$scope.createItem = function(a) {
    console.log($('form#mark').serialize())
    $http({
          method: "post",
          url: '/api/mark/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#mark').serialize()
    })
    .success(function(data, status, headers, config) {
     $scope.status = data.status; $scope.msg=data.msg
     console.log(data)
     $scope.getMiniView(1);
    })
    .error(function(data, status, headers, config) {

    }); 
}

/************ Updating an Item data  *****************/
$scope.updateItem = function(a) {
    if($scope.item.id == null)
    {
     $scope.status = 'error'; $scope.msg=' Please select a raw in left panel to update';
     return;
    }
    $http({
          method: "post",
          url: '/api/mark/'+$scope.item.id+'/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#mark').serialize()
    })
    .success(function(data, status, headers, config) {
     $scope.status = data.status; $scope.msg=data.msg
     console.log(data);
     $scope.getMiniView(1);
    })
    .error(function(data, status, headers, config) {
    }); 
}

/************ delete an Item data  *****************/
$scope.deleteItem = function(a){
  $http.delete("/api/mark/"+a+"/")
      .success(function(data, status, headers, config) {
        $scope.item_list = data;
        $scope.status = data.status; $scope.msg=data.msg
        console.log(data);
        $scope.getMiniView(1);
      })
      .error(function(data, status, headers, config) {
        console.log('Error happen with status:'+status)
      });  
}

/*************** reset an item<used in form>***********************/
$scope.resetItem = function() {
  $scope.getItem($scope.item.id)
}


$scope.getStudent = function(a) {
     $http.get("/api/mark/"+a+"/student/")
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = data.res;
      $scope.ref_list_items = {};
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#o2o-mark','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }


$scope.getSubject = function(a) {
     $http.get("/api/mark/"+a+"/subject/")
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = data.res;
      $scope.ref_list_items = {};
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#o2o-mark','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }


$scope.getExam = function(a) {
     $http.get("/api/mark/"+a+"/exam/")
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = data.res;
      $scope.ref_list_items = {};
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#o2o-mark','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }


$scope.qsExam= function(a) {
     $http.get("/api/mark/qs/?q="+$scope.quick_search.in)
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.quick_search.out= data.res;
      $scope.status = data.status; $scope.msg=data.msg
      //addClass('#m2m-mark','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }



});
/************ End of Mark Controller*****************/


  
/************ start of Result Controller*****************/
myApp.controller("ResultController",  function ($scope,$http,$sce) { 

    $scope.renderHtml = function (htmlCode) {
            return $sce.trustAsHtml(htmlCode);
    };
/************ Initialize all Data Variable. *****************/
$scope.item ={}
$scope.item_list ={}
$scope.ref_list_items =[]
$scope.limit=10;

$scope.quick_search={'in':'','out':''}


/*********************  get MiniView *****************/
$scope.getMiniView=function(a) {
  $http.get("/api/result/?page="+a+"&limit="+$scope.limit+"")
      .success(function(data, status, headers, config) {
        console.log(data)
        $scope.item_list = data.res;
        // DONT DO THIS BAD USER EXP$scope.status = data.status; $scope.msg=data.msg
        $scope.orderByField = 'id';
        $scope.reverseSort = false;
       // Not incduing this feature tableResize('#table_miniview_Result');
      })
      .error(function(data, status, headers, config) { console.log('Error happen with status:'+status) });  
}
$scope.getMiniView(1);
/************ getting full data for an Item *****************/
$scope.getItem = function(a) {
     $http.get("/api/result/"+a+"/")
    .success(function(data, status, headers, config) {
      console.log(data)
      $scope.item = data.res;
      $scope.status = data.status; $scope.msg=data.msg
    })
    .error(function(data, status, headers, config) {console.log('Error happen with status:'+status)}); 
  }

/************ creating a new Item  *****************/
$scope.createItem = function(a) {
    console.log($('form#result').serialize())
    $http({
          method: "post",
          url: '/api/result/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#result').serialize()
    })
    .success(function(data, status, headers, config) {
     $scope.status = data.status; $scope.msg=data.msg
     console.log(data)
     $scope.getMiniView(1);
    })
    .error(function(data, status, headers, config) {

    }); 
}

/************ Updating an Item data  *****************/
$scope.updateItem = function(a) {
    if($scope.item.id == null)
    {
     $scope.status = 'error'; $scope.msg=' Please select a raw in left panel to update';
     return;
    }
    $http({
          method: "post",
          url: '/api/result/'+$scope.item.id+'/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#result').serialize()
    })
    .success(function(data, status, headers, config) {
     $scope.status = data.status; $scope.msg=data.msg
     console.log(data);
     $scope.getMiniView(1);
    })
    .error(function(data, status, headers, config) {
    }); 
}

/************ delete an Item data  *****************/
$scope.deleteItem = function(a){
  $http.delete("/api/result/"+a+"/")
      .success(function(data, status, headers, config) {
        $scope.item_list = data;
        $scope.status = data.status; $scope.msg=data.msg
        console.log(data);
        $scope.getMiniView(1);
      })
      .error(function(data, status, headers, config) {
        console.log('Error happen with status:'+status)
      });  
}

/*************** reset an item<used in form>***********************/
$scope.resetItem = function() {
  $scope.getItem($scope.item.id)
}


$scope.getExam = function(a) {
     $http.get("/api/result/"+a+"/exam/")
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = data.res;
      $scope.ref_list_items = {};
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#o2o-result','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }


//Get
$scope.getStudent= function(a) {
     $http.get("/api/result/"+a+"/student/")
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = {}
      $scope.ref_list_items = data.res;
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#m2m-result','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }
//Add + remove
$scope.addStudent= function(a,b,c) {
    $http({
          method: "post",
          url: "/api/result/"+a+"/student/",
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:{student: b, action: c}
    })
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = {}
      $scope.ref_list_items = data.res;
      $scope.status = data.status; $scope.msg=data.msg
     
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
    //repopulate..
    $scope.getStudent;
  }


$scope.qsStudent= function(a) {
     $http.get("/api/result/qs/?q="+$scope.quick_search.in)
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.quick_search.out= data.res;
      $scope.status = data.status; $scope.msg=data.msg
      //addClass('#m2m-result','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }



});
/************ End of Result Controller*****************/


  
/************ start of Attendance Controller*****************/
myApp.controller("AttendanceController",  function ($scope,$http,$sce) { 

    $scope.renderHtml = function (htmlCode) {
            return $sce.trustAsHtml(htmlCode);
    };
/************ Initialize all Data Variable. *****************/
$scope.item ={}
$scope.item_list ={}
$scope.ref_list_items =[]
$scope.limit=10;

$scope.quick_search={'in':'','out':''}


/*********************  get MiniView *****************/
$scope.getMiniView=function(a) {
  $http.get("/api/attendance/?page="+a+"&limit="+$scope.limit+"")
      .success(function(data, status, headers, config) {
        console.log(data)
        $scope.item_list = data.res;
        // DONT DO THIS BAD USER EXP$scope.status = data.status; $scope.msg=data.msg
        $scope.orderByField = 'id';
        $scope.reverseSort = false;
       // Not incduing this feature tableResize('#table_miniview_Attendance');
      })
      .error(function(data, status, headers, config) { console.log('Error happen with status:'+status) });  
}
$scope.getMiniView(1);
/************ getting full data for an Item *****************/
$scope.getItem = function(a) {
     $http.get("/api/attendance/"+a+"/")
    .success(function(data, status, headers, config) {
      console.log(data)
      $scope.item = data.res;
      $scope.status = data.status; $scope.msg=data.msg
    })
    .error(function(data, status, headers, config) {console.log('Error happen with status:'+status)}); 
  }

/************ creating a new Item  *****************/
$scope.createItem = function(a) {
    console.log($('form#attendance').serialize())
    $http({
          method: "post",
          url: '/api/attendance/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#attendance').serialize()
    })
    .success(function(data, status, headers, config) {
     $scope.status = data.status; $scope.msg=data.msg
     console.log(data)
     $scope.getMiniView(1);
    })
    .error(function(data, status, headers, config) {

    }); 
}

/************ Updating an Item data  *****************/
$scope.updateItem = function(a) {
    if($scope.item.id == null)
    {
     $scope.status = 'error'; $scope.msg=' Please select a raw in left panel to update';
     return;
    }
    $http({
          method: "post",
          url: '/api/attendance/'+$scope.item.id+'/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#attendance').serialize()
    })
    .success(function(data, status, headers, config) {
     $scope.status = data.status; $scope.msg=data.msg
     console.log(data);
     $scope.getMiniView(1);
    })
    .error(function(data, status, headers, config) {
    }); 
}

/************ delete an Item data  *****************/
$scope.deleteItem = function(a){
  $http.delete("/api/attendance/"+a+"/")
      .success(function(data, status, headers, config) {
        $scope.item_list = data;
        $scope.status = data.status; $scope.msg=data.msg
        console.log(data);
        $scope.getMiniView(1);
      })
      .error(function(data, status, headers, config) {
        console.log('Error happen with status:'+status)
      });  
}

/*************** reset an item<used in form>***********************/
$scope.resetItem = function() {
  $scope.getItem($scope.item.id)
}


$scope.getStudent = function(a) {
     $http.get("/api/attendance/"+a+"/student/")
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = data.res;
      $scope.ref_list_items = {};
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#o2o-attendance','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }


$scope.getMyClass = function(a) {
     $http.get("/api/attendance/"+a+"/myclass/")
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = data.res;
      $scope.ref_list_items = {};
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#o2o-attendance','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }


$scope.qsMyClass= function(a) {
     $http.get("/api/attendance/qs/?q="+$scope.quick_search.in)
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.quick_search.out= data.res;
      $scope.status = data.status; $scope.msg=data.msg
      //addClass('#m2m-attendance','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }



});
/************ End of Attendance Controller*****************/


  
/************ start of Fees Controller*****************/
myApp.controller("FeesController",  function ($scope,$http,$sce) { 

    $scope.renderHtml = function (htmlCode) {
            return $sce.trustAsHtml(htmlCode);
    };
/************ Initialize all Data Variable. *****************/
$scope.item ={}
$scope.item_list ={}
$scope.ref_list_items =[]
$scope.limit=10;

$scope.quick_search={'in':'','out':''}


/*********************  get MiniView *****************/
$scope.getMiniView=function(a) {
  $http.get("/api/fees/?page="+a+"&limit="+$scope.limit+"")
      .success(function(data, status, headers, config) {
        console.log(data)
        $scope.item_list = data.res;
        // DONT DO THIS BAD USER EXP$scope.status = data.status; $scope.msg=data.msg
        $scope.orderByField = 'id';
        $scope.reverseSort = false;
       // Not incduing this feature tableResize('#table_miniview_Fees');
      })
      .error(function(data, status, headers, config) { console.log('Error happen with status:'+status) });  
}
$scope.getMiniView(1);
/************ getting full data for an Item *****************/
$scope.getItem = function(a) {
     $http.get("/api/fees/"+a+"/")
    .success(function(data, status, headers, config) {
      console.log(data)
      $scope.item = data.res;
      $scope.status = data.status; $scope.msg=data.msg
    })
    .error(function(data, status, headers, config) {console.log('Error happen with status:'+status)}); 
  }

/************ creating a new Item  *****************/
$scope.createItem = function(a) {
    console.log($('form#fees').serialize())
    $http({
          method: "post",
          url: '/api/fees/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#fees').serialize()
    })
    .success(function(data, status, headers, config) {
     $scope.status = data.status; $scope.msg=data.msg
     console.log(data)
     $scope.getMiniView(1);
    })
    .error(function(data, status, headers, config) {

    }); 
}

/************ Updating an Item data  *****************/
$scope.updateItem = function(a) {
    if($scope.item.id == null)
    {
     $scope.status = 'error'; $scope.msg=' Please select a raw in left panel to update';
     return;
    }
    $http({
          method: "post",
          url: '/api/fees/'+$scope.item.id+'/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#fees').serialize()
    })
    .success(function(data, status, headers, config) {
     $scope.status = data.status; $scope.msg=data.msg
     console.log(data);
     $scope.getMiniView(1);
    })
    .error(function(data, status, headers, config) {
    }); 
}

/************ delete an Item data  *****************/
$scope.deleteItem = function(a){
  $http.delete("/api/fees/"+a+"/")
      .success(function(data, status, headers, config) {
        $scope.item_list = data;
        $scope.status = data.status; $scope.msg=data.msg
        console.log(data);
        $scope.getMiniView(1);
      })
      .error(function(data, status, headers, config) {
        console.log('Error happen with status:'+status)
      });  
}

/*************** reset an item<used in form>***********************/
$scope.resetItem = function() {
  $scope.getItem($scope.item.id)
}


//Get
$scope.getStudent= function(a) {
     $http.get("/api/fees/"+a+"/student/")
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = {}
      $scope.ref_list_items = data.res;
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#m2m-fees','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }
//Add + remove
$scope.addStudent= function(a,b,c) {
    $http({
          method: "post",
          url: "/api/fees/"+a+"/student/",
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:{student: b, action: c}
    })
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = {}
      $scope.ref_list_items = data.res;
      $scope.status = data.status; $scope.msg=data.msg
     
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
    //repopulate..
    $scope.getStudent;
  }


$scope.qsStudent= function(a) {
     $http.get("/api/fees/qs/?q="+$scope.quick_search.in)
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.quick_search.out= data.res;
      $scope.status = data.status; $scope.msg=data.msg
      //addClass('#m2m-fees','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }



});
/************ End of Fees Controller*****************/


  
/************ start of Sport Controller*****************/
myApp.controller("SportController",  function ($scope,$http,$sce) { 

    $scope.renderHtml = function (htmlCode) {
            return $sce.trustAsHtml(htmlCode);
    };
/************ Initialize all Data Variable. *****************/
$scope.item ={}
$scope.item_list ={}
$scope.ref_list_items =[]
$scope.limit=10;

$scope.quick_search={'in':'','out':''}


/*********************  get MiniView *****************/
$scope.getMiniView=function(a) {
  $http.get("/api/sport/?page="+a+"&limit="+$scope.limit+"")
      .success(function(data, status, headers, config) {
        console.log(data)
        $scope.item_list = data.res;
        // DONT DO THIS BAD USER EXP$scope.status = data.status; $scope.msg=data.msg
        $scope.orderByField = 'id';
        $scope.reverseSort = false;
       // Not incduing this feature tableResize('#table_miniview_Sport');
      })
      .error(function(data, status, headers, config) { console.log('Error happen with status:'+status) });  
}
$scope.getMiniView(1);
/************ getting full data for an Item *****************/
$scope.getItem = function(a) {
     $http.get("/api/sport/"+a+"/")
    .success(function(data, status, headers, config) {
      console.log(data)
      $scope.item = data.res;
      $scope.status = data.status; $scope.msg=data.msg
    })
    .error(function(data, status, headers, config) {console.log('Error happen with status:'+status)}); 
  }

/************ creating a new Item  *****************/
$scope.createItem = function(a) {
    console.log($('form#sport').serialize())
    $http({
          method: "post",
          url: '/api/sport/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#sport').serialize()
    })
    .success(function(data, status, headers, config) {
     $scope.status = data.status; $scope.msg=data.msg
     console.log(data)
     $scope.getMiniView(1);
    })
    .error(function(data, status, headers, config) {

    }); 
}

/************ Updating an Item data  *****************/
$scope.updateItem = function(a) {
    if($scope.item.id == null)
    {
     $scope.status = 'error'; $scope.msg=' Please select a raw in left panel to update';
     return;
    }
    $http({
          method: "post",
          url: '/api/sport/'+$scope.item.id+'/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#sport').serialize()
    })
    .success(function(data, status, headers, config) {
     $scope.status = data.status; $scope.msg=data.msg
     console.log(data);
     $scope.getMiniView(1);
    })
    .error(function(data, status, headers, config) {
    }); 
}

/************ delete an Item data  *****************/
$scope.deleteItem = function(a){
  $http.delete("/api/sport/"+a+"/")
      .success(function(data, status, headers, config) {
        $scope.item_list = data;
        $scope.status = data.status; $scope.msg=data.msg
        console.log(data);
        $scope.getMiniView(1);
      })
      .error(function(data, status, headers, config) {
        console.log('Error happen with status:'+status)
      });  
}

/*************** reset an item<used in form>***********************/
$scope.resetItem = function() {
  $scope.getItem($scope.item.id)
}


//Get
$scope.getStudent= function(a) {
     $http.get("/api/sport/"+a+"/student/")
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = {}
      $scope.ref_list_items = data.res;
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#m2m-sport','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }
//Add + remove
$scope.addStudent= function(a,b,c) {
    $http({
          method: "post",
          url: "/api/sport/"+a+"/student/",
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:{student: b, action: c}
    })
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = {}
      $scope.ref_list_items = data.res;
      $scope.status = data.status; $scope.msg=data.msg
     
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
    //repopulate..
    $scope.getStudent;
  }


$scope.qsStudent= function(a) {
     $http.get("/api/sport/qs/?q="+$scope.quick_search.in)
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.quick_search.out= data.res;
      $scope.status = data.status; $scope.msg=data.msg
      //addClass('#m2m-sport','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }



});
/************ End of Sport Controller*****************/


  
/************ start of Account Controller*****************/
myApp.controller("AccountController",  function ($scope,$http,$sce) { 

    $scope.renderHtml = function (htmlCode) {
            return $sce.trustAsHtml(htmlCode);
    };
/************ Initialize all Data Variable. *****************/
$scope.item ={}
$scope.item_list ={}
$scope.ref_list_items =[]
$scope.limit=10;

$scope.quick_search={'in':'','out':''}


/*********************  get MiniView *****************/
$scope.getMiniView=function(a) {
  $http.get("/api/account/?page="+a+"&limit="+$scope.limit+"")
      .success(function(data, status, headers, config) {
        console.log(data)
        $scope.item_list = data.res;
        // DONT DO THIS BAD USER EXP$scope.status = data.status; $scope.msg=data.msg
        $scope.orderByField = 'id';
        $scope.reverseSort = false;
       // Not incduing this feature tableResize('#table_miniview_Account');
      })
      .error(function(data, status, headers, config) { console.log('Error happen with status:'+status) });  
}
$scope.getMiniView(1);
/************ getting full data for an Item *****************/
$scope.getItem = function(a) {
     $http.get("/api/account/"+a+"/")
    .success(function(data, status, headers, config) {
      console.log(data)
      $scope.item = data.res;
      $scope.status = data.status; $scope.msg=data.msg
    })
    .error(function(data, status, headers, config) {console.log('Error happen with status:'+status)}); 
  }

/************ creating a new Item  *****************/
$scope.createItem = function(a) {
    console.log($('form#account').serialize())
    $http({
          method: "post",
          url: '/api/account/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#account').serialize()
    })
    .success(function(data, status, headers, config) {
     $scope.status = data.status; $scope.msg=data.msg
     console.log(data)
     $scope.getMiniView(1);
    })
    .error(function(data, status, headers, config) {

    }); 
}

/************ Updating an Item data  *****************/
$scope.updateItem = function(a) {
    if($scope.item.id == null)
    {
     $scope.status = 'error'; $scope.msg=' Please select a raw in left panel to update';
     return;
    }
    $http({
          method: "post",
          url: '/api/account/'+$scope.item.id+'/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#account').serialize()
    })
    .success(function(data, status, headers, config) {
     $scope.status = data.status; $scope.msg=data.msg
     console.log(data);
     $scope.getMiniView(1);
    })
    .error(function(data, status, headers, config) {
    }); 
}

/************ delete an Item data  *****************/
$scope.deleteItem = function(a){
  $http.delete("/api/account/"+a+"/")
      .success(function(data, status, headers, config) {
        $scope.item_list = data;
        $scope.status = data.status; $scope.msg=data.msg
        console.log(data);
        $scope.getMiniView(1);
      })
      .error(function(data, status, headers, config) {
        console.log('Error happen with status:'+status)
      });  
}

/*************** reset an item<used in form>***********************/
$scope.resetItem = function() {
  $scope.getItem($scope.item.id)
}


$scope.getSetting = function(a) {
     $http.get("/api/account/"+a+"/setting/")
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = data.res;
      $scope.ref_list_items = {};
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#o2o-account','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }


$scope.qsSetting= function(a) {
     $http.get("/api/account/qs/?q="+$scope.quick_search.in)
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.quick_search.out= data.res;
      $scope.status = data.status; $scope.msg=data.msg
      //addClass('#m2m-account','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }



});
/************ End of Account Controller*****************/


  
/************ start of Setting Controller*****************/
myApp.controller("SettingController",  function ($scope,$http,$sce) { 

    $scope.renderHtml = function (htmlCode) {
            return $sce.trustAsHtml(htmlCode);
    };
/************ Initialize all Data Variable. *****************/
$scope.item ={}
$scope.item_list ={}
$scope.ref_list_items =[]
$scope.limit=10;

$scope.quick_search={'in':'','out':''}


/*********************  get MiniView *****************/
$scope.getMiniView=function(a) {
  $http.get("/api/setting/?page="+a+"&limit="+$scope.limit+"")
      .success(function(data, status, headers, config) {
        console.log(data)
        $scope.item_list = data.res;
        // DONT DO THIS BAD USER EXP$scope.status = data.status; $scope.msg=data.msg
        $scope.orderByField = 'id';
        $scope.reverseSort = false;
       // Not incduing this feature tableResize('#table_miniview_Setting');
      })
      .error(function(data, status, headers, config) { console.log('Error happen with status:'+status) });  
}
$scope.getMiniView(1);
/************ getting full data for an Item *****************/
$scope.getItem = function(a) {
     $http.get("/api/setting/"+a+"/")
    .success(function(data, status, headers, config) {
      console.log(data)
      $scope.item = data.res;
      $scope.status = data.status; $scope.msg=data.msg
    })
    .error(function(data, status, headers, config) {console.log('Error happen with status:'+status)}); 
  }

/************ creating a new Item  *****************/
$scope.createItem = function(a) {
    console.log($('form#setting').serialize())
    $http({
          method: "post",
          url: '/api/setting/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#setting').serialize()
    })
    .success(function(data, status, headers, config) {
     $scope.status = data.status; $scope.msg=data.msg
     console.log(data)
     $scope.getMiniView(1);
    })
    .error(function(data, status, headers, config) {

    }); 
}

/************ Updating an Item data  *****************/
$scope.updateItem = function(a) {
    if($scope.item.id == null)
    {
     $scope.status = 'error'; $scope.msg=' Please select a raw in left panel to update';
     return;
    }
    $http({
          method: "post",
          url: '/api/setting/'+$scope.item.id+'/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#setting').serialize()
    })
    .success(function(data, status, headers, config) {
     $scope.status = data.status; $scope.msg=data.msg
     console.log(data);
     $scope.getMiniView(1);
    })
    .error(function(data, status, headers, config) {
    }); 
}

/************ delete an Item data  *****************/
$scope.deleteItem = function(a){
  $http.delete("/api/setting/"+a+"/")
      .success(function(data, status, headers, config) {
        $scope.item_list = data;
        $scope.status = data.status; $scope.msg=data.msg
        console.log(data);
        $scope.getMiniView(1);
      })
      .error(function(data, status, headers, config) {
        console.log('Error happen with status:'+status)
      });  
}

/*************** reset an item<used in form>***********************/
$scope.resetItem = function() {
  $scope.getItem($scope.item.id)
}


//Get
$scope.getAccount= function(a) {
     $http.get("/api/setting/"+a+"/account/")
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = {}
      $scope.ref_list_items = data.res;
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#m2m-setting','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }
//Add + remove
$scope.addAccount= function(a,b,c) {
    $http({
          method: "post",
          url: "/api/setting/"+a+"/account/",
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:{account: b, action: c}
    })
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = {}
      $scope.ref_list_items = data.res;
      $scope.status = data.status; $scope.msg=data.msg
     
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
    //repopulate..
    $scope.getAccount;
  }


$scope.qsAccount= function(a) {
     $http.get("/api/setting/qs/?q="+$scope.quick_search.in)
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.quick_search.out= data.res;
      $scope.status = data.status; $scope.msg=data.msg
      //addClass('#m2m-setting','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }



});
/************ End of Setting Controller*****************/


  
/************ start of Fund Controller*****************/
myApp.controller("FundController",  function ($scope,$http,$sce) { 

    $scope.renderHtml = function (htmlCode) {
            return $sce.trustAsHtml(htmlCode);
    };
/************ Initialize all Data Variable. *****************/
$scope.item ={}
$scope.item_list ={}
$scope.ref_list_items =[]
$scope.limit=10;

$scope.quick_search={'in':'','out':''}


/*********************  get MiniView *****************/
$scope.getMiniView=function(a) {
  $http.get("/api/fund/?page="+a+"&limit="+$scope.limit+"")
      .success(function(data, status, headers, config) {
        console.log(data)
        $scope.item_list = data.res;
        // DONT DO THIS BAD USER EXP$scope.status = data.status; $scope.msg=data.msg
        $scope.orderByField = 'id';
        $scope.reverseSort = false;
       // Not incduing this feature tableResize('#table_miniview_Fund');
      })
      .error(function(data, status, headers, config) { console.log('Error happen with status:'+status) });  
}
$scope.getMiniView(1);
/************ getting full data for an Item *****************/
$scope.getItem = function(a) {
     $http.get("/api/fund/"+a+"/")
    .success(function(data, status, headers, config) {
      console.log(data)
      $scope.item = data.res;
      $scope.status = data.status; $scope.msg=data.msg
    })
    .error(function(data, status, headers, config) {console.log('Error happen with status:'+status)}); 
  }

/************ creating a new Item  *****************/
$scope.createItem = function(a) {
    console.log($('form#fund').serialize())
    $http({
          method: "post",
          url: '/api/fund/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#fund').serialize()
    })
    .success(function(data, status, headers, config) {
     $scope.status = data.status; $scope.msg=data.msg
     console.log(data)
     $scope.getMiniView(1);
    })
    .error(function(data, status, headers, config) {

    }); 
}

/************ Updating an Item data  *****************/
$scope.updateItem = function(a) {
    if($scope.item.id == null)
    {
     $scope.status = 'error'; $scope.msg=' Please select a raw in left panel to update';
     return;
    }
    $http({
          method: "post",
          url: '/api/fund/'+$scope.item.id+'/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#fund').serialize()
    })
    .success(function(data, status, headers, config) {
     $scope.status = data.status; $scope.msg=data.msg
     console.log(data);
     $scope.getMiniView(1);
    })
    .error(function(data, status, headers, config) {
    }); 
}

/************ delete an Item data  *****************/
$scope.deleteItem = function(a){
  $http.delete("/api/fund/"+a+"/")
      .success(function(data, status, headers, config) {
        $scope.item_list = data;
        $scope.status = data.status; $scope.msg=data.msg
        console.log(data);
        $scope.getMiniView(1);
      })
      .error(function(data, status, headers, config) {
        console.log('Error happen with status:'+status)
      });  
}

/*************** reset an item<used in form>***********************/
$scope.resetItem = function() {
  $scope.getItem($scope.item.id)
}


$scope.qsAccount= function(a) {
     $http.get("/api/fund/qs/?q="+$scope.quick_search.in)
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.quick_search.out= data.res;
      $scope.status = data.status; $scope.msg=data.msg
      //addClass('#m2m-fund','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }



});
/************ End of Fund Controller*****************/


  
/************ start of Book Controller*****************/
myApp.controller("BookController",  function ($scope,$http,$sce) { 

    $scope.renderHtml = function (htmlCode) {
            return $sce.trustAsHtml(htmlCode);
    };
/************ Initialize all Data Variable. *****************/
$scope.item ={}
$scope.item_list ={}
$scope.ref_list_items =[]
$scope.limit=10;

$scope.quick_search={'in':'','out':''}


/*********************  get MiniView *****************/
$scope.getMiniView=function(a) {
  $http.get("/api/book/?page="+a+"&limit="+$scope.limit+"")
      .success(function(data, status, headers, config) {
        console.log(data)
        $scope.item_list = data.res;
        // DONT DO THIS BAD USER EXP$scope.status = data.status; $scope.msg=data.msg
        $scope.orderByField = 'id';
        $scope.reverseSort = false;
       // Not incduing this feature tableResize('#table_miniview_Book');
      })
      .error(function(data, status, headers, config) { console.log('Error happen with status:'+status) });  
}
$scope.getMiniView(1);
/************ getting full data for an Item *****************/
$scope.getItem = function(a) {
     $http.get("/api/book/"+a+"/")
    .success(function(data, status, headers, config) {
      console.log(data)
      $scope.item = data.res;
      $scope.status = data.status; $scope.msg=data.msg
    })
    .error(function(data, status, headers, config) {console.log('Error happen with status:'+status)}); 
  }

/************ creating a new Item  *****************/
$scope.createItem = function(a) {
    console.log($('form#book').serialize())
    $http({
          method: "post",
          url: '/api/book/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#book').serialize()
    })
    .success(function(data, status, headers, config) {
     $scope.status = data.status; $scope.msg=data.msg
     console.log(data)
     $scope.getMiniView(1);
    })
    .error(function(data, status, headers, config) {

    }); 
}

/************ Updating an Item data  *****************/
$scope.updateItem = function(a) {
    if($scope.item.id == null)
    {
     $scope.status = 'error'; $scope.msg=' Please select a raw in left panel to update';
     return;
    }
    $http({
          method: "post",
          url: '/api/book/'+$scope.item.id+'/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#book').serialize()
    })
    .success(function(data, status, headers, config) {
     $scope.status = data.status; $scope.msg=data.msg
     console.log(data);
     $scope.getMiniView(1);
    })
    .error(function(data, status, headers, config) {
    }); 
}

/************ delete an Item data  *****************/
$scope.deleteItem = function(a){
  $http.delete("/api/book/"+a+"/")
      .success(function(data, status, headers, config) {
        $scope.item_list = data;
        $scope.status = data.status; $scope.msg=data.msg
        console.log(data);
        $scope.getMiniView(1);
      })
      .error(function(data, status, headers, config) {
        console.log('Error happen with status:'+status)
      });  
}

/*************** reset an item<used in form>***********************/
$scope.resetItem = function() {
  $scope.getItem($scope.item.id)
}


$scope.qsAccount= function(a) {
     $http.get("/api/book/qs/?q="+$scope.quick_search.in)
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.quick_search.out= data.res;
      $scope.status = data.status; $scope.msg=data.msg
      //addClass('#m2m-book','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }



});
/************ End of Book Controller*****************/


  
/************ start of Event Controller*****************/
myApp.controller("EventController",  function ($scope,$http,$sce) { 

    $scope.renderHtml = function (htmlCode) {
            return $sce.trustAsHtml(htmlCode);
    };
/************ Initialize all Data Variable. *****************/
$scope.item ={}
$scope.item_list ={}
$scope.ref_list_items =[]
$scope.limit=10;

$scope.quick_search={'in':'','out':''}


/*********************  get MiniView *****************/
$scope.getMiniView=function(a) {
  $http.get("/api/event/?page="+a+"&limit="+$scope.limit+"")
      .success(function(data, status, headers, config) {
        console.log(data)
        $scope.item_list = data.res;
        // DONT DO THIS BAD USER EXP$scope.status = data.status; $scope.msg=data.msg
        $scope.orderByField = 'id';
        $scope.reverseSort = false;
       // Not incduing this feature tableResize('#table_miniview_Event');
      })
      .error(function(data, status, headers, config) { console.log('Error happen with status:'+status) });  
}
$scope.getMiniView(1);
/************ getting full data for an Item *****************/
$scope.getItem = function(a) {
     $http.get("/api/event/"+a+"/")
    .success(function(data, status, headers, config) {
      console.log(data)
      $scope.item = data.res;
      $scope.status = data.status; $scope.msg=data.msg
    })
    .error(function(data, status, headers, config) {console.log('Error happen with status:'+status)}); 
  }

/************ creating a new Item  *****************/
$scope.createItem = function(a) {
    console.log($('form#event').serialize())
    $http({
          method: "post",
          url: '/api/event/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#event').serialize()
    })
    .success(function(data, status, headers, config) {
     $scope.status = data.status; $scope.msg=data.msg
     console.log(data)
     $scope.getMiniView(1);
    })
    .error(function(data, status, headers, config) {

    }); 
}

/************ Updating an Item data  *****************/
$scope.updateItem = function(a) {
    if($scope.item.id == null)
    {
     $scope.status = 'error'; $scope.msg=' Please select a raw in left panel to update';
     return;
    }
    $http({
          method: "post",
          url: '/api/event/'+$scope.item.id+'/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#event').serialize()
    })
    .success(function(data, status, headers, config) {
     $scope.status = data.status; $scope.msg=data.msg
     console.log(data);
     $scope.getMiniView(1);
    })
    .error(function(data, status, headers, config) {
    }); 
}

/************ delete an Item data  *****************/
$scope.deleteItem = function(a){
  $http.delete("/api/event/"+a+"/")
      .success(function(data, status, headers, config) {
        $scope.item_list = data;
        $scope.status = data.status; $scope.msg=data.msg
        console.log(data);
        $scope.getMiniView(1);
      })
      .error(function(data, status, headers, config) {
        console.log('Error happen with status:'+status)
      });  
}

/*************** reset an item<used in form>***********************/
$scope.resetItem = function() {
  $scope.getItem($scope.item.id)
}


$scope.qsAccount= function(a) {
     $http.get("/api/event/qs/?q="+$scope.quick_search.in)
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.quick_search.out= data.res;
      $scope.status = data.status; $scope.msg=data.msg
      //addClass('#m2m-event','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }



});
/************ End of Event Controller*****************/


  
/************ start of Discipline Controller*****************/
myApp.controller("DisciplineController",  function ($scope,$http,$sce) { 

    $scope.renderHtml = function (htmlCode) {
            return $sce.trustAsHtml(htmlCode);
    };
/************ Initialize all Data Variable. *****************/
$scope.item ={}
$scope.item_list ={}
$scope.ref_list_items =[]
$scope.limit=10;

$scope.quick_search={'in':'','out':''}


/*********************  get MiniView *****************/
$scope.getMiniView=function(a) {
  $http.get("/api/discipline/?page="+a+"&limit="+$scope.limit+"")
      .success(function(data, status, headers, config) {
        console.log(data)
        $scope.item_list = data.res;
        // DONT DO THIS BAD USER EXP$scope.status = data.status; $scope.msg=data.msg
        $scope.orderByField = 'id';
        $scope.reverseSort = false;
       // Not incduing this feature tableResize('#table_miniview_Discipline');
      })
      .error(function(data, status, headers, config) { console.log('Error happen with status:'+status) });  
}
$scope.getMiniView(1);
/************ getting full data for an Item *****************/
$scope.getItem = function(a) {
     $http.get("/api/discipline/"+a+"/")
    .success(function(data, status, headers, config) {
      console.log(data)
      $scope.item = data.res;
      $scope.status = data.status; $scope.msg=data.msg
    })
    .error(function(data, status, headers, config) {console.log('Error happen with status:'+status)}); 
  }

/************ creating a new Item  *****************/
$scope.createItem = function(a) {
    console.log($('form#discipline').serialize())
    $http({
          method: "post",
          url: '/api/discipline/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#discipline').serialize()
    })
    .success(function(data, status, headers, config) {
     $scope.status = data.status; $scope.msg=data.msg
     console.log(data)
     $scope.getMiniView(1);
    })
    .error(function(data, status, headers, config) {

    }); 
}

/************ Updating an Item data  *****************/
$scope.updateItem = function(a) {
    if($scope.item.id == null)
    {
     $scope.status = 'error'; $scope.msg=' Please select a raw in left panel to update';
     return;
    }
    $http({
          method: "post",
          url: '/api/discipline/'+$scope.item.id+'/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#discipline').serialize()
    })
    .success(function(data, status, headers, config) {
     $scope.status = data.status; $scope.msg=data.msg
     console.log(data);
     $scope.getMiniView(1);
    })
    .error(function(data, status, headers, config) {
    }); 
}

/************ delete an Item data  *****************/
$scope.deleteItem = function(a){
  $http.delete("/api/discipline/"+a+"/")
      .success(function(data, status, headers, config) {
        $scope.item_list = data;
        $scope.status = data.status; $scope.msg=data.msg
        console.log(data);
        $scope.getMiniView(1);
      })
      .error(function(data, status, headers, config) {
        console.log('Error happen with status:'+status)
      });  
}

/*************** reset an item<used in form>***********************/
$scope.resetItem = function() {
  $scope.getItem($scope.item.id)
}


$scope.qsAccount= function(a) {
     $http.get("/api/discipline/qs/?q="+$scope.quick_search.in)
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.quick_search.out= data.res;
      $scope.status = data.status; $scope.msg=data.msg
      //addClass('#m2m-discipline','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }



});
/************ End of Discipline Controller*****************/


  
/************ start of Notice Controller*****************/
myApp.controller("NoticeController",  function ($scope,$http,$sce) { 

    $scope.renderHtml = function (htmlCode) {
            return $sce.trustAsHtml(htmlCode);
    };
/************ Initialize all Data Variable. *****************/
$scope.item ={}
$scope.item_list ={}
$scope.ref_list_items =[]
$scope.limit=10;

$scope.quick_search={'in':'','out':''}


/*********************  get MiniView *****************/
$scope.getMiniView=function(a) {
  $http.get("/api/notice/?page="+a+"&limit="+$scope.limit+"")
      .success(function(data, status, headers, config) {
        console.log(data)
        $scope.item_list = data.res;
        // DONT DO THIS BAD USER EXP$scope.status = data.status; $scope.msg=data.msg
        $scope.orderByField = 'id';
        $scope.reverseSort = false;
       // Not incduing this feature tableResize('#table_miniview_Notice');
      })
      .error(function(data, status, headers, config) { console.log('Error happen with status:'+status) });  
}
$scope.getMiniView(1);
/************ getting full data for an Item *****************/
$scope.getItem = function(a) {
     $http.get("/api/notice/"+a+"/")
    .success(function(data, status, headers, config) {
      console.log(data)
      $scope.item = data.res;
      $scope.status = data.status; $scope.msg=data.msg
    })
    .error(function(data, status, headers, config) {console.log('Error happen with status:'+status)}); 
  }

/************ creating a new Item  *****************/
$scope.createItem = function(a) {
    console.log($('form#notice').serialize())
    $http({
          method: "post",
          url: '/api/notice/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#notice').serialize()
    })
    .success(function(data, status, headers, config) {
     $scope.status = data.status; $scope.msg=data.msg
     console.log(data)
     $scope.getMiniView(1);
    })
    .error(function(data, status, headers, config) {

    }); 
}

/************ Updating an Item data  *****************/
$scope.updateItem = function(a) {
    if($scope.item.id == null)
    {
     $scope.status = 'error'; $scope.msg=' Please select a raw in left panel to update';
     return;
    }
    $http({
          method: "post",
          url: '/api/notice/'+$scope.item.id+'/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#notice').serialize()
    })
    .success(function(data, status, headers, config) {
     $scope.status = data.status; $scope.msg=data.msg
     console.log(data);
     $scope.getMiniView(1);
    })
    .error(function(data, status, headers, config) {
    }); 
}

/************ delete an Item data  *****************/
$scope.deleteItem = function(a){
  $http.delete("/api/notice/"+a+"/")
      .success(function(data, status, headers, config) {
        $scope.item_list = data;
        $scope.status = data.status; $scope.msg=data.msg
        console.log(data);
        $scope.getMiniView(1);
      })
      .error(function(data, status, headers, config) {
        console.log('Error happen with status:'+status)
      });  
}

/*************** reset an item<used in form>***********************/
$scope.resetItem = function() {
  $scope.getItem($scope.item.id)
}


$scope.qsAccount= function(a) {
     $http.get("/api/notice/qs/?q="+$scope.quick_search.in)
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.quick_search.out= data.res;
      $scope.status = data.status; $scope.msg=data.msg
      //addClass('#m2m-notice','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }



});
/************ End of Notice Controller*****************/


  
/************ start of Instrument Controller*****************/
myApp.controller("InstrumentController",  function ($scope,$http,$sce) { 

    $scope.renderHtml = function (htmlCode) {
            return $sce.trustAsHtml(htmlCode);
    };
/************ Initialize all Data Variable. *****************/
$scope.item ={}
$scope.item_list ={}
$scope.ref_list_items =[]
$scope.limit=10;

$scope.quick_search={'in':'','out':''}


/*********************  get MiniView *****************/
$scope.getMiniView=function(a) {
  $http.get("/api/instrument/?page="+a+"&limit="+$scope.limit+"")
      .success(function(data, status, headers, config) {
        console.log(data)
        $scope.item_list = data.res;
        // DONT DO THIS BAD USER EXP$scope.status = data.status; $scope.msg=data.msg
        $scope.orderByField = 'id';
        $scope.reverseSort = false;
       // Not incduing this feature tableResize('#table_miniview_Instrument');
      })
      .error(function(data, status, headers, config) { console.log('Error happen with status:'+status) });  
}
$scope.getMiniView(1);
/************ getting full data for an Item *****************/
$scope.getItem = function(a) {
     $http.get("/api/instrument/"+a+"/")
    .success(function(data, status, headers, config) {
      console.log(data)
      $scope.item = data.res;
      $scope.status = data.status; $scope.msg=data.msg
    })
    .error(function(data, status, headers, config) {console.log('Error happen with status:'+status)}); 
  }

/************ creating a new Item  *****************/
$scope.createItem = function(a) {
    console.log($('form#instrument').serialize())
    $http({
          method: "post",
          url: '/api/instrument/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#instrument').serialize()
    })
    .success(function(data, status, headers, config) {
     $scope.status = data.status; $scope.msg=data.msg
     console.log(data)
     $scope.getMiniView(1);
    })
    .error(function(data, status, headers, config) {

    }); 
}

/************ Updating an Item data  *****************/
$scope.updateItem = function(a) {
    if($scope.item.id == null)
    {
     $scope.status = 'error'; $scope.msg=' Please select a raw in left panel to update';
     return;
    }
    $http({
          method: "post",
          url: '/api/instrument/'+$scope.item.id+'/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#instrument').serialize()
    })
    .success(function(data, status, headers, config) {
     $scope.status = data.status; $scope.msg=data.msg
     console.log(data);
     $scope.getMiniView(1);
    })
    .error(function(data, status, headers, config) {
    }); 
}

/************ delete an Item data  *****************/
$scope.deleteItem = function(a){
  $http.delete("/api/instrument/"+a+"/")
      .success(function(data, status, headers, config) {
        $scope.item_list = data;
        $scope.status = data.status; $scope.msg=data.msg
        console.log(data);
        $scope.getMiniView(1);
      })
      .error(function(data, status, headers, config) {
        console.log('Error happen with status:'+status)
      });  
}

/*************** reset an item<used in form>***********************/
$scope.resetItem = function() {
  $scope.getItem($scope.item.id)
}


$scope.qsAccount= function(a) {
     $http.get("/api/instrument/qs/?q="+$scope.quick_search.in)
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.quick_search.out= data.res;
      $scope.status = data.status; $scope.msg=data.msg
      //addClass('#m2m-instrument','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }



});
/************ End of Instrument Controller*****************/



/*** End of JS file ***/

