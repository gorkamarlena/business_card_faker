from faker import Faker
fake = Faker('en_US')

class BaseContact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f'{self.name}, {self.phone}, {self.email}'
    
    def contact(self):
        return (f'I am choosing number {self.phone} and calling to {self.name}')
    
    @property
    def label_length(self):
        return len(self.name)

    
class BusinessContact(BaseContact):
    def __init__(self,job,company,work_phone, *args , **kwargs):
        super().__init__(*args, **kwargs)
        self.job = job
        self.company = company
        self.work_phone = work_phone


def __str__(self):
        return f'{self.name}, {self.phone}, {self.email}, {self.job}, {self.company}, {self.work_phone}'

def create_contact(kind, amount):
    if kind == BaseContact:
        for i in range(0,amount):
            i = BaseContact(name=fake.name(),phone=fake.phone_number(), email=fake.email())
            print(i)
    if kind == BusinessContact:
        for i in range (0, amount):
            i = BusinessContact(name=fake.name(),phone=fake.phone_number(), email=fake.email(), job=fake.job(),company=fake.company(),work_phone=fake.phone_number())
            print(i)

create_contact(BusinessContact, 5)




