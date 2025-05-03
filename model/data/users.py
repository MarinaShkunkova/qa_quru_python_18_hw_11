import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile_number: str
    year_of_birth: str
    month_of_birth: str
    day_of_birth: str
    subject: str
    hobby: str
    picture: str
    address: str
    state: str
    city: str


user = User(first_name='Masha',
            last_name='Ivanova',
            email='MIvanova@yandex.ru',
            gender='Female',
            mobile_number='5648765439',
            year_of_birth='1980',
            month_of_birth='July',
            day_of_birth='22',
            subject='History',
            hobby='Reading',
            picture='picture.jpeg',
            address='Moscow, Pionovaya street, 12',
            state='NCR',
            city='Gurgaon')
