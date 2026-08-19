# 8. Компоненты интерфейса Bootstrap

## Краткое описание

Bootstrap содержит готовые UI-компоненты.

Они позволяют быстро добавлять:

* уведомления;
* бейджи;
* модальные окна;
* выпадающие списки;
* слайдеры.

---

# 1. Уведомления (Alerts)

## Класс `alert`

Используются для сообщений пользователю.

---

## Примеры

```html
<div class="alert alert-primary">
    Информационное сообщение
</div>

<div class="alert alert-success">
    Успех!
</div>

<div class="alert alert-danger">
    Ошибка!
</div>
```

---

## Важные типы:

* `alert-primary`
* `alert-success`
* `alert-warning`
* `alert-danger`

---

# 2. Бейджи (Badges)

## Класс `badge`

Используются для меток и счётчиков.

---

## Пример

```html
<h1>
    Сообщения
    <span class="badge bg-primary">5</span>
</h1>
```

---

## Внутри кнопок

```html
<button class="btn btn-primary">
    Уведомления
    <span class="badge bg-light text-dark">3</span>
</button>
```

---

# 3. Выпадающее меню (Dropdown)

## Основные классы:

* `dropdown`
* `dropdown-toggle`
* `dropdown-menu`

---

## Пример

```html
<div class="dropdown">

    <button class="btn btn-secondary dropdown-toggle" data-bs-toggle="dropdown">
        Меню
    </button>

    <ul class="dropdown-menu">

        <li><a class="dropdown-item" href="#">Пункт 1</a></li>
        <li><a class="dropdown-item" href="#">Пункт 2</a></li>
        <li><a class="dropdown-item" href="#">Пункт 3</a></li>

    </ul>

</div>
```

---

# 4. Модальные окна (Modal)

## Кратко

Modal — всплывающее окно.

---

## Кнопка открытия

```html
<button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#myModal">
    Открыть окно
</button>
```

---

## Само окно

```html
<div class="modal fade" id="myModal">

    <div class="modal-dialog">

        <div class="modal-content">

            <div class="modal-header">
                <h5 class="modal-title">Заголовок</h5>
            </div>

            <div class="modal-body">
                Контент модального окна
            </div>

            <div class="modal-footer">
                <button class="btn btn-secondary" data-bs-dismiss="modal">
                    Закрыть
                </button>
            </div>

        </div>

    </div>

</div>
```

---

# 5. Слайдер (Carousel)

## Класс `carousel`

Используется для изображений.

---

## Пример

```html
<div id="carouselExample" class="carousel slide" data-bs-ride="carousel">

    <div class="carousel-inner">

        <div class="carousel-item active">
            <img src="https://via.placeholder.com/800x300" class="d-block w-100">
        </div>

        <div class="carousel-item">
            <img src="https://via.placeholder.com/800x300/aaa" class="d-block w-100">
        </div>

        <div class="carousel-item">
            <img src="https://via.placeholder.com/800x300/ccc" class="d-block w-100">
        </div>

    </div>

</div>
```

---

# 6. Комбинирование компонентов

## Пример страницы

```html
<div class="container mt-4">

    <h1>
        Компоненты Bootstrap
    </h1>

    <div class="alert alert-success">
        Успешное действие!
    </div>

    <button class="btn btn-primary">
        Уведомления
        <span class="badge bg-light text-dark">4</span>
    </button>

</div>
```

---

# Полный пример страницы

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Components</title>

    <link
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css"
        rel="stylesheet"
    >
</head>

<body>

<div class="container mt-4">

    <h1 class="mb-4">
        Bootstrap компоненты
    </h1>

    <div class="alert alert-primary">
        Информационное сообщение
    </div>

    <div class="alert alert-success">
        Успех операции
    </div>

    <button class="btn btn-primary">
        Уведомления
        <span class="badge bg-light text-dark">3</span>
    </button>

    <hr>

    <div class="dropdown mt-3">

        <button class="btn btn-secondary dropdown-toggle" data-bs-toggle="dropdown">
            Меню
        </button>

        <ul class="dropdown-menu">

            <li><a class="dropdown-item" href="#">Пункт 1</a></li>
            <li><a class="dropdown-item" href="#">Пункт 2</a></li>
            <li><a class="dropdown-item" href="#">Пункт 3</a></li>

        </ul>

    </div>

</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>
```

---

# Мини-практика

## Задание

Создайте страницу:

* alert (success + danger);
* кнопку с badge;
* dropdown меню;
* модальное окно (если получится).

---

## Пример результата

```html
<div class="container mt-4">

    <div class="alert alert-success">Успех</div>
    <div class="alert alert-danger">Ошибка</div>

    <button class="btn btn-primary">
        Сообщения <span class="badge bg-light text-dark">2</span>
    </button>

</div>
```
