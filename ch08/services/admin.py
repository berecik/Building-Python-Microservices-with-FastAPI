import asyncio
from asyncio import Queue
from models.data.nsms import Admin, Billing
from cryptography.fernet import Fernet


async def process_billing(query_list):
    billing_list = []

    async def extract_billing(qlist, q: Queue):
        assigned_billing = {}
        for record in qlist:
            await asyncio.sleep(2)
            assigned_billing['admin_name'] = "{} {}".format(record.firstname, record.lastname)
            if len(record.children) != 0:
                assigned_billing['billing_items'] = record.children
            else:
                assigned_billing['billing_items'] = None

            await q.put(assigned_billing)

    async def build_billing_sheet(q: Queue):
        while True: 
            await asyncio.sleep(2)
            assigned_billing = await q.get()
            name = assigned_billing['admin_name']
            billing_items = assigned_billing['billing_items']
            if billing_items is not None:
                for item in billing_items:
                    billing_list.append({'admin_name': name, 'billing': item})
            else: 
                billing_list.append({'admin_name': name, 'billing': None})
            q.task_done()

    q = asyncio.Queue()
    build_sheet = asyncio.create_task(build_billing_sheet(q))
    await asyncio.gather(asyncio.create_task(extract_billing(query_list, q)))

    await q.join()
    build_sheet.cancel()
    return billing_list

 
async def extract_profile(admin_details):
    login = admin_details.parent
    profile = {
        'firstname': admin_details.firstname,
        'lastname': admin_details.lastname,
        'age': admin_details.age,
        'status': admin_details.status,
        'birthday': admin_details.birthday,
        'username': login.username,
        'password': login.password,
    }
    await asyncio.sleep(1)
    return profile

async def extract_condensed(profiles):
    profile_info = " ".join([profiles['firstname'], profiles['lastname'], profiles['username'], profiles['password']])
    await asyncio.sleep(1)
    return profile_info 

async def decrypt_profile(profile_info):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    return fernet.encrypt(profile_info.encode())

async def extract_enc_admin_profile(admin_rec):
    p = await extract_profile(admin_rec)
    pinfo = await extract_condensed(p)
    return await decrypt_profile(pinfo)