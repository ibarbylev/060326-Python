# 5. Формы (Forms) в Bootstrap

## Краткое описание

Формы используются для взаимодействия с пользователем:

* ввод текста;
* регистрация;
* обратная связь;
* поиск;
* отправка данных.

Bootstrap делает формы:

* аккуратными;
* одинаковыми по стилю;
* адаптивными.

---

# Основной элемент формы

## Тег `<form>`

```html
<form>
    ...
</form>
```

---

# Поле ввода

## Класс `form-control`

Это главный класс для всех текстовых полей.

---

## Пример

```html
<input
    type="text"
    class="form-control"
    placeholder="Введите имя"
/>
```

---

# Подписи к полям

## Класс `form-label`

Используется для текста над полем.

---

## Пример

```html
<label class="form-label">
    Имя
</label>

<input type="text" class="form-control">
```

---

# Структура формы

## Блоки с отступами

Класс:

* `mb-3` — отступ снизу

---

## Пример

```html id="c7m2xr"
<form>

    <div class="mb-3">
        <label class="form-label">Имя</label>
        <input type="text" class="form-control">
    </div>

</form>
```

---

# Типы полей

## Email

```html
<input type="email" class="form-control" placeholder="Email">
```

---

## Пароль

```html
<input type="password" class="form-control" placeholder="Пароль">
```

---

## Число

```html
<input type="number" class="form-control" placeholder="Возраст">
```

---

# Кнопка отправки

## Класс `btn btn-primary`

```html
<button class="btn btn-primary">
    Отправить
</button>
```

---

# Полная форма

## Пример

```html
<form>

    <div class="mb-3">
        <label class="form-label">Имя</label>
        <input type="text" class="form-control" placeholder="Введите имя">
    </div>

    <div class="mb-3">
        <label class="form-label">Email</label>
        <input type="email" class="form-control" placeholder="Введите email">
    </div>

    <div class="mb-3">
        <label class="form-label">Возраст</label>
        <input type="number" class="form-control" placeholder="Введите возраст">
    </div>

    <button class="btn btn-primary">
        Отправить
    </button>

</form>
```

---

# Checkbox и radio

## Checkbox

```html
<div class="form-check">
    <input class="form-check-input" type="checkbox">
    <label class="form-check-label">
        Согласен с правилами
    </label>
</div>
```

---

## Radio

```html
<div class="form-check">
    <input class="form-check-input" type="radio" name="r1">
    <label class="form-check-label">
        Вариант 1
    </label>
</div>
```

---

# Bootstrap layout формы

## Группировка полей

```html
<div class="mb-3">
    <input type="text" class="form-control" placeholder="Поле 1">
</div>

<div class="mb-3">
    <input type="text" class="form-control" placeholder="Поле 2">
</div>
```

---

# Кнопка на всю ширину

## Класс `d-grid`

```html
<div class="d-grid">
    <button class="btn btn-success">
        Отправить форму
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

    <title>Forms</title>

    <link
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css"
        rel="stylesheet"
    >
</head>

<body>

<div class="container mt-4">

    <h1 class="mb-4">
        Форма регистрации
    </h1>

    <form>

        <div class="mb-3">
            <label class="form-label">Имя</label>
            <input type="text" class="form-control">
        </div>

        <div class="mb-3">
            <label class="form-label">Email</label>
            <input type="email" class="form-control">
        </div>

        <div class="mb-3">
            <label class="form-label">Пароль</label>
            <input type="password" class="form-control">
        </div>

        <div class="form-check mb-3">
            <input class="form-check-input" type="checkbox">
            <label class="form-check-label">
                Согласен с условиями
            </label>
        </div>

        <div class="d-grid">
            <button class="btn btn-primary">
                Зарегистрироваться
            </button>
        </div>

    </form>

</div>

</body>
</html>
```

---

# Мини-практика

## Задание

Создайте форму:

* имя;
* email;
* пароль;
* checkbox;
* кнопку отправки;
* используйте Bootstrap классы.

---

## Пример результата

```html
<div class="container mt-4">

    <form>

        <input class="form-control mb-3" placeholder="Имя">
        <input class="form-control mb-3" placeholder="Email">
        <input class="form-control mb-3" type="password" placeholder="Пароль">

        <div class="form-check mb-3">
            <input class="form-check-input" type="checkbox">
            <label class="form-check-label">Согласен</label>
        </div>

        <button class="btn btn-primary w-100">
            Отправить
        </button>

    </form>

</div>
```
