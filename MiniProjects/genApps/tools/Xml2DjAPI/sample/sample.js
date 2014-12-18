
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






  
/************ start of Author Controller*****************/
myApp.controller("AuthorController",  function ($scope,$http,$sce) { 

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
  $http.get("/api/author/?page="+a+"&limit="+$scope.limit+"")
      .success(function(data, status, headers, config) {
        console.log(data)
        $scope.item_list = data.res;
        // DONT DO THIS BAD USER EXP$scope.status = data.status; $scope.msg=data.msg
        $scope.orderByField = 'id';
        $scope.reverseSort = false;
       // Not incduing this feature tableResize('#table_miniview_Author');
      })
      .error(function(data, status, headers, config) { console.log('Error happen with status:'+status) });  
}
$scope.getMiniView(1);
/************ getting full data for an Item *****************/
$scope.getItem = function(a) {
     $http.get("/api/author/"+a+"/")
    .success(function(data, status, headers, config) {
      console.log(data)
      $scope.item = data.res;
      $scope.status = data.status; $scope.msg=data.msg
    })
    .error(function(data, status, headers, config) {console.log('Error happen with status:'+status)}); 
  }

/************ creating a new Item  *****************/
$scope.createItem = function(a) {
    console.log($('form#author').serialize())
    $http({
          method: "post",
          url: '/api/author/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#author').serialize()
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
          url: '/api/author/'+$scope.item.id+'/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#author').serialize()
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
  $http.delete("/api/author/"+a+"/")
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


$scope.getBook = function(a) {
     $http.get("/api/author/"+a+"/book/")
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = data.res;
      $scope.ref_list_items = {};
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#o2o-author','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }


$scope.qsBook= function(a) {
     $http.get("/api/author/qs/?q="+$scope.quick_search.in)
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.quick_search.out= data.res;
      $scope.status = data.status; $scope.msg=data.msg
      //addClass('#m2m-author','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }



});
/************ End of Author Controller*****************/


  
/************ start of Publication Controller*****************/
myApp.controller("PublicationController",  function ($scope,$http,$sce) { 

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
  $http.get("/api/publication/?page="+a+"&limit="+$scope.limit+"")
      .success(function(data, status, headers, config) {
        console.log(data)
        $scope.item_list = data.res;
        // DONT DO THIS BAD USER EXP$scope.status = data.status; $scope.msg=data.msg
        $scope.orderByField = 'id';
        $scope.reverseSort = false;
       // Not incduing this feature tableResize('#table_miniview_Publication');
      })
      .error(function(data, status, headers, config) { console.log('Error happen with status:'+status) });  
}
$scope.getMiniView(1);
/************ getting full data for an Item *****************/
$scope.getItem = function(a) {
     $http.get("/api/publication/"+a+"/")
    .success(function(data, status, headers, config) {
      console.log(data)
      $scope.item = data.res;
      $scope.status = data.status; $scope.msg=data.msg
    })
    .error(function(data, status, headers, config) {console.log('Error happen with status:'+status)}); 
  }

/************ creating a new Item  *****************/
$scope.createItem = function(a) {
    console.log($('form#publication').serialize())
    $http({
          method: "post",
          url: '/api/publication/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#publication').serialize()
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
          url: '/api/publication/'+$scope.item.id+'/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#publication').serialize()
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
  $http.delete("/api/publication/"+a+"/")
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


$scope.getBook = function(a) {
     $http.get("/api/publication/"+a+"/book/")
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = data.res;
      $scope.ref_list_items = {};
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#o2o-publication','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }


$scope.qsBook= function(a) {
     $http.get("/api/publication/qs/?q="+$scope.quick_search.in)
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.quick_search.out= data.res;
      $scope.status = data.status; $scope.msg=data.msg
      //addClass('#m2m-publication','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }



});
/************ End of Publication Controller*****************/


  
/************ start of TOC Controller*****************/
myApp.controller("TOCController",  function ($scope,$http,$sce) { 

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
  $http.get("/api/toc/?page="+a+"&limit="+$scope.limit+"")
      .success(function(data, status, headers, config) {
        console.log(data)
        $scope.item_list = data.res;
        // DONT DO THIS BAD USER EXP$scope.status = data.status; $scope.msg=data.msg
        $scope.orderByField = 'id';
        $scope.reverseSort = false;
       // Not incduing this feature tableResize('#table_miniview_TOC');
      })
      .error(function(data, status, headers, config) { console.log('Error happen with status:'+status) });  
}
$scope.getMiniView(1);
/************ getting full data for an Item *****************/
$scope.getItem = function(a) {
     $http.get("/api/toc/"+a+"/")
    .success(function(data, status, headers, config) {
      console.log(data)
      $scope.item = data.res;
      $scope.status = data.status; $scope.msg=data.msg
    })
    .error(function(data, status, headers, config) {console.log('Error happen with status:'+status)}); 
  }

/************ creating a new Item  *****************/
$scope.createItem = function(a) {
    console.log($('form#toc').serialize())
    $http({
          method: "post",
          url: '/api/toc/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#toc').serialize()
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
          url: '/api/toc/'+$scope.item.id+'/',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:$('form#toc').serialize()
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
  $http.delete("/api/toc/"+a+"/")
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


$scope.getBook = function(a) {
     $http.get("/api/toc/"+a+"/book/")
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = data.res;
      $scope.ref_list_items = {};
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#o2o-toc','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }


$scope.qsBook= function(a) {
     $http.get("/api/toc/qs/?q="+$scope.quick_search.in)
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.quick_search.out= data.res;
      $scope.status = data.status; $scope.msg=data.msg
      //addClass('#m2m-toc','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }



});
/************ End of TOC Controller*****************/


  
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


$scope.getTOC = function(a) {
     $http.get("/api/book/"+a+"/toc/")
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = data.res;
      $scope.ref_list_items = {};
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#o2o-book','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }


//Get
$scope.getAuthor= function(a) {
     $http.get("/api/book/"+a+"/author/")
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = {}
      $scope.ref_list_items = data.res;
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#m2m-book','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }
//Add + remove
$scope.addAuthor= function(a,b,c) {
    $http({
          method: "post",
          url: "/api/book/"+a+"/author/",
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:{author: b, action: c}
    })
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = {}
      $scope.ref_list_items = data.res;
      $scope.status = data.status; $scope.msg=data.msg
     
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
    //repopulate..
    $scope.getAuthor;
  }


//Get
$scope.getPublication= function(a) {
     $http.get("/api/book/"+a+"/publication/")
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = {}
      $scope.ref_list_items = data.res;
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#m2m-book','show');
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
  }
//Add + remove
$scope.addPublication= function(a,b,c) {
    $http({
          method: "post",
          url: "/api/book/"+a+"/publication/",
          headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
          data:{publication: b, action: c}
    })
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.ref_item = {}
      $scope.ref_list_items = data.res;
      $scope.status = data.status; $scope.msg=data.msg
     
    })
    .error(function(data, status, headers, config) { console.log('Error happen with status:'+status)}); 
    //repopulate..
    $scope.getPublication;
  }


$scope.qsPublication= function(a) {
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



/*** End of JS file ***/

