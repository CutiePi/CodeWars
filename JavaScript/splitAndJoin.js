function split(arr){
    //coding and coding..
    var output = [];
    var partone = [];
    var parttwo = [];
    for(var i=0;i<arr.length;i++){
        for(var  j=0;j<arr[i].length;j++){
        partone.push(arr[i][j]);
        }
        parttwo.push([arr[i].length]);
    }
    output.push(partone);
    output.push(parttwo);
    return output;
  }
  
  function join(arr1,arr2){
    //coding and coding..
    var output = [];
    var arr1index = 0;
    for(var i=0;i<arr2.length;i++){
       var insertion = [];
         for(var z = 0;z<arr2[i][0];z++,arr1index++){
         insertion.push(arr1[arr1index]);
     }
            output.push(insertion);
    }
    return output;
   
  }