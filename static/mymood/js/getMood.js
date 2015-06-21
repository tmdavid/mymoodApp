/**
 * Created by david on 6/21/15.
 */


$('#yourmoodform').on('submit', function(event){

    event.preventDefault();
    console.log("form submitted!")  // sanity check
    alert('do not reload');

    create_post();
});

function create_post(form_var){
    var text = document.getElementById("textform").value;
    alert(text)
    document.getElementById("Menu").value = text;
}


