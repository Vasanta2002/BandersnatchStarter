from os import getenv
from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient


class Database:
    """
    A class representing a MongoDB database and collection for Monster data.

    Attributes:
        database: A MongoClient instance representing the MongoDB connection.
        collection: The MongoDB collection for storing Monster data.
    """

    load_dotenv()
    database = MongoClient(getenv('DB_URL'), tlsCAFile=where())['Database']

    def __init__(self, collection: str):
        """
        Initialize the Database object.

        Parameters:
            collection (str): The name of the MongoDB collection.
        """
        self.collection = self.database[collection]

    def seed(self, amount):
        """
        Seed the collection with a specified number of Monster documents.

        Parameters:
            amount (int): The number of Monster documents to insert.

        Returns:
            pymongo.results.InsertManyResult: The result of the insertion operation.
        """
        amount = int(amount)
        lis = []
        for i in range(amount):
            monster = Monster()
            lis.append(monster.to_dict())
        return self.collection.insert_many(lis)

    def reset(self):
        """Delete all documents from the collection."""
        self.collection.delete_many({})

    def count(self) -> int:
        """
        Get the number of documents in the collection.

        Returns:
            int: The number of documents in the collection.
        """
        return self.collection.count_documents({})

    def dataframe(self) -> DataFrame:
        """
        Convert the collection data to a Pandas DataFrame.

        Returns:
            DataFrame: The DataFrame representing the collection data.
        """
        cursor = self.collection.find()
        data_list = list(cursor)
        return DataFrame(data_list)

    def html_table(self) -> str:
        """
        Generate an HTML table from the collection data.

        Returns:
            str: The HTML table as a string or None if the collection is empty.
        """
        count = self.count()
        if count == 0:
            return None

        cursor = self.collection.find()
        data_list = list(cursor)

        if not data_list:
            return None

        df = DataFrame(data_list)
        return df.to_html()


#if __name__ == '__main__':
    #db = Database("Collection")
    #db.seed(1000)
    #print('U did it')

