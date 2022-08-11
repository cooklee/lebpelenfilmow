import pytest
from django.urls import reverse

from accounts.forms import LoginForm
from filmy.forms import AddPersonForm
from filmy.models import Person, Category


def test_index(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200


def test_login_view_get(client):
    url = reverse('login')
    response = client.get(url)
    assert response.status_code == 200
    form = response.context['form']
    assert isinstance(form, LoginForm)


@pytest.mark.django_db
def test_login_view_post(client, user_login):
    url = reverse('login')
    response = client.post(url, user_login)
    assert response.status_code == 302
    assert response.url == reverse('index')


@pytest.mark.django_db
def test_login_view_post_next(client, user_login):
    url = reverse('login')
    url += "?next=" + reverse('add_movie')
    response = client.post(url, user_login)
    assert response.status_code == 302
    assert response.url == reverse('add_movie')



def test_create_person_get(client):
    url = reverse('add_person')
    response = client.get(url)
    assert response.status_code == 200
    form = response.context['form']
    assert isinstance(form, AddPersonForm)


@pytest.mark.django_db
def test_create_person_post(client):
    url = reverse('add_person')
    person_dict  = {
        'first_name':'slawek',
        'last_name':'bo'
    }
    response = client.post(url, person_dict)
    assert response.status_code == 200
    assert Person.objects.get(**person_dict)


def test_create_category_get_not_login(client):
    url = reverse('add_category')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))


@pytest.mark.django_db
def test_create_category_get_login(client, user):
    url = reverse('add_category')
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_create_category_get_login(client, user):
    url = reverse('add_category')
    data = {
        'name':'ala'
    }
    client.force_login(user)
    response = client.post(url,data)
    assert response.status_code == 302
    assert Category.objects.get(**data)
    assert response.url == reverse('add_category')



def test_list_movie_not_login(client):
    url = reverse('movie_list')
    response= client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))

@pytest.mark.django_db
def test_list_movie_without_permission(client, user):
    url = reverse('movie_list')
    client.force_login(user)
    response= client.get(url)
    assert response.status_code == 403

@pytest.mark.django_db
def test_list_movie(client, user_with_permission, movies):
    url = reverse('movie_list')
    client.force_login(user_with_permission)
    response= client.get(url)
    assert response.status_code == 200
    assert response.context['object_list'].count() == len(movies)
    for movie in movies:
        assert movie in response.context['object_list']