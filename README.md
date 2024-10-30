## Установка и запуск

```bash
git clone https://github.com/n1x1337/lb2_otrpo.git
cd lb2_otrpo
```

### Локальный запуск

```bash
pip install opencv-python-headless
python main.py
```

### Сборка образа и запуск
```bash
docker build -t face-detection-app .
docker run --rm face-detection-app
```

### Запуск образа с dockerhub
```bash
docker run --rm n1x1337/face-detection-app:latest
```
