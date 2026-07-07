
const input = document.getElementById("message");

input.addEventListener("keypress", function(event){

    if(event.key==="Enter"){
        sendMessage();
    }

});


async function sendMessage(){

    const message=input.value.trim();

    if(message==="") return;

    const chat=document.getElementById("chat-box");

    chat.innerHTML +=
    `<p class="user"><b>You:</b> ${message}</p>`;

    input.value="";

    chat.innerHTML +=
    `<p id="typing"><i>AI is typing...</i></p>`;

    chat.scrollTop=chat.scrollHeight;

    const response = await fetch("/chat",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({
            message:message
        })

    });

    const data = await response.json();

    document.getElementById("typing").remove();

    chat.innerHTML +=
    `<p class="bot"><b>Bot:</b> ${data.reply}</p>`;

    chat.scrollTop=chat.scrollHeight;

}


async function clearChat(){

    await fetch("/clear",{
        method:"POST"
    });

    document.getElementById("chat-box").innerHTML="";
}


