import traceback, random

from utils.db_api.schemas.schema_user import User
from utils.db_api.schemas.schema_turtle import Turtle
from utils.db_api.db_gino import db

async def add_user(user_id: int, username: str, status: str, name: str, surname: str, role='USER'):
    '''Добавить пользователя в БД'''
    try:
        user = User(user_id=user_id, username=username,
                    status=status, name=name,
                    surname=surname, role=role)
        await user.create()
    except:
        print('Пользователь не добавлен в БД!', traceback.format_exc())


async def add_turtle(turtle_id: int, comm: str, weight: str, user_id: int, issuer_id: int, admin_id: int, status: str):
    '''Добавить черепаху в БД'''
    try:
        turtle = Turtle(turtle_id=turtle_id, comm=comm,
                        weight=weight, user_id=user_id,
                        issuer_id=issuer_id, admin_id=admin_id,
                        status=status)
        await turtle.create()
    except:
        print('Черепаха не добавлена в БД!', traceback.format_exc())


async def select_all_users():
    '''Выбрать всех пользователей из БД'''
    users = await User.query.gino.all()
    return users

async def count_users():
    '''Посчитать количество пользователей в БД'''
    count = db.func.count(User.user_id).gino.scalar()
    return count

async def select_user(user_id):
    '''Получить пользователя из БД по его Telegram id'''
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user

async def drop_user(user):
    '''Удалить пользователя из БД'''
    await user.delete()

async def update_user_name(user_id, new_name):
    '''Обновить имя пользователя'''
    user = await select_user(user_id)
    await user.update(update_name=new_name).apply()

async def get_user_role(user_id):
    '''Получить роль пользователя из БД по его Telegram id'''
    user = await select_user(user_id)
    return user.role

async def select_turtle(turtle_id):
    '''Получить черепаху из БД по её id'''
    turtle = await Turtle.query.where(Turtle.turtle_id == turtle_id).gino.first()
    return turtle

async def generate_turtle_id():
    '''Сгенерировать уникальный id для черепахи'''
    while True:
        turtle_id = random.randint(1_000_000, 999_999_999)
        if await select_turtle(turtle_id) == None:
            return turtle_id
        else:
            pass

async def report_single_turtle(turtle_id, header, show_issuer=None, show_reciever=None):
    '''Сформировать отчет о конкретной черепахе по её id'''
    turtle = await select_turtle(turtle_id)
    user_rec = await select_user(turtle.user_id)
    message = header + '\n'
    message += f'ID чепепахи: {turtle_id}\n'
    if show_issuer:
        user_iss = await select_user(turtle.issuer_id)
        message += f'Отправитель: {user_iss.name} {user_iss.surname}\n'
    if show_reciever:
        message += f'Получатель: {user_rec.name} {user_rec.surname}\n'
    message += f'Критичность: {turtle.weight}\n'
    message += f'Комментарий: {turtle.comm}'
    return message


async def count_user_turtles(user_id):
    '''Посчитать черепах пользователя по его Telegram id'''
    turtles = await Turtle.query.where(Turtle.user_id == user_id).where(Turtle.status == 'ACTIVE').gino.all()
    result = {'minor':[], 'major':[], 'critical':[], 'letal':[], 'fatality':[]}
    for turtle in turtles:
        if 'minor' in turtle.weight:
            result['minor'].append(turtle.comm)
        elif 'major' in turtle.weight:
            result['major'].append(turtle.comm)
        elif 'critical' in turtle.weight:
            result['critical'].append(turtle.comm)
        elif 'letal' in turtle.weight:
            result['letal'].append(turtle.comm)
        elif 'fatality' in turtle.weight:
            result['fatality'].append(turtle.comm)
    return result

async def select_all_turtles():
    '''Получить всех черепах из БД'''
    turtles = await Turtle.query.gino.all()
    return turtles

async def report_user_turtles(user_id):
    '''Собрать отчет по черепахам пользователя через его Telegram id
    {'minor': 0, 'major': 0, 'critical': 0, 'letal': 0, 'fatality': 0}'''
    crit = await count_user_turtles(user_id)
    final_message = 'Ваши черепахи:\n'
    delimeter = '__________________________________'
    for c in crit:
        if len(crit[c]) == 0:
            final_message += c + ': 0\n'
            final_message += delimeter + '\n'
        else:
            final_message += c + ': ' + str(len(crit[c])) + '\n'
            for comm in crit[c]:
                final_message += comm + '\n'
            final_message += delimeter + '\n'
    return final_message

