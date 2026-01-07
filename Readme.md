<h1>📘 FastAPI Blog Application</h1>

<p>
This project is a <strong>RESTful Blog API</strong> built using <strong>FastAPI</strong>.
It provides authentication, user management, and blog management features
with secured endpoints using JWT-based authentication.
</p>

<hr />

<h2>🚀 Features</h2>
<ul>
  <li>User Registration and Login</li>
  <li>JWT-based Authentication</li>
  <li>Create, Read, Update, Delete Blogs</li>
  <li>View All Users</li>
  <li>Versioned APIs (v1, v2)</li>
  <li>Swagger UI documentation</li>
</ul>

<hr />

<h2>🛠️ Tech Stack</h2>
<ul>
  <li>FastAPI</li>
  <li>Python</li>
  <li>SQLAlchemy</li>
  <li>JWT Authentication</li>
  <li>Uvicorn ASGI Server</li>
</ul>

<hr />

<h2>📂 API Endpoints</h2>

<h3>🔐 Authentication</h3>
<table border="1" cellpadding="8">
  <tr>
    <th>Method</th>
    <th>Endpoint</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>POST</td>
    <td>/login</td>
    <td>User Login (returns access token)</td>
  </tr>
</table>

<hr />

<h3>📝 Blogs</h3>
<table border="1" cellpadding="8">
  <tr>
    <th>Method</th>
    <th>Endpoint</th>
    <th>Description</th>
    <th>Auth Required</th>
  </tr>
  <tr>
    <td>GET</td>
    <td>/v2/get-all-blogs</td>
    <td>Get all blogs</td>
    <td>No</td>
  </tr>
  <tr>
    <td>POST</td>
    <td>/v2/create-blog</td>
    <td>Create a new blog</td>
    <td>Yes</td>
  </tr>
  <tr>
    <td>DELETE</td>
    <td>/v2/delete-blog/{id}</td>
    <td>Delete a blog by ID</td>
    <td>Yes</td>
  </tr>
  <tr>
    <td>PUT</td>
    <td>/v2/update-blog/{id}</td>
    <td>Update a blog by ID</td>
    <td>Yes</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>/v2/get-blog/{id}</td>
    <td>Get a single blog by ID</td>
    <td>Yes</td>
  </tr>
</table>

<hr />

<h3>👤 Users</h3>
<table border="1" cellpadding="8">
  <tr>
    <th>Method</th>
    <th>Endpoint</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>GET</td>
    <td>/v1/get-all-users</td>
    <td>Get all users</td>
  </tr>
  <tr>
    <td>POST</td>
    <td>/v1/create-user</td>
    <td>Create a new user</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>/v1/get-user/{id}</td>
    <td>Get user by ID</td>
  </tr>
</table>

<hr />

<h2>🔑 Authentication Flow</h2>
<ol>
  <li>User logs in using <code>/login</code></li>
  <li>API returns a JWT access token</li>
  <li>Click <strong>Authorize</strong> in Swagger UI</li>
  <li>Use token in format: <code>Bearer &lt;token&gt;</code></li>
  <li>Access protected routes</li>
</ol>

<hr />

<h2>▶️ Run the Project</h2>
<pre>
uvicorn blog.main:app --reload
</pre>

<p>Swagger UI will be available at:</p>
<pre>
http://127.0.0.1:8000/docs
</pre>

<hr />

<h2>📌 Notes</h2>
<ul>
  <li>Make sure virtual environment is activated</li>
  <li>Run the server from the project root directory</li>
  <li>Use correct API versioning while calling endpoints</li>
</ul>

<hr />

<h2>📄 License</h2>
