
  //a function that takes a number as an input and returns that number seperated by commas e.g 1000 -> 1,000
function numberWithCommas(number) {
          return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

 // a function that is used to compare 2 object's country property (used to sort countries alphabetically)
function compare( a, b ) {

  if ( a.country < b.country){
    return -1;
  }
  else if ( a.country > b.country ){
    return 1;
  }

  return 0;
}



