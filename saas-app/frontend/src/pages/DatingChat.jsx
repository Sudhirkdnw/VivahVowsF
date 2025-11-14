import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useParams } from 'react-router-dom';

import { appendMessage, fetchThreadMessages } from '../features/chat/chatSlice.js';
import { useChatWebSocket } from '../services/websocket.js';

function DatingChat() {
  const { threadId } = useParams();
  const dispatch = useDispatch();
  const [content, setContent] = useState('');
  const { messages: liveMessages, sendMessage } = useChatWebSocket(threadId);
  const storedMessages = useSelector((state) => state.chat.messages[threadId] ?? []);

  useEffect(() => {
    dispatch(fetchThreadMessages(threadId));
  }, [dispatch, threadId]);

  useEffect(() => {
    if (liveMessages.length) {
      const latest = liveMessages[liveMessages.length - 1];
      dispatch(appendMessage({ threadId, message: latest }));
    }
  }, [liveMessages, threadId, dispatch]);

  const handleSubmit = (event) => {
    event.preventDefault();
    if (!content) return;
    sendMessage(content);
    setContent('');
  };

  const allMessages = [...storedMessages];

  return (
    <div className="max-w-3xl space-y-4">
      <h1 className="text-xl font-semibold text-slate-800">Chat</h1>
      <div className="bg-white rounded-xl shadow p-6 h-96 overflow-y-auto space-y-3">
        {allMessages.map((message) => (
          <div key={message.id} className="bg-indigo-50 rounded-lg p-3">
            <p className="text-xs text-slate-500">{message.sender?.username}</p>
            <p className="text-sm text-slate-700">{message.content}</p>
          </div>
        ))}
      </div>
      <form className="flex gap-3" onSubmit={handleSubmit}>
        <input
          value={content}
          onChange={(event) => setContent(event.target.value)}
          className="flex-1 border border-slate-200 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-400"
          placeholder="Type your message..."
        />
        <button type="submit" className="bg-indigo-500 hover:bg-indigo-600 text-white px-4 py-2 rounded-lg">
          Send
        </button>
      </form>
    </div>
  );
}

export default DatingChat;
