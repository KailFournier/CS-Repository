import sqlite3
import random
import matplotlib.pyplot as plt


def create_and_populate_db():
    # Connect to SQLite database (creates if doesn't exist)
    conn = sqlite3.connect('population_KF.db')
    cursor = conn.cursor()

    # Create population table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    ''')

    # 10 Florida cities with 2023 population data (approximate)
    # Replaced Pembroke Pines and Hialeah with North Port and Port Charlotte
    initial_data = [
        ('Miami', 2023, 449514),
        ('Tampa', 2023, 398173),
        ('Orlando', 2023, 316081),
        ('Jacksonville', 2023, 970021),
        ('St. Petersburg', 2023, 259043),
        ('North Port', 2023, 85426),  # Approximate 2023 population
        ('Fort Lauderdale', 2023, 182760),
        ('Tallahassee', 2023, 201731),
        ('Cape Coral', 2023, 216992),
        ('Port Charlotte', 2023, 62640)  # Approximate 2023 population
    ]

    # Insert initial 2023 data
    cursor.executemany('INSERT INTO population (city, year, population) VALUES (?, ?, ?)', initial_data)
    conn.commit()
    conn.close()


def simulate_population_growth():
    conn = sqlite3.connect('population_KF.db')
    cursor = conn.cursor()

    # Get all cities
    cursor.execute('SELECT DISTINCT city FROM population')
    cities = [row[0] for row in cursor.fetchall()]

    for city in cities:
        cursor.execute('SELECT population FROM population WHERE city = ? AND year = 2023', (city,))
        current_pop = cursor.fetchone()[0]

        # Simulate population for 2024-2043
        for year in range(2024, 2044):
            # Random growth rate between -2% and +3% annually
            growth_rate = random.uniform(-0.02, 0.03)
            current_pop = int(current_pop * (1 + growth_rate))

            # Insert new population data
            cursor.execute('INSERT INTO population (city, year, population) VALUES (?, ?, ?)',
                           (city, year, current_pop))

    conn.commit()
    conn.close()


def plot_population_growth():
    import sqlite3
    import random
    import matplotlib.pyplot as plt

    def create_and_populate_db():
        # Connect to SQLite database (creates if doesn't exist)
        conn = sqlite3.connect('population_KF.db')
        cursor = conn.cursor()

        # Create population table with UNIQUE constraint on city and year
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS population (
                city TEXT,
                year INTEGER,
                population INTEGER,
                UNIQUE(city, year)
            )
        ''')

        # 10 Florida cities with 2023 population data (approximate)
        initial_data = [
            ('Miami', 2023, 449514),
            ('Tampa', 2023, 398173),
            ('Orlando', 2023, 316081),
            ('Jacksonville', 2023, 970021),
            ('St. Petersburg', 2023, 259043),
            ('North Port', 2023, 85426),
            ('Fort Lauderdale', 2023, 182760),
            ('Tallahassee', 2023, 201731),
            ('Cape Coral', 2023, 216992),
            ('Port Charlotte', 2023, 62640)
        ]

        # Insert initial 2023 data, ignore duplicates
        cursor.executemany('INSERT OR IGNORE INTO population (city, year, population) VALUES (?, ?, ?)', initial_data)
        conn.commit()
        conn.close()

    def simulate_population_growth():
        conn = sqlite3.connect('population_KF.db')
        cursor = conn.cursor()

        # Clear existing data for years >= 2024 to prevent duplicates
        cursor.execute('DELETE FROM population WHERE year >= 2024')

        # Get all cities
        cursor.execute('SELECT DISTINCT city FROM population')
        cities = [row[0] for row in cursor.fetchall()]

        for city in cities:
            cursor.execute('SELECT population FROM population WHERE city = ? AND year = 2023', (city,))
            current_pop = cursor.fetchone()[0]

            # Simulate population for 2024-2043
            for year in range(2024, 2044):
                # Random growth rate between -2% and +3% annually
                growth_rate = random.uniform(-0.02, 0.03)
                current_pop = int(current_pop * (1 + growth_rate))

                # Insert new population data
                cursor.execute('INSERT OR IGNORE INTO population (city, year, population) VALUES (?, ?, ?)',
                               (city, year, current_pop))

        conn.commit()
        conn.close()

    def plot_population_growth():
        # Connect to database
        conn = sqlite3.connect('population_KF.db')
        cursor = conn.cursor()

        # Get list of cities
        cursor.execute('SELECT DISTINCT city FROM population')
        cities = [row[0] for row in cursor.fetchall()]

        # Display city options
        print("Available cities:", ", ".join(cities))
        selected_city = input("Please choose a city from the list above: ").strip()

        # Validate city selection
        if selected_city not in cities:
            print("Invalid city selection!")
            conn.close()
            return

        # Fetch population data for selected city
        cursor.execute('SELECT year, population FROM population WHERE city = ? ORDER BY year',
                       (selected_city,))
        data = cursor.fetchall()

        # Separate years and populations
        years = [row[0] for row in data]
        populations = [row[1] for row in data]

        # Create line plot
        plt.figure(figsize=(10, 6))
        plt.plot(years, populations, marker='o')
        plt.title(f'Population Growth for {selected_city} (2023-2043)')
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.grid(True)
        plt.xticks(years, rotation=45)
        plt.tight_layout()

        # Show plot
        plt.show()

        conn.close()

    if __name__ == "__main__":
        create_and_populate_db()
        simulate_population_growth()
        plot_population_growth()

if __name__ == "__main__":
    create_and_populate_db()
    simulate_population_growth()
    plot_population_growth()