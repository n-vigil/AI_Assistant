const chatInput = document.querySelector(".chat-input input");
const sendButton = document.querySelector(".chat-input span");
const chatbox = document.querySelector(".chatbot-log");

let userMessage;

const createChatLi = (message, className) => {
    const chatLi = document.createElement("li");
    chatLi.classList.add("chat", className);
    let chatContent = className == "output" ? `<p>${message}</p>`: `<span class="material-symbols-outlined">smart_toy</span> <p>${message}</p>`;
    chatLi.innerHTML = chatContent;
    return chatLi
}


const generateResponse = async (incomingChatLi) => {
    // turn the thinking.. into p element
   // const messageElement = incomingChatLi.querySelector("p");
   try {
    const response = await fetch('http://127.0.0.1:8080/bot', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ question: userMessage }),
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const responseData = await response.json();
        console.log(responseData["answer"]);
        chatbox.appendChild(createChatLi(responseData["answer"], "intro"));
    } catch (error) {
        console.error('Error:', error);
    }
};

const handleChat = () => {
    userMessage = chatInput.value.trim();
    
    if(!userMessage) return;
    
    // create chat List Item (users message) and append to chatbox
    chatbox.appendChild(createChatLi(userMessage, "output"));

    //bot output 
    setTimeout(() => {
        const incomingChatLi = createChatLi("Thinking...", "incoming")
        chatbox.appendChild(incomingChatLi)
        generateResponse(userMessage);

    }, 600);

}

sendButton.addEventListener("click", handleChat);
