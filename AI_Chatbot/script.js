document.addEventListener('DOMContentLoaded', () => {
    const chatBox = document.getElementById('chat-box');
    const userInput = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');
    const themeToggle = document.getElementById('theme-toggle');
    const clearChat = document.getElementById('clear-chat');
    
    // Initialize Theme
    const currentTheme = localStorage.getItem('theme') || 'dark';
    document.documentElement.setAttribute('data-theme', currentTheme);
    updateThemeIcon(currentTheme);

    // Initial Welcome Message
    setTimeout(() => {
        addMessage("Hello! I am DecodeBot AI 🤖", false);
    }, 500);

    // Theme Toggle Logic
    themeToggle.addEventListener('click', () => {
        let theme = document.documentElement.getAttribute('data-theme');
        theme = theme === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);
        updateThemeIcon(theme);
    });

    function updateThemeIcon(theme) {
        const icon = themeToggle.querySelector('i');
        if (theme === 'dark') {
            icon.className = 'fa-solid fa-sun';
        } else {
            icon.className = 'fa-solid fa-moon';
        }
    }

    // Clear Chat Logic
    clearChat.addEventListener('click', () => {
        chatBox.innerHTML = '';
        setTimeout(() => {
            addMessage("Chat cleared. Hello! I am DecodeBot AI 🤖", false);
        }, 300);
    });

    function getTimestamp() {
        const now = new Date();
        let hours = now.getHours();
        let minutes = now.getMinutes();
        const ampm = hours >= 12 ? 'PM' : 'AM';
        hours = hours % 12;
        hours = hours ? hours : 12; 
        minutes = minutes < 10 ? '0' + minutes : minutes;
        return `${hours}:${minutes} ${ampm}`;
    }

    function scrollToBottom() {
        chatBox.scrollTo({
            top: chatBox.scrollHeight,
            behavior: 'smooth'
        });
    }

    function addMessage(message, isUser = false) {
        const wrapperDiv = document.createElement('div');
        wrapperDiv.className = `message-wrapper ${isUser ? 'user-message' : 'bot-message'}`;
        
        const avatarHtml = isUser 
            ? '' 
            : `<div class="avatar"><i class="fa-solid fa-robot"></i></div>`;
        
        wrapperDiv.innerHTML = `
            <div class="message">
                ${avatarHtml}
                <div class="content">
                    <p>${message}</p>
                </div>
            </div>
            <div class="timestamp">${getTimestamp()}</div>
        `;
        
        chatBox.appendChild(wrapperDiv);
        scrollToBottom();
    }

    function addTypingIndicator() {
        const wrapperDiv = document.createElement('div');
        wrapperDiv.className = 'message-wrapper bot-message';
        wrapperDiv.id = 'typing-indicator';
        
        wrapperDiv.innerHTML = `
            <div class="message">
                <div class="avatar"><i class="fa-solid fa-robot"></i></div>
                <div class="content" style="padding: 12px 18px;">
                    <div class="typing-indicator">
                        <div class="dot"></div>
                        <div class="dot"></div>
                        <div class="dot"></div>
                    </div>
                </div>
            </div>
        `;
        chatBox.appendChild(wrapperDiv);
        scrollToBottom();
    }

    function removeTypingIndicator() {
        const typingDiv = document.getElementById('typing-indicator');
        if (typingDiv) {
            typingDiv.remove();
        }
    }

    async function sendMessage() {
        const message = userInput.value.trim();
        if (!message) return;

        // Add user message
        addMessage(message, true);
        userInput.value = '';
        userInput.focus();

        // Add bot typing indicator
        addTypingIndicator();

        try {
            const response = await fetch('/get', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message })
            });
            
            const data = await response.json();
            
            // Artificial delay to simulate thinking/typing
            setTimeout(() => {
                removeTypingIndicator();
                addMessage(data.response, false);
            }, 800 + Math.random() * 700);

        } catch (error) {
            console.error('Error:', error);
            removeTypingIndicator();
            addMessage("Sorry, I encountered a network error. Please try again.", false);
        }
    }

    sendBtn.addEventListener('click', sendMessage);

    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            e.preventDefault();
            sendMessage();
        }
    });
    
    // Focus input on load
    userInput.focus();
});
