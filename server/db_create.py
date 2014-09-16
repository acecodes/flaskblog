try:
	from app.server import db

except ImportError:
	from server import db

db.create_all()