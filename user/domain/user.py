from dataclasses import dataclass
from enum import StrEnum

from common.domain import Domain


class OAuthType(StrEnum):
    KAKAO = "kakao"
    GOOGLE = "google"
    APPLE = "apple"


class RelationType(StrEnum):
    FRIEND = "FRIEND"
    # 추가 가능


class RelationStatus(StrEnum):
    PENDING = "PENDING"
    REJECT = "REJECT"
    SUCCESS = "SUCCESS"


@dataclass
class User(Domain):
    """
    유저: OAuth 로그인만 가능
    """

    FIELD_ID = "id"
    FIELD_APP_ID = "app_id"
    FIELD_NAME = "name"
    FIELD_EMAIL = "email"
    FIELD_MOBILE_NO = "mobile_no"
    FIELD_OAUTH_TYPE = "oauth_type"
    FIELD_OAUTH_ID = "oauth_id"
    FIELD_TOS_AGREED = "tos_agreed"
    FIELD_CREATED_AT = "created_at"
    FIELD_UPDATED_AT = "updated_at"

    id: str
    app_id: str
    name: str | None
    email: str | None
    mobile_no: str | None
    oauth_type: OAuthType
    oauth_id: str
    tos_agreed: bool
    created_at: str
    updated_at: str


@dataclass
class UserRelation(Domain):
    """
    유저끼리의 관계 정의
    """

    FIELD_ID = "id"
    FIELD_TO_ID = "to_id"
    FIELD_FROM_ID = "from_id"
    FIELD_RELATION_TYPE = "relation_type"
    FIELD_RELATION_STATUS = "relation_status"
    FIELD_CREATED_AT = "created_at"
    FIELD_UPDATED_AT = "updated_at"

    id: str
    to_id: str
    from_id: str
    relation_type: RelationType
    relation_status: RelationStatus
    created_at: str
    updated_at: str


@dataclass
class OAuthUser:
    id: str  # id는 uuid가 아니라 Oauth server가 넘겨준 id 를 의미함
    oauth_type: OAuthType
    name: str | None = None
    email: str | None = None
    mobile_no: str | None = None
