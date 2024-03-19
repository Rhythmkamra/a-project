<html> <body> <h1>Basic Concepts of an EDMS</h1> <ol> <li><strong>Project and App Folders:</strong> The project folder and app folder are created on the same level.</li> <li><strong>Include App in Project:</strong> The app is included in the project folder in the <code>settings.py</code> file.</li> <li><strong>Templates:</strong> Templates are created in the following way: <code>app/templates/app</code></li> <li><strong>Static Files:</strong> The static folder is also created in the same way for CSS and JS files.</li> <li><strong>Create Model:</strong> A model is created for the table in the database.</li> <li><strong>Frontend View:</strong> A frontend view is created for the model.</li> <li><strong>Load Model:</strong> The model is loaded in the <code>views.py</code> file for the same.</li> <li><strong>Load Views:</strong> The views file is loaded for the URL in the project folder.</li> <li><strong>Create URL:</strong> A URL is created for each view.</li> <li><strong>Makemigrations:</strong> <code>python3 manage.py makemigrations</code> is used for making the changes.</li> <li><strong>Migrate:</strong> <code>python3 manage.py migrate</code> is used to apply the changes.</li> <li><strong>Home Page URL:</strong> Note that the home page URL is this: <code>"/"</code> (no space)</li> <li><strong>Register Models:</strong> Models are registered in <code>admin.py</code> so that they are visible on the admin panel.</li> </ol> </body> </html>




user authentication system:
d.contrib.auth-core
class user-core -people interacting -only one class of user is defined in django all django users are created here the admin the staff .with diff permissions though


d.contrib.contenttypes-permissions stuff