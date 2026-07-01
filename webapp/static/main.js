const chat = document.getElementById('chat');
const form = document.getElementById('chat-form');
const input = document.getElementById('message');
const statusBox = document.getElementById('status');
let history = [];

function addMessage(role, content) {
  const div = document.createElement('div');
  div.className = `message ${role}`;
  div.textContent = content;
  chat.appendChild(div);
  chat.scrollTop = chat.scrollHeight;
}

async function checkHealth() {
  try {
    const res = await fetch('/health');
    const data = await res.json();
    statusBox.textContent = data.ollama ? `Ollama OK - ${data.model}` : 'Ollama indisponible';
  } catch {
    statusBox.textContent = 'API indisponible';
  }
}

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const message = input.value.trim();
  if (!message) return;

  addMessage('user', message);
  history.push({ role: 'user', content: message });
  input.value = '';
  form.querySelector('button').disabled = true;

  try {
    const res = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message, history })
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.detail || 'Erreur API');
    addMessage('assistant', data.answer);
    history.push({ role: 'assistant', content: data.answer });
  } catch (err) {
    addMessage('assistant', `Erreur : ${err.message}`);
  } finally {
    form.querySelector('button').disabled = false;
  }
});

checkHealth();
