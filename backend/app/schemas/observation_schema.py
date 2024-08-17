from enum import Enum

from decimal import Decimal

from pydantic import BaseModel, Field


class ObservationModel(BaseModel):
    """Info required to query the ml model."""
    sepal_length: Decimal = Field(
        description= "Sepal Length (cm)",
        gt=0, le=11, decimal_places=2)
    sepal_width: Decimal = Field(
        description="Sepal Width (cm)",
        gt=0, le=6, decimal_places=2)
    petal_length: Decimal = Field(
        description="Petal Length (cm)",
        gt=0, le=10, decimal_places=2)
    petal_width: Decimal = Field(
        description="Petal Width (cm)",
        gt=0, le=4, decimal_places=2)


class SpeciesEnum(str, Enum):
    setosa = 'setosa'
    versicolor = 'versicolor'
    virginica = 'virginica'


class SpeciesModel(BaseModel):
    """Contains species."""
    species: SpeciesEnum
