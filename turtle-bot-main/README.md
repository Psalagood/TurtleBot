# Turtle bot

Привет. Можете пушить сюда свои наработки, либо, что лучше, пушить их в отдельную ветку (не main), например:
```
git commit -m 'Новый commit'
git push origin test
```
Вместо "test" можете называть свою ветку как хотите.
Merge веток (в main) можно делать после того, как одобрим изменения (через gitlab создадим merge request)

По всем вопросам обязательно тянуть Олежкина, он всю эту кашу варит.

В начале работы:
```
git config http.sslVerify "false"
git config --global user.email "test@mail.local"
git config --global user.name "username"
git clone https://gitlab.loc/gitlab-instance-94c409ba/turtle-bot.git
# Если не работает - попробуйте вместо "gitlab.loc" использовать "172.20.0.10:443"
```

Получить новые обновления (из main)
```
git pull origin main
```
Подключиться к PSQL (DB gino, test/prod):
```
psql --host=172.70.0.10 --username=turtle_bot --dbname=gino -W
psql --host=172.70.0.110 --username=turtle_bot --dbname=gino -W
```
Или:
```
psql --host=localhost:54032 --username=turtle_bot --dbname=gino -W
psql --host=localhost:54000 --username=turtle_bot --dbname=gino -W
```
Пароль к БД у Олега
