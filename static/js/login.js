var i = 0;
document.getElementById("id_username").addEventListener("click", clickNumber());


function clickNumber() {
    console.log(i);
}

function addClick() {
    let e = document.getElementById('id_usersname')
    console.log(e);
    clickNumber();
    document.getElementById('id_username').click();
}

console.log('a');
// let e = document.querySelectorAll("div label");
let labels = document.getElementsByTagName("labels");
let inputs = document.getElementsByTagName("input");
// console.log(e[0])


// for (i = 0; i < inputs.length; i++) {
//     inputs[i].addEventListener("click", function() {
//         this.classList.toggle("active");
//         let label = document.getElementsByTagName("labels")[i]
//         if (label.style.display === "block") {
//             dropdownContent.style.display = "none";
//         } else {
//             dropdownContent.style.display = "block";
//         }
//     });
//     console.log(labels[i]);
// }

console.log('end');