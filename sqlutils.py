import sqlite3
import pandas as pd

DATABASE = 'crop.db'


def create_price_table():
	with sqlite3.connect(DATABASE) as conn:
		conn.execute('''CREATE TABLE IF NOT EXISTS crops_pricing (
						name TEXT PRIMARY KEY,
						seed_price REAL NOT NULL,
						sale_price REAL NOT NULL
					);
					''')
		conn.commit()
		cursor = conn.cursor()
		crops_info = [
			('Strawberry', 0.20, 4.50),
			('Watermelon', 0.15, 1.20),
			('Grapes', 0.10, 3.00),
			('Arugula', 0.02, 10.00),
			('Beet', 0.05, 4.00),
			('Chard', 0.03, 3.00),
			('Cress', 0.01, 12.00),
			('Endive', 0.02, 3.00),
			('Kale', 0.03, 3.50),
			('Lettuce', 0.02, 2.50),
			('Radicchio', 0.03, 6.00),
			('Spinach', 0.02, 4.00),
			('Tomatoes', 0.05, 2.50),
			('Eggplants', 0.05, 2.00),
			('Asparagus', 0.10, 5.00),
			('Chilli Peppers', 0.05, 8.00),
			('Cabbage', 0.02, 1.00),
			('Cucumbers', 0.04, 1.50),
			('Potatoes', 0.02, 0.70),
			('Cauliflowers', 0.04, 1.80),
			('Broccoli', 0.03, 2.20),
			('Green Peas', 0.02, 3.00)
		]

		cursor.executemany('''
			INSERT INTO crops_pricing (name, seed_price, sale_price)
			VALUES (?, ?, ?)
		''', crops_info)

		conn.commit()


def create_tables():
	with sqlite3.connect(DATABASE) as conn:
		conn.execute('''CREATE TABLE IF NOT EXISTS soil_data (
						id INTEGER PRIMARY KEY,
						name TEXT,
						fertility TEXT,
						photoperiod TEXT,
						temperature REAL,
						rainfall REAL,
						ph REAL,
						light_hours REAL,
						light_intensity REAL,
						rh REAL,
						nitrogen REAL,
						phosphorus REAL,
						potassium REAL,
						yield REAL,
						category_ph TEXT,
						soil_type TEXT,
						season TEXT,
						n_ratio REAL,
						p_ratio REAL,
						k_ratio REAL);
					''')
		
		conn.commit()
	create_price_table()


def insert_data(data: pd.DataFrame) -> None:
	with sqlite3.connect(DATABASE) as conn:
		data.to_sql('soil_data', conn, if_exists='replace', index=False)
		conn.commit()


def get_data(table: str) -> pd.DataFrame:
	with sqlite3.connect(DATABASE) as conn:
		df = pd.read_sql(f'SELECT * FROM {table}', conn)
	return df


def query_db(query: str) -> pd.DataFrame:
	with sqlite3.connect(DATABASE) as conn:
		df = pd.read_sql(query, conn)
	return df