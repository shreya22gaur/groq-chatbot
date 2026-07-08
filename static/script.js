
const chatBox = document.getElementById("chat-box");
const input = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");
const clearBtn = document.getElementById("clear-btn");

// ----------------------
// Add message to screen
// ----------------------
function addMessage(role,text){

    const message=document.createElement("div");

    message.className=`message ${role==="user"?"user":"bot"}`;

    const bubble=document.createElement("div");

    bubble.className="bubble";

    bubble.innerHTML=text;

    message.appendChild(bubble);

    chatBox.appendChild(message);

    chatBox.scrollTop=chatBox.scrollHeight;

}


// ----------------------
// Load previous messages
// ----------------------
async function loadHistory() {

    const response = await fetch("/history");

    const history = await response.json();

    chatBox.innerHTML = "";

    history.forEach(msg => {

        if (msg.role === "system") return;

        addMessage(msg.role, msg.content);

    });

}


// ----------------------
// Send Message
// ----------------------
async function sendMessage() {

    const message = input.value.trim();

    if (message === "")
        return;

    addMessage("user", message);

    input.value = "";

    const response = await fetch("/chat", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            message: message
        })

    });

    const data = await response.json();

    addMessage("assistant", data.reply);

}


// ----------------------
// Clear Chat
// ----------------------
async function clearChat() {

    await fetch("/clear", {
        method: "POST"
    });

    chatBox.innerHTML = "";

}


// Button Click
sendBtn.addEventListener("click", sendMessage);

// Enter key
input.addEventListener("keypress", function(e){

    if(e.key==="Enter")
        sendMessage();

});

// Clear
clearBtn.addEventListener("click", clearChat);


// Load history on page open
loadHistory();