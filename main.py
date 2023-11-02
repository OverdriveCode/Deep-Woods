from colorama import Style
import cursor
from os import system
import time
import random
from os import environ
from requests import post, get
from threading import Thread
from time import sleep
from replit import db

cursor.hide()

normal = '\033[1m'
red = '\033[38;2;255;0;0m'
orange = '\033[38;2;255;90;0m'
gold = '\033[38;2;230;190;0m'
silver = '\033[38;2;221;221;221m'
copper = '\033[38;2;170;44;0m'
paleyellow = '\033[38;2;255;255;215m'
yellow = '\033[38;2;255;255;0m'
green = '\033[38;2;00;160;00m'
lime = '\033[38;2;00;255;00m'
darkgrey = '\033[38;2;100;100;100m'
grey = '\033[38;2;130;130;130m'
turquoise = '\033[38;2;0;255;255m'
teal = '\033[38;2;0;170;170m'
blue = '\033[38;2;0;40;255m'
purple = '\033[38;2;130;0;250m'
white = '\033[38;2;255;255;255m'
platinum = '\033[38;2;205;192;255m'
ironc = '\033[38;2;255;205;192m'
brown = '\033[38;2;135;62;35m'

character = f'{teal}Hunter{white}'
user = environ['REPL_OWNER']

print(f'{Style.BRIGHT}')

all_animals = {
    'squirrel': {
        'damage': 0,
        'drop': ['animal hide x1', 'squirrel meat x1']
    },
    'lizard': {
        'damage': 0,
        'drop': ['lizard tail x1', 'lizard meat x1']
    },
    'rabbit': {
        'damage': 0,
        'drop': ['animal hide x3', 'rabbit meat x1']
    },
    'deer': {
        'damage': 0,
        'drop': ['animal hide x5', 'deer meat x1']
    },
    'buck': {
        'damage': 10,
        'drop': ['animal hide x5', 'antlers x2', 'buck meat x1']
    },
    'bear': {
        'damage':
        30,
        'drop':
        ['animal hide x10', 'bear claws x8', 'bear teeth x20', 'bear meat x2']
    },
    'wolf': {
        'damage': 20,
        'drop': ['animal hide x3', 'wolf teeth x20', 'wolf meat']
    },
    'fox': {
        'damage': 10,
        'drop': ['animal hide x3', 'fox tail', 'fox meat']
    }
}

all_foods = {
    'squirrel meat': {
        'health': 2,
        'hunger': 10
    },
    'lizard meat': {
        'health': 3,
        'hunger': 5
    },
    'rabbit meat': {
        'health': 3,
        'hunger': 13
    },
    'deer meat': {
        'health': 4,
        'hunger': 25
    },
    'buck meat': {
        'health': 5,
        'hunger': 20
    },
    'bear meat': {
        'health': 5,
        'hunger': 30
    },
    'fox meat': {
        'health': 6,
        'hunger': 20
    },
    'wolf meat': {
        'health': 7,
        'hunger': 25
    },
    'dry grass': {
        'health': 0,
        'hunger': 2
    },
    'dry shrub': {
        'health': 0,
        'hunger': 3
    },
    'vark': {
        'health': 2,
        'hunger': 1
    },
    'coneflower': {
        'health': 1,
        'hunger': 4
    },
    'burdock': {
        'health': 1,
        'hunger': 5
    },
    'berry': {
        'health': 3,
        'hunger': 3
    },
    'red clover': {
        'health': 2,
        'hunger': 4
    },
    'wood lily': {
        'health': 2,
        'hunger': 5
    },
    'wild corn': {
        'health': 1,
        'hunger': 10
    },
    'blueberry': {
        'health': 4,
        'hunger': 5
    },
    'strawberry': {
        'health': 4,
        'hunger': 6
    },
    'apple': {
        'health': 3,
        'hunger': 8
    },
    'orange': {
        'health': 4,
        'hunger': 6
    },
    'peach': {
        'health': 3,
        'hunger': 9
    },
    'karp': {
        'health': 1,
        'hunger': 7
    },
    'salmon': {
        'health': 3,
        'hunger': 6
    },
    'trout': {
        'health': 2,
        'hunger': 9
    },
    'pufferfish': {
        'health': -1,
        'hunger': 20
    },
    'sunfish': {
        'health': 5,
        'hunger': 10
    },
    'swordfish': {
        'health': 4,
        'hunger': 15
    },
    'power bar': {
        'health': 5,
        'hunger': 20
    }
}

all_weapons = {
    'wooden spear': {
        'name': 'wooden spear',
        'multiplier': 0.8
    },
    'tooth spear': {
        'name': 'tooth spear',
        'multiplier': 0.6
    },
    'wolf spear': {
        'name': 'wolf spear',
        'multiplier': 0.4
    }
}

all_boots = {
    'hide boots': {
        'name': 'hide boots',
        'spd': 4
    },
    'fox boots': {
        'name': 'fox boots',
        'spd': 5
    }
}

all_jackets = {
    'hide jacket': {
        'name': 'wooden spear',
        'defense': 2
    },
    'animal jacket': {
        'name': 'animal jacket',
        'defense': 5
    }
}

inv = [
    'medical pack x2',
    'water bottle x2',
    'power bar x3',
]

energy = 100
bear_spd = 1
bear_dis = 100
hunger = 0
thirst = 0
dis = 200
day = 1
heat = 100
health = 100

area = {
    'river': True,
    'dry': False,
    'rocky': False,
    'animals': 3,
    'plants': 7,
    'camp': False
}

sweapon = {
    'name': 'fists',
    'multiplier': 2,
}

sjacket = {'name': 'shirt', 'defense': 0}

