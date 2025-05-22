# py-selenium
selenium framework para trabajar trabajar sobre cualquier sitio.
* Patron de diseño POM
* Usamos webdriver_manager para manejar los browsers
* Allure para guardar informacion
* dotenv para secret keys (todavia no hay ninguna)
* pytest y pytest-html
* request para usar apis mas adelante
* pandas y faker, instalado, ya que este va a ser un esqueleto para futuros proyectos.
* implementamos loggers para trazabilidad


# Run tests through console ->
pytest --browser=chrome
 o
pytest --browser=firefox

# If you want to run a particular test on the console you can do it like this ->

pytest tests/login/test_login.py --browser=chrome

# if you want to run it and see the logs

pytest -s tests/home/test_home_page.py --browser=chrome

# If you want to run it, see the logs and make it headless

pytest -s tests/home/test_home_page.py --browser=chrome --headless


# Using the Makefile

make test

make test-headless

make test-ci


# TODO
Allure para reportes detallados: pytest --alluredir=allure-results

Integración con Docker para ejecución aislada

Uso de .env para credenciales

Test Data Factories (con Faker)




# Esqueleto

selenium_framework/
├── conftest.py                     # Configuraciones globales para pytest
├── requirements.txt               # Dependencias
├── pytest.ini                     # Configuración de pytest
├── Makefile                       # Comandos útiles (opcional pero recomendado)
├── .env                           # Variables sensibles
├── .github/
│   └── workflows/
│       └── ci.yml                 # Integración continua con GitHub Actions
├── config/
│   └── config.py                  # Variables de entorno, rutas, etc.
├── drivers/
│   └── driver_factory.py          # Inicialización de WebDrivers
├── pages/
│   ├── base_page.py               # Page Object base (métodos comunes)
│   ├── login_page.py              # Ejemplo concreto de una página
│   └── dashboard_page.py          # Otra página
├── tests/
│   ├── test_login.py              # Test usando el login_page
│   └── test_dashboard.py
├── utils/
│   ├── logger.py                  # Logger custom
│   └── helpers.py                 # Funciones utilitarias (por ejemplo, waits)
├── reports/
│   └── report.html                # Resultados (allure o html)
└── data/
    └── users.json                 # Datos de prueba (puede venir de Excel, CSV, etc.)