// Just for the sake of if I will try using two spaces for ident insted of 4;

function DayOfWeek(input) {
  let day = Number(input.shift());

  switch(day) {
    case 1: 
      console.log('Monday'); 
      break;
    case 2: 
      console.log('Tuesday'); 
      break;
    case 3: 
      console.log('Wednesday'); 
      break;
    case 4: 
      console.log('Thursday'); 
      break;
    case 5: 
      console.log('Friday'); 
      break;
    case 6: 
      console.log('Saturday'); 
      break;
    case 7: 
      console.log('Sunday'); 
      break;
    default: 
      console.log("Error"); 
  }
}

// No expexted outputs here!
DayOfWeek(['-1']);
