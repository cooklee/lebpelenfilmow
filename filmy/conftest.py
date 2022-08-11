from django.contrib.auth.models import User, Permission
import pytest

from filmy.models import Film, Category, Person


@pytest.fixture
def user_login():
    data = {
        'username': 'testowy',
        'password': 'alamakota'
    }
    User.objects.create_user(**data)
    return data

@pytest.fixture
def user():
    data = {
        'username': 'testowy',
        'password': 'alamakota'
    }
    return User.objects.create_user(**data)


@pytest.fixture
def user_with_permission():
    data = {
        'username': 'testowy',
        'password': 'alamakota'
    }
    u = User.objects.create_user(**data)
    p = Permission.objects.get(codename='view_film')
    u.user_permissions.add(p)
    return u


@pytest.fixture
def category():
    return Category.objects.create(name='ala ma kota')

@pytest.fixture
def persons():
    lst = [
        Person.objects.create(first_name='rezyser',last_name='kiepski'),
        Person.objects.create(first_name='scenarzysta', last_name='good')
    ]
    return lst


@pytest.fixture
def movies(category, persons):
    lst = []
    for x in range(10):
        m = Film()
        m.title = x
        m.year = 1990 + x
        m.category = category
        m.director = persons[0]
        m.screenwriter = persons[1]
        m.save()
        lst.append(m)
    return lst
