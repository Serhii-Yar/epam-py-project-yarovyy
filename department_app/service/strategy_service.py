from sqlalchemy.orm import lazyload, joinedload, subqueryload, selectinload, raiseload, noload


class StrategiesService:
    strategies = {lazyload, joinedload, subqueryload, selectinload, raiseload, noload}

    @classmethod
    def _check_strat(cls,strat):
        if strat not in cls.strategies:
            raise ValueError(f'Use only supported strategies: {cls.strategies}')