sboots = {'name': 'shoes', 'spd': 2}

weapon = sweapon
jacket = sjacket
boots = sboots

hour = 15


def send_data():
    post(
        "https://DP-LB.bigminiboss.repl.co/person",
        json={
            "score": -day,  # just make the day negative :P
            "username": environ["REPL_OWNER"]
        })


def get_leaderboard():
    """gets first 10 people"""
    return list(
        map(
            lambda x: {
                'username': x['username'],
                'value': -x['value']
            },
            get("https://DP-LB.bigminiboss.repl.co/leaderboard",
                json={
                    "number_of_players": 10
                }).json()))


def print_leaderboard():
    lb = get_leaderboard()
    conversion = ["st", "nd", "rd"]
    for i in range(len(lb)):
        print(
            lb[i]['username'],
            f"is in {i + 1}{conversion[i] if i < len(conversion) else 'th'} place with",
            lb[i]['value'], "days")


def title():
    print(f'''
 {copper}S U R V I V E{white} | {green}F O R A G E{white} | {red}H U N T{darkgrey}
————————————————————————————————————————
 █▀▄ █▀▀ █▀▀ █▀█   █░█░█ █▀█ █▀█ █▀▄ █▀
 █▄▀ ██▄ ██▄ █▀▀   ▀▄▀▄▀ █▄█ █▄█ █▄▀ ▄█ 
————————————————————————————————————————{white}
''')


def enter():
    print(f'⌈{blue}ENTER{white}⌋ to {platinum}(continue){white}')
    input()


def clear():
    system('clear')
    title()


def lore():
    print(f'Your name is {teal}Hunter{white}')
    print(f'Never have {teal}you{white} seen such a HUGE {brown}bear{white}!')

    time.sleep(1)
    print('')

    print(
        f'It all started this {yellow}summer{white}, your family always goes {brown}bear{white} hunting during this {blue}time{white} of the year'
    )
    print(f'You and your family arrive at a {copper}cabbin{white}')

    time.sleep(1)
    print('')

    print(
        f'While your family settles down, {teal}you{white} decided to go {paleyellow}early{white}'
    )

    time.sleep(1)
    print('')

    print(
        f'Not long after exploring the {green}woods{white}, {teal}You{white} find a sign that reads, \"{grey}TITAN BEAR{white} ━❯\"'
    )
    print(f'{teal}You{white} decide to follow the {copper}sign{white}')

    time.sleep(1)
    print('')

    print(
        f'Not long {red}after{white}, {teal}you{white} find a HUGE {silver}silver{white} {brown}bear{white}'
    )
    print(
        f'Fumbling {teal}you{white} shoot the {brown}bear{white} but it only slightly {orange}slows{white} down'
    )

    time.sleep(1)
    print('')

    print(
        f'{teal}You{white} runs as {blue}fast{white} as you can to your {purple}cabin{white}'
    )
    print(f'{teal}You{white} drop your {darkgrey}gun{white} while running')
    print(f'{teal}You{white} finally makes it to the {purple}cabin{white}')
    print(f'But your {orange}family{white} is no where to be seen')

    time.sleep(1)
    print('')

    print(
        f'In a {turquoise}desperate{white} attempt to flee {teal}you{white} jump in a {platinum}golf cart{white} and speed away'
    )
    print(
        f'After about an {orange}hour{white} the golf cart runs out of {grey}gas{white}'
    )
    print(
        f'{teal}You{white} are now {blue}alone{white}, in the {green}woods{white} with a {silver}titan bear{white} chasing you!'
    )

    time.sleep(1)
    print('')

    print(
        f'The {brown}bear{white} {red}hunting{white} {blue}reservation{white} is {ironc}200{white} miles away'
    )
    enter()


def die(death):
    print(f'🪦{teal} Hunter{white}/{blue}{user}{white}🪦')
    print(f'Traveled {orange}{200-dis}{white} miles')
    print(f'Died from {red}{death}{white}')
    quit()


def covert_time(hour):
    if hour > 12:
        if hour != 24:
            new_hour = f'{hour-12} pm'
        else:
            new_hour = f'{hour-12} am'

    else:
        if hour != 12:
            new_hour = f'{hour} am'
        else:
            new_hour = f'{12} pm'
    return new_hour


def check_how_many(item):

    check = False
    final = ''

    for char in item:
        other_check = False

        try:
            total = int(char)
            other_check = True
        except:
            other_check = False

        if check is True and other_check is True:
            final = f'{final}{total}'
        if char == 'x':
            check = True

    return int(final)


def get_item(item):
    check = False
    yx = 0

    final = ''

    if True:

        for char in item:
            other_check = False

            try:
                total = int(char)
                other_check = True
            except:
                other_check = False

            if check is True and other_check is True:
                v = 2
                if check_how_many(item) > 9:
                    v = 3
                if check_how_many(item) > 99:
                    v = 4
                start_power = yx - v
            if char == 'x':
                check = True

            yx += 1

        new_item = ''

        yx = 0
        for char in item:
            if yx < start_power:
                new_item = f'{new_item}{char}'
            yx += 1

        return new_item


def remove_item(item, amount=1):
    global inv

    how_many = check_how_many(item)
    item = get_item(item)

    if True:
        inv.remove(f'{item} x{how_many}')
        if how_many - 1 != 0:
            inv.append(f'{item} x{how_many-amount}')


def fix_inv():
    global inv
    new_inv = {}

    appending = []
    removing = []

    for i in inv:
        try:
            x = get_item(i)

        except:
            removing.append(i)
            appending.append(f'{i} x1')

    for i in appending:
        inv.append(i)
    for i in removing:
        inv.remove(i)

    for i in inv:
        try:
            new_inv[get_item(i)] += check_how_many(i)
        except:
            new_inv[get_item(i)] = check_how_many(i)

    inv = []

    for x, y in new_inv.items():
        inv.append(f'{x} x{y}')


