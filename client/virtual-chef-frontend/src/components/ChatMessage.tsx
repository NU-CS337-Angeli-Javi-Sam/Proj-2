import React from 'react';

interface ChatMessageProps {
  message: MessageType
}

const ChatMessage = ({ message }: ChatMessageProps) => {
  return (
    <div className={`bg-white border rounded-md p-3 m-2 break-words ${message.isUser ? 'text-left bg-gray-400' : 'text-right'}`}>
      {message.text}
    </div>
  );
};

export default ChatMessage;
