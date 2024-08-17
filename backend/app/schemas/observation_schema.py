from enum import Enum

from pydantic import BaseModel, Field


class ObservationModel(BaseModel):
    """Info required to query the ml model."""
    sepal_length: float = Field(
        description= "Sepal Length (cm)",
        gt=0, le=11)
    sepal_width: float = Field(
        description="Sepal Width (cm)",
        gt=0, le=6)
    petal_length: float = Field(
        description="Petal Length (cm)",
        gt=0, le=10)
    petal_width: float = Field(
        description="Petal Width (cm)",
        gt=0, le=4)


class SpeciesEnum(str, Enum):
    setosa = 'setosa'
    versicolor = 'versicolor'
    virginica = 'virginica'


class SpeciesModel(BaseModel):
    """Contains species."""
    species: SpeciesEnum
