# 7. Навигация (Navbar) в Bootstrap

## Краткое описание

Navbar — это верхнее меню сайта.

Он используется для:

* перехода между страницами;
* логотипа сайта;
* навигации по разделам;
* адаптивного меню (мобильная версия).

---

# Базовая структура navbar

## Класс `navbar`

```html
<nav class="navbar">
    ...
</nav>
```

---

# Простая навигация

## Пример без оформления

```html
<nav class="navbar">
    <a href="#">Главная</a>
    <a href="#">О нас</a>
    <a href="#">Контакты</a>
</nav>
```

---

# Bootstrap navbar (базовый)

## Класс `navbar-brand`

```html
<nav class="navbar bg-light">

    <a class="navbar-brand" href="#">
        Мой сайт
    </a>

</nav>
```

---

# Меню внутри navbar

## Класс `nav`

```html
<nav class="navbar bg-light">

    <a class="navbar-brand" href="#">
        Логотип
    </a>

    <ul class="nav">
        <li class="nav-item">
            <a class="nav-link" href="#">Главная</a>
        </li>

        <li class="nav-item">
            <a class="nav-link" href="#">О нас</a>
        </li>

        <li class="nav-item">
            <a class="nav-link" href="#">Контакты</a>
        </li>
    </ul>

</nav>
```

---

# Цветной navbar

## Классы:

* `navbar-dark`
* `bg-dark`

```html
<nav class="navbar navbar-dark bg-dark">
    <a class="navbar-brand text-white" href="#">
        Сайт
    </a>
</nav>
```

---

# Центрирование элементов

## Flex внутри navbar

```html
<nav class="navbar bg-light d-flex justify-content-between">

    <a class="navbar-brand" href="#">
        Лого
    </a>

    <div>
        Меню
    </div>

</nav>
```

---

# Адаптивный navbar (бургер меню)

## Класс `navbar-expand`

```html
<nav class="navbar navbar-expand-lg navbar-light bg-light">

    <a class="navbar-brand" href="#">Сайт</a>

    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#menu">
        ☰
    </button>

    <div class="collapse navbar-collapse" id="menu">

        <ul class="navbar-nav ms-auto">

            <li class="nav-item">
                <a class="nav-link" href="#">Главная</a>
            </li>

            <li class="nav-item">
                <a class="nav-link" href="#">О нас</a>
            </li>

            <li class="nav-item">
                <a class="nav-link" href="#">Контакты</a>
            </li>

        </ul>

    </div>

</nav>
```

---

## Как это работает:

* на большом экране меню видно сразу
* на маленьком — появляется кнопка ☰
* при нажатии меню раскрывается

---

# Выравнивание меню вправо

## Класс `ms-auto`

```html
<ul class="navbar-nav ms-auto">
```

---

# Полный пример страницы

```html id="k4m7qp"
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Navbar</title>

    <link
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css"
        rel="stylesheet"
    >
</head>

<body>

<nav class="navbar navbar-expand-lg navbar-dark bg-dark">

    <div class="container">

        <a class="navbar-brand" href="#">
            MySite
        </a>

        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#menu">
            ☰
        </button>

        <div class="collapse navbar-collapse" id="menu">

            <ul class="navbar-nav ms-auto">

                <li class="nav-item">
                    <a class="nav-link" href="#">Главная</a>
                </li>

                <li class="nav-item">
                    <a class="nav-link" href="#">О нас</a>
                </li>

                <li class="nav-item">
                    <a class="nav-link" href="#">Контакты</a>
                </li>

            </ul>

        </div>

    </div>

</nav>

<div class="container mt-4">

    <h1>
        Добро пожаловать
    </h1>

    <p>
        Это пример страницы с navbar Bootstrap.
    </p>

</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>
```

---

# Мини-практика

## Задание

Создайте navbar:

* логотип слева;
* 3 ссылки справа;
* тёмный фон;
* адаптивное бургер-меню.

---

## Пример результата

```html
<nav class="navbar navbar-dark bg-dark navbar-expand-lg">

    <div class="container">

        <a class="navbar-brand">Logo</a>

        <button class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#nav">
            ☰
        </button>

        <div class="collapse navbar-collapse" id="nav">

            <ul class="navbar-nav ms-auto">

                <li class="nav-item">
                    <a class="nav-link">Home</a>
                </li>

                <li class="nav-item">
                    <a class="nav-link">About</a>
                </li>

                <li class="nav-item">
                    <a class="nav-link">Contact</a>
                </li>

            </ul>

        </div>

    </div>

</nav>
```
