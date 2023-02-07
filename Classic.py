from Art import ArtPieces
import pandas as pd


class Classic(ArtPieces):
    """
    First child class Classic that inherit all the attributes and functions
    from the parent class and has new individual attributes about the origin
    of the classical art piece and the art history period it belongs to
    according to their year created. It is a subcategory of art pieces that exist in
    the reality

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
    period: str
        The art period when the art was created in
    origin: str
        The origin of the art, in this program it is the birth country of the artist
    discount : float
        The discount that used for calculation

    Methods
    -------
    checking_art_period() -> None
        It determines the art period attribute for the classical art piece by
        putting the year value through some ranges
    update_data() -> None
        It updates the new value of origin or art period to the new csv file
        since this program presumes that the user knows nothing about art periods
    """

    __period = ''
    _discount = 0.8

    def __init__(self, artist, year, name, price, origin, sold=False):
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
        origin: str
            The birth country of the artist
        sold : bool
            The condition of whether the art is already sold
        discount : float
            The discount that used for calculation
        """
        super().__init__(
            artist=artist, year=year, name=name, price=price, sold=sold
        )

        self.__origin = origin

    def checking_art_period(self) -> None:
        """
        Checking the art period by using a predetermined timeline of art history
        and categories the classical art piece by its year. It selects the
        appropriate period for the art by comparing the value to conditions with ranges

        Raises
        ------
        AttributeException
            If the attribute is non-existent and Python cannot call it
        IndexError
            The index exceeds the length of the list - 1
        """
        art_periods = "Ancient Medieval Renaissance Baroque Neoclassicism Romanticism Realism Modern PostModern".split()
        if 0 <= self._year < 400:
            self.__period = art_periods[0]
        elif 400 <= self._year < 1300:
            self.__period = art_periods[1]
        elif 1300 <= self._year < 1600:
            self.__period = art_periods[2]
        elif 1600 <= self._year < 1800:
            if self.__origin.lower() == 'rome':
                self.__period = art_periods[3]
            else:
                self.__period = art_periods[4]
        elif 1800 <= self._year < 1830:
            self.__period = art_periods[5]
        elif 1830 <= self._year < 1900:
            self.__period = art_periods[6]
        elif 1900 <= self._year < 1970:
            self.__period = art_periods[7]
        elif 1970 <= self._year < 1990:
            self.__period = art_periods[8]
        else:
            self.__period = None

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
        df.loc[art_index, 'period'] = self.__period
        df.loc[art_index, 'sold'] = self._sold
        df.to_csv('class_obj.csv', index=False)

    def __str__(self):
        """
        This is a prebuilt function that can display the class obj and their attrobutes

        Return
        ---------------
        The formatted string of the object name with their attributes shown
        """
        return f"{self.__class__.__name__} Art {self._artist}: {self._name} ({self._year} from {self.__origin})--${self._price} period:{self.__period}     sold?:{self._sold}"

