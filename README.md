# Campaign\_manager\_backend

Welcome to the **Campaign\_manager\_backend** project! This README provides an overview of the project structure, dependencies, instructions for getting started, and how to run the application.

---

## Table of Contents

* [Project Structure](#project-structure)
* [Dependencies](#dependencies)
* [Getting Started](#getting-started)
* [Running the Application](#running-the-application)
* [Contributing](#contributing)
* [License](#license)

---

## Project Structure

Below is a summary of the main files and folders in this repository (excluding `.pyc` caches and the `env` folder):

```
/Campaign_manager_backend/
├── requirements.txt
├── README.md
├── <other source files and folders>
```

> **Note:** The `env/` folder contains your virtual environment and is excluded from version control. `.pyc` files are also ignored.

---

## Dependencies

All Python dependencies are listed in `requirements.txt`. To install them, run:

```bash
pip install -r requirements.txt
```

---

## Getting Started

1. Clone the repository.
2. Set up your Python environment.
3. Install dependencies from `requirements.txt`.
4. Create a `.env` file.

> **Note:** This is where you configure the variable for `ALLOWED_ORIGIN` for handling **CORS**:

```
ALLOWED_ORIGIN=http://localhost:5173
```

---

## Running the Application

After installing the dependencies, you can run the application using:

```bash
python -m fastapi dev ./app/main.py
```

---

## Contributing

🚀 **Contribution Workflow**

This project uses a **stable `main`, integration `dev`, and personal developer branch workflow** for contributions:

✅ **Branch Workflow:**

1️⃣ **Branch off `dev` using your name:**

```bash
git checkout dev
git pull
git checkout -b <your-name>/dev
git push -u origin <your-name>/dev
```

2️⃣ **Create features off your personal branch:**

```bash
git checkout <your-name>/dev
git checkout -b feature/<feature-name>
# work, commit, push regularly
```

3️⃣ **Merge your feature branch into your personal branch:**

```bash
git checkout <your-name>/dev
git merge feature/<feature-name>
git push
```

4️⃣ **Keep your personal branch updated with `dev`:**

```bash
git checkout <your-name>/dev
git pull origin dev
git push
```

5️⃣ **When your work is ready, open a Pull Request from your personal branch to `dev`.**

6️⃣ After team review and testing, `dev` is periodically merged into `main` for releases.

✅ **Best Practices:**

* Write clear, meaningful commit messages (e.g., `feat: add JWT middleware`, `fix: handle token expiry`).
* Ensure tests and lint checks pass before opening a PR.
* Request a code review before merging.
* Use feature flags for incomplete work if needed.

---

## License

This project is licensed under the MIT License.

---
