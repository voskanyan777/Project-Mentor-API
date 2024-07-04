from sqlalchemy import insert, select

class AsyncOrm:
    '''
    Class with async functions for working with database
    '''

    async def get_user_by_email(self, email):
