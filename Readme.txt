Here are the instructions to follow as well as the list of APIs to check

1. Install django, rest_framework and djoser
2. Run scripts for migration:
    i. python3 manage.py makemigrations
    ii. python3 manage.py migrate
3. Create a superuser to access the django-admin: python3 manage.py createsuperuser
4. Run server with script: python3 manage.py runserver
5. List of API endpoints are as follows:
    i. Registration	/auth/users/	
    ii. Activation	/auth/users/activation/	
    iii. Login (Token)	/auth/token/login/	
    iv. Logout (Token)	/auth/token/logout/
    v. Menu Items /restaurant/menu-items/
    vi. Single Menu Item  /restaurant/menu-items/<id>
    vii. Booking /restaurant/booking/
    viii. Get auth token using djoser restaurant/api-token-auth/
