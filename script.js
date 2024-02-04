const chatInput = document.querySelector(".chat-input input");
const sendButton = document.querySelector(".chat-input span");
const chatbox = document.querySelector(".chatbot-log");

let userMessage;

const createChatLi = (message, className) => {
    const chatLi = document.createElement("li");
    chatLi.classList.add("chat", className);
    console.log("chat", className)
    let chatContent = className == "output" ? `<p>${message}</p>`: `<span class="material-symbols-outlined">smart_toy</span> <p>${message}</p>`;
    chatLi.innerHTML = chatContent;
    return chatLi
}

const generateResponse = async (incomingChatLi) => {
    const messageElement = incomingChatLi.querySelector("p");
    console.log(messageElement)
    try {
        const response = await fetch('http://127.0.0.1:8080/bot', {
            method: 'GET',
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const responseData = await response.text();
        console.log(responseData);
        chatbox.appendChild(createChatLi(responseData.message, "intro"));
    } catch (error) {
        console.error('Error:', error);
    }
};

const handleChat = () => {
    userMessage = chatInput.value.trim();
    console.log(userMessage);
    
    if(!userMessage) return;
    // create chat List Item (users message) and append to chatbox
    chatbox.appendChild(createChatLi(userMessage, "output"));

    //bot output 
    setTimeout(() => {
        const incomingChatLi = createChatLi("Thinking...", "incoming")
        chatbox.appendChild(incomingChatLi)
        generateResponse(incomingChatLi);
    }, 600);

}

sendButton.addEventListener("click", handleChat);
