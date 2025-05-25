from faker import Faker
import random
import sys
import re

LOCALES = {
    "ua": "uk_UA",
    "ru": "ru_RU",
    "by": "ru_RU",
    "us": "en_US",
    "de": "de_DE"
}

PROFESSIONS_EDUCATION = {
    "Агроном": ["Агрономія", "Сільськогосподарський університет", "Агрономічний факультет"],
    "Інженер": ["Інженерія", "Технічний університет", "Факультет інженерії"],
    "Програміст": ["Комп'ютерні науки", "ІТ-університет", "Факультет інформатики"],
    "Лікар": ["Медицина", "Медичний університет", "Факультет лікувальної справи"],
    "Вчитель": ["Педагогіка", "Педагогічний інститут", "Факультет освіти"],
    "Юрист": ["Право", "Юридична академія", "Юридичний факультет"],
    "Менеджер": ["Менеджмент", "Економічний університет", "Факультет менеджменту"],
    "Бухгалтер": ["Бухгалтерія", "Економічний університет", "Факультет фінансів"]
}

def generate_email(full_name):
    name = full_name.lower()
    name = re.sub(r"[^a-zA-Z]", " ", name)
    parts = name.split()
    if len(parts) >= 2:
        username = f"{parts[0]}.{parts[1]}"
    elif parts:
        username = parts[0]
    else:
        username = "user"
    username = re.sub(r"[^a-z]", "", username)
    domains = ["gmail.com", "yahoo.com", "outlook.com", "mail.com"]
    return f"{username}@{random.choice(domains)}"

def generate_username(full_name):
    name = full_name.lower()
    name = re.sub(r"[^a-zA-Z]", " ", name)
    parts = name.split()
    if len(parts) >= 2:
        base = f"{parts[0]}_{parts[1]}"
    elif parts:
        base = parts[0]
    else:
        base = "user"
    base = re.sub(r"[^a-z]", "", base)
    return base + str(random.randint(10, 99))

def generate_socials(full_name):
    username = generate_username(full_name)
    return {
        "Telegram": f"@{username}",
        "Instagram": f"https://instagram.com/{username}",
        "Facebook": f"https://facebook.com/{username}"
    }

def generate_car(fake):
    brands = ["Toyota Corolla", "BMW 320i", "Skoda Octavia", "Audi A4", "Ford Focus", "Lada Vesta"]
    plate = f"{random.choice('ABCEHK')}{random.randint(1000,9999)}{random.choice('ABCEHK')}{random.choice('ABCEHK')}"
    return f"{random.choice(brands)} ({plate})"

def generate_education_and_profession():
    profession = random.choice(list(PROFESSIONS_EDUCATION.keys()))
    edu_list = PROFESSIONS_EDUCATION[profession]
    education_field, university, faculty = edu_list[0], edu_list[1], edu_list[2]
    education = f"{university}, {faculty} ({education_field})"
    return profession, education

def generate_profile(fake):
    gender = random.choice(["male", "female"])
    if gender == "male":
        full_name = fake.name_male()
        father = fake.first_name_male()
        mother = fake.first_name_female()
    else:
        full_name = fake.name_female()
        father = fake.first_name_male()
        mother = fake.first_name_female()

    profession, education = generate_education_and_profession()
    socials = generate_socials(full_name)

    dob = fake.date_of_birth(minimum_age=18, maximum_age=65)
    if hasattr(dob, 'strftime'):
        dob_str = dob.strftime("%d.%m.%Y")
    else:
        dob_str = str(dob)

    profile = {
        "ПІБ": full_name,
        "Стать": gender,
        "Дата народження": dob_str,
        "Ім'я батька": father,
        "Ім'я матері": mother,
        "Сімейний стан": random.choice(["одружений", "неодружений", "розлучений"]),
        "Кількість дітей": random.choice([0, 0, 1, 2]),
        "Освіта": education,
        "Професія": profession,
        "Адреса": fake.address().replace("\n", ", "),
        "Телефон": fake.phone_number(),
        "Email": generate_email(full_name),
        "Місце роботи": fake.company(),
        "Авто": generate_car(fake),
        "Соцмережі": socials,
        "Фото": f"https://thispersondoesnotexist.com/?rnd={random.randint(10000,99999)}"
    }
    return profile

