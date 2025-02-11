from models.donation_schema import DonationSchema
from models.donor_schema import DonorSchemaGet
class DonationSchemaGet(DonationSchema):
    id: int  # מזהה ייחודי של התרומה
    donor: DonorSchemaGet  # פרטי התורם
    class Config:
        orm_mode = True
        from_attributes = True