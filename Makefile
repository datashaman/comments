run:
	FLASK_APP=comments FLASK_ENV=development flask run

db-reset:
	rm comments/data/comments.db

db-seed:
	python -m comments.seed
