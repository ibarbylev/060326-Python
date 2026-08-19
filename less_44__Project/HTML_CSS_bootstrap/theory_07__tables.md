# 6. Таблицы

## Краткое описание

Таблицы в HTML используются для отображения структурированных данных:

* списков;
* расписаний;
* характеристик;
* сравнений.

Таблица состоит из строк и ячеек.

---

# Основные теги таблиц

## `<table>`

Контейнер всей таблицы.

```html
<table>
    ...
</table>
```

---

## `<tr>` (table row)

Строка таблицы.

```html
<tr>
    ...
</tr>
```

---

## `<td>` (table data)

Обычная ячейка.

```html
<td>Данные</td>
```

---

## `<th>` (table header)

Заголовочная ячейка (обычно жирная и по центру).

```html
<th>Заголовок</th>
```

---

# Простая таблица

## Пример

```html
<table>
    <tr>
        <th>Имя</th>
        <th>Возраст</th>
    </tr>

    <tr>
        <td>Анна</td>
        <td>25</td>
    </tr>

    <tr>
        <td>Иван</td>
        <td>30</td>
    </tr>
</table>
```

---

# Таблицы и Bootstrap

Bootstrap делает таблицы более красивыми.

## Класс:

* `table` — базовый стиль Bootstrap

---

## Пример

```html
<table class="table">
    <tr>
        <th>Имя</th>
        <th>Возраст</th>
    </tr>

    <tr>
        <td>Анна</td>
        <td>25</td>
    </tr>
</table>
```

---

# Улучшенные таблицы Bootstrap

## Полосатая таблица

Класс:

* `table-striped`

```html
<table class="table table-striped">
    <tr>
        <th>Имя</th>
        <th>Возраст</th>
    </tr>

    <tr>
        <td>Анна</td>
        <td>25</td>
    </tr>

    <tr>
        <td>Иван</td>
        <td>30</td>
    </tr>
</table>
```

---

## Таблица с границами

Класс:

* `table-bordered`

```html
<table class="table table-bordered">
    <tr>
        <th>Продукт</th>
        <th>Цена</th>
    </tr>

    <tr>
        <td>Ноутбук</td>
        <td>1000$</td>
    </tr>
</table>
```

---

## Hover-эффект

Класс:

* `table-hover`

```html
<table class="table table-hover">
    <tr>
        <th>Город</th>
        <th>Страна</th>
    </tr>

    <tr>
        <td>София</td>
        <td>Болгария</td>
    </tr>
</table>
```

---

# Полный пример

```html
<!-- Начало страницы -->

<main class="container mt-4">

    <h1>
        Таблицы в HTML
    </h1>

    <p>
        Таблицы используются для отображения данных.
    </p>

    <table class="table table-striped table-hover">

        <tr>
            <th>Имя</th>
            <th>Возраст</th>
        </tr>

        <tr>
            <td>Анна</td>
            <td>25</td>
        </tr>

        <tr>
            <td>Иван</td>
            <td>30</td>
        </tr>

        <tr>
            <td>Мария</td>
            <td>35</td>
        </tr>

        <tr>
            <td>Пётр</td>
            <td>36</td>
        </tr>

    </table>

</main>

<!-- Конец страницы -->
```

---

# Мини-практика

## Задание

Создайте таблицу:

* с заголовками;
* минимум 3 строки;
* примените Bootstrap-класс `table`;
* добавьте ещё один класс по желанию (`table-striped`, `table-hover` или `table-bordered`).

---

## Пример результата

```html
<!-- Начало страницы -->

<main class="container mt-4">

    <h1>
        Список студентов
    </h1>

    <table class="table table-striped">

        <tr>
            <th>Имя</th>
            <th>Группа</th>
        </tr>

        <tr>
            <td>Анна</td>
            <td>IT-101</td>
        </tr>

        <tr>
            <td>Иван</td>
            <td>IT-102</td>
        </tr>

        <tr>
            <td>Мария</td>
            <td>IT-103</td>
        </tr>

    </table>

</main>

<!-- Конец страницы -->
```
