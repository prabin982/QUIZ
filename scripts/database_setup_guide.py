"""
Database Setup Guide for Django Quiz Platform
This script provides instructions for setting up different databases
"""

def print_database_setup_guide():
    print("🗄️  DATABASE SETUP GUIDE FOR DJANGO QUIZ PLATFORM")
    print("=" * 60)
    
    print("\n1️⃣  SQLITE (Default - No setup required)")
    print("   ✅ Already configured and ready to use")
    print("   ✅ Perfect for development and testing")
    print("   ✅ Database file: db.sqlite3 (created automatically)")
    
    print("\n2️⃣  POSTGRESQL (Recommended for production)")
    print("   📋 Installation steps:")
    print("   • Install PostgreSQL: https://www.postgresql.org/download/")
    print("   • Install Python driver: pip install psycopg2-binary")
    print("   • Create database:")
    print("     - Open PostgreSQL command line (psql)")
    print("     - CREATE DATABASE quiz_platform_db;")
    print("     - CREATE USER quiz_user WITH PASSWORD 'your_password';")
    print("     - GRANT ALL PRIVILEGES ON DATABASE quiz_platform_db TO quiz_user;")
    print("   • Update .env file with your credentials")
    
    print("\n3️⃣  MYSQL")
    print("   📋 Installation steps:")
    print("   • Install MySQL: https://dev.mysql.com/downloads/")
    print("   • Install Python driver: pip install mysqlclient")
    print("   • Create database:")
    print("     - Open MySQL command line")
    print("     - CREATE DATABASE quiz_platform_db;")
    print("     - CREATE USER 'quiz_user'@'localhost' IDENTIFIED BY 'your_password';")
    print("     - GRANT ALL PRIVILEGES ON quiz_platform_db.* TO 'quiz_user'@'localhost';")
    print("   • Update .env file with your credentials")
    
    print("\n4️⃣  CLOUD DATABASES")
    print("   🌐 Popular options:")
    print("   • Heroku Postgres (Free tier available)")
    print("   • AWS RDS (PostgreSQL/MySQL)")
    print("   • Google Cloud SQL")
    print("   • DigitalOcean Managed Databases")
    print("   • PlanetScale (MySQL-compatible)")
    
    print("\n📝 ENVIRONMENT VARIABLES (.env file)")
    print("   Create a .env file in your project root:")
    print("   DB_ENGINE=django.db.backends.postgresql")
    print("   DB_NAME=quiz_platform_db")
    print("   DB_USER=your_username")
    print("   DB_PASSWORD=your_password")
    print("   DB_HOST=localhost")
    print("   DB_PORT=5432")
    
    print("\n🚀 AFTER DATABASE SETUP:")
    print("   1. Run: python manage.py makemigrations")
    print("   2. Run: python manage.py migrate")
    print("   3. Run: python scripts/setup_database.py")
    print("   4. Run: python manage.py runserver")
    
    print("\n💡 RECOMMENDATIONS:")
    print("   • Development: Use SQLite (default)")
    print("   • Production: Use PostgreSQL")
    print("   • Always use environment variables for credentials")
    print("   • Never commit database credentials to version control")
    
    print("\n🔒 SECURITY TIPS:")
    print("   • Use strong passwords")
    print("   • Limit database user permissions")
    print("   • Use SSL connections in production")
    print("   • Regular backups")
    print("   • Monitor database access logs")

if __name__ == '__main__':
    print_database_setup_guide()
