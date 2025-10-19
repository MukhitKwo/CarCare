## **1️⃣ Install dependencies**

```bash
pip install psycopg2-binary djangorestframework
```

* `psycopg2-binary` → Postgres adapter
* `djangorestframework` → for APIs

---

## **2️⃣ Configure Django to connect to Supabase**

Edit `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_supabase_db_name',
        'USER': 'your_supabase_user',
        'PASSWORD': 'your_supabase_password',
        'HOST': 'your_supabase_host',  # something like xyz.supabase.co
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'require',  # Supabase requires SSL
        },
    }
}
```

> You can put credentials in environment variables for security.

---

## **3️⃣ Create a model**

```python
# myapp/models.py
from django.db import models

class Table1(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} - {self.name}"
```

---

## **4️⃣ Run migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

* This creates the table in **Supabase Postgres**.

---

## **5️⃣ Create API using Django REST Framework**

### Serializer:

```python
# myapp/serializers.py
from rest_framework import serializers
from .models import Table1

class Table1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Table1
        fields = ['id', 'name']
```

### Views:

```python
# myapp/views.py
from rest_framework import viewsets
from .models import Table1
from .serializers import Table1Serializer

class Table1ViewSet(viewsets.ModelViewSet):
    queryset = Table1.objects.all()
    serializer_class = Table1Serializer
```

### URLs:

```python
# myapp/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Table1ViewSet

router = DefaultRouter()
router.register(r'table1', Table1ViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

---

## **6️⃣ Test it**

* Start server: `python manage.py runserver`
* API endpoints will work:

| Method | URL           | Action      |
| ------ | ------------- | ----------- |
| GET    | /table1/      | List rows   |
| POST   | /table1/      | Add row     |
| GET    | /table1/{id}/ | Get one row |
| PUT    | /table1/{id}/ | Update row  |
| DELETE | /table1/{id}/ | Delete row  |

* You can also use **Django admin** if you create a superuser:

```bash
python manage.py createsuperuser
```

* Don't forget to add the tables to admin.py

```bash
admin.site.register(Table1)
```

---

## **7️⃣ Connect a React app to your API**

### Install Axios

```bash
npm install axios
```

### Example: Fetch data from `/table1/`

```jsx
// src/Table1List.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Table1List() {
    const [rows, setRows] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:8000/table1/')
            .then(response => setRows(response.data))
            .catch(error => console.error(error));
    }, []);

    return (
        <div>
            <h2>Table1 Data</h2>
            <ul>
                {rows.map(row => (
                    <li key={row.id}>{row.name}</li>
                ))}
            </ul>
        </div>
    );
}

export default Table1List;
```

### Use the component

```jsx
// src/App.js
import React from 'react';
import Table1List from './Table1List';

function App() {
    return (
        <div>
            <Table1List />
        </div>
    );
}

export default App;
```

> Make sure your Django server allows CORS requests. Install `django-cors-headers` and add it to `INSTALLED_APPS` and middleware.
