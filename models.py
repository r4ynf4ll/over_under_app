from sqlmodel import Field, SQLModel, create_engine

class participants(SQLModel, table=True):
    name:str = Field(primary_key=True)
    diamondbacks:str
    braves:str
    orioles:str
    redsox:str
    cubs:str
    whitesox:str
    reds:str
    guardians:str
    rockies:str
    tigers:str
    astros:str
    royals:str
    angels:str
    dodgers:str
    marlins:str
    brewers:str
    twins:str
    mets:str
    yankees:str
    athletics:str
    phillies:str
    pirates:str
    padres:str
    giants:str
    mariners:str
    cardinals:str
    rays:str
    rangers:str
    bluejays:str
    nationals:str
    favteam:str

class stats(SQLModel, table=True):
    diamondbacks:float = Field(primary_key=True)
    braves:float
    orioles:float
    redsox:float
    cubs:float
    whitesox:float
    reds:float
    guardians:float
    rockies:float
    tigers:float
    astros:float
    royals:float
    angels:float
    dodgers:float
    marlins:float
    brewers:float
    twins:float
    mets:float
    yankees:float
    athletics:float
    phillies:float
    pirates:float
    padres:float
    giants:float
    mariners:float
    cardinals:float
    rays:float
    rangers:float
    bluejays:float
    nationals:float
    favteam:float

engine = create_engine('sqlite:///baseball.db')
SQLModel.metadata.create_all(engine)