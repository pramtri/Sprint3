DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "provesi_db",
        "USER": "provesi_user",
        "PASSWORD": "isis2503",
        "HOST": "provesi-db.c1ikg4aowpxo.us-east-1.rds.amazonaws.com",
        "PORT": "5432",
    }
}
ALLOWED_HOSTS = ["*",]  # para pruebas

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'inventory.apps.InventoryConfig',
    'social_django',
    'management',
    'inventory',
]

ROOT_URLCONF = 'provesi.urls'

WSGI_APPLICATION = 'provesi.wsgi.application'
ALLOWED_HOSTS = ['*']


SOCIAL_AUTH_TRAILING_SLASH = False
SOCIAL_AUTH_AUTH0_DOMAIN = 'dev-wdbajyjynfqnfhfb.us.auth0.com'
SOCIAL_AUTH_AUTH0_KEY = 'i9EUeCXJJfbLcc3PUEnYKpjPBOcPBfGR'
SOCIAL_AUTH_AUTH0_SECRET = 'XGECXfhr7vnal_I1-pOonLIqLmYc0sahEQG0ApkXWJx5I3CCE6LYty9dIY-vv4-l'
SOCIAL_AUTH_AUTH0_SCOPE = ['openid', 'profile', 'email', 'role',]

AUTHENTICATION_BACKENDS = {
    'provesi.auth0backend.Auth0',
    'django.contrib.auth.backends.ModelBackend',
}

LOGIN_URL = "/login/auth0"
LOGIN_REDIRECT_URL = "/orders/" 
LOGOUT_REDIRECT_URL = "/" 

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware', # Vital para Auth0
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Vital para request.user
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware', # Manejo de errores Auth0
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [], # Django buscará en carpetas 'templates' dentro de las apps
        'APP_DIRS': True, # Esto debe estar en True
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]
