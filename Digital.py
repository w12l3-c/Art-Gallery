from Art import ArtPieces
from bs4 import BeautifulSoup as soup
import requests
import pandas as pd


class Digital(ArtPieces):
    """
    Second child class Digital, it is the subcategory of art pieces nowadays in
    digital form, meaning that it is most likely created by painting software and
    exist in forms of illustrations and NFTs. It exists in the virtual world. It inherited
    all the attributes and functions in the parent class while having new properties
    like the website it was uploaded.

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
    discount : float
        The discount that used for calculation
    format: str
        All objects in Digital has the same format, Digital
    website: str
        The website that the art was uploaded, or currently selling, basically any online
        platform that this art is posted.

    Methods
    -------
    calculate_price() -> None
        Scrape the newest conversion price from ethereum to CAD from cryptocurrency websites
        and calculate the price of the Digital art (NFT in this case) to a real cash
    reverse_price() -> None
        Scrape the newest conversion price from ethereum to CAD from cryptocurrency websites
        and reverse the price of the Digital art from CAD back to ethereum in order to prepare the value
        for next time running the program
    update_data() -> None
        Updating the newly calculated price into the csv file, since the price of
        eth can change vastly than CAD
    """

    __format = 'Digital'
    _discount = 0.9

    def __init__(self, artist: str, year: int, name: str, price: float, website: str, sold=False):
        """
        Constructor to build a classical art piece object

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
        website: str
            The website where the art is uploaded
        sold : bool
            The condition of whether the art is already sold
        discount : float
            The discount that used for calculation
        """
        super().__init__(
            artist=artist, year=year, name=name, price=price, sold=sold
        )
        if year < 1980:
            raise ValueError(f"Digital Art doesn't exist at {year}")

        self.__website = website

    def calculate_price(self) -> None:
        """
        Converting price of ethereum into CAD when the price of the art is an NFT
        that is auctioned in ETH on most NFT trading platforms. The price conversion
        value is scraped from the website https://coinmarketcap.com/currencies/ethereum/eth/cad/

        Raises
        ------
        AttributeException
            If the attribute is non-existent and Python cannot call it
        TypeError
            If the scraping text is a NoneType, so it cannot convert the value
            into float for calculation
        Request.Exceptions
            If the website url doesn't exist, the request.get will fail because it is missing
            schema. Will happen if one day the host decide brought down their website
        """
        html_text = requests.get("https://coinmarketcap.com/currencies/ethereum/eth/cad/").text
        html_soup = soup(html_text, "lxml")
        eth_to_cad = html_soup.find("div", {"class": "priceValue"}).span.text
        eth_to_cad = ''.join(char for char in eth_to_cad if char not in '$,')
        eth_to_cad = float(eth_to_cad)
        self._price = round(self._price * eth_to_cad, 2)

    def reverse_price(self) -> None:
        """
        Reversing the price of CAD back to ETH for data saving purpose. The price conversion
        value is scraped from the website https://coinmarketcap.com/currencies/ethereum/eth/cad/

        Raises
        ------
        AttributeException
            If the attribute is non-existent and Python cannot call it
        TypeError
            If the scraping text is a NoneType, so it cannot convert the value
            into float for calculation
        Request.Exceptions
            If the website url doesn't exist, the request.get will fail because it is missing
            schema. Will happen if one day the host decide brought down their website
        """
        html_text = requests.get("https://coinmarketcap.com/currencies/ethereum/eth/cad/").text
        html_soup = soup(html_text, "lxml")
        cad_to_eth = html_soup.find("div", {"class": "priceValue"}).span.text
        cad_to_eth = ''.join(char for char in cad_to_eth if char not in '$,')
        cad_to_eth = float(cad_to_eth)
        self._price = round(self._price/cad_to_eth, 2)

    def update_data(self) -> None:
        """
        Updating the data with the newly obtained art period
        by editing the data in the csv file through dataframe

        Raises
        ------
        AttributeException
            If the attribute is non-existent and Python cannot call it
        FileNotFoundError
            If the file has not created, or it doesn't exist
        KeyError
            If the key value doesn't exit, it will be calling a non-existing value pair
        """
        df = pd.read_csv("class_obj.csv").copy()
        art_index = df[df['name'] == self._name].index[0]
        df.loc[art_index, 'format'] = self.__format
        df.loc[art_index, 'price'] = self._price
        df.loc[art_index, 'sold'] = self._sold
        df.to_csv('class_obj.csv', index=False)

    def __str__(self):
        """
        This is a prebuilt function that can display the class obj and their attributes

        Return
        ---------------
        The formatted string of the object name with their attributes shown
        """
        return f"{self.__class__.__name__} Art {self._artist}: {self._name} ({self._year})--${self._price} website:{self.__website}    sold?:{self._sold}"


