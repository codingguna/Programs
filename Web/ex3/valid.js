function compValidate() {
    
    var fname = document.forms["comp"]["fname"].value;
    if (fname == "") {
      alert("Please enter your first name");
      return false;
    }
    
    return true;
  }