def stats():
    print(f'{character}/{blue}{user}{white}')
    print()
    print(f'Distance traveled {turquoise}{200-dis}{white}')
    print(f'Health {red}{health}{white}')
    print(f'Hunger {brown}{hunger}{white}')
    print(f'Thirst {blue}{thirst}{white}')
    print(f'Body Heat {orange}{heat}{white}')
    print(f'Energy {yellow}{energy}{white}')
    print()
    print(f'Weapon {grey}' + '{}'.format(weapon['name']) + f'{white}')
    print(f'Jacket {grey}' + '{}'.format(jacket['name']) + f'{white}')
    print(f'Boots {grey}' + '{}'.format(boots['name']) + f'{white}')


def inventory():
    global inv
    global weapon
    global health
    global hunger
    global energy
    global thirst

    while True:
        clear()
        fix_inv()

        x = 1

        for i in inv:
            print(f'({red}{x}{white}) {i}')
            x += 1

        print()
        print(f'[{red}l{white}] to {purple}leave{white}')
        print()

        commands = []

        for i in range(x):
            commands.append(str(i))

        commands.remove('0')
        commands.append('l')

        answer = input()

        while answer not in commands:
            print(f'Invalid {red}answer{white}')
            answer = input()

        if answer == 'l':
            break

        else:

            item = inv[int(answer) - 1]

            how_many = check_how_many(item)

            item = get_item(item)
            worked = False

            try:
                item_stats = all_foods[item]
                print('')
                print(f'You ate a {grey}{item}{white}')
                h_plus = item_stats['hunger']
                hl_plus = item_stats['health']
                print(f'+ {red}{hl_plus} {white}health')
                print(f'- {brown}{h_plus} {white}hunger')

                hunger -= h_plus
                health += hl_plus

                worked = True

            except:
                try:
                    item_stats = all_weapons[item]
                    print('')
                    print(f'{grey}{item}{white} {turquoise}equiped{white}!')
                    weapon['name'] = item_stats['name']
                    weapon['multiplier'] = item_stats['multiplier']

                    worked = True

                except:
                    try:
                        item_stats = all_boots[item]
                        print('')
                        print(
                            f'{grey}{item}{white} {turquoise}equiped{white}!')
                        boots['name'] = item_stats['name']
                        boots['spd'] = item_stats['spd']

                        worked = True
                    except:
                        try:
                            item_stats = all_jackets[item]
                            print('')
                            print(
                                f'{grey}{item}{white} {turquoise}equiped{white}!'
                            )
                            jacket['name'] = item_stats['name']
                            jacket['defense'] = item_stats['defense']

                            worked = True
                        except:
                            if item in ['medical pack', 'water bottle']:
                                if item == 'medical pack':
                                    print('')
                                    print(f'You used a {grey}{item}{white}')
                                    print(f'+ {red}{20} {white}health')

                                    health += 20
                                    worked = True

                                else:
                                    print('')
                                    print(f'You drank a {grey}{item}{white}')
                                    print(f'- {blue}{50} {white}thirst')

                                    inv.append('empty bottle x1')

                                    thirst -= 50
                                    worked = True

                            else:
                                print()
                                print(f'This {grey}item{white} has no use')

            if worked is True:
                remove_item(f'{item} x{how_many}')

            if thirst < 0:
                thirst = 0

            if hunger < 0:
                hunger = 0

            enter()


def craft():
    global inv

    while True:
        clear()

        items = [
            'wooden spear', 'tooth spear', 'hide boots', 'hide jacket',
            'bear tooth axe', 'wolf spear', 'fox boots', 'animal jacket'
        ]

        materials = {
            'wooden spear': ['antlers x2', 'wood x20'],
            'tooth spear': ['bear teeth x8', 'wood x20'],
            'wolf spear': ['wolf teeth x40', 'wood x20'],
            'bear tooth axe': ['bear claws x20', 'wood x20', 'bear teeth x40'],
            'animal jacket': [
                'bear claws x20', 'wood x20', 'bear teeth x40',
                'wolf teeth x40', 'animal hide x40'
            ],
            'hide boots': ['animal hide 20'],
            'hide jacket': ['animal hide x40'],
            'fox boots': ['fox tail x2', 'animal hide x20'],
        }

        print(f"""
({red}1{white}) Wooden spear    [{paleyellow}2 antlers{white}] [{brown}20 wood{white}] 
({red}2{white}) Tooth spear     [{copper}8 bear claws{white}] [{brown}20 wood{white}]
({red}3{white}) Hide Boots      [{ironc}20 animal hide{white}]
({red}4{white}) Hide jacket     [{ironc}40 animal hide{white}]
({red}5{white}) Bear Tooth Axe  [{copper}40 bear teeth{white}] [{copper}20 bear claws{white}] [{brown}20 wood{white}]
({red}6{white}) Wolf Spear      [{grey}40 wolf teeth{white}] [{brown}20 wood{white}]
({red}7{white}) Fox Boots       [{orange}2 fox tails{white}] [{ironc}20 animal hide{white}]
({red}8{white}) Animal jacket   [{ironc}40 animal hide{white}] [{copper}20 bear claws{white}] [{copper}40 bear teeth{white}] [{grey}40 wolf teeth{white}]  """
              )

        print()
        print(f'[{red}l{white}] to {purple}leave{white}')
        print()

        answer = input()
        while answer not in ['1', '2', '3', '4', '5', '6', '7', '8', 'l']:
            print(f'Invalid {red}answer{white}')
            answer = input()

        if answer == 'l':
            break

        item = items[int(answer) - 1]

        check = True

        for i in materials[item]:
            other_check = False
            ni = get_item(i)
            for x in inv:
                if check_how_many(i) <= check_how_many(x) and ni == get_item(
                        x):
                    other_check = True

            if other_check is False:
                check = False

        if check is False:
            print('')
            print(f'You don\'t have enough {blue}materials{white}!')

        else:
            for i in materials[item]:
                remove_item(get_item(i), check_how_many(i))
            print()
            print(f'{purple}{item}{white} crafted!')

            inv.append(f'{item} x1')

        enter()


