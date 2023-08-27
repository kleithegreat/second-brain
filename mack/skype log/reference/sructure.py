from enum import Enum
from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Callable, Type, cast
from uuid import UUID
from datetime import datetime
import dateutil.parser


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y)
 for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


class Messagetype(Enum):
    EVENT_CALL = "Event/Call"
    INVITE_FREE_RELATIONSHIP_CHANGED_INITIALIZED = "InviteFreeRelationshipChanged/Initialized"
    NOTICE = "Notice"
    POP_CARD = "PopCard"
    RICH_TEXT = "RichText"
    RICH_TEXT_CONTACTS = "RichText/Contacts"
    RICH_TEXT_MEDIA_ALBUM = "RichText/Media_Album"
    RICH_TEXT_MEDIA_CALL_RECORDING = "RichText/Media_CallRecording"
    RICH_TEXT_MEDIA_CARD = "RichText/Media_Card"
    RICH_TEXT_MEDIA_GENERIC_FILE = "RichText/Media_GenericFile"
    RICH_TEXT_MEDIA_VIDEO = "RichText/Media_Video"
    RICH_TEXT_URI_OBJECT = "RichText/UriObject"
    TEXT = "Text"
    THREAD_ACTIVITY_ADD_MEMBER = "ThreadActivity/AddMember"
    THREAD_ACTIVITY_DELETE_MEMBER = "ThreadActivity/DeleteMember"
    THREAD_ACTIVITY_HISTORY_DISCLOSED_UPDATE = "ThreadActivity/HistoryDisclosedUpdate"
    THREAD_ACTIVITY_JOINING_ENABLED_UPDATE = "ThreadActivity/JoiningEnabledUpdate"
    THREAD_ACTIVITY_PICTURE_UPDATE = "ThreadActivity/PictureUpdate"
    THREAD_ACTIVITY_ROLE_UPDATE = "ThreadActivity/RoleUpdate"
    THREAD_ACTIVITY_TOPIC_UPDATE = "ThreadActivity/TopicUpdate"
    TRANSLATION_SETTINGS = "TranslationSettings"


