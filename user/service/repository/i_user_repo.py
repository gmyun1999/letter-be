from abc import ABCMeta, abstractmethod

from user.domain.user import User as userVo


class IUserRepo(metaclass=ABCMeta):
    class Filter:
        def __init__(
            self,
            user_id: str | None = None,
            app_id: str | None = None,
            name: str | None = None,
            app_ids: list[str] | None = None,
        ):
            self.user_id = user_id
            self.app_id = app_id
            self.app_ids = app_ids
            self.name = name

    @abstractmethod
    def get_user(self, filter: Filter) -> userVo | None:
        pass

    @abstractmethod
    def get_users_by_app_ids(self, filter: Filter) -> list[userVo]:
        pass

    @abstractmethod
    def create(self, user_vo: userVo) -> userVo:
        pass

    @abstractmethod
    def delete(self, user_vo: userVo) -> None:
        pass