def save():
    global db

    db['inv'] = inv
    db['energy'] = energy
    db['bear_dis'] = bear_dis
    db['hunger'] = hunger
    db['thirst'] = thirst
    db['dis'] = dis
    db['day'] = day
    db['heat'] = heat
    db['health'] = health
    db['area'] = area
    db['weapon'] = weapon
    db['jacket'] = jacket
    db['boots'] = boots
    db['hour'] = hour


def load():
    global db, inv, energy, bear_dis, hunger, thirst, dis, day, heat, health, area, weapon, jacket, boots, hour

    inv = db['inv']
    energy = db['energy']
    bear_dis = db['bear_dis']
    hunger = db['hunger']
    thirst = db['thirst']
    dis = db['dis']
    day = db['day']
    heat = db['heat']
    health = db['health']
    area = db['area']
    jacket = db['jacket']
    boots = db['boots']
    hour = db['hour']


title()
enter()

clear()

message1 = False

try:
    check_if_has_save = db['hour']

    print(f'Would you like to load your {blue}save{white}? yes/no')

    answer = input()

    while answer not in ['yes', 'no']:
        print(f'Invalid {red}answer{white}')
        answer = input()

    if answer == 'yes':
        load()

    elif answer == 'no':
        clear()
        lore()
        save()

        message1 = True

except:
    lore()
    save()

    message1 = True

message2 = False

sleeping = False

time_spent = 0

