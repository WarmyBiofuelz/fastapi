# 📝 FastAPI ToDo CRUD App – Step-by-Step Guide

This is a fully working FastAPI CRUD app for managing ToDos.  
It stores ToDos in memory, includes duplicate protection, and has a working REST API.

---

## ✅ 1. Create GitHub Repository

1. Go to [https://github.com/new](https://github.com/new)
2. Name your repo, e.g. `todos-fastapi`
3. Check ✅ "Add a README"
4. Check ✅ "Add .gitignore" → choose Python
5. Click **Create Repository**

---

## ✅ 2. Clone Repo with Cursor

1. Open Cursor
2. Press `Cmd+P` → type and choose `Git: Clone`
3. Paste your GitHub repo URL
4. Select folder, open it when asked

---

## ✅ 3. Create Local Project Folder

In Cursor terminal:

```bash
mkdir todos-homework
cd todos-homework
touch main.py
```

---

## ✅ 4. Initialize Project with uv

1. If you don't have `uv`, install it:

```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```

2. Create virtual environment:

```bash
uv venv
```

3. Activate it:
- On macOS/Linux:
```bash
source .venv/bin/activate
```
- On Windows:
```bash
.venv\Scripts\activate
```

4. Install FastAPI and Uvicorn:

```bash
uv pip install 'fastapi[all]' 'uvicorn[standard]'
```

---

## ✅ 5. Build Your FastAPI App

Paste this into `main.py`: *(see actual main.py in your repo)*

---

## ✅ 6. Run the Server

```bash
uvicorn main:app --reload
```

Server runs at:
- [http://127.0.0.1:8000](http://127.0.0.1:8000)
- API docs at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## ✅ 7. Test ToDo API in Swagger UI

Go to `/docs`, scroll to `POST /todos/` and click:

```json
{
  "name": "Learn FastAPI",
  "description": "Build a CRUD app for homework",
  "date": "2025-06-10"
}
```

Click Execute to create a todo.

---

## ✅ 8. Use curl from Terminal

Create a todo:

```bash
curl -X POST http://127.0.0.1:8000/todos/ \
-H "Content-Type: application/json" \
-d '{"name":"Write report","description":"Prepare Monday slides","date":"2025-06-10"}'
```

List all todos:

```bash
curl http://127.0.0.1:8000/todos/
```

Pretty print with `jq`:

```bash
brew install jq
curl http://127.0.0.1:8000/todos/ | jq
```

---

## ✅ 9. Commit & Push to GitHub

```bash
git add .
git commit -m "Complete FastAPI ToDo CRUD app with duplicate check"
git push
```

---

## ✅ 10. Done!

Congratulations! 🎉 You now have a working ToDo CRUD API with FastAPI.
