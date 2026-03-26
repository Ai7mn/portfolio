<h1 align="center">Aiman Daba - Elite Open-Source Portfolio 🚀</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white" />
</p>

A production-grade, highly-optimized showcase built with Django. Designed for elite architectural patterns, AI-integrated features, and superior UI/UX with global accessibility.

## ✨ Features

- **Modular Architecture**: Built with multiple apps (`core`, `portfolio`, `blog`, `api`) utilizing best practices.
- **Headless-Ready API**: Features a robust RESTful API built on the Django REST Framework.
- **AI Chatbot Service**: Seamless integration with the Gemini API to serve professional inquiries.
- **Glassmorphism Theme Engine**: Features Lottie micro-interactions, AOS.js scrolling, and persistent Dark/Light themes.
- **Global Accessibility (i18n)**: Fully internationalized with English (LTR) and Arabic (RTL) support.
- **High-Performance Assets**: Automatically converts uploaded images to optimized `WebP` files to ensure a 100/100 Lighthouse score.
- **Real-Time GitHub Metrics**: A dashboard that synchronizes real-time metrics using the GitHub GraphQL API.
- **Production-Grade DevOps**: Includes multi-stage Docker builds, docker-compose, and GitHub Actions CI pipelines.

## 🚀 Quick Deployment

Click the button below to deploy this application seamlessly via Render.

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

## 🗺️ Roadmap

- [x] Phase 1: Architectural Reconstruction (Backend & DevOps)
- [x] Phase 2: Luxurious UI/UX & I18N
- [x] Phase 3: The "Star-Magnet" Features (AI, GitHub APIs, WebP optimizations)
- [ ] Phase 4: Developer Experience (Interactive README & Docs)
- [ ] Phase 5: Additional test coverage & E2E Verification.

## 🛠️ Local Installation

### Prerequisites
- Python 3.10+
- Docker & docker-compose

### Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/aimandaba/portfolio.git
   cd portfolio
   ```

2. **Configure Environment Variables:**
   Copy the example environment variables file and configure it as needed.
   ```bash
   cp .env.example .env
   ```

3. **Deploy using Docker Compose:**
   ```bash
   docker-compose up --build
   ```

4. **Run Migrations (if running locally without Docker):**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start Development Server:**
   ```bash
   python manage.py runserver
   ```
