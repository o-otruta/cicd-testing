const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const port = 3000;

app.use(bodyParser.json());

// Дані (для прикладу)
let users = [
    { id: 1, name: "John Doe", email: "john@example.com" },
    { id: 2, name: "Jane Smith", email: "jane@example.com" }
];

// GET: отримати список користувачів
app.get('/api/users', (req, res) => {
    res.status(200).json(users);
});

// POST: створити нового користувача
app.post('/api/users', (req, res) => {
    const newUser = { id: users.length + 1, ...req.body };
    users.push(newUser);
    res.status(201).json(newUser);
});

// PUT: оновити користувача за ID
app.put('/api/users/:id', (req, res) => {
    const userId = parseInt(req.params.id);
    const userIndex = users.findIndex(u => u.id === userId);
    if (userIndex !== -1) {
        users[userIndex] = { id: userId, ...req.body };
        res.status(200).json(users[userIndex]);
    } else {
        res.status(404).json({ message: "User not found" });
    }
});

// DELETE: видалити користувача за ID
app.delete('/api/users/:id', (req, res) => {
    const userId = parseInt(req.params.id);
    users = users.filter(u => u.id !== userId);
    res.status(200).json({ message: "User deleted" });
});

// Запуск сервера
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
