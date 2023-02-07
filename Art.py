import random
import pandas as pd


class ArtPieces:
    """
    A class that hold the artist, year created, name of the art, price,
    whether it is sold, and discount value of the art piece

    Attributes
    ----------
    artist : str
        The name of the artist
    year : int
        The year value when the art was created
    name : str
        The name of the art
    price : float
        The price of the art in normal currency
    sold : bool
        The condition of whether the art is already sold
    discount : str
        The discount that used for calculation

    Methods
    -------
    compare_price() -> str
        Compare the price between two art pieces
    get_discount() -> float
        A 50% chance of winning a discount and reduce the price of the art
    buying() -> int
        The buying of the art and turning the condition sold to True
    name() -> str
        Getter for attribute name
    """

    _discount = 0.75

    def __init__(self, artist: str, year: int, name: str, price: float, sold):
        """
        Constructor to build an art piece object

        Parameters
        ----------
        artist : str
            The name of the artist
        year : int
            The year value when the art was created
        name : str
            The name of the art
        price : float
            The price of the art in normal currency
        sold : bool
            The condition of whether the art is already sold
        discount : float
            The discount that used for calculation
        """
        self._name = name
        self._artist = artist
        self._year = year
        self._price = price
        self._sold = sold

    def __str__(self):
        """
        This is a prebuilt function that can display the class obj in strings instead of <class object at XXXXXXXXXXXXX>

        Return
        ---------------
        The formatted string of the object name with their attributes shown
        """
        return f"{self.__class__.__name__} Art {self._artist}: {self._name} ({self._year})--${self._price}    sold?:{self._sold}"

    def compare_price(self, art_compare):
        """
        Comparing the price between two art pieces
        This will collect the data from the csv file for both art pieces,
        and calculate the difference between the price with a message to the
        console about it

        Parameters
        ----------
        art_compare : str
            The another art piece the user wanted to compare the with

        Returns
        -------
        str
            A statement where it includes the difference between the price of two
            art pieces after calculations

        Raises
        ------
        AttributeException
            If the attribute is non-existent and Python cannot call it
        FileNotFoundError
            If the file has not created, or it doesn't exist
        KeyError
            If the key value doesn't exit, it will be calling a non-existing value pair
        """
        # df is pandas Dataframe, pd is Pandas
        df = pd.read_csv("class_obj.csv")
        self_art_index = df[df['name'] == self._name].index[0]
        self_art_price = df.loc[self_art_index, 'price']
        compared_art_index = df[df['name'] == art_compare].index[0]
        compared_art_price = df.loc[compared_art_index, 'price']

        diff_price = compared_art_price - self_art_price
        return f"The price difference between {self._name} and {art_compare} is ${diff_price}"

    def get_discount(self) -> float:
        """
        Random getting discounts, there is a 50% probability that
        the art will be on 20% discount (80% of the original price)
        then change the price to the new price

        Return
        -------
        float
            The new calculated price by the multiplication of discount value and price

        Raises
        ------
        AttributeException
            If the attribute is non-existent and Python cannot call it
        """
        if random.random() > 0.5:
            self._price = self._price * self._discount
            return self._price * self._discount

    def buying(self, money) -> int:
        """
        Buying the artwork by the user, it will turn the condition that the
        Art is not sold (False) to being sold (True)

        Parameters
        ----------
        money : int
            The money the user currently have on his/her budget

        Returns
        -------
        int
            A statement which restate which art the user bought and how much money they
            had left

        Raises
        ------
        AttributeException
            If the attribute is non-existent and Python cannot call it
        ValueError
            If the user didn't have enough money to buy the art, it will raise
            Value Error and a message that told the user the lack of budget
        """
        self._sold = True
        if money < self._price:
            raise ValueError("You cannot buy an Art without enough money")
        money -= self._price
        return money

    @property
    def name(self):
        """
        The name attribute getter

        Returns
        -------
        str
            The name of the object
        """
        return self._name
