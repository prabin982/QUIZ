# Nepali Quiz Platform

A comprehensive online quiz platform built with Django specifically for Nepali content, featuring questions about Nepal's culture, history, geography, sports, and general science knowledge.

**Created by: Prabin Dhungana**

## Features

### Core Features
- **Admin Panel**: Admins can add/edit Nepal-focused quizzes, questions, and categories
- **User Authentication**: Registration, login, and user management
- **Nepal-Focused Content**: Quizzes covering Nepali General Knowledge, History, Sports, and Science
- **Score Tracking**: Automatic scoring and result display

### Categories
- **Nepali General Knowledge**: Culture, geography, traditions, and current affairs of Nepal
- **Nepali History**: From ancient times to modern Nepal
- **Sports**: Sports in Nepal and international sports knowledge  
- **Science**: General science and technology questions

### Bonus Features
- **Timer System**: Individual question timers with visual countdown
- **Random Questions**: Questions are randomized for each quiz attempt
- **Leaderboard**: Global and quiz-specific leaderboards for Nepal quizzes
- **Progress Tracking**: Visual progress indicators during quizzes
- **Responsive Design**: Mobile-friendly interface optimized for Nepali users

## Installation

1. **Clone the repository**
   \`\`\`bash
   git clone <repository-url>
   cd nepali-quiz-platform
   \`\`\`

2. **Create virtual environment**
   \`\`\`bash
   python -m venv quiz_env
   source quiz_env/bin/activate  # On Windows: quiz_env\Scripts\activate
   \`\`\`

3. **Install dependencies**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Run migrations**
   \`\`\`bash
   python manage.py makemigrations
   python manage.py migrate
   \`\`\`

5. **Create Nepali sample data**
   \`\`\`bash
   python scripts/setup_nepali_database.py
   \`\`\`

6. **Run the server**
   \`\`\`bash
   python manage.py runserver
   \`\`\`

7. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/
   - Login: pad / pad123

## Sample Quizzes Created

- **Nepal General Knowledge Quiz** (8 questions) - About Nepal's capital, mountains, culture, festivals
- **Nepal History Quiz** (6 questions) - From Prithvi Narayan Shah to modern Nepal
- **Nepal Sports Quiz** (5 questions) - Football, cricket, and traditional sports in Nepal
- **Science Knowledge Quiz** (6 questions) - General science and technology

## Admin Access

- **Username**: pad
- **Password**: pad123
- **Creator**: Prabin Dhungana
- **Email**: prabin.dhungana@example.com

## Project Structure

\`\`\`
quiz_platform/
├── quiz_platform/          # Main project settings
├── quiz/                   # Quiz app
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── urls.py            # URL patterns
│   └── admin.py           # Admin configuration
├── accounts/              # User authentication app
├── templates/             # HTML templates
├── static/               # Static files (CSS, JS, images)
└── scripts/              # Setup scripts
\`\`\`

## Models

- **Category**: Quiz categories
- **Quiz**: Quiz configuration and metadata
- **Question**: Individual questions with timing
- **Choice**: Answer choices for questions
- **QuizAttempt**: User quiz attempts and scores
- **UserAnswer**: Individual question responses

## Usage

### For Admins
1. Access admin panel at `/admin/`
2. Create categories and quizzes
3. Add questions with multiple choices
4. Set timers and difficulty levels
5. Monitor user performance

### For Users
1. Register/login to the platform
2. Browse available quizzes
3. Take quizzes with timed questions
4. View results and scores
5. Check leaderboards

## Features in Detail

### Timer System
- Each question has an individual timer
- Visual countdown with color changes
- Auto-submit when time expires
- Time tracking for performance analysis

### Random Questions
- Questions are shuffled for each attempt
- Configurable number of questions per quiz
- Prevents memorization and cheating

### Leaderboard
- Global leaderboard across all quizzes
- Quiz-specific leaderboards
- Ranking by score and completion time
- Recent attempts display

### Responsive Design
- Mobile-friendly interface
- Bootstrap-based styling
- Progressive web app features
- Touch-friendly controls

## Customization

### Adding New Question Types
1. Update `Question.QUESTION_TYPES` in models.py
2. Modify templates to handle new types
3. Update view logic for processing

### Styling
- Modify `templates/base.html` for global styles
- Update Bootstrap classes in templates
- Add custom CSS in static files

### Additional Features
- Email notifications
- Certificate generation
- Social sharing
- Advanced analytics

## About the Creator

This Nepali Quiz Platform was created by **Prabin Dhungana** to promote knowledge about Nepal's rich culture, history, and traditions through an interactive quiz format.

## Contributing

Contributions are welcome! Please focus on:
- Adding more Nepal-specific questions
- Improving Nepali language support
- Adding more categories relevant to Nepal
- Enhancing the user experience for Nepali users

## License

This project is created by Prabin Dhungana and is open source under the MIT License.
