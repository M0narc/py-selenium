FROM debian:bullseye-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copiamos primero para instalar deps
COPY requirements.txt .

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip python3-venv \
    wget curl unzip gnupg ca-certificates \
    openjdk-11-jre-headless \
    fonts-liberation libasound2 libatk-bridge2.0-0 libatk1.0-0 libc6 \
    libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 \
    libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libnss3 libpango-1.0-0 \
    libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 \
    libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 \
    libxss1 libxtst6 xdg-utils \
    && wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google.gpg \
    && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends google-chrome-stable \
    && CHROMEDRIVER_VERSION=$(curl -sS https://chromedriver.storage.googleapis.com/LATEST_RELEASE) \
    && wget -O /tmp/chromedriver.zip "https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip" \
    && unzip /tmp/chromedriver.zip -d /usr/local/bin/ \
    && chmod +x /usr/local/bin/chromedriver \
    && ALLURE_VERSION=$(curl -s https://api.github.com/repos/allure-framework/allure2/releases/latest | grep tag_name | cut -d '"' -f 4) \
    && wget -O /tmp/allure.zip https://github.com/allure-framework/allure2/releases/download/${ALLURE_VERSION}/allure-${ALLURE_VERSION#v}.zip \
    && unzip /tmp/allure.zip -d /opt/ \
    && ln -s /opt/allure-${ALLURE_VERSION#v}/bin/allure /usr/bin/allure \
    && pip3 install --no-cache-dir -r requirements.txt \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY . .

CMD ["pytest", "--browser=chrome", "--headless", "--alluredir=allure-results"]
