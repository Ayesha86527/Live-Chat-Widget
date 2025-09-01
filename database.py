from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


URL_DATABASE="postgresql://postgres.wcqnfnnbyoriwudlpula:Revotic45##@aws-1-ap-south-1.pooler.supabase.com:6543/postgres"

engine=create_engine(URL_DATABASE)

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()

