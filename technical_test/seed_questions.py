from technical_test.models import Question, Choice

def seed_all_questions():
    # CLEAR OLD QUESTIONS
    Question.objects.all().delete()

    # -------------------------
    # 🎯 PYTHON QUESTIONS (10)
    # -------------------------
    python_questions = [
        {
            "text": "What is the output of print(type([]))?",
            "options": ["list", "dict", "tuple", "set"],
            "correct": "list"
        },
        {
            "text": "Which keyword is used to create a function in Python?",
            "options": ["func", "def", "function", "lambda"],
            "correct": "def"
        },
        {
            "text": "Which of the following is immutable?",
            "options": ["List", "Tuple", "Dictionary", "Set"],
            "correct": "Tuple"
        },
        {
            "text": "Which operator is used for floor division?",
            "options": ["//", "/", "%", "**"],
            "correct": "//"
        },
        {
            "text": "Which function is used to get user input?",
            "options": ["scan()", "input()", "get()", "read()"],
            "correct": "input()"
        },
        {
            "text": "Which loop executes at least once?",
            "options": ["for", "while", "do-while", "None"],
            "correct": "None"
        },
        {
            "text": "What is the output of 3 * 'hi'?",
            "options": ["hihihi", "hi3", "error", "hi hi hi"],
            "correct": "hihihi"
        },
        {
            "text": "Which is a Python data type?",
            "options": ["String", "Class", "Package", "Module"],
            "correct": "String"
        },
        {
            "text": "Which keyword is used to handle exceptions?",
            "options": ["exception", "try", "error", "catch"],
            "correct": "try"
        },
        {
            "text": "Which keyword creates a class?",
            "options": ["struct", "class", "new", "define"],
            "correct": "class"
        },
    ]

    # -------------------------
    # 🎯 DJANGO QUESTIONS (10)
    # -------------------------
    django_questions = [
        {
            "text": "Which file contains Django project settings?",
            "options": ["settings.py", "views.py", "urls.py", "admin.py"],
            "correct": "settings.py"
        },
        {
            "text": "Which command creates a Django project?",
            "options": ["django-admin startproject", "django new", "django create", "makeproject"],
            "correct": "django-admin startproject"
        },
        {
            "text": "Which function renders templates?",
            "options": ["render()", "template()", "show()", "display()"],
            "correct": "render()"
        },
        {
            "text": "Which file stores URL routes?",
            "options": ["settings.py", "urls.py", "models.py", "apps.py"],
            "correct": "urls.py"
        },
        {
            "text": "Which database is default in Django?",
            "options": ["MySQL", "SQLite", "PostgreSQL", "MongoDB"],
            "correct": "SQLite"
        },
        {
            "text": "Which command creates migrations?",
            "options": ["makemigrations", "migrate", "syncdb", "create"],
            "correct": "makemigrations"
        },
        {
            "text": "What is Django's template file extension?",
            "options": [".html", ".py", ".db", ".dj"],
            "correct": ".html"
        },
        {
            "text": "Which architecture Django follows?",
            "options": ["MVC", "MVT", "MVP", "MVMM"],
            "correct": "MVT"
        },
        {
            "text": "Which decorator restricts page to logged-in users?",
            "options": ["@secure", "@login_required", "@authenticated", "@private"],
            "correct": "@login_required"
        },
        {
            "text": "Which file registers models in Django admin?",
            "options": ["admin.py", "views.py", "urls.py", "apps.py"],
            "correct": "admin.py"
        },
    ]

    # -------------------------
    # 🎯 SQL QUESTIONS (10)
    # -------------------------
    sql_questions = [
        {
            "text": "Which SQL keyword is used to get unique values?",
            "options": ["DISTINCT", "UNIQUE", "FILTER", "ONLY"],
            "correct": "DISTINCT"
        },
        {
            "text": "Which command retrieves data?",
            "options": ["SELECT", "GET", "FETCH", "SHOW"],
            "correct": "SELECT"
        },
        {
            "text": "Which clause sorts data?",
            "options": ["ORDER BY", "SORT", "GROUP BY", "RANGE"],
            "correct": "ORDER BY"
        },
        {
            "text": "Which SQL function counts rows?",
            "options": ["COUNT()", "TOTAL()", "ROWS()", "NUMBER()"],
            "correct": "COUNT()"
        },
        {
            "text": "Which joins return common records?",
            "options": ["INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL JOIN"],
            "correct": "INNER JOIN"
        },
        {
            "text": "Which symbol denotes wildcard?",
            "options": ["%", "#", "@", "^"],
            "correct": "%"
        },
        {
            "text": "Which command removes all records?",
            "options": ["DELETE", "ERASE", "REMOVE", "CUT"],
            "correct": "DELETE"
        },
        {
            "text": "Which operator checks a range?",
            "options": ["BETWEEN", "WITHIN", "INRANGE", "MID"],
            "correct": "BETWEEN"
        },
        {
            "text": "Which command updates data?",
            "options": ["UPDATE", "CHANGE", "MODIFY", "FIX"],
            "correct": "UPDATE"
        },
        {
            "text": "Which clause groups rows?",
            "options": ["GROUP BY", "ORDER BY", "SORT BY", "UNION"],
            "correct": "GROUP BY"
        },
    ]

    # FUNCTION to insert questions
    def insert_questions(data, category):
        for q in data:
            ques = Question.objects.create(
                text=q["text"],
                category=category,
                difficulty=1
            )
            for opt in q["options"]:
                Choice.objects.create(
                    question=ques,
                    text=opt,
                    is_correct=(opt == q["correct"])
                )

    insert_questions(python_questions, "python")
    insert_questions(django_questions, "django")
    insert_questions(sql_questions, "sql")

    print("🎉 30 Questions Added Successfully!")

