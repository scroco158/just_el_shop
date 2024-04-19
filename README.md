Задание 1

Создайте новое приложения для работы с пользователем. 
Определите собственную форму для пользователя, 
при этом задайте электронную почту как поле для авторизации.

Также добавьте поля:

    аватар,
    номер телефона,
    страна.

    Не забудьте откатить миграции приложения auth
    до внесения изменений в настройки проекта и переопределения модели для авторизации. 
    Если этого не сделать, вы не сможете взаимодействовать с базой данных. 
    Чтобы откатить миграции приложения auth , можно воспользоваться командой
    python manage.py migrate auth zero


Задание 2

В сервисе реализуйте функционал аутентификации, а именно:

    1. Регистрация пользователя по почте и паролю.
          Создайте контроллер для регистрации, который будет взаимодействовать с 
          формой регистрации — пользователю достаточно ввести почту и пароль.

    
    2. Верификация почты пользователя через отправленное письмо.

            В контроллере регистрации переопределите метод form_valid()
            и встройте автоматическую отправку электронного сообщения пользователю на 
            указанный в форме регистрации адрес.
            Для отправки электронной почты воспользуйтесь встроенной в Django функцией
            send_mail()

    3. Авторизация пользователя.
        
            Создайте отдельный контроллер для авторизации (LoginView) и зарегистрируйте его в приложении.

    4. Восстановление пароля зарегистрированного пользователя на автоматически сгенерированный пароль.
            Создайте новый контроллер для восстановления пароля.
            В интерфейсе кнопка «Восстановить пароль» должна отображаться на странице входа.
            Пользователь вводит адрес электронной почты, в контроллере происходит генерация пароля, 
            перезапись пароля для пользователя с соответсвующим адресом электронной почты и отправка сообщения 
            с новым паролем на адрес почты.
            Пароль можно сгенерировать с помощью библиотеки random

        .

            Помните, что пароль в базе данных хранится в захешированном виде. 
            Для установки пароля пользователю можно воспользоваться функцией
            make_password()
            (посмотреть в документации про эту функцию).



для запуска приложения необходимо:
в файле config/settings.py


EMAIL_HOST = 'smtp.mail.ru'
изменить адрес который будет использоваться

EMAIL_PORT = '465'                                      
изменить порт на который будет использоваться

EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
создать переменную окружения это эл.адрес с которого будет происходить рассылка

EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')  
создать переменную окружения пароль доступа для стороннего приложения  