while dis > 0:
    save()
    fix_inv()
    clear()

    pre_hour = hour

    if hour > 24:
        hour -= 24
        day += 1

    if message1 is True:
        message1 = False
        area = {
            'river': random.choice([True, False]),
            'dry': random.choice([True, False]),
            'rocky': random.choice([True, False]),
            'animals': random.randint(1, 10),
            'plants': random.randint(1, 10),
            'camp': False
        }

        message = f'❰The {blue}area{white} you are in'

        if area['river'] is True:
            message = message + f' has a {teal}river{white}'
        else:
            message = message + f' has no {teal}river{white}'
        if area['rocky'] is True:
            message = message + f', and is {brown}rocky{white}'
        else:
            message = message + f', and isn\'t {brown}rocky{white}'
        if area['dry'] is True:
            message = message + f', and is {grey}dry{white}❯'
        else:
            message = message + f', and isn\'t {grey}dry{white}❯'

        print(message)

    if hour in range(19, 25) or hour in range(0, 6):
        print()
        print(
            f'❰Its {blue}nightime{white}, you will rapidly lose {orange}body heat{white}❯'
        )

    if message2 is True and sleeping is False:
        print()
        print(f'❰You lost {orange}{15*time_spent}{white} body heat❯')
        heat -= 15 * time_spent

    if sleeping is True:
        sleeping = False

    if hunger > 70:
        print()
        print(f'❰You are {brown}hungry{white}❯')
    if thirst > 70:
        print()
        print(f'❰You are {blue}thirsty{white}❯')

    if heat < 31:
        print()
        print(f'❰You are {turquoise}cold{white}❯')
    if energy < 31:
        print()
        print(f'❰You are {paleyellow}tired{white}❯')

    if bear_dis < 10:
        print()
        print(f'❰The {platinum}Titan Bear{white} is close❯')

    print(f"""
({red}1{white}) {green}Collect Resources{white}
({red}2{white}) {brown}Build{white}
({red}3{white}) {paleyellow}Rest{white}
({red}4{white}) {blue}Travel{white}
({red}5{white}) {purple}Stats & Inventory{white}

    
The {platinum}Titan Bear{white} is {red}{bear_dis}{white} miles away
The {brown}Bear {red}Hunting {blue}Reservation{white} is {orange}{dis}{white} miles away
It\'s day {purple}{day}{white}, it\'s {teal}{hour}:00{white} or {turquoise}{covert_time(hour)}{white}
    
    """)

    answer = input()

    while answer not in ['1', '2', '3', '4', '5']:
        print(f'Invalid {red}answer{white}')
        answer = input()

    if answer == '1':
        clear()
        print(f"""
({red}1{white}) {green}Forage{white}
({red}2{white}) {orange}Hunt{white}""")

        check = False

        for i in inv:
            if 'axe' in inv:
                check = True

        if check is True:
            print(f'({red}3{white}) {brown}Chop wood{white}')
        else:
            print(f'({red}3{white}) {brown}Gather wood{white}')

        commands = ['1', '2', '3']

        if area['river'] is True:
            print(f'({red}4{white}) {blue}Fill Water{white}')
            commands.append('4')

            print(f'({red}5{white}) {purple}Fish{white}')
            commands.append('5')

        print()
        print(f'[{red}l{white}] to {purple}leave{white}')
        print()

        commands.append('l')

        answer = input()

        while answer not in commands:
            print(f'Invalid {red}answer{white}')
            answer = input()

        if answer == 'l':
            enter()
        else:
            if answer == '1':
                clear()

                dot = ''

                for i in range(9):

                    print(f'{green}Foraging{white}{dot}')

                    if dot != '...':
                        dot = f'{dot}.'
                    else:
                        dot = ''

                    time.sleep(0.5)
                    clear()

                plant_score = area['plants'] + int(area['animals'] / 2)

                if area['dry'] is True:
                    plant_score -= 4
                if area['rocky'] is True:
                    plant_score -= 5
                if area['river'] is True:
                    plant_score += 5

                if plant_score in range(-10, 0):
                    plants = ['dry grass', 'dry shrub']
                elif plant_score in range(0, 5):
                    plants = ['vark', 'coneflower', 'burdock']
                elif plant_score in range(5, 10):
                    plants = ['berry', 'red clover', 'wood lily']
                elif plant_score in range(10, 15):
                    plants = ['wild corn', 'strawberry', 'blueberry']
                elif plant_score in range(15, 20):
                    plants = ['apple', 'orange', 'peach']

                how_many = random.randint(1, int(plant_score / 2) + 1)
                got = []

                for i in range(how_many):
                    got.append(random.choice(plants))

                no = []
                for i in got:
                    x = 0
                    if i not in no:
                        for y in got:
                            if i == y:
                                x += 1
                        inv.append(i + ' x' + str(x))
                        print(f'You got a {green}{i}{white} x{x}')

                        no.append(i)

                print()
                e_loss = random.randint(10, 20)
                h_loss = random.randint(10, 20)
                t_loss = random.randint(20, 30)
                time_loss = random.randint(1, 2)

                print(f'You lost {yellow}{e_loss}{white} energy')
                print(f'You gained {ironc}{h_loss}{white} hunger')
                print(f'You gained {blue}{t_loss}{white} thirst')
                print()

                print(f'This took {teal}{time_loss}{white} hours')

                energy -= e_loss
                hunger += h_loss
                thirst += t_loss

                hour += time_loss

                enter()

            elif answer == '3':
                check = False

                for i in inv:
                    if 'axe' in inv:
                        check = True
                if check is True:
                    clear()

                    dot = ''

                    for i in range(9):

                        print(f'{brown}Chopping Wood{white}{dot}')

                        if dot != '...':
                            dot = f'{dot}.'
                        else:
                            dot = ''

                        time.sleep(0.5)
                        clear()
                    wood_gain = random.randint(20, 25)

                    print(f'You chopped {brown}{wood_gain}{white} wood')

                    inv.append(f'wood x{wood_gain}')

                    print()
                    e_loss = random.randint(20, 30)
                    h_loss = random.randint(10, 20)
                    t_loss = random.randint(20, 30)
                    time_loss = random.randint(1, 2)

                    print(f'You lost {yellow}{e_loss}{white} energy')
                    print(f'You gained {ironc}{h_loss}{white} hunger')
                    print(f'You gained {blue}{t_loss}{white} thirst')
                    print()

                    print(f'This took {teal}{time_loss}{white} hours')

                    if random.randint(1, 20) == 1:
                        print()
                        print(f'Your {grey}axe{white} {red}broke{white}!')

                        check = False

                        for i in inv:
                            if 'axe' in i and check is False:
                                check = True
                                inv.remove(i)

                else:
                    clear()

                    dot = ''

                    for i in range(9):

                        print(f'{brown}Gathering wood{white}{dot}')

                        if dot != '...':
                            dot = f'{dot}.'
                        else:
                            dot = ''

                        time.sleep(0.5)
                        clear()
                    wood_gain = random.randint(
                        5, 10
                    )  # how do you want to print the LB, there's already a get_leaderboard func

                    print(f'You found {brown}{wood_gain}{white} wood')

                    inv.append(f'wood x{wood_gain}')

                    print()
                    e_loss = random.randint(20, 30)
                    h_loss = random.randint(10, 20)
                    t_loss = random.randint(20, 30)
                    time_loss = random.randint(1, 2)

                    print(f'You lost {yellow}{e_loss}{white} energy')
                    print(f'You gained {ironc}{h_loss}{white} hunger')
                    print(f'You gained {blue}{t_loss}{white} thirst')
                    print()

                    print(f'This took {teal}{time_loss}{white} hours')

                    energy -= e_loss
                    hunger += h_loss
                    thirst += t_loss

                    hour += time_loss

                enter()

            elif answer == '2':
                clear()

                dot = ''

                for i in range(9):

                    print(f'{orange}Hunting{white}{dot}')

                    if dot != '...':
                        dot = f'{dot}.'
                    else:
                        dot = ''

                    time.sleep(0.5)
                    clear()

                animal_score = area['animals'] + int(area['plants'] / 2)

                if area['dry'] is True:
                    animal_score -= 4
                if area['rocky'] is True:
                    animal_score -= 5
                if area['river'] is True:
                    animal_score += 5

                if animal_score in range(-10, 0):
                    animals = ['squirrel', 'lizard']
                elif animal_score in range(0, 5):
                    animals = ['rabbit', 'deer', 'buck']
                elif animal_score in range(5, 10):
                    animals = ['deer', 'buck', 'rabbit', 'bear']
                elif animal_score in range(10, 15):
                    animals = ['deer', 'buck', 'rabbit', 'bear', 'wolf']
                elif animal_score in range(15, 20):
                    animals = ['deer', 'buck', 'rabbit', 'bear', 'wolf', 'fox']

                animal = random.choice(animals)
                animal_stats = all_animals[animal]
                print(f'You found a {copper}{animal}{white}')

                if health - (animal_stats['damage'] *
                             weapon['multiplier']) < 1:
                    print(f'You were {red}killed{white} 💀')
                    print()
                    die(f'a {animal}')

                health -= int(animal_stats['damage'] * weapon['multiplier'])

                damage = int(animal_stats['damage'] * weapon['multiplier'])

                print(f'You {darkgrey}kill{white} it with your {silver}' +
                      '{}'.format(weapon['name']) + f'{white}')
                print('')
                print(
                    f'After {grey}killing{white} the {copper}{animal}{white}')
                print(f'You took {red}{damage}{white} damage')
                print(f'Health remaning {red}{health}{white}')
                print()

                for i in animal_stats['drop']:
                    print(f'You got {brown}{i}{white}')
                    inv.append(i)

                print()
                e_loss = random.randint(20, 30)
                h_loss = random.randint(20, 30)
                t_loss = random.randint(20, 30)
                time_loss = random.randint(2, 4)

                print(f'You lost {yellow}{e_loss}{white} energy')
                print(f'You gained {ironc}{h_loss}{white} hunger')
                print(f'You gained {blue}{t_loss}{white} thirst')
                print()

                print(f'This took {teal}{time_loss}{white} hours')

                energy -= e_loss
                hunger += h_loss
                thirst += t_loss

                hour += time_loss

                if random.randint(1, 20) == 1 and weapon['name'] != 'fists':
                    print()
                    print(f'Your {grey} ' + '{}'.format(weapon['name']) +
                          f' {red}broke{white}!')
                    weapon = sweapon

                enter()

            elif answer == '4':
                clear()

                dot = ''

                for i in range(9):

                    print(f'{blue}Filling Empty bottles{white}{dot}')

                    if dot != '...':
                        dot = f'{dot}.'
                    else:
                        dot = ''

                    time.sleep(0.5)
                    clear()

                x = 0
                removing = []
                appending = []
                for i in inv:
                    if 'empty bottle' in i:
                        x += check_how_many(i)
                        removing.append(i)
                        appending.append(f'water bottle x{check_how_many(i)}')

                for i in removing:
                    inv.remove(i)
                for i in appending:
                    inv.append(i)

                print(
                    f'You filled {purple}{x}{white} empty bottles with {blue}water{white}!'
                )

                print()
                e_loss = random.randint(3, 5) * x
                h_loss = random.randint(1, 5) * x
                t_loss = random.randint(1, 5) * x
                time_loss = random.randint(0, 1) * x

                print(f'You lost {yellow}{e_loss}{white} energy')
                print(f'You gained {ironc}{h_loss}{white} hunger')
                print(f'You gained {blue}{t_loss}{white} thirst')
                print()

                print(f'This took {teal}{time_loss}{white} hours')

                energy -= e_loss
                hunger += h_loss
                thirst += t_loss

                hour += time_loss

                enter()

            elif answer == '5':
                clear()

                dot = ''

                for i in range(9):

                    print(f'{purple}Fishing{white}{dot}')

                    if dot != '...':
                        dot = f'{dot}.'
                    else:
                        dot = ''

                    time.sleep(0.5)
                    clear()

                fish = [
                    'karp', 'salmon', 'trout', 'pufferfish', 'sunfish',
                    'swordfish'
                ]

                how_many = random.randint(3, 5)

                got = []

                for i in range(how_many):
                    got.append(random.choice(fish))

                no = []
                for i in got:
                    x = 0
                    if i not in no:
                        for y in got:
                            if i == y:
                                x += 1
                        inv.append(i + ' x' + str(x))
                        print(f'You got a {blue}{i}{white} x{x}')

                        no.append(i)

                print()
                e_loss = random.randint(10, 20)
                h_loss = random.randint(10, 20)
                t_loss = random.randint(20, 30)
                time_loss = random.randint(2, 3)

                print(f'You lost {yellow}{e_loss}{white} energy')
                print(f'You gained {ironc}{h_loss}{white} hunger')
                print(f'You gained {blue}{t_loss}{white} thirst')
                print()

                print(f'This took {teal}{time_loss}{white} hours')

                energy -= e_loss
                hunger += h_loss
                thirst += t_loss

                hour += time_loss

                enter()
    elif answer == '2':
        if True:
            clear()
            print(f"""
({red}1{white}) {silver}Craft{white}
({red}2{white}) {red}Build fire{white}
({red}3{white}) {copper}Build Camp{white}""")

            print()
            print(f'[{red}l{white}] to {purple}leave{white}')
            print()

            answer = input()

            while answer not in ['1', '2', '3', 'l']:
                print(f'Invalid {red}answer{white}')
                answer = input()

            if answer == 'l':
                enter()
            else:
                if answer == '1':
                    clear()
                    craft()
                    print()
                    enter()

                elif answer == '2':
                    clear()
                    check = False

                    for i in inv:
                        if 'wood' in i:
                            how_many = check_how_many(i)

                            if how_many > 4:
                                check = True

                    if check is False:
                        print(f'You don\'t have enough {brown}wood{white}!')
                        print(f'You need {brown}5{white} wood')
                        enter()

                    else:
                        dot = ''

                        for i in range(9):

                            print(f'{red}Building A Fire{white}{dot}')

                            if dot != '...':
                                dot = f'{dot}.'
                            else:
                                dot = ''

                            time.sleep(0.5)
                            clear()

                        print(f'{red}Fire{white} made!')
                        print(f'Body Heat {orange}100{white}')

                        heat = 100

                        for i in inv:
                            if 'wood' in i:
                                remove_item(i, 5)

                        print()
                        e_loss = random.randint(5, 10)
                        h_loss = random.randint(5, 10)
                        t_loss = random.randint(10, 20)
                        time_loss = random.randint(0, 1)

                        print(f'You lost {yellow}{e_loss}{white} energy')
                        print(f'You gained {ironc}{h_loss}{white} hunger')
                        print(f'You gained {blue}{t_loss}{white} thirst')
                        print()

                        print(f'This took {teal}{time_loss}{white} hours')

                        energy -= e_loss
                        hunger += h_loss
                        thirst += t_loss

                        hour += time_loss

                        enter()

                elif answer == '3':
                    clear()
                    check = False

                    for i in inv:
                        if 'wood' in i:
                            how_many = check_how_many(i)

                            if how_many > 9:
                                check = True

                    if check is False:
                        print(f'You don\'t have enough {brown}wood{white}!')
                        print(f'You need {brown}10{white} wood')
                        enter()

                    else:
                        dot = ''

                        for i in range(9):

                            print(f'{copper}Building A Camp{white}{dot}')

                            if dot != '...':
                                dot = f'{dot}.'
                            else:
                                dot = ''

                            time.sleep(0.5)
                            clear()

                        print(f'{copper}Camp{white} made!')
                        area['camp'] = True
                        print(
                            f'You won\'t lose {orange}heat{white} when sleeping during the {blue}night{white}'
                        )
                        print(
                            f'If you travel you can\'t take your {copper}camp{white} with you'
                        )

                        for i in inv:
                            if 'wood' in i:
                                remove_item(i, 10)

                        print()
                        e_loss = random.randint(10, 20)
                        h_loss = random.randint(10, 20)
                        t_loss = random.randint(20, 30)
                        time_loss = random.randint(1, 3)

                        print(f'You lost {yellow}{e_loss}{white} energy')
                        print(f'You gained {ironc}{h_loss}{white} hunger')
                        print(f'You gained {blue}{t_loss}{white} thirst')
                        print()

                        print(f'This took {teal}{time_loss}{white} hours')

                        energy -= e_loss
                        hunger += h_loss
                        thirst += t_loss

                        hour += time_loss

                        enter()
    elif answer == '5':
        if True:
            clear()
            print(f"""
({red}1{white}) {purple}Stats{white}
({red}2{white}) {darkgrey}Inventory{white}
({red}3{white}) {gold}Leaderboard{white}""")

            print()
            print(f'[{red}l{white}] to {purple}leave{white}')
            print()

            answer = input()

            while answer not in ['1', '2', '3', 'l']:
                print(f'Invalid {red}answer{white}')
                answer = input()

            if answer == 'l':
                enter()
            else:

                if answer == '1':
                    clear()
                    stats()
                    print()
                    enter()

                if answer == '2':
                    clear()
                    inventory()
                    print()
                    enter()

                if answer == '3':
                    clear()
                    print_leaderboard()
                    print()
                    enter()

    elif answer == '4':
        if True:
            clear()
            print(f"""
({red}1{white}) {purple}Long Walk{white}
({red}2{white}) {blue}Short Walk{white}
({red}3{white}) {grey}Short Run{white}""")

            print()
            print(f'[{red}l{white}] to {purple}leave{white}')
            print()

            answer = input()

            while answer not in ['1', '2', '3', 'l']:
                print(f'Invalid {red}answer{white}')
                answer = input()

            if answer == 'l':
                enter()
            else:
                if answer == '1':
                    message1 = True
                    clear()

                    dot = ''

                    for i in range(9):

                        print(f'{purple}Walking{white}{dot}')

                        if dot != '...':
                            dot = f'{dot}.'
                        else:
                            dot = ''

                        time.sleep(0.5)
                        clear()

                    print(f'{copper}Walk{white} complete!')
                    traveled = boots['spd'] * 5
                    print(f'You traveled {orange}{traveled}{white} miles')

                    dis -= traveled

                    print()
                    e_loss = random.randint(20, 30)
                    h_loss = random.randint(20, 30)
                    t_loss = random.randint(30, 40)
                    time_loss = 5

                    print(f'You lost {yellow}{e_loss}{white} energy')
                    print(f'You gained {ironc}{h_loss}{white} hunger')
                    print(f'You gained {blue}{t_loss}{white} thirst')
                    print()

                    print(f'This took {teal}{time_loss}{white} hours')

                    energy -= e_loss
                    hunger += h_loss
                    thirst += t_loss

                    hour += time_loss
                    enter()
                elif answer == '2':
                    message1 = True
                    clear()

                    dot = ''

                    for i in range(9):

                        print(f'{purple}Walking{white}{dot}')

                        if dot != '...':
                            dot = f'{dot}.'
                        else:
                            dot = ''

                        time.sleep(0.5)
                        clear()

                    print(f'{copper}Walk{white} complete!')
                    traveled = boots['spd'] * 1
                    print(f'You traveled {orange}{traveled}{white} miles')

                    dis -= traveled

                    print()
                    e_loss = random.randint(10, 20)
                    h_loss = random.randint(10, 20)
                    t_loss = random.randint(10, 20)
                    time_loss = 1

                    print(f'You lost {yellow}{e_loss}{white} energy')
                    print(f'You gained {ironc}{h_loss}{white} hunger')
                    print(f'You gained {blue}{t_loss}{white} thirst')
                    print()

                    print(f'This took {teal}{time_loss}{white} hours')

                    energy -= e_loss
                    hunger += h_loss
                    thirst += t_loss

                    hour += time_loss
                    enter()
                elif answer == '3':
                    message1 = True
                    clear()

                    dot = ''

                    for i in range(9):

                        print(f'{red}Running{white}{dot}')

                        if dot != '...':
                            dot = f'{dot}.'
                        else:
                            dot = ''

                        time.sleep(0.5)
                        clear()

                    print(f'{copper}Walk{white} complete!')
                    traveled = (boots['spd'] * 2)
                    print(f'You traveled {orange}{traveled}{white} miles')

                    dis -= traveled

                    print()
                    e_loss = random.randint(20, 30)
                    h_loss = random.randint(20, 30)
                    t_loss = random.randint(20, 30)
                    time_loss = 1

                    print(f'You lost {yellow}{e_loss}{white} energy')
                    print(f'You gained {ironc}{h_loss}{white} hunger')
                    print(f'You gained {blue}{t_loss}{white} thirst')
                    print()

                    print(f'This took {teal}{time_loss}{white} hours')

                    energy -= e_loss
                    hunger += h_loss
                    thirst += t_loss

                    hour += time_loss
                    enter()
                bear_dis += traveled
    elif answer == '3':
        if True:
            clear()
            print(f"""
({red}1{white}) {grey}Sleep{white}
({red}2{white}) {paleyellow}Nap{white}
({red}3{white}) {yellow}Idle{white}""")

            print()
            print(f'[{red}l{white}] to {purple}leave{white}')
            print()

            answer = input()

            while answer not in ['1', '2', '3', 'l']:
                print(f'Invalid {red}answer{white}')
                answer = input()

            if answer in ['1', '2', '3']:
                sleeping = True

            if answer == 'l':
                enter()

            else:

                if answer == '1':
                    clear()

                    dot = ''

                    for i in range(9):

                        print(f'{grey}Sleeping{white}{dot}')

                        if dot != '...':
                            dot = f'{dot}.'
                        else:
                            dot = ''

                        time.sleep(0.5)
                        clear()

                    print(f'{grey}Sleep{white} complete!')
                    print(f'Energy {yellow}100{white}')

                    energy = 100

                    print()
                    heat_loss = random.randint(40, 60)
                    h_loss = random.randint(10, 20)
                    t_loss = random.randint(10, 20)
                    time_loss = 10

                    if hour in range(
                            19, 25) and area['camp'] is False or hour in range(
                                0, 6) and area['camp'] is False:
                        heat -= heat_loss
                        print(f'You lost {orange}{heat_loss}{white} heat')
                    print(f'You gained {ironc}{h_loss}{white} hunger')
                    print(f'You gained {blue}{t_loss}{white} thirst')
                    print()

                    print(f'This took {teal}{time_loss}{white} hours')
                    hunger += h_loss
                    thirst += t_loss

                    hour += time_loss
                    enter()
                elif answer == '2':
                    clear()

                    dot = ''

                    for i in range(9):

                        print(f'{paleyellow}Napping{white}{dot}')

                        if dot != '...':
                            dot = f'{dot}.'
                        else:
                            dot = ''

                        time.sleep(0.5)
                        clear()

                    print(f'{paleyellow}Nap{white} complete!')
                    print(f'Energy +{yellow}30{white}')

                    energy = min(100, energy + 30)

                    print()
                    heat_loss = random.randint(20, 30)
                    h_loss = random.randint(5, 10)
                    t_loss = random.randint(5, 10)
                    time_loss = 4

                    if hour in range(
                            19, 25) and area['camp'] is False or hour in range(
                                0, 6) and area['camp'] is False:
                        heat -= heat_loss
                        print(f'You lost {orange}{heat_loss}{white} heat')
                    print(f'You gained {ironc}{h_loss}{white} hunger')
                    print(f'You gained {blue}{t_loss}{white} thirst')
                    print()

                    print(f'This took {teal}{time_loss}{white} hours')
                    hunger += h_loss
                    thirst += t_loss

                    hour += time_loss
                    enter()
                elif answer == '3':
                    clear()

                    dot = ''

                    for i in range(9):

                        print(f'{yellow}Idling{white}{dot}')

                        if dot != '...':
                            dot = f'{dot}.'
                        else:
                            dot = ''

                        time.sleep(0.5)
                        clear()

                    print(f'{yellow}Idle{white} complete!')
                    print(f'Energy +{yellow}10{white}')

                    energy = min(100, energy + 10)

                    print()
                    heat_loss = random.randint(10, 20)
                    h_loss = random.randint(1, 3)
                    t_loss = random.randint(2, 7)
                    time_loss = 1

                    if hour in range(
                            19, 25) and area['camp'] is False or hour in range(
                                0, 6) and area['camp'] is False:
                        heat -= heat_loss
                        print(f'You lost {orange}{heat_loss}{white} heat')
                    print(f'You gained {ironc}{h_loss}{white} hunger')
                    print(f'You gained {blue}{t_loss}{white} thirst')
                    print()

                    print(f'This took {teal}{time_loss}{white} hours')
                    hunger += h_loss
                    thirst += t_loss

                    hour += time_loss
                    enter()

    time_spent = hour - pre_hour

    if hour not in range(19, 25) and hour not in range(0, 6):
        if random.randint(1, 2) == 1:
            bear_dis -= max(bear_spd * (hour - pre_hour), 0)

    if hour in range(19, 25) or hour in range(0, 6):
        message2 = True

    if time_spent > hour - 20:
        time_spent = hour - 20

    if time_spent <= 0:
        message2 = False

    if bear_dis < 1:
        clear()
        print(f'You {red}died{white} 💀')
        print()
        die(f'the TITAN BEAR')

    if hunger > 100:
        clear()
        print(f'You {red}died{white} 💀')
        print()
        die(f'hunger')
    if thirst > 100:
        clear()
        print(f'You {red}died{white} 💀')
        print()
        die(f'dehydration')
    if heat < 0:
        clear()
        print(f'You {red}died{white} 💀')
        print()
        die(f'freezing')
    if energy < 0:
        clear()
        print(f'You {red}died{white} 💀')
        print()
        die(f'exhaustion')

clear()
print(f'{gold}YOU DID IT!{white}')
print(f'You {blue}survived{white} and made it to {turquoise}safety{white}')
print()

send_data()
print_leaderboard()

quit()
