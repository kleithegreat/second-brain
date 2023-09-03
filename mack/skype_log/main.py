from typing import Any, List, Optional
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from bs4 import BeautifulSoup
from datetime import datetime
import csv


@dataclass_json
@dataclass
class Properties:
    conversationblocked: bool
    lastimreceivedtime: Optional[str]
    consumptionhorizon: Optional[str]
    conversationstatus: Optional[str]


@dataclass_json
@dataclass
class ConsumptionHorizons:
    id: str
    consumptionhorizon: str


@dataclass_json
@dataclass
class ConsumptionHorizons2:
    version: str
    consumptionhorizons: List[ConsumptionHorizons]


@dataclass_json
@dataclass
class ThreadProperties:
    membercount: int
    members: Optional[str]
    topic: Optional[str]
    picture: Optional[Any]
    description: Optional[Any]
    guidelines: Optional[Any]
    consumptionhorizons: Optional[str]


@dataclass_json
@dataclass
class Message:
   id: str
   displayName: Optional[Any]
   originalarrivaltime: str
   messagetype: str
   version: float
   content: str
   conversationid: str
   from_: str = field(metadata=config(field_name="from"))
   properties: Optional[Any]
   amsreferences: Optional[Any]


@dataclass_json
@dataclass
class Conversation:
    id: str
    displayName: Optional[str]
    version: float
    properties: Properties
    threadProperties: Optional[ThreadProperties]
    MessageList: List[Message]


@dataclass_json
@dataclass
class Document:
    userId: str
    exportDate: str
    conversations: List[Conversation]


def parse_duration(duration: float) -> str:
    """Convert duration in seconds to a format (hours:minutes:seconds)."""
    duration = int(duration)
    hours, remainder = divmod(duration, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def parse_timestamp(timestamp: str):
    """Parse timestamp into date, time and duration."""
    try:
        return datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%fZ")
    except ValueError:
        return datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")


def extract_call_logs(messages: List[Message]) -> List[dict]:
    """Extract call logs from messages."""
    call_logs = []
    for message in messages:
        if message.messagetype == "Event/Call":
            # Parse the XML content to get duration
            soup = BeautifulSoup(message.content, "html.parser")
            duration_tag = soup.find("duration")
            if duration_tag is None:
                print(f"Warning: No duration tag found in message {message.id}. Skipping this message.")
                continue  # Skip this message and go to the next one
            duration = duration_tag.text
            duration = parse_duration(float(duration))
            
            # Parse the originalarrivaltime to get date and time
            timestamp = parse_timestamp(message.originalarrivaltime)
            date = timestamp.strftime("%m/%d/%Y")
            time = timestamp.strftime("%H:%M:%S")
            
            call_logs.append({"date": date, "timestamp": time, "duration": duration})
    return call_logs


def clean_filename(filename):
    """Remove or replace invalid characters for file names."""
    if filename is None:
        return "NoName"
        
    invalid_chars = ["<", ">", ":", "\"", "/", "\\", "|", "?", "*"]
    for char in invalid_chars:
        filename = filename.replace(char, "_")
    return filename


def generate_call_logs(document: Document):
    """Generate CSV file with call logs from Skype data."""
    
    for conversation in document.conversations:
        id = clean_filename(conversation.id)
        displayName = clean_filename(conversation.displayName)
        filename = id + "_" + displayName
        
        call_logs = extract_call_logs(conversation.MessageList)
        if call_logs:
            with open(f"output/{filename}.csv", mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Date", "Timestamp", "Duration"])
                for log in call_logs:
                    writer.writerow(log.values())


with open('formatted.json', 'r', encoding='utf-8') as f:
    data = Document.from_json(f.read())

generate_call_logs(data)