def ascii():
   return """
....................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
..........................................148-+abccbb]-962..........................................
......................................_mvswszwvutrstvvvsedqxn+:.....................................
.....................................p%v+5:..............16[s&x.....................................
.....................................0vdqwpjec[+====]adfkotzdz=.....................................
.......................................18]dglossttvuvtroke]92.......................................
....................................................................................................
...........n0.................................:7]dd[8:.................................=l...........
..........d%s..............................:bwrrszv>L.wb1.............................:f&a..........
..........a,mq...........................1jn.q_1.7gv.K**vf:...........................v.,x..........
..........fa8va7........................_vmk2..5bse,>L>:HHe9........................9wf6eq..........
..........mm:1qnq6.....................c:q5....8ess.:L::K:>b_.....................8sbo:3>j..........
..........3,r..7pfwa1.................b*w:...1_jxn<::>L:.rLH.9.................2awdn6..x.2..........
.........:.0no...2dxwuc6.............0Lz.....7chpznHKLLLKdsvHd3.............5bsqwc2...rm9.:.........
.........vaeaez8....5dqxwnb6........2vr2....6fvb.vn:LKncvm,is%w.........4anvzrc4....9vebevs.........
.........p*orwb<v0......7bnxxf:.....tK0...bqvsn[967-bod..exv=s&e......bwwre9:.....0u>nvrp&o.........
.........3fs22=ivwtb6:.....:+rs1..._*o..ar>s8..........-r,:ea1v.3...:wv[:.....:6bsqxj=22wf3.........
..........4vce....6==7.......f:7...sn16v:t6..............3mK>g=Kq...5<h.......7=_6....dvx3..........
............=wai6............g:6..=Hic<d_..................0q*nw:6..3Lk............6gsv=............
...........eibkqnwnc05:......bH8..t<s:q:.....................p*sLm..7Hd......:5-cnqbqlcic...........
...........a,.mehmkfb-1......2nk.:c::h........................j:Kw..kb2......1-bgkkhfo<.+...........
............6rqm-:............=s35.>k..........................mH.23s_............:=oqq4............
..............6hvwsmfaa]6......653mn4..........................5:n:56......6[abflqsqd4..............
................-nvefvh-:.........p&l..........................m^l.........1_hwfdvm0................
................9qwzlb_0_+c[3.....:q:u6......................4vLk.2....4cc]_-_amqfq8................
..................:0dlnkkc-1..8gwb..+emq6..................5ome0.fmqoc7.1_gklljd8:..................
...........................+qddtoqd1..]zbv-..............0s,q[.1mcc:K:nek5..........................
.........................cqzm=1..3cc3...9qrv[:.........]wrs0.:bqi8cL<><KKmp2........................
........................m<h.........:.....2+nrb1....1aoo[1...9-.6ef,Lf::KmHa:.......................
.......................d>i.:5.............g5.3aj8..8ie4.b7.....[qirndnK>veKKg.......................
......................7bt..:t0............nl...:4..5:...re....=f0kp5.q:a.nHbn9......................
......................vb3...ca:...........is............vj....13=7..[:s1+:s7me1.....................
.....................cL[.13..zd...........iu............xl.....:...1d<-2xg..h*g.....................
....................2vv...=4.az...........lv............xp.........jrq.32....sf:....................
....................bb5...:5.:v5..........ow............xo........_a=b.......0ma....................
....................gj........h-..........ou............zo.......:5.g6........da....................
....................21........99..........hq............xj..........[...............................
...............................:..........+l............[0..........:...............................
..........................................:5........................................................
....................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
"""

def main():
    try:
        count_str = input("Скільки особистостей згенерувати? ")
        if not count_str.isdigit():
            print("Помилка: введено не число.")
            return
        count = int(count_str)

        locale_input = input("Введи локалізацію (ua, ru, by, us, de): ").strip().lower()

        if locale_input not in LOCALES:
            print(f"Непідтримувана локалізація '{locale_input}'")
            return

        fake = Faker(LOCALES[locale_input])
        Faker.seed(random.randint(0, 9999))
        print(ascii())

        for i in range(count):
            print(f"\n=== Особистість #{i + 1} ===")
            profile = generate_profile(fake)
            for key, value in profile.items():
                if isinstance(value, dict):
                    print(f"{key}:")
                    for subkey, subval in value.items():
                        print(f"  {subkey}: {subval}")
                else:
                    print(f"{key}: {value}")

    except Exception as e:
        print("Сталася помилка:", e)

if __name__ == "__main__":
    main()
