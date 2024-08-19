from fastapi.middleware.cors import CORSMiddleware


origins = [
    'http://localhost:3000',
]

cors = {
    'middleware_class': CORSMiddleware,
    'allow_origins': origins,
    'allow_credentials': True,
    'allow_methods': ["*"],
    'allow_headers': ["*"],
}
