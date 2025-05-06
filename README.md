# 🧮 Matrix Multiplication using OpenMP, AngularJS, and Docker

This project demonstrates parallel matrix multiplication using OpenMP in C, wrapped with a Python Flask backend, and an AngularJS frontend. The entire application is containerized using Docker.

---

## 🚀 Clone This Project

To clone this repository:

```bash
git clone https://github.com/sameekshya1999/Matrix-Multiplication-using-OpenMP.git
cd Matrix-Multiplication-using-OpenMP
```

---

## 🐳 Run the App Using Docker

Make sure Docker is installed and running.

### 🔧 Build Docker Image

```bash
docker build -t matrix-app .
```

### ▶️ Run the Container

```bash
docker run -d -p 5000:5000 --name matrix-container matrix-app
```

---

## 🌐 Access the Web Interface

Open your browser and go to:

```
http://localhost:5000
```

If you're running it on a remote server, replace `localhost` with the server's IP.

---

## 🛠 Technologies Used

- 🧠 C with OpenMP (for parallel matrix multiplication)
- 🐍 Python Flask (as backend API)
- 💻 AngularJS (for frontend interaction)
- 🐳 Docker (for containerization)
