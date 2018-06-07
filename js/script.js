alert("Viva!")

function isChecked(id){
    return document.getElementById(id).checked;
}

for(i = 0; i < 100; i++){
    checked = isChecked("check_"+(i/10+1)+"_"+(i%10));

}