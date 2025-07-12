# 🧩 Django Basic Boilerplate

A clean and minimal Django boilerplate to kickstart new projects — now with Tailwind CSS integration and a structured setup for settings, apps, templates, and static files.

---

## 🚀 Features

- Modular Django settings
- Pre-configured app layout
- Tailwind CSS via `django-tailwind`
- Structured templates and static directories
- Environment variable support via `.env`
- Ready-to-scale project architecture

---

## 🖌️ Styling & Frontend

- Integrated [Django-Tailwind](https://django-tailwind.readthedocs.io/en/latest/) for utility-first CSS styling.
- Hot-reload support for Tailwind during development.
- Custom static directory setup for additional CSS, JS, and image assets.

---

## 📁 Project Structure

```
Project
├── LICENSE
├── manage.py
├── project
│   ├── app/
│   ├── Django-Boilerplate/  # Tailwind app
│   ├── static/              # Static files (e.g., CSS, JS)
│   ├── templates/           # HTML templates
│   ├── db.sqlite3
│   └── project/
│       ├── settings.py
│       ├── urls.py
│       ├── wsgi.py
│       └── ...
├── requirements.txt
├── tailwind.config.js
├── postcss.config.js
├── .env
└── README.md
```

---

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/kushalyadav0/Django-Boilerplate.git
cd Django-Boilerplate
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Setup `.env`

Create a `.env` file:

```env
SECRET_KEY=your-django-secret-key
DEBUG=True
```

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Tailwind Setup

Install Tailwind dependencies inside the Tailwind app directory:

```bash
python manage.py tailwind install
```

Run Tailwind in dev mode (with hot reload):

```bash
python manage.py tailwind start
```

### 7. Start Development Server

In a **separate terminal**, run:

```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000

---

## 🧪 Testing Tailwind

Make sure your template extends `base.html` and uses Tailwind classes. Example:

```html
<h1 class="text-3xl font-bold text-blue-600">Hello, Tailwind!</h1>
```

---

## 🔐 Environment Variables

Use the `.env` file to store secrets and configuration:

```env
SECRET_KEY=...
DEBUG=True
DATABASE_URL=...
```

---

## 🪪 License

This project is licensed under the [MIT License](LICENSE).