@dataclass
class User:
    mri: str
    time: int
    value: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        assert isinstance(obj, dict)
        mri = from_str(obj.get("mri"))
        time = from_int(obj.get("time"))
        value = from_union([from_str, from_none], obj.get("value"))
        return User(mri, time, value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["mri"] = from_str(self.mri)
        result["time"] = from_int(self.time)
        if self.value is not None:
            result["value"] = from_union([from_str, from_none], self.value)
        return result


@dataclass
class Emotion:
    key: str
    users: List[User]

    @staticmethod
    def from_dict(obj: Any) -> 'Emotion':
        assert isinstance(obj, dict)
        key = from_str(obj.get("key"))
        users = from_list(User.from_dict, obj.get("users"))
        return Emotion(key, users)

    def to_dict(self) -> dict:
        result: dict = {}
        result["key"] = from_str(self.key)
        result["users"] = from_list(lambda x: to_class(User, x), self.users)
        return result


class Isserversidegenerated(Enum):
    TRUE = "True"


@dataclass
class MessageListProperties:
    urlpreviews: Optional[str] = None
    edittime: Optional[str] = None
    isserversidegenerated: Optional[Isserversidegenerated] = None
    deletetime: Optional[str] = None
    album_id: Optional[UUID] = None
    emotions: Optional[List[Emotion]] = None
    call_log: Optional[str] = None
    forward_metadata: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MessageListProperties':
        assert isinstance(obj, dict)
        urlpreviews = from_union([from_str, from_none], obj.get("urlpreviews"))
        edittime = from_union([from_str, from_none], obj.get("edittime"))
        isserversidegenerated = from_union([Isserversidegenerated, from_none], obj.get("isserversidegenerated"))
        deletetime = from_union([from_str, from_none], obj.get("deletetime"))
        album_id = from_union([lambda x: UUID(x), from_none], obj.get("albumId"))
        emotions = from_union([lambda x: from_list(Emotion.from_dict, x), from_none], obj.get("emotions"))
        call_log = from_union([from_str, from_none], obj.get("call-log"))
        forward_metadata = from_union([from_str, from_none], obj.get("forwardMetadata"))
        return MessageListProperties(urlpreviews, edittime, isserversidegenerated, deletetime, album_id, emotions, call_log, forward_metadata)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.urlpreviews is not None:
            result["urlpreviews"] = from_union([from_str, from_none], self.urlpreviews)
        if self.edittime is not None:
            result["edittime"] = from_union([from_str, from_none], self.edittime)
        if self.isserversidegenerated is not None:
            result["isserversidegenerated"] = from_union([lambda x: to_enum(Isserversidegenerated, x), from_none], self.isserversidegenerated)
        if self.deletetime is not None:
            result["deletetime"] = from_union([from_str, from_none], self.deletetime)
        if self.album_id is not None:
            result["albumId"] = from_union([lambda x: str(x), from_none], self.album_id)
        if self.emotions is not None:
            result["emotions"] = from_union([lambda x: from_list(lambda x: to_class(Emotion, x), x), from_none], self.emotions)
        if self.call_log is not None:
            result["call-log"] = from_union([from_str, from_none], self.call_log)
        if self.forward_metadata is not None:
            result["forwardMetadata"] = from_union([from_str, from_none], self.forward_metadata)
        return result


@dataclass
class MessageList:
    id: str
    originalarrivaltime: datetime
    messagetype: Messagetype
    version: int
    content: str
    conversationid: str
    message_list_from: str
    display_name: Optional[str] = None
    properties: Optional[MessageListProperties] = None
    amsreferences: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MessageList':
        assert isinstance(obj, dict)
        id = from_str(obj.get("id"))
        originalarrivaltime = from_datetime(obj.get("originalarrivaltime"))
        messagetype = Messagetype(obj.get("messagetype"))
        version = from_int(obj.get("version"))
        content = from_str(obj.get("content"))
        conversationid = from_str(obj.get("conversationid"))
        message_list_from = from_str(obj.get("from"))
        display_name = from_union([from_none, from_str], obj.get("displayName"))
        properties = from_union([from_none, MessageListProperties.from_dict], obj.get("properties"))
        amsreferences = from_union([from_none, lambda x: from_list(from_str, x)], obj.get("amsreferences"))
        return MessageList(id, originalarrivaltime, messagetype, version, content, conversationid, message_list_from, display_name, properties, amsreferences)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_str(self.id)
        result["originalarrivaltime"] = self.originalarrivaltime.isoformat()
        result["messagetype"] = to_enum(Messagetype, self.messagetype)
        result["version"] = from_int(self.version)
        result["content"] = from_str(self.content)
        result["conversationid"] = from_str(self.conversationid)
        result["from"] = from_str(self.message_list_from)
        result["displayName"] = from_union([from_none, from_str], self.display_name)
        result["properties"] = from_union([from_none, lambda x: to_class(MessageListProperties, x)], self.properties)
        result["amsreferences"] = from_union([from_none, lambda x: from_list(from_str, x)], self.amsreferences)
        return result


class Conversationstatus(Enum):
    ACCEPTED = "Accepted"
    ACCEPT_PENDING_RECIPIENT = "AcceptPendingRecipient"
    ACCEPT_PENDING_SENDER = "AcceptPendingSender"


@dataclass
class ConversationProperties:
    conversationblocked: bool
    lastimreceivedtime: Optional[datetime] = None
    consumptionhorizon: Optional[str] = None
    conversationstatus: Optional[Conversationstatus] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ConversationProperties':
        assert isinstance(obj, dict)
        conversationblocked = from_bool(obj.get("conversationblocked"))
        lastimreceivedtime = from_union([from_none, from_datetime], obj.get("lastimreceivedtime"))
        consumptionhorizon = from_union([from_none, from_str], obj.get("consumptionhorizon"))
        conversationstatus = from_union([from_none, Conversationstatus], obj.get("conversationstatus"))
        return ConversationProperties(conversationblocked, lastimreceivedtime, consumptionhorizon, conversationstatus)

    def to_dict(self) -> dict:
        result: dict = {}
        result["conversationblocked"] = from_bool(self.conversationblocked)
        result["lastimreceivedtime"] = from_union([from_none, lambda x: x.isoformat()], self.lastimreceivedtime)
        result["consumptionhorizon"] = from_union([from_none, from_str], self.consumptionhorizon)
        result["conversationstatus"] = from_union([from_none, lambda x: to_enum(Conversationstatus, x)], self.conversationstatus)
        return result


@dataclass
class Consumptionhorizon:
    id: str
    consumptionhorizon: str

    @staticmethod
    def from_dict(obj: Any) -> 'Consumptionhorizon':
        assert isinstance(obj, dict)
        id = from_str(obj.get("id"))
        consumptionhorizon = from_str(obj.get("consumptionhorizon"))
        return Consumptionhorizon(id, consumptionhorizon)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_str(self.id)
        result["consumptionhorizon"] = from_str(self.consumptionhorizon)
        return result


@dataclass
class Consumptionhorizons:
    version: str
    consumptionhorizons: List[Consumptionhorizon]

    @staticmethod
    def from_dict(obj: Any) -> 'Consumptionhorizons':
        assert isinstance(obj, dict)
        version = from_str(obj.get("version"))
        consumptionhorizons = from_list(Consumptionhorizon.from_dict, obj.get("consumptionhorizons"))
        return Consumptionhorizons(version, consumptionhorizons)

    def to_dict(self) -> dict:
        result: dict = {}
        result["version"] = from_str(self.version)
        result["consumptionhorizons"] = from_list(lambda x: to_class(Consumptionhorizon, x), self.consumptionhorizons)
        return result


@dataclass
class ThreadProperties:
    membercount: int
    description: None
    guidelines: None
    members: Optional[str] = None
    topic: Optional[str] = None
    picture: Optional[str] = None
    consumptionhorizons: Optional[Consumptionhorizons] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ThreadProperties':
        assert isinstance(obj, dict)
        membercount = from_int(obj.get("membercount"))
        description = from_none(obj.get("description"))
        guidelines = from_none(obj.get("guidelines"))
        members = from_union([from_none, from_str], obj.get("members"))
        topic = from_union([from_none, from_str], obj.get("topic"))
        picture = from_union([from_none, from_str], obj.get("picture"))
        consumptionhorizons = from_union([Consumptionhorizons.from_dict, from_none], obj.get("consumptionhorizons"))
        return ThreadProperties(membercount, description, guidelines, members, topic, picture, consumptionhorizons)

    def to_dict(self) -> dict:
        result: dict = {}
        result["membercount"] = from_int(self.membercount)
        result["description"] = from_none(self.description)
        result["guidelines"] = from_none(self.guidelines)
        result["members"] = from_union([from_none, from_str], self.members)
        result["topic"] = from_union([from_none, from_str], self.topic)
        result["picture"] = from_union([from_none, from_str], self.picture)
        result["consumptionhorizons"] = from_union([lambda x: to_class(Consumptionhorizons, x), from_none], self.consumptionhorizons)
        return result


@dataclass
class Conversation:
    id: str
    version: int
    properties: ConversationProperties
    message_list: List[MessageList]
    display_name: Optional[str] = None
    thread_properties: Optional[ThreadProperties] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Conversation':
        assert isinstance(obj, dict)
        id = from_str(obj.get("id"))
        version = from_int(obj.get("version"))
        properties = ConversationProperties.from_dict(obj.get("properties"))
        message_list = from_list(MessageList.from_dict, obj.get("MessageList"))
        display_name = from_union([from_none, from_str], obj.get("displayName"))
        thread_properties = from_union([ThreadProperties.from_dict, from_none], obj.get("threadProperties"))
        return Conversation(id, version, properties, message_list, display_name, thread_properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_str(self.id)
        result["version"] = from_int(self.version)
        result["properties"] = to_class(ConversationProperties, self.properties)
        result["MessageList"] = from_list(lambda x: to_class(MessageList, x), self.message_list)
        result["displayName"] = from_union([from_none, from_str], self.display_name)
        result["threadProperties"] = from_union([lambda x: to_class(ThreadProperties, x), from_none], self.thread_properties)
        return result


@dataclass
class Messages2:
    user_id: str
    export_date: str
    conversations: List[Conversation]

    @staticmethod
    def from_dict(obj: Any) -> 'Messages2':
        assert isinstance(obj, dict)
        user_id = from_str(obj.get("userId"))
        export_date = from_str(obj.get("exportDate"))
        conversations = from_list(Conversation.from_dict, obj.get("conversations"))
        return Messages2(user_id, export_date, conversations)

    def to_dict(self) -> dict:
        result: dict = {}
        result["userId"] = from_str(self.user_id)
        result["exportDate"] = from_str(self.export_date)
        result["conversations"] = from_list(lambda x: to_class(Conversation, x), self.conversations)
        return result


def messages2_from_dict(s: Any) -> Messages2:
    return Messages2.from_dict(s)


def messages2_to_dict(x: Messages2) -> Any:
    return to_class(Messages2, x)
