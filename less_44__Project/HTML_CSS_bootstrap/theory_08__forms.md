# 7. Формы

## Краткое описание

Формы в HTML используются для взаимодействия с пользователем:

* ввод текста;
* отправка данных;
* регистрация;
* поиск;
* обратная связь.

Форма состоит из полей ввода и кнопок.

---

# Основной контейнер формы

## Тег `<form>`

Оборачивает все элементы формы.

```html
<form>
    ...
</form>
```

---

## Куда отправляются данные

Главный атрибут:

* `action` — адрес отправки данных (пока можно не использовать)
* `method` — способ отправки (`GET` или `POST`)

---

## Пример

```html
<form action="/submit" method="post">
    ...
</form>
```

---

# Поле ввода текста

## Тег `<input type="text">`

Используется для ввода текста.

---

## Пример

```html
<input type="text" placeholder="Введите имя">
```

---

## Атрибут `placeholder`

Подсказка внутри поля.

---

# Кнопка

## Тег `<button>`

Используется для отправки формы или действий.

---

## Пример

```html
<button>
    Отправить
</button>
```

---

# Полная простая форма

## Пример

```html
<form>

    <input type="text" placeholder="Ваше имя">

    <button>
        Отправить
    </button>

</form>
```

---

# Bootstrap и формы

Bootstrap делает формы более удобными и красивыми.

---

## Класс для поля ввода:

* `form-control`

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

# Bootstrap кнопки

## Класс:

* `btn`
* `btn-primary`

---

## Пример

```html
<button class="btn btn-primary">
    Отправить
</button>
```

---

# Дополнительные типы input

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

# Полный пример страницы

```html 
<!-- Начало страницы -->

<main class="container mt-4">

    <h1>
        Форма обратной связи
    </h1>

    <div class="container">
        <div class="row justify-content-center">
            <div class="col-12 col-md-6 col-lg-5">
    
                <form class="p-3 border rounded shadow-sm">
    
                    <!-- скрытое поле -->
                    <input type="hidden" name="form_id" value="12345">
    
                    <div class="mb-3">
                        <label for="name" class="form-label">Ваше имя</label>
                        <input
                            type="text"
                            class="form-control"
                            id="name"
                            name="name"
                            placeholder="Введите имя"
                            required
                        >
                    </div>
    
                    <div class="mb-3">
                        <label for="email" class="form-label">Email</label>
                        <input
                            type="email"
                            class="form-control"
                            id="email"
                            name="email"
                            placeholder="name@example.com"
                            required
                        >
                    </div>
    
                    <div class="mb-3">
                        <label for="age" class="form-label">Возраст</label>
                        <input
                            type="number"
                            class="form-control"
                            id="age"
                            name="age"
                            min="0"
                            max="120"
                            placeholder="Введите возраст"
                        >
                    </div>
    
                    <div class="mb-3">
                        <label for="rating" class="form-label">Оценка (0–10)</label>
                        <input
                            type="range"
                            class="form-range"
                            id="rating"
                            name="rating"
                            min="0"
                            max="10"
                            step="1"
                        >
                        <div class="d-flex justify-content-between">
                            <small class="text-muted">0</small>
                            <small class="text-muted">10</small>
                        </div>
                    </div>
    
                    <div class="mb-3">
                        <label for="comment" class="form-label">Комментарий</label>
                        <textarea
                            class="form-control"
                            id="comment"
                            name="comment"
                            rows="3"
                            placeholder="Напишите что-нибудь..."
                        ></textarea>
                    </div>
    
                    <button type="submit" class="btn btn-primary w-100">
                        Отправить
                    </button>
    
                </form>
    
            </div>
        </div>
    </div>

</main>

<!-- Конец страницы -->
```
---

# Мини-практика

## Задание
Создайте форму:
- поле имени;
- поле email;
- поле возраста;
- кнопку отправки;
- используйте Bootstrap-классы.

---

## Пример результата

```html
<!-- Начало страницы -->

<main class="container mt-4">

    <h1>
        Регистрация
    </h1>

    <form>

        <div class="mb-3">
            <input type="text" class="form-control" placeholder="Имя">
        </div>

        <div class="mb-3">
            <input type="email" class="form-control" placeholder="Email">
        </div>

        <div class="mb-3">
            <input type="number" class="form-control" placeholder="Возраст">
        </div>

        <button class="btn btn-success">
            Зарегистрироваться
        </button>

    </form>

</main>

<!-- Конец страницы -->
````
