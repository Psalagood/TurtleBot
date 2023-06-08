from aiogram.dispatcher.filters.state import StatesGroup, State


class all_balances(StatesGroup):
    balanceT = State() #состояние баланса черепах
    balanceT2 = State()
    balanceL = State() #состояние баланса лайков
    balanceL2 = State()

class start_feedback(StatesGroup):
    comm = State()

class start_register(StatesGroup):
    name = State()
    surname = State()

class admin_register(StatesGroup):
    user = State()
    reg_id = State()
    action = State()

class turtle_add(StatesGroup):
    reciever = State()
    reason = State()
    crit = State()

class like_add(StatesGroup):
    reciever = State()
    reason = State()
    crit = State()


class turtle_register(StatesGroup):
    turtle_id = State()
    action = State()
    admin = State()

class admin_get_user_stats(StatesGroup):
    user = State()