from application import app

app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='development key',
    SQLALCHEMY_DATABASE_URI = 'mysql+gaerdbms:///snsdb?instance=likelion-pro:likelion-prog',
    migration_directory = 'migrations'
))
