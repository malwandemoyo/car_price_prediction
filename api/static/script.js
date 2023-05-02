mileage_box = document.getElementsByName('mileage')
year_box = document.getElementsByName('mileage')

// function isNumeric(event) {
//     var keyCode = event.which ? event.which : event.keyCode;
//     if (keyCode < 48 || keyCode > 57) {
//       event.preventDefault();
//       return false;
//     }
//     return true;
//   }

function isNumeric(e){
    let keyCode = e.which ? e.which: e.keyCode;
    if(keyCode < 48 || keyCode > 57){
        e.preventDefault()
        return false;
    }
    return true;
}