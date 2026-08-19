# 6. Карточки (Cards) в Bootstrap

## Краткое описание

Карточки — это один из самых популярных компонентов Bootstrap.

Они используются для:

* товаров;
* новостей;
* профилей;
* блоков информации.

Карточка обычно содержит:

* изображение;
* заголовок;
* текст;
* кнопку.

---

# Базовая структура карточки

## Класс `card`

```html
<div class="card">
    ...
</div>
```

---

# Тело карточки

## Класс `card-body`

Основной контент карточки.

```html
<div class="card">
    <div class="card-body">
        Контент карточки
    </div>
</div>
```

---

# Заголовок и текст

## Классы:

* `card-title`
* `card-text`

---

## Пример

```html
<div class="card" style="width: 18rem;">

    <div class="card-body">

        <h5 class="card-title">
            Заголовок
        </h5>

        <p class="card-text">
            Описание карточки
        </p>

    </div>

</div>
```

---

# Картинка в карточке

## Класс `card-img-top`

```html
<div class="card" style="width: 18rem;">

    <img
        src="https://via.placeholder.com/300"
        class="card-img-top"
        alt="..."
    >

    <div class="card-body">
        <h5 class="card-title">Карточка</h5>
        <p class="card-text">Описание</p>
    </div>

</div>
```

---

# Кнопка в карточке

## Используется `btn`

```html
<div class="card" style="width: 18rem;">

    <div class="card-body">

        <h5 class="card-title">Товар</h5>

        <p class="card-text">
            Описание товара
        </p>

        <a href="#" class="btn btn-primary">
            Купить
        </a>

    </div>

</div>
```

---

# Несколько карточек (Grid)

## Использование сетки Bootstrap

```html
<div class="container">

    <div class="row g-3">

        <div class="col-md-4">
            <div class="card">
                <div class="card-body">Карточка 1</div>
            </div>
        </div>

        <div class="col-md-4">
            <div class="card">
                <div class="card-body">Карточка 2</div>
            </div>
        </div>

        <div class="col-md-4">
            <div class="card">
                <div class="card-body">Карточка 3</div>
            </div>
        </div>

    </div>

</div>
```

---

# Карточка товара (пример)

```html
<div class="card" style="width: 18rem;">

    <img src="https://via.placeholder.com/300" class="card-img-top">

    <div class="card-body">

        <h5 class="card-title">
            Ноутбук
        </h5>

        <p class="card-text">
            Мощный игровой ноутбук
        </p>

        <a href="#" class="btn btn-success">
            Купить
        </a>

    </div>

</div>
```

---

# Центрирование карточек

```html 
<div class="d-flex justify-content-center">

    <div class="card" style="width: 18rem;">
        <div class="card-body">
            Центрированная карточка
        </div>
    </div>

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

    <title>Cards</title>

    <link
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css"
        rel="stylesheet"
    >
</head>

<body>

<div class="container mt-4">

    <h1 class="mb-4">
        Карточки Bootstrap
    </h1>

    <div class="row g-3">

        <div class="col-md-4">

            <div class="card">

                <img src="https://via.placeholder.com/300" class="card-img-top">

                <div class="card-body">

                    <h5 class="card-title">
                        Карточка 1
                    </h5>

                    <p class="card-text">
                        Описание первой карточки
                    </p>

                    <a href="#" class="btn btn-primary">
                        Подробнее
                    </a>

                </div>

            </div>

        </div>

        <div class="col-md-4">

            <div class="card">

                <img src="https://via.placeholder.com/300" class="card-img-top">

                <div class="card-body">

                    <h5 class="card-title">
                        Карточка 2
                    </h5>

                    <p class="card-text">
                        Описание второй карточки
                    </p>

                    <a href="#" class="btn btn-success">
                        Купить
                    </a>

                </div>

            </div>

        </div>

        <div class="col-md-4">

            <div class="card">

                <img src="https://via.placeholder.com/300" class="card-img-top">

                <div class="card-body">

                    <h5 class="card-title">
                        Карточка 3
                    </h5>

                    <p class="card-text">
                        Описание третьей карточки
                    </p>

                    <a href="#" class="btn btn-danger">
                        Подробнее
                    </a>

                </div>

            </div>

        </div>

    </div>

</div>

</body>
</html>
```

---

# Мини-практика

## Задание

Создайте:

* 3 карточки;
* изображение в каждой;
* заголовок + текст;
* кнопку;
* расположение через `row` и `col-md-4`.

---

## Пример результата

```html
<div class="container mt-4">

    <div class="row">

        <div class="col-md-4">
            <div class="card">
                <div class="card-body">
                    Карточка 1
                </div>
            </div>
        </div>

        <div class="col-md-4">
            <div class="card">
                <div class="card-body">
                    Карточка 2
                </div>
            </div>
        </div>

        <div class="col-md-4">
            <div class="card">
                <div class="card-body">
                    Карточка 3
                </div>
            </div>
        </div>

    </div>

</div>
```
