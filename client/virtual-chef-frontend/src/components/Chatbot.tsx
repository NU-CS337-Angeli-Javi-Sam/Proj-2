'use client'
import React, { useState, useRef, useEffect, ChangeEvent, KeyboardEvent } from 'react';
import ChatMessage from './ChatMessage';
import {BiSolidSend} from 'react-icons/bi'

const Chatbot = () => {
  const [messages, setMessages] = useState<Array<MessageType>>([]);
  const [userMessage, setUserMessage] = useState<string>('');
  const messageListRef = useRef(null);

  const handleUserMessage = (e: ChangeEvent<HTMLInputElement>) => {
    setUserMessage(e.target.value);
  };

  const handleSendMessage = () => {
    if (userMessage.trim() !== '') {
      setMessages([...messages, { text: userMessage, isUser: true }]);
      setUserMessage('');
      // You can add logic to send userMessage to your backend or API here.
    }
  };

  const handleKeyPress = (e: KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      handleSendMessage();
    }
  };

  useEffect(() => {
    // Example: Simulate a response from the "chatbot" (You would replace this with API calls to a GPT-3 model).
    if (messages.length % 2 === 1) {
      setTimeout(() => {
        setMessages([...messages, { text: 'This is a sample response.', isUser: false }]);
      }, 1000);
    }
    // Scroll to the bottom of the chat messages when a new message is added.
    // messageListRef && messageListRef.current && messageListRef.current.scrollTop = messageListRef.current.scrollHeight;
  }, [messages]);

  return (
    <div className="p-4 bg-gray-100 rounded-lg w-[50rem]">
      <div className="max-h-[38rem] overflow-y-auto" ref={messageListRef}>
        {messages.map((message, index) => (
          <ChatMessage key={index} message={message} />
        ))}
      </div>
      <div className="flex flex-1 p-2 rounded-md w-full">
        <input
          type="text"
          value={userMessage}
          placeholder="Type your message..."
          onChange={handleUserMessage}
          className='w-[95%] mr-4 rounded bg-slate-50 px-4'
          onKeyPress={handleKeyPress}
        />
        <button className='rounded h-8 w-8 flex justify-center items-center' onClick={handleSendMessage}><BiSolidSend className="w-6 h-6" /></button>
      </div>
    </div>
  );
};

export default Chatbot;
