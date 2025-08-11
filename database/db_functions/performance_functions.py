from database.config import Performance
from database.config.engine import SessionLocal
from uuid import UUID


def paginate_query(query, page: int = 1, page_size: int = 10):
    return query.offset((page - 1) * page_size).limit(page_size).all()


def get_all_performance(campaighn_id: UUID = None, talent_id: UUID = None,page:int = 1,page_size:int = 20):
    with SessionLocal() as session:
        query= session.query(Performance)
        if talent_id != None:
            query = query.filter(Performance.talent_id == talent_id)
        if campaighn_id != None:
            query = query.filter(Performance.campaighn_id == campaighn_id)

        total = query.count()
        items = paginate_query(query,page,page_size)
