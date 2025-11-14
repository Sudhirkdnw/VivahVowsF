import { useEffect, useMemo, useRef, useState } from 'react';

const WS_BASE = 'ws://localhost:8000/ws/chat';

export function useChatWebSocket(threadId) {
  const [messages, setMessages] = useState([]);
  const socketRef = useRef(null);
  const token = localStorage.getItem('accessToken');

  const url = useMemo(() => {
    if (!threadId) return null;
    const tokenParam = token ? `?token=${token}` : '';
    return `${WS_BASE}/${threadId}/${tokenParam}`;
  }, [threadId, token]);

  useEffect(() => {
    if (!url) return undefined;
    const socket = new WebSocket(url);
    socketRef.current = socket;

    socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      setMessages((prev) => [...prev, data]);
    };

    return () => {
      socket.close();
    };
  }, [url]);

  const sendMessage = (content) => {
    if (socketRef.current && socketRef.current.readyState === WebSocket.OPEN) {
      socketRef.current.send(JSON.stringify({ content }));
    }
  };

  return { messages, sendMessage };
}
