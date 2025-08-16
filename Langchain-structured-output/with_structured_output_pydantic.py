from langchain_openai import ChatOpenAI
from typing import Literal, List, Optional
from pydantic import BaseModel, Field
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

class StructuredOutput(BaseModel):
    key_features: List[str] = Field(description="Key features of the product")
    summary: str
    sentiment: Literal["positive", "neutral", "negative"]
    pros: Optional[List[str]] = Field(default=None, description="Pros about the product")
    cons: Optional[List[str]] = Field(default=None, description="Cons about the product")

model = ChatOpenAI()

text = """Got myself a M4 MBP 14' base model without any added features. Coming from a 8/256 M1 Macbook Air, my real-life use has been a big jump in performance and user experience.

As a PhD student with a month of use, I can say this machine is a beast. My day to day use involves writing and presentations, chrome tabs, AI tools, SPSS data processing and light video editing. I find the 24 hour battery life promise delivers while the HDMI and extra ports comes handy for my work needs. Not needing a dongle is a win here too.

Was initially kicking myself for not getting the M4 Pro due to faster speeds and larger RAM, but the base model is enough for my needs. If I have to compare between the two, the battery life on the regular M4 is the biggest win IMO, and the priority for me.

Though the thunderbolt 4 ports aren't as fast as the ones on the M4 Pro, I also do not own any high end accessories, nor do I require the latest compatible high end accessories such as ultra fast hard-drives or ultra high resolution monitors.

RAM-wise, I have so far not maxxed out the given 16GB, though it could be a concern later on, only time will tell. If it weren't for my tight budget, I would perhaps added on the RAM, though that would mean waiting another week or so for the specced-out unit, coming from where I live.

All in all, this beast performs exceptionally well for my use, and I consider myself a fairly regular user. I based my decision to buy this masterpiece of a laptop on what I need it for NOW, and it is serving me well.

Anyone else with base M4 MBP kind enough to share your experience? pros: ["Great battery life", "Multiple ports", "Good performance for regular use"], cons: ["Limited RAM upgrade options"]"""

output = model.with_structured_output(StructuredOutput).invoke(text)
pprint(dict(output))
