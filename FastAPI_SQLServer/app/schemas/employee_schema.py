from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, EmailStr, Field


class EmployeeCreate(BaseModel):

    EmployeeName: str = Field(
        ...,
        min_length=3,
        max_length=100
    )

    Department: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    Salary: Decimal = Field(
        ...,
        gt=0
    )

    Email: EmailStr


class EmployeeResponse(BaseModel):

    EmployeeId: int
    EmployeeName: str
    Department: str
    Salary: Decimal
    Email: EmailStr
    CreatedDate: datetime

    model_config = {
        "from_attributes": True
    